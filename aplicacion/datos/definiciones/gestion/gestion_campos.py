#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Base general con atributos basicos
from librerias.datos.sql import sqalchemy_tipo_campos as tipos
 
from . import gestion_atributos
 
campos = {
    "creado_por_id"    : tipos.clave_obligatorio(propiedades={"titulo": "Ubicación geografica", "longitud": 60}),  
    "creado_por_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Dependencia responsable", "longitud": 250}),   
    
    # Informacion del radicado
    "origen_tipo"                : tipos.clave(propiedades={"columna": "no", "titulo": "Tipo documento",    "longitud": 50,   "propiedad": gestion_atributos.origen_tipo}),
    "clase_radicado"             : tipos.clave(propiedades={"columna": "no", "titulo": "Clase radicado",    "longitud": 50,   "propiedad": gestion_atributos.clase_radicado}),    
    "nro_radicado"               : tipos.clave(propiedades={"columna": "no", "titulo": "Nómero radicado",   "longitud": 50,   "propiedad": gestion_atributos.nro_radicado}),
    "fecha_radicado"             : tipos.clave(propiedades={"columna": "no", "titulo": "Nómero radicado",   "longitud": 50,   "propiedad": gestion_atributos.fecha_radicado}),  
    "tercero_nombres_apellidos"  : tipos.clave(propiedades={"columna": "no", "titulo": "Nombres apellidos", "longitud": 250,  "propiedad": gestion_atributos.tercero_nombres_apellidos}), 
    "tercero_razon_social"       : tipos.clave(propiedades={"columna": "no", "titulo": "Razón social",      "longitud": 250,  "propiedad": gestion_atributos.tercero_razon_social}), 
    "tercero_clase"              : tipos.clave(propiedades={"columna": "no", "titulo": "Clase remitente",   "longitud": 250,  "propiedad": gestion_atributos.tercero_clase}), 
    "tercero_tipo_tercero_nombre": tipos.clave(propiedades={"columna": "no", "titulo": "Tipo remitente",    "longitud": 250,  "propiedad": gestion_atributos.tercero_tipo_tercero_nombre}), 
    "asunto"                     : tipos.clave(propiedades={"columna": "no", "titulo": "Asunto",            "longitud": 2500, "propiedad": gestion_atributos.asunto}), 
    "origen_id"                  : tipos.clave(propiedades={"columna": "no", "titulo": "Origen id",         "longitud": 120,  "propiedad": gestion_atributos.origen_id}), 

    # Informacion del responsable
    "responsable_id"     : tipos.clave_obligatorio(propiedades={"titulo": "Dependencia", "longitud": 60}),   
    "responsable_nombre" : tipos.texto(propiedades={"columna": "no", "titulo": "Responsable", "longitud": 250}), 

    # Informacion del responsable anterior
    "anterior_id"     : tipos.clave(propiedades={"titulo": "Anterior id", "longitud": 60}),   
    "anterior_nombre" : tipos.texto(propiedades={"columna": "no", "titulo": "Anterior responsable nombre", "longitud": 250}),

    # Dependencia responsable
    "dependencia_id"     : tipos.clave_obligatorio(propiedades={"titulo": "Dependencia", "longitud": 60}),
    "dependencia_nombre" : tipos.texto(propiedades={"columna": "no", "titulo": "Dependencia responsable", "longitud": 250}),   
    "sede_nombre"        : tipos.texto(propiedades={"columna": "no", "titulo": "Sede/Territorial", "longitud": 250}),   

    # Petición
    "rapida"             : tipos.clave_obligatorio(propiedades={"titulo": "Respuesta rapida", "longitud": 20}),  
    "colaborativa"       : tipos.clave(propiedades={"titulo": "Respuesta colaborativa", "longitud": 60}), 
    "peticion_id"        : tipos.clave_obligatorio(propiedades={"titulo": "Tipo petición", "longitud": 60}),  
    "peticion_nombre"    : tipos.texto(propiedades={"columna": "no", "titulo": "Petición nombre", "longitud": 250}),     

    # Terminos de respuesta basicos
    "horas_dias"         : tipos.clave_obligatorio(propiedades={"titulo": "Plazo en HORAS, DIAS", "longitud": 60}), 
    "total_tiempo"       : tipos.entero(propiedades={"titulo": "Plazo total"}),  
    "prioridad"          : tipos.clave_obligatorio(propiedades={"titulo": "Prioridad ALTA, MEDIA, BAJA", "longitud": 60}), 
         
    # Estado, vencimiento
    "gestion_inicio"       : tipos.fecha_obligatorio(propiedades={"titulo": "Fecha creación"}),
    "tipo_gestion"         : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Tipo gestión", "propiedad": gestion_atributos.tipo_gestion}), 
    "etapa_gestion"        : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Etapa gestión", "propiedad": gestion_atributos.etapa_gestion}), 
    "etapa_estado"         : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Etapa estado", "propiedad": gestion_atributos.etapa_estado}), 
    "vence_en"             : tipos.fecha_obligatorio(propiedades={"columna": "no", "titulo": "Fecha vencimiento", "propiedad": gestion_atributos.vence_en}), 
    "estado_gestion"       : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Estado gestión", "longitud": 60, "propiedad": gestion_atributos.estado_gestion}),
    "dias_vencimiento"     : tipos.entero(propiedades={"columna": "no", "titulo": "Dias vencimiento", "propiedad": gestion_atributos.dias_vencimiento}),   
    "finalizado_modo"      : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Modo de finalización", "longitud": 60, "propiedad": gestion_atributos.finalizado_modo}),
    "estado_vencimiento"   : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Estado vencimiento", "longitud": 60, "propiedad": gestion_atributos.estado_vencimiento}),
    "fecha_respuesta"      : tipos.fecha(propiedades={"columna": "no", "titulo": "Fecha respuesta", "propiedad": gestion_atributos.fecha_respuesta}),
    "finalizado_por_id"    : tipos.clave(propiedades={"columna": "no", "titulo": "Finalizado por id", "propiedad": gestion_atributos.finalizado_por_id}),
    "finalizado_por_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Finalizado por nombre", "propiedad": gestion_atributos.finalizado_por_nombre}),
    "finalizado_en"        : tipos.fecha(propiedades={"columna": "no", "titulo": "Finalizado fecha", "propiedad": gestion_atributos.finalizado_en}),
    "finalizado_comentario": tipos.fecha(propiedades={"columna": "no", "titulo": "Finalizado comentario", "propiedad": gestion_atributos.finalizado_comentario}),
  
    # Valores para tablero de control
    "valor"              : tipos.entero(propiedades={"columna": "no", "titulo": "Valor", "propiedad": gestion_atributos.valor_gestion}), 

     # Informacion trd
    "trd_dependencia_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Dependencia expediente", "propiedad": gestion_atributos.trd_dependencia_nombre}),
    "expediente_nombre"     : tipos.texto(propiedades={"columna": "no", "titulo": "Expediente",             "propiedad": gestion_atributos.expediente_nombre}),
    "tipo_nombre"           : tipos.texto(propiedades={"columna": "no", "titulo": "Tipo documental",        "propiedad": gestion_atributos.tipo_nombre}),    

    # Logs
    "logs_gestion"       : tipos.clave(propiedades={"columna": "no", "titulo": "Logs procesados", "propiedad": gestion_atributos.logs_gestion}),   

    # Manejo de borrador
    "borrador_id"        : tipos.clave(propiedades={"titulo": "Id borrador", "longitud": 60}),
    
    # Archivos
    "archivos"           : tipos.clave(propiedades={"columna": "no", "titulo": "Archivos"}),  

    # Atributos especificos
    "atributos_"         : tipos.json(propiedades={"titulo": "Atributos", "defecto": 'json'})
}

########
# Logs #
########    
from aplicacion.datos.comunes.elastic import logs

############
# Archivos #
############    
from aplicacion.datos.comunes.elastic import archivos

indexamiento = {
    "logs_gestion": logs.logs_estructura,
    "archivos"    : archivos.archivos_estructura,
    #"borradores"  : archivos.archivos_estructura
}