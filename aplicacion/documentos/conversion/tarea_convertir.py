#!/usr/bin/python
# -*- coding: ISO-8859-15 -*-

import os, json, builtins, pprint, datetime

import PyPDF2

from librerias.datos.base  import globales

from librerias.datos.elastic  import elastic_busquedas, elastic_ordenamientos
from librerias.datos.archivos import leer_archivo
from librerias.datos.minio    import minio_acciones
from librerias.datos.sql      import sqalchemy_comunes
from aplicacion.comunes       import indexar_datos

"""
from acappella.utils   import utils
from app_utilidades    import clasesMedio
from acappella.data    import fulltext, sources
import app_gestion
from app_databases_def import comunes_estructuras
from acappella.data    import fulltext
"""
######################
# elastics funciones #
######################
from elasticsearch_dsl import Q as Q_dsl

def query_base( querys ):  
    # Crea query
    estructura    = "archivos_anexos"  
    busqueda      = elastic_busquedas.crea_conexion_query(estructura)

    # Ordenamientos
    orden_lista   = [ {'creado_en_': -1} ]
    busqueda      = elastic_ordenamientos.asigna_ordenamientos(busqueda, orden_lista)
    busqueda      = busqueda[0:9999]

    # Querys
    for query in querys:
      busqueda = busqueda.query(query)

    """"
    print("")
    print("")
    print("diccionario:")
    pprint.pprint(busqueda.to_dict())
    print("")
    print("")
    """

    elementos = busqueda.execute().to_dict().get("hits", {}).get("hits", [])       
    
    return elementos

# Solo para archivos en formato PDF
def query_sin_ocr_pdfa():
    #################
    # Query elastic #
    #################
    querys = []
    q_sin_ocr_pdfa = Q_dsl( 
      Q_dsl( "match", **{ "tipo_archivo": 'pdf' } ) | \
      Q_dsl( "match", **{ "tipo_archivo": 'PDF' } ) 
    ) & Q_dsl( "match", **{ "pdf_a": 'no' } )
    querys.append( q_sin_ocr_pdfa )
    items = query_base( querys )
    
    return items

# Archivos que nos PDF (word,excel, etc)
def query_sin_texto():
    # Solo se validan los que estan en gestion
    querys = []
    q_sin_texto = Q_dsl( 
      ~Q_dsl( "match", **{ "tipo_archivo": 'pdf' } ) & 
      ~Q_dsl( "match", **{ "tipo_archivo": 'PDF' } ) 
    ) & ~Q_dsl( "match", **{ "texto_extraido": 'NO' } )
    querys.append( q_sin_texto )
    items = query_base( querys )
    
    return items
  
################################
# TIKA                         #
# Extrae texto archivos office #
################################
import requests, mimetypes
# Extrae el texto del archivo de oficina
def texto_archivo( directorio, entrada, salida ):
  headers = {'Accept': "text/plain"}
  r       = requests.put( 'http://'+builtins.appServices+':9998/tika', data=open(entrada, 'rb'), headers=headers)
  content = r.content.decode("utf-8") 
  
  # Contenido
  nombre_content = salida + ".txt"
  texto_pagina   = content.lower().replace( "\n\n\n\n\n\n", " " ).replace( "\n\n\n\n\n", " " ).replace( "\n\n\n\n", " " ) \
                                  .replace( "\n\n\n", " " ).replace( "\n\n", " " ).replace( "\n", " " )  \
                                  .replace( "      ", " " ).replace( "     ", " " ).replace( "    ", " " ).replace( "   ", " " ).replace( "  ", " " )
  texto          = "".join( [ caracter for caracter in texto_pagina if ( caracter in comunes_estructuras.letras_validas )  ] )
  paginas_texto  = [texto]  
  with open( nombre_content, 'w', encoding = "utf-8" ) as archivo_salva:
    json.dump( paginas_texto, archivo_salva, ensure_ascii=True )
  
#################################
# OCRMYPDF                      #
# Convierte archivo pdf a pdf/a #
# y OCR                         #
#################################
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

def convierte_archivo( directorio, entrada, salida ):
    nombre_convertido = None
    nombre_original   = (directorio + os.sep + entrada).replace("//", "/").replace("\\\\", "\\")
    try:    
        # Configuración del proceso de conversión
        params = [
            # Lenguaje español.
            "-l spa",
            # Intenta determinar la orientación correcta para cada página y gira la página si es necesario.
            " --rotate-pages",
            # Las páginas correctas se escanearon en un ángulo sesgado al girarlas de nuevo a su lugar.
            " --deskew", 
            # Maxima optimización de imagen
            "  --jbig2-lossy",
            # Mejora para vista en navegador web, se da con --optimize 3
            " --fast-web-view 0"
            # Maxima optimización de imagen
            " --optimize 3",
            # Salida pdfa
            "--output-type pdfa-2",
            #" --pdfa-image-compression jpeg", --skip-text
            #" --force-ocr", # genera archivos gigantescos si estan en solo texto
            "--skip-text",
            # Número de tareas 
            "--jobs 4 ",
            # Limpiar páginas antes de OCR, pero no altera el resultado final. 
            # Esto hace que sea menos probable que OCR intente encontrar texto en el ruido de fondo.
            "--clean", 
            #"--pdfa-image-compression jpeg"
        ]

        # Parametros configuración
        dataFile = open(nombre_original, 'rb')
        archivos        = MultipartEncoder(
            fields = {
                "params": "  ".join(params),
                "file"  : ('file.pdf', dataFile, mimetypes.guess_type(nombre_original)[0])
            }
        )

        # Llamado de conversión
        r = requests.post( 'http://'+builtins._appServicios+':5000', data=archivos, headers={'Content-Type': archivos.content_type} )
        dataFile.close()
        
        # Resultado
        nombre_sale  = (directorio + os.sep + salida).replace("//", "/").replace("\\\\", "\\")
        with open(nombre_sale, 'wb') as archivo:
            archivo.write(r.content)
            archivo.close()

        nombre_convertido = nombre_sale     

    except Exception as e:
        print("Error tarea_convertir.py convierte_archivo", str(e))

    return nombre_convertido
        
################################
# PDFTOTEXT                    #
# Extrae texto del PDF con OCR #
################################
# Extrae el texto del archivo PDF con OCR
def genera_texto( archivo ):
  try:
    sistemaOperativo = utils.sistemaOperativo().lower()
    rutaBasica       = builtins.leerNodoZk(builtins.nsBase + "ruta/basica")
    print("rutaBasica:", rutaBasica)
    print("sistemaOperativo:", sistemaOperativo)
    rutaPdftotext    = (rutaBasica + os.sep + 'utilitarios' + os.sep + 'pdftotext' + os.sep + sistemaOperativo + os.sep + 'pdftotext').replace('//', '/').replace('\\\\', '\\')
    if os.path.isfile(archivo):
      nombre_original  = archivo
      nombre_texto     = nombre_original + '.txt'
      paginas_texto    = []
      paginas_archivos = []
      pdf_leido        = PyPDF2.PdfFileReader( open(nombre_original,'rb') )
      numero_paginas   = len(pdf_leido.pages)
      # Genera archivos de texto
      for pagina_texto in range(1, (numero_paginas+1)):
        pagina_txt  = str(pagina_texto).zfill(4)
        sale_pagina = nombre_original + "_" + pagina_txt + '.txt'    
        pdftotext   = rutaPdftotext +  ' -layout -f %s -l %s  %s %s ' % (pagina_texto, pagina_texto, nombre_original, sale_pagina)
        try:
          status = str(os.system(pdftotext))
          # Adiciona archivo con texto.
          paginas_archivos.append(sale_pagina)
        except Exception as e:
          print( 'pdftotext:', str(e) )   
      
      # Lee archivos de texto
      tamano = 0
      for archivo_texto in paginas_archivos:
        archivo      = open(archivo_texto, "r") 
        texto        =  archivo.read()
        texto_pagina = texto.lower().replace( "\n\n\n\n\n\n", " " ).replace( "\n\n\n\n\n", " " ).replace( "\n\n\n\n", " " ) \
                                    .replace( "\n\n\n", " " ).replace( "\n\n", " " ).replace( "\n", " " )  \
                                    .replace( "      ", " " ).replace( "     ", " " ).replace( "    ", " " ).replace( "   ", " " ).replace( "  ", " " )
        texto        = "".join( [ caracter for caracter in texto_pagina if ( caracter in comunes_estructuras.letras_validas )  ] )
        tamano       += len(texto)
        paginas_texto.append(texto)
        archivo.close()
        os.remove(archivo_texto)
      # Salva archivo json
      with open( nombre_texto, 'w', encoding = "iso-8859-1" ) as archivo_salva:      
        json.dump( paginas_texto, archivo_salva, ensure_ascii=True )

  except Exception as e:
    print("Error tarea_convertir.py genera_texto", str(e))
      
#################################
# INDEXAR RADICADO Y DE GESTION #
#################################
def indexaRadicados(session, archivo_id):  
  radicados = session.query( MEDIOS_ARCHIVOS_ELECTRONICOS ).filter( MEDIOS_ARCHIVOS_ELECTRONICOS.archivo_id == archivo_id).all()
  for radicado in radicados:    
    if radicado.tipoRadicacion in ["ENTRADA","SALIDA","INTERNO"]:
      # RADICADO
      CLASE        = clasesMedio.claseMedio( radicado.medioRadicacion )
      radicado_obj = session.query( CLASE ).filter( CLASE.id == radicado.radicado_id ).one()
      print("indexa RADICADO:", radicado_obj.nro_radicado)
      fulltext.indexOneRecord( radicado_obj.tiporecord, radicado_obj, connPyes, flush=True)
      
      # GESTION
      gestionRadicados = session.query(GESTION_RADICADOS).filter( GESTION_RADICADOS.radicado_id == radicado.radicado_id ).all()
      for gestionRadicado in gestionRadicados:
        gestionObj = session.query( GESTION ).filter( GESTION.id == gestionRadicado.gestion_id ).first()
        fulltext.indexOneRecord( 'GESTION', gestionObj, connPyes, flush=True )              
        gestion_id = gestionObj.id
        app_gestion.comunesRoles.indexAsociadosGestion( gestion_id )
        
  # Firma digital            
  firmar = session.query( FIRMA_DIGITAL_ARCHIVOS ).filter( FIRMA_DIGITAL_ARCHIVOS.archivo_id == archivo_id ).all()
  print("firmar:", firmar, archivo_id)
  for firma in firmar:
    print("firma:", firma)
    fulltext.indexOneRecord( 'FIRMA_DIGITAL_ARCHIVOS', firma, connPyes, flush=True )
        
################################
# INDEXAR EXPEDIENTES-CARPETAS #
################################
def indexaArchivo(session, archivo_id):
  # Documentos por expediente
  documentos = session.query( AGN_EXPEDIENTE_DOCUMENTO ).filter( AGN_EXPEDIENTE_DOCUMENTO.archivo_id == archivo_id).all()
  for documento in documentos:
    carpeta    = session.query( AGN_TRD_CARPETA_EXPEDIENTE ).filter( AGN_TRD_CARPETA_EXPEDIENTE.id == documento.carpeta_id).one()
    fulltext.indexOneRecord( 'AGN_TRD_CARPETA_EXPEDIENTE', carpeta, connPyes, flush=True)
    expediente = session.query( AGN_TRD_EXPEDIENTE ).filter( AGN_TRD_EXPEDIENTE.id == documento.expediente_id).one()
    print("indexa EXPEDIENTE DOCUMENTO", expediente.nombre)
    fulltext.indexOneRecord( 'AGN_TRD_EXPEDIENTE', expediente, connPyes, flush=True )
    
  # Documentos del RADICADO por expediente
  documentos = session.query( AGN_EXPEDIENTE_RADICADO ).filter( AGN_EXPEDIENTE_RADICADO.archivo_id == archivo_id).all()
  for documento in documentos:
    carpeta    = session.query( AGN_TRD_CARPETA_EXPEDIENTE ).filter( AGN_TRD_CARPETA_EXPEDIENTE.id == documento.carpeta_id).one()
    fulltext.indexOneRecord( 'AGN_TRD_CARPETA_EXPEDIENTE', carpeta, connPyes, flush=True)
    expediente = session.query( AGN_TRD_EXPEDIENTE ).filter( AGN_TRD_EXPEDIENTE.id == documento.expediente_id).one()
    print("indexa EXPEDIENTE RADICADO", expediente.nombre)
    fulltext.indexOneRecord( 'AGN_TRD_EXPEDIENTE', expediente, connPyes, flush=True )

# Convierte archivos a PDF/A, extrae el texto del pdf con ocr
# Extrae texto de archivos de oficina
def valida_sin_ocr_pfda():  
    ARCHIVOS_CLASE = globales.lee_clase("global_base_archivo_electronico")    
    # Convierte archivos a PDF/A, extrae el texto del pdf con ocr
    contador       = 0
    sin_ocr_pdfa   = query_sin_ocr_pdfa()
    print("--------------------------")  
    print("")
    print( "SIN OCR:", len(sin_ocr_pdfa) )

    #"""
    lista_a_ocr = []
    ids_a_ocr   = []
    for pdf in sin_ocr_pdfa[:20]:     
        try: 
          #pprint.pprint(pdf["_source"].keys())
          _source           = pdf["_source"]
          nombre_pdf        = leer_archivo.salva_archivo_minio(_source["id"])   
          directorio        = os.path.dirname( nombre_pdf )  
          # Pdf original y procesado
          entrada_pdf       = os.path.basename( nombre_pdf )#.replace("_pdfa_ocr", "").replace("_PDFA_OCR", "")
          salida            = entrada_pdf.replace( ".pdf", "_pdfa_ocr.pdf")
          nombre_convertido = convierte_archivo( directorio, entrada_pdf, salida )
          print("SALE:", entrada_pdf, nombre_convertido)
          resultado         = minio_acciones.cargar_objeto(_source["cubeta"], _source["nombre"], nombre_convertido)
          if os.path.exists(nombre_convertido):
              sesion      = sqalchemy_comunes.nuevaSesion('base')  
              archivo_obj = sesion.query( ARCHIVOS_CLASE ).filter( ARCHIVOS_CLASE.id == _source["id"] ).first()        
              archivo_obj.actualizado_en_ = datetime.datetime.now()
              archivo_obj.pdf_a           = "SI"            
              sesion.commit()   
              indexar_datos.indexar_estructura("archivos_anexos", _source["id"])
          print("archivo_obj:", archivo_obj.id)
        except Exception as e:
          print("Conversión:", str(e))

        """
        contador      += 1
        ruta_original = pdf['rutaCompleta']
        directorio    = os.path.dirname( ruta_original )
        # Pdf original y procesado
        entrada       = os.path.basename( ruta_original ).replace("_pdfa_ocr", "").replace("_PDFA_OCR", "")
        salida        = entrada.replace( ".pdf", "_pdfa_ocr.pdf").replace("_PDFA_OCR", "")
        # Salida para texto
        ruta_salida   = ruta_original.replace("_pdfa_ocr", "").replace( ".pdf", "_pdfa_ocr.pdf")
        archivo_obj   = session.query( ARCHIVOS_ELECTRONICOS ).filter( ARCHIVOS_ELECTRONICOS.id == pdf['id'] ).first()
        print("ENTRA:", contador, ruta_original)
        convierte_archivo( directorio, entrada, salida )
        print("SALE:", contador, ruta_original)
        nombre_salida = (directorio + os.sep + salida).replace("//", "/").replace("\\\\", "\\")
        print("SALE:", contador, nombre_salida)
        
        if os.path.exists(nombre_salida):
          print("imagen:", entrada )
          print("salida:", salida )    
          archivo_obj.nombre = salida
          data = {
            'archivo_id'      : pdf['id'],
            'estado_actual'   : "PDFA_OCR",
            'ultima_operacion': "CONVERTIR_PDFA_OCR",
            'fecha_operacion' : utils.getOnlyDateTime()
          }
          estado = ARCHIVOS_ELECT_ESTADO( **data )
          session.add( estado )   
          session.commit()        
          
          # A texto
          print("")
          print("")
          print("+++++++++++++++++++++++++++++++++++++++++")
          genera_texto( ruta_salida )
          print("+++++++++++++++++++++++++++++++++++++++++")
          print("")
          # Indexa archivo electronico
          fulltext.indexOneRecord( 'ARCHIVOS_ELECTRONICOS', archivo_obj, connPyes, flush=True)
          print("RADICADOS IMAGEN>>>>")
          indexaRadicados(session, archivo_obj.id)
          indexaArchivo(session, archivo_obj.id)        
        """
    
    """        
    # Extrae texto de archivos de oficina
    contador      += 0
    sin_sin_texto = query_sin_texto()
    print("--------------------------")  
    print("")    
    print( "SIN TEXTO:", len(sin_sin_texto) )  
    for sin in sin_sin_texto:
      try:
        print( sin["tipo"], sin["nombre"], sin["ultimo_estado"] )
        contador      += 1
        ruta_original = sin['rutaCompleta']
        directorio    = os.path.dirname( ruta_original )
        # Salida para texto
        salida        = ruta_original.lower()      
        archivo_obj   = session.query( ARCHIVOS_ELECTRONICOS ).filter( ARCHIVOS_ELECTRONICOS.id == sin['id'] ).first()
        # Estado del archivo electronico
        data = {
          'archivo_id'      : sin['id'],
          'estado_actual'   : "TEXTO",
          'ultima_operacion': "EXTRAE_TEXTO",
          'fecha_operacion' : utils.getOnlyDateTime()
        }
        estado = ARCHIVOS_ELECT_ESTADO( **data )
        session.add( estado )   
        session.commit()
        
        texto_archivo( directorio, ruta_original, salida )      
        
        # Indexa archivo electronico
        fulltext.indexOneRecord( 'ARCHIVOS_ELECTRONICOS', archivo_obj, connPyes, flush=True)
        indexaRadicados(session, archivo_obj.id)
        indexaArchivo(session, archivo_obj.id)  
      except Exception as e:
        print( "Error:", str(e) )

    fulltext.toFullText( 'FIRMA_DIGITAL_ARCHIVOS', connPyes )
    
    #session.close()        
    """

    print("termina.............")
