#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base import base_general_campos
from librerias.datos.sql import sqalchemy_tipo_campos as tipos
from . import interno_propiedades

campos = {
    "tipo_radicado": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Tipo de radicado", "defecto": "ENTRADA", "propiedad": interno_propiedades.tipo_radicado}),    
    # Sitio de radicación
    "radicado_en"    : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Radicado en id",   "longitud": 64}),
    "radicado_en_nombre": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Radicado en"}),

    # Usuario que radico
    "radicado_por"    : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Radicador id",     "longitud": 64}),
    "radicado_por_nombre": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Radicador"}),

    "fecha_radicado"    : tipos.fecha_obligatorio(propiedades={"titulo": "Fecha radicado"}),    
    "fecha_documento"   : tipos.fecha(propiedades={"columna": "no", "titulo": "Fecha documento"}), # Valor defecto
    
    # Información basica
    "nro_radicado"      : tipos.clave_obligatorio(propiedades={"titulo": "Numero de radicado", "longitud": 64}),    
    "asunto"            : tipos.texto(propiedades={"titulo": "Asunto", "longitud": 2048}),  

    "nro_folios"        : tipos.entero(propiedades={"columna": "no", "titulo": "Número de folios"}),
    "anexos"            : tipos.texto(propiedades={"columna": "no", "titulo": "Anexos"}),

    "medio_notificacion": tipos.clave(propiedades={"titulo": "Medio notificación", "longitud": 64, "validador": "clave_lista"}),  

    #######################
    # Información gestion #
    #######################
    # Dependencia envia
    "dependencia_envia_id"    : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Dependencia envia id",     "longitud": 64}),
    "dependencia_envia_nombre": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Dependencia envia nombre"}),

    # Funcionario envia
    "funcionario_envia_id"    : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Funcionario envia id",     "longitud": 64}),
    "funcionario_envia_nombre": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Funcionario envia nombre"}),

    # Dependencia recibe
    "dependencia_recibe_id"    : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Dependencia recibe id",     "longitud": 64}),
    "dependencia_recibe_nombre": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Dependencia recibe nombre"}),

    # Funcionario recibe
    "funcionario_recibe_id"    : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Funcionario recibe id",     "longitud": 64}),
    "funcionario_recibe_nombre": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Funcionario recibe nombre"}),

    ###############################
    # Información gestion externa #
    ###############################
    "gestion_id": tipos.clave(propiedades={"columna": "no", "titulo": "Gestión id"}),
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
    "fecha_respuesta"      : tipos.fecha(propiedades={"columna": "no", "titulo": "Fecha respuesta"}),
    "dias_gestion": tipos.entero(propiedades={"columna": "no", "titulo": "Dias en gestion"}),   
    

    # Tipo de firma
    "tipo_firma"    : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Tipo de firma",     "longitud": 64}),

    # Tipo respuesta
    "respuesta_tipo"   : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Respuesta tipo", "longitud": 64}),

    # Radicado que contesta
    "radicado_responde": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Radicado responde", "longitud": 64}),

    # Reserva del documento
    "reserva": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Reserva", "longitud": 20}), 

    # Firma digital
    "firma_electronica"      : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Requiere firma electronica", "propiedad": interno_propiedades.firma_electronica}), 
    "firmado_electronica"    : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Tiene firma electronica", "propiedad": interno_propiedades.firmado_electronica}), 
    "firmado_electronica_por": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Quien firmo electronicamente", "propiedad": interno_propiedades.firmado_electronica_por}), 
    "esta_firmado": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Esta firmado", "propiedad": interno_propiedades.esta_firmado}),
    

    # Trazabilidad
    "dependencias_id": tipos.clave(propiedades={"columna": "no", "titulo": "Dependencias id", "propiedad": interno_propiedades.dependencias_id}), 
    "funcionarios_id": tipos.clave(propiedades={"columna": "no", "titulo": "Funcionarios id", "propiedad": interno_propiedades.funcionarios_id}), 

    ########
    # logs #
    ########
    "logs": tipos.json(propiedades={"columna": "no", "titulo": "Log radicado"}),

    ######################
    # Copia del radicado #
    ######################
    "copia_usuarios_id" : tipos.clave(propiedades={"columna": "no", "titulo": "Con copia a usuarios", "longitud": 256, "validador": "clave_lista"}),  
    "copia_grupos_id"   : tipos.clave(propiedades={"columna": "no", "titulo": "Con copia a grupos", "longitud": 256, "validador": "clave_lista"}),  
    
    ############
    # archivos #
    ############
    "archivos"         : tipos.clave(propiedades={"columna": "no", "titulo": "Archivos"}),  
    "pdf_base"        : tipos.json(propiedades={"columna": "no", "titulo": "Archivos pdf base"}), 

    #####################
    # Información comun #
    #####################
    "remite_ent_dep_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Remitente entidad/dependencia", "propiedad": interno_propiedades.remite_ent_dep_nombre}),
    "remite_per_fun_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Remitente persona/funcionario", "propiedad": interno_propiedades.remite_per_fun_nombre}),
    "recibe_ent_dep_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Recibe entidad/dependencia", "propiedad": interno_propiedades.recibe_ent_dep_nombre}),
    "recibe_per_fun_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Recibe persona/funcionario", "propiedad": interno_propiedades.recibe_per_fun_nombre})
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