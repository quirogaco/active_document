#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base import base_general_campos
from librerias.datos.sql import sqalchemy_tipo_campos as tipos
from . import salida_propiedades

campos = {
    "tipo_radicado": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Tipo de radicado", "defecto": "ENTRADA", "propiedad": salida_propiedades.tipo_radicado}),
    # Sitio de radicación
    "radicado_en_id"    : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Radicado en id",   "longitud": 64}),
    "radicado_en_nombre": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Radicado en"}),

    # Usuario que radico
    "radicado_por_id"    : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Radicador id",     "longitud": 64}),
    "radicado_por_nombre": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Radicador"}),

    # Responde radicado
    "fecha_radicado"    : tipos.fecha_obligatorio(propiedades={"titulo": "Fecha radicado"}),    
    "fecha_documento"   : tipos.fecha(propiedades={"columna": "no", "titulo": "Fecha documento"}), # Valor defecto
    "responde_radicado" : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Responde radicado", "longitud": 512}),
    
    # Información basica
    "nro_radicado"      : tipos.clave_obligatorio(propiedades={"titulo": "Numero de radicado", "longitud": 64}),    
    "asunto"            : tipos.texto(propiedades={"titulo": "Asunto", "longitud": 2048}),  

    "nro_folios"        : tipos.entero(propiedades={"columna": "no", "titulo": "Nómero de folios"}),
    "anexos"            : tipos.texto(propiedades={"columna": "no", "titulo": "Anexos"}),

    ###############################
    # Información tercero externa #
    ###############################
    "tercero_id"                    : tipos.clave(propiedades={"columna": "no", "titulo": "Tercero id", "longitud": 64}),  
    "tercero_clase"                 : tipos.texto(propiedades={"columna": "no", "titulo": "Clase de tercero", "longitud": 256, "reporte": "SI"}),  
    # Tipo tercero
    "tercero_tipo_tercero_id"       : tipos.clave(propiedades={"columna": "no", "titulo": "Tipo de tercero id", "longitud": 64}),  
    "tercero_tipo_tercero_nombre"   : tipos.texto(propiedades={"columna": "no", "titulo": "Tipo de tercero", "longitud": 64, "reporte": "SI"}),
    # Tipo de identificación
    "tercero_tipo_identificacion_id"     : tipos.clave(propiedades={"columna": "no", "titulo": "Tipo de identificación id", "longitud": 64}),  
    "tercero_tipo_identificacion_nombre" : tipos.texto(propiedades={"columna": "no", "titulo": "Tipo de identificación", "longitud": 256, "reporte": "SI"}),  
    "tercero_nro_identificacion"    : tipos.texto(propiedades={"columna": "no", "titulo": "Nómero de identificación", "longitud": 64, "reporte": "SI"}),  
    "tercero_razon_social"          : tipos.texto(propiedades={"columna": "no", "titulo": "Razon social", "longitud": 256, "reporte": "SI"}),   
    "tercero_cargo"                 : tipos.texto(propiedades={"columna": "no", "titulo": "Cargo", "longitud": 256, "reporte": "SI"}),   
    "tercero_nombres"               : tipos.texto(propiedades={"columna": "no", "titulo": "Nombres remitente", "longitud": 128, "reporte": "SI"}),           
    "tercero_apellidos"             : tipos.texto(propiedades={"columna": "no", "titulo": "Apellidos remitente", "longitud": 128, "reporte": "SI"}),             
    "tercero_correo_electronico"    : tipos.texto(propiedades={"columna": "no", "titulo": "Correo electrónico", "longitud": 64, "reporte": "SI"}),
    "tercero_direccion"             : tipos.texto(propiedades={"columna": "no", "titulo": "Dirección notificación", "longitud": 128, "reporte": "SI"}),  
    "tercero_codigo_postal"         : tipos.texto(propiedades={"columna": "no", "titulo": "Codigo postal",   "longitud": 64, "reporte": "SI"}),
    "tercero_telefono"              : tipos.texto(propiedades={"columna": "no", "titulo": "Telefono", "longitud": 64, "reporte": "SI"}),  
    "tercero_telefono_movil"        : tipos.texto(propiedades={"columna": "no", "titulo": "Telefono movil", "longitud": 64, "reporte": "SI"}),  
    "tercero_fax"                   : tipos.texto(propiedades={"columna": "no", "titulo": "Fax", "longitud": 64, "reporte": "SI"}),  
    "tercero_ciudad_id"             : tipos.clave(propiedades={"columna": "no", "titulo": "Ciudad",   "longitud": 64}),
    "tercero_ciudad_nombre"         : tipos.texto(propiedades={"columna": "no", "titulo": "Ciudad", "longitud": 128, "reporte": "SI"}),  
    "tercero_nombre_completo"       : tipos.texto(propiedades={"columna": "no", "titulo": "Nombre completo", "longitud": 256, "reporte": "SI"}),  
    "tercero_nombres_apellidos"     : tipos.texto(propiedades={"columna": "no", "titulo": "Nombre", "longitud": 256, "reporte": "SI"}),  
    
    #######################
    # Información gestión #
    #######################
    "gestion_id": tipos.clave(propiedades={"columna": "no", "titulo": "Gestión id", "longitud": 64}),
    
    # Dependencia responde
    "dependencia_responde_id"    : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Dependencia id",     "longitud": 64}),
    "dependencia_responde_nombre": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Dependencia nombre"}),

    # Funcionario responde
    "funcionario_responde_id"    : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Funcionario id",     "longitud": 64}),
    "funcionario_responde_nombre": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Funcionario nombre"}),

    # Tipo de firma
    "tipo_firma"    : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Tipo de firma",     "longitud": 64}),

    # Tipo respuesta
    "respuesta_tipo"   : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Respuesta tipo", "longitud": 64}),

    # Radicado que contesta
    "radicado_responde": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Radicado responde", "longitud": 64}),

    # Reserva del documento
    "reserva"            : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Reserva", "longitud": 20}), 

    # Firma digital
    "firma_electronica"      : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Requiere firma electronica", "propiedad": salida_propiedades.firma_electronica}), 
    "firmado_electronica"    : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Tiene firma electronica", "propiedad": salida_propiedades.firmado_electronica}), 
    "firmado_electronica_por": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Quien firmo electronicamente", "propiedad": salida_propiedades.firmado_electronica_por}), 

    "medio_notificacion": tipos.clave(propiedades={"titulo": "Medio notificación", "longitud": 64, "validador": "clave_lista"}),  

    "esta_firmado": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Esta firmado", "propiedad": salida_propiedades.esta_firmado}),

    # Trazabilidad
    "dependencias_id": tipos.clave(propiedades={"columna": "no", "titulo": "Dependencias id", "propiedad": salida_propiedades.dependencias_id}), 
    "funcionarios_id": tipos.clave(propiedades={"columna": "no", "titulo": "Funcionarios id", "propiedad": salida_propiedades.funcionarios_id}), 
    
    ########
    # logs #
    ########
    "logs": tipos.json(propiedades={"columna": "no", "titulo": "Log radicado"}),

    ######################
    # Copia del radicado #
    ######################
    "copia_usuarios_id": tipos.clave(propiedades={"columna": "no", "titulo": "Con copia a usuarios", "longitud": 256, "validador": "clave_lista"}),  
    "copia_grupos_id": tipos.clave(propiedades={"columna": "no", "titulo": "Con copia a grupos", "longitud": 256, "validador": "clave_lista"}),  
    
    ############
    # archivos #
    ############
    "archivos"         : tipos.clave(propiedades={"columna": "no", "titulo": "Archivos"}),  
    "pdf_base"        : tipos.json(propiedades={"columna": "no", "titulo": "Archivos pdf base"}), 
}
campos.update(base_general_campos.campos)


###################################
# Campos indexamiento adicionales #
###################################

############
# Archivos #
############    
from aplicacion.datos.comunes.elastic import archivos
indexamiento = {
    "archivos": archivos.archivos_estructura
}