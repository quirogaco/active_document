#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Base general con atributos basicos
from librerias.datos.sql import sqalchemy_tipo_campos as tipos

def completo_(self):    
    return dict(self.to_dict(5))

campos = {
    # Accionante
    "accionante_tipo"  : tipos.clave(propiedades={"titulo": "Accionante tipo", "longitud": 64}),  
    "accionante_id"    : tipos.clave(propiedades={"titulo": "Accionante id", "longitud": 64}),  
    "accionante_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Accionante nombre", "longitud": 250, "reporte": "SI"}), #, "propiedad": accionante_nombre}),   
    
    # Destinatario
    "destinatario_tipo"  : tipos.clave(propiedades={"titulo": "Destinatario tipo", "longitud": 64}),  
    "destinatario_id"    : tipos.clave(propiedades={"titulo": "Destinatario id", "longitud": 64}),  
    "destinatario_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Destinatario nombre", "longitud": 250, "reporte": "SI"}), #, "propiedad": destinatario_nombre}),   
    
    # proceso: RADICACION, GESTION, ENVIOS, ETC
    "proceso"          : tipos.texto_obligatorio(propiedades={"titulo": "Proceso de la acción", "longitud": 64, "reporte": "SI"}),     
    # fuente: ENTRADA, SALIDA, GESTION
    "fuente"           : tipos.texto_obligatorio(propiedades={"titulo": "Fuente de datos", "longitud": 64, "reporte": "SI"}),         
    "fuente_id"        : tipos.clave(propiedades={"titulo": "Id del elemento fuente", "longitud": 64}),     

    # Acción realizada
    "accion"           : tipos.clave(propiedades={"titulo": "Accion", "longitud": 64, "reporte": "SI"}), 
    "detalle"          : tipos.texto(propiedades={"titulo": "Detalle", "longitud": 512, "reporte": "SI"}),   
    # Estado resulatdo del objeto proceso
    "estado"           : tipos.clave(propiedades={"titulo": "Estado", "longitud": 64, "reporte": "SI"}), 
    # Mensaje para grillas y formas, asociado al estado
    "detalle_estado"   : tipos.texto(propiedades={"titulo": "Detalle estado", "longitud": 128}), 
    # Información completa del log
    "completo_"        : tipos.texto(propiedades={"columna": "no", "serializa": "no", "titulo": "Este registro", "propiedad": completo_}),  
}