#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint
 
# Base general con atributos basicos
from aplicacion.datos.clases.clases_base import base_general_campos
from librerias.datos.sql import sqalchemy_tipo_campos as tipos
from . import radicado_propiedades

campos = {
    "tipo_radicado": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Tipo de radicado", "defecto": "ENTRADA", "propiedad": radicado_propiedades.tipo_radicado}),
    # Sitio de radicación
    "radicado_en"    : tipos.clave_obligatorio(propiedades={"titulo": "Radicado en id",   "longitud": 64}),
    "radicado_en_nombre": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Radicado en", "reporte": "SI"}),

    # Usuario que radico
    "radicado_por"    : tipos.clave_obligatorio(propiedades={"titulo": "Radicador id",     "longitud": 64}),
    "radicado_por_nombre": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Radicador Nombre", "reporte": "SI"}),

    # Clasificación de radicado
    # CLASE RADICADO (PRQS, VENTANILLA, TRAMITE)
    "clase_radicado"    : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Clase radicado", "longitud": 64, "reporte": "SI"}),
    
    # Canal
    "canal_radicado_id"    : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Canal id", "longitud": 64}),
    "canal_radicado_nombre": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Canal Radicación", "longitud": 256, "reporte": "SI"}),
    
    # Información basica
    "nro_radicado"      : tipos.clave_obligatorio(propiedades={"titulo": "Número de radicado", "longitud": 64, "reporte": "SI"}),
    "fecha_radicado"    : tipos.fecha_obligatorio(propiedades={"titulo": "Fecha radicado", "reporte": "SI", 
                                                "formato": {"nombre": "fecha_radicado_", "tipo": "fecha_hora"}}),    
    "medio_notificacion": tipos.clave(propiedades={"columna": "no", "titulo": "Medio notificación", "longitud": 64, "validador": "clave_lista", "reporte": "SI"}),  
    "asunto"            : tipos.texto(propiedades={"columna": "no", "titulo": "Asunto", "longitud": 2048, "reporte": "SI"}),  

    # Campos basicos
    "fecha_documento"   : tipos.fecha(propiedades={"columna": "no", "titulo": "Fecha documento", "reporte": "SI", 
                                                "formato": {"nombre": "fecha_documento_", "tipo": "fecha"}}), 
    "radicado_remitente": tipos.texto(propiedades={"columna": "no", "titulo": "Radicado remitente", "longitud": 64, "reporte": "SI"}),  
    
    # Empresa de mensajeria
    "empresa_mensajeria_id": tipos.clave(propiedades={"columna": "no", "titulo": "Empresa mensajeria id", "longitud": 64}),
    "empresa_mensajeria_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Empresa mensajeria", "longitud": 64, "reporte": "SI"}),    

    "numero_guia"       : tipos.texto(propiedades={"columna": "no", "titulo": "Número guia", "longitud": 64, "reporte": "SI"}),  
    "nro_folios"        : tipos.entero(propiedades={"columna": "no", "titulo": "Número de folios", "reporte": "SI"}),
    "anexos"            : tipos.texto(propiedades={"columna": "no", "titulo": "Anexos", "reporte": "SI"}),
    "entidad_traslada"  : tipos.texto(propiedades={"columna": "no", "titulo": "Entidad que traslada","longitud": 256, "reporte": "SI"}),  
    "persona_traslada"  : tipos.texto(propiedades={"columna": "no", "titulo": "Persona que traslada","longitud": 256, "reporte": "SI"}),

    # Reserva del documento
    "reserva"           : tipos.clave_obligatorio(propiedades={"titulo": "Reserva", "longitud": 20, "reporte": "SI"}), 
    "manejo_informacion": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Manejo de información", "longitud": 10, "reporte": "SI"}),


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
    "tercero_nro_identificacion"    : tipos.texto(propiedades={"columna": "no", "titulo": "Número de identificación", "longitud": 64, "reporte": "SI"}),  
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
    
    # TEMA tema id y subtema id deben ser campos del regitro
    "tema_dependencia_id"       : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Tema id", "longitud": 64}),
    "tema_dependencia_nombre"   : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Tema Nombre", "longitud": 256, "reporte": "SI"}),
    "subtema_dependencia_id"    : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "SubTema id", "longitud": 64}),
    "subtema_dependencia_nombre": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "SubTema Nombre", "longitud": 256, "reporte": "SI"}),

    ###############################
    # Información gestion externa #
    ###############################
    "resuelto_inmediato"      : tipos.clave(propiedades={"columna": "no", "titulo": "Resuelto primer contacto", "reporte": "SI", "defecto": 'NO'}),
    "repone_entrada"          : tipos.clave(propiedades={"columna": "no", "titulo": "Repone entrada", "reporte": "SI"}),
    "gestion_id": tipos.clave(propiedades={"columna": "no", "titulo": "Gestión id"}), # es una lista de id's, radicado_propiedades -> gestion_asignada_peticion
    # Propiedades con información de gestion
    "gestion_asignada_peticion": tipos.clave(propiedades={"columna": "no", "titulo": "Petición asignada"}),
    "gestion_relacion"         : tipos.clave(propiedades={"columna": "no", "titulo": "Tipo relación gestion"}),

    # Dependencia
    "gestion_dependencia_id"    : tipos.clave(propiedades={"columna": "no", "titulo": "Gestión dependencia responsable id"}),
    "gestion_dependencia_nombre": tipos.clave(propiedades={"columna": "no", "titulo": "Gestión dependencia responsable", "reporte": "SI"}),
    
    # Usuario
    "gestion_responsable_id"    : tipos.clave(propiedades={"columna": "no", "titulo": "Usuario responsable id"}),
    "gestion_responsable_nombre": tipos.clave(propiedades={"columna": "no", "titulo": "Gestión Usuario responsable", "reporte": "SI"}),
    
    # Petición
    "gestion_peticion_id"      : tipos.clave(propiedades={"columna": "no", "titulo": "Gestión Petición id",    "longitud": 256}),
    "gestion_peticion_nombre"  : tipos.clave(propiedades={"columna": "no", "titulo": "Gestión tipo de petición",    "longitud": 256, "reporte": "SI"}),
    
    # Terminos de respuesta basicos, prioridad
    "gestion_horas_dias"   : tipos.texto(propiedades={"columna": "no", "titulo": "Gestión Plazo en HORAS, DIAS", "longitud": 60, "reporte": "SI"}), 
    "gestion_total_tiempo" : tipos.entero(propiedades={"columna": "no", "titulo": "Gestión Plazo total", "reporte": "SI"}),  
    "gestion_prioridad"    : tipos.clave(propiedades={"columna": "no", "titulo": "Gestión Prioridad", "longitud": 60, "reporte": "SI"}), 

    # Estado de gestion
    "gestion_inicio"       : tipos.fecha(propiedades={"columna": "no", "titulo": "Gestión inicia en", "reporte": "SI"}), 
    "gestion_vence_en"     : tipos.fecha(propiedades={"columna": "no", "titulo": "Gestión vence en", "reporte": "SI"}), 
    "gestion_estado"       : tipos.clave(propiedades={"columna": "no", "titulo": "Gestión estado", "longitud": 60, "reporte": "SI"}), 
    "gestion_etapa"        : tipos.clave(propiedades={"columna": "no", "titulo": "Gestión etapa", "longitud": 60, "reporte": "SI"}), 
    "gestion_estado_vencimiento": tipos.clave(propiedades={"columna": "no", "titulo": "Gestión estado vencimiento", "longitud": 60, "reporte": "SI"}), 

    # Trazabilidad
    "dependencias_id": tipos.clave(propiedades={"columna": "no", "titulo": "Dependencias id"}), 
    "funcionarios_id": tipos.clave(propiedades={"columna": "no", "titulo": "Funcionarios id"}), 
    
    ######################
    # Copia del radicado #
    ######################
    "copia_usuarios_id" : tipos.clave(propiedades={"columna": "no", "titulo": "Con copia a usuarios", "longitud": 256, "validador": "clave_lista"}),  
    "copia_grupos_id"   : tipos.clave(propiedades={"columna": "no", "titulo": "Con copia a grupos", "longitud": 256, "validador": "clave_lista"}),  

    # Dinamicos clasificación
    "discapacidad_id"       : tipos.clave(propiedades={"titulo": "Tipo de discapacidad",   "longitud": 64}),  
    'discapacidad_nombre'   : tipos.texto(propiedades={"columna": "no", "titulo": "Tipo de  Discapacidad", "longitud": 128, "reporte": "SI"}),  

    "poblacion_id"          : tipos.clave(propiedades={"titulo": "Tipo de población especial",   "longitud": 64}),  
    'poblacion_nombre'      : tipos.texto(propiedades={"columna": "no", "titulo": "Tipo de población especial", "longitud": 128, "reporte": "SI"}),  
    
    "rango_id"              : tipos.clave(propiedades={"titulo": "Rango de edad",   "longitud": 64}),  
    'rango_nombre'          : tipos.texto(propiedades={"columna": "no", "titulo": "Rango de edad", "longitud": 128, "reporte": "SI"}),
    
    "genero_id"             : tipos.clave(propiedades={"titulo": "Genero",   "longitud": 64}),  
    'genero_nombre'         : tipos.texto(propiedades={"columna": "no", "titulo": "Genero", "longitud": 128, "reporte": "SI"}),

    ############
    # archivos #
    ############
    "archivos"        : tipos.clave(propiedades={"columna": "no", "titulo": "Archivos"}),  
    "pdf_base"        : tipos.json(propiedades={"columna": "no", "titulo": "Archivos pdf base"}), 
    "archivos_nombres": tipos.texto(propiedades={"columna": "no", "titulo": "Nombres de archivos"}),
    "archivos_total"  : tipos.entero(propiedades={"columna": "no", "titulo": "Total anexos", "reporte": "SI"}),

    ########
    # logs #
    ########
    "logs": tipos.json(propiedades={"columna": "no", "titulo": "Log radicado"}),

    ################
    # Relacionados #
    ################
    "relacionados_id": tipos.clave(propiedades={"columna": "no", "titulo": "Relacionados id", "validador": "clave_lista"}), 
    "relacionados"   : tipos.json(propiedades={"columna": "no", "titulo": "Radicados relacionados"}),

    #############
    # Con copia #
    #############
    "con_copia": tipos.json(propiedades={"columna": "no", "titulo": "Con copia a"})
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