#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint, datetime, random, builtins, os, shutil

from librerias.datos.base   import globales
from librerias.datos.sql    import sqalchemy_leer
from aplicacion.datos.redis import redis_datos

def pre_procesa(estructura, operacion, datos, id_tarea):
    radicado = "S-2021-" + str(random.randint(0, 10000))
    datos["nro_radicado"]   = radicado
    datos["fecha_radicado"] = datetime.datetime.now()

    # validar fecha del documento y valores basicos

    return datos
globales.carga_procesamiento("radicados_salida", "pre_estructura", pre_procesa)
#globales.carga_procesamiento("radicados_salida", "post_estructura", post_procesa)

#############################
# PROCESOS FINALES RADICADO #
#############################
from librerias.datos.sql             import sqalchemy_leer
from librerias.documentos.plantillas import word_plantilla
from librerias.documentos.plantillas import word_plantilla
from librerias.documentos.conversion import conversion
from librerias.email                 import email

def ultima_procesa(estructura, operacion, datos, tarea, archivos, id_tarea):
    datos = sqalchemy_leer.leer_un_registro("radicados_salida", datos["id"])
    print("ultima_procesa:", datos)
    nro_radicado       = datos["nro_radicado"]
    # Mezcla datos
    ruta_archivo   = builtins.rutaBase + 'temporal' + os.sep + "salida.docx"     
    archivo_salida = nro_radicado + ".docx" 
    ruta_salida    = builtins.rutaBase + 'temporal' + os.sep + archivo_salida
    word_plantilla.mezcla_plantilla_archivos(ruta_archivo, ruta_salida, datos=datos)    

    # Convertir
    url = "http://" + str(builtins._appAnfitrion) + ":" + str(builtins._appPuerto) + '/entregar_archivo_temporal/' + archivo_salida    
    print("url:", url)
    print("builtins._appServicios:", builtins._appServicios)
    parametros = {
        "filetype"  : "docx",
        "title"     : "convertido",
        "url"       : url
    }
    ruta_destino  = conversion.a_pdfa(str(builtins._appServicios), "80", parametros)  
    jpg_ruta      = conversion.a_jpg(str(builtins._appServicios), "80", parametros)    
    print("ruta destino:", ruta_destino)

    # Envia archivo de salida
    correos_electronicos = datos["tercero_correo_electronico"].split(",")
    correos_electronicos.append("quirogaco@gmail.com")
    correos_electronicos.append("fabigonz@esap.edu.co")
    archivo_salida_pdf   = nro_radicado + ".pdf" 
    ruta_salida_pdf      = builtins.rutaBase + 'temporal' + os.sep + archivo_salida_pdf
    shutil.copyfile(ruta_destino, ruta_salida_pdf)
    
    de        = "quirogaco@gmail.com"
    clave     = "sreojrjewsjkxnml"
    para      = correos_electronicos
    asunto    = "Notificación de comunicado [" + nro_radicado  + "]"     
    archivos  = [ruta_salida_pdf]

    direccion_smtp = "smtp.gmail.com"
    puerto_smtp    = 587

    mensaje = email.mensaje_imagen(
        de, 
        para, 
        asunto, 
        jpg_ruta, 
        archivos=archivos
    )

    email.enviar_mensaje_smtp(
        mensaje, 
        de, 
        clave, 
        para, 
        direccion_smtp, 
        puerto_smtp
    )

    return datos
globales.carga_procesamiento("radicados_salida", "ultima_estructura", ultima_procesa)