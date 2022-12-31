#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os, pathlib, pprint
import shortuuid

from PyPDF2 import PdfFileReader

from librerias.datos.base   import globales
from aplicacion.datos.redis import redis_datos
from librerias.datos.minio  import minio_acciones
from librerias.datos.sql    import sqalchemy_insertar, sqalchemy_filtrar 

###################################
# Crea un archivo Minio           #
# Crea registro en la:            #
#  tabla de archivos elecronicos  #
###################################
def crear_archivo(   
   nombre_archivo_fuente, 
   nombre_destino, 
   cubeta          = None,   
   tipo_archivo    = None, 
   temporal        = False, 
   borrar_temporal = True,
   buffer          = None,
   detalle         = "ANEXO",
   id_tarea        = ""
   
):
   # Crea archivo MINIO
   if cubeta is None:
      cubeta = "contenedor.general"
   
   if buffer != None:
      resultado = minio_acciones.cargar_objeto_buffer(cubeta, nombre_destino, buffer)
   else:
      resultado = minio_acciones.cargar_objeto(cubeta, nombre_destino, nombre_archivo_fuente)

   # Elimina temporal
   if temporal == True and borrar_temporal == True:
      try:
         os.remove(file)
      except:
         pass

   # Tipo de archivo 
   if tipo_archivo is None:
      extension = pathlib.Path(nombre_archivo_fuente).suffix
   else:
      extension = tipo_archivo
   extension = str(extension).replace(".", "").lower()

   # Nómero de folios
   folios = 1
   if extension == "pdf":
      try:
         if buffer == None:
            # Archivo
            with open(nombre_archivo_fuente, "rb") as pdf_archivo:
               pdf_lector = PdfFileReader(pdf_archivo)
               folios     = pdf_lector.numPages 
         else:
            # Buffer                        
            pdf_lector = PdfFileReader(buffer)
            folios     = pdf_lector.numPages     
            buffer.file.seek(0)        
      except Exception as e:
         print("")
         print("..........................")
         print("Leyendo nómero de folios:", str(e))
         print("..........................")
         print("")
                  
   ############################
   # Crea registro de archivo #
   ############################
   datos_tarea = redis_datos.lee_tarea_ejecucion(id_tarea)
   usuario_id  = datos_tarea.get('_usuario_', {}).get('id', None)
   CLASE  = globales.lee_clase("global_base_archivo_electronico")
   data = {
      'cubeta'       : cubeta,
      'nombre'       : nombre_destino,
      'detalle'      : detalle,
      'ruta'         : "", # es minio, no es archivo fisico
      'tamano'       : resultado.get("tamano", 0),
      'tipo_archivo' : extension,
      'folios'       : folios,
      'creado_por_id': usuario_id
   }
   registro = sqalchemy_insertar.insertar_registro('base', CLASE, data)
   
   return registro

####################################
# Lee registro en la:              #
#  tabla de archivos elecronicos   #
# Regresa el archivo opcionalmente #
####################################
def leer_archivo(   
   cubeta,   
   nombre_objeto,
   archivo_destino = ''
):

   # Crea archivo MINIO
   if cubeta is None:
      cubeta = "contenedor.general"

   ############################
   # Lee registro de archivo #
   ############################
   cubeta        = cubeta.lower()
   nombre_objeto = nombre_objeto.lower()
   registro      = None
   filtros       = [ [ "cubeta", "=", cubeta ], [ "nombre", "=", nombre_objeto ] ]
   registros     = sqalchemy_filtrar.filtrarOrdena("base", "archivos_electronicos", filtros)
   if len(registros) > 0:
      registro = registros[0]

   if (registro is not None) and (archivo_destino not in ["", None]):
      minio_acciones.leer_objeto_archivo(cubeta, nombre_objeto, archivo_destino) 
      
   return registro

#####################################
# Crea registro de relacion ARCHIVO #
#####################################
def crear_registro_relacion(   
   origen,                    # Estructura
   origen_id,                 # Id de la estructura
   archivo_id,                # Id del archivo
   origen_role   = "padre", 
   tipo_relacion = "anexos",
   cardinalidad  = "multiple"
):
   ############################
   # Crea registro de archivo #
   ############################
   CLASE  = globales.lee_clase("global_base_relacion_archivo")
   data = {
      'origen'       : origen,
      'origen_id'    : origen_id,
      'archivo_id'   : archivo_id,
      'origen_role'  : origen_role,
      'tipo_relacion': tipo_relacion,
      'cardinalidad' : cardinalidad
   }
   print("crear_registro_relacion:")
   pprint.pprint(data)
   registro = sqalchemy_insertar.insertar_registro('base', CLASE, data)
   
   return registro

########################################
# Crea registro archivo, archivo MINIO #
# Crea registro de relacion ARCHIVO    #
########################################
def crear_archivo_relacion(   
   estructura,                # Estructura
   estructura_id,             # Id de la estructura
   nombre_archivo_fuente,     # Archivo en disco
   nombre_objeto,             # Nombre del objeto MINIO
   cubeta          = None,    # Bucket MINIO
   tipo_archivo    = None,    
   temporal        = False, 
   borrar_temporal = True,
   buffer          = None,
   tipo_relacion   = "anexos",
   detalle         = "Anexo",
   id_tarea        = ""
):
   uuid_corto = shortuuid.uuid()
   nombre, extension = os.path.splitext(nombre_objeto)
   nombre_objeto = (nombre + "___" + uuid_corto + extension).lower().replace(" ", "_")
   # Archivo MINIO
   resultado_archivo = crear_archivo(   
      nombre_archivo_fuente, 
      nombre_objeto, 
      cubeta,
      tipo_archivo, 
      temporal, 
      borrar_temporal,
      buffer,
      detalle,
      id_tarea
   )

   # Relación a archivo
   print("crear_archivo_relacion:", estructura_id)
   resultado_relacion = crear_registro_relacion(   
      estructura,
      estructura_id,
      archivo_id  = resultado_archivo['id'],   
      tipo_relacion = tipo_relacion  
   )

   return resultado_relacion

def insertar_archivos(
   estructura, 
   datos, 
   tarea, 
   archivos, 
   tipo_relacion = "anexos", 
   cubeta = "contenedor.general", 
   id_tarea=""
):
   for archivo in archivos:
      estructura_id = datos["id"]
      print("insertar_archivos:", estructura_id)
      registro = crear_archivo_relacion(   
         estructura,     # Estructura
         estructura_id,  # Id de la estructura
         archivo["nombre_completo"], # Archivo en disco
         archivo["nombre"],          # Nombre del objeto MINIO
         detalle = archivo["nombre"],
         cubeta = cubeta,
         tipo_relacion = tipo_relacion,
         id_tarea = id_tarea
      ) 

def manejo_archivos(
   estructura, 
   accion, 
   datos, 
   tarea, 
   archivos, 
   id_tarea, 
   tipo_relacion = "anexos", 
   cubeta = "contenedor.general"
):
   accion_archivo = tarea.get('accion', accion) 
   if accion_archivo == 'insertar':
      print("Manejo_archivos:", datos, archivos)
      insertar_archivos(
         estructura, 
         datos, 
         tarea, 
         archivos, 
         tipo_relacion, 
         cubeta, 
         id_tarea
      )

   elif accion_archivo == 'modificar':
      eliminar_archivos(estructura, datos, tarea, archivos)
      insertar_archivos(
         estructura, 
         datos, 
         tarea, 
         archivos, 
         tipo_relacion, 
         cubeta, 
         id_tarea
      )
      
   elif accion_archivo == 'eliminar':
      eliminar_archivos(
         estructura, 
         datos, 
         tarea, 
         archivos, 
         tipo_relacion, 
         cubeta, 
         id_tarea
      ) # Falta lemeinar archivo

CONFIGURACION_GENERAL["FUNCIONES_TAREAS"]['archivos'] = manejo_archivos