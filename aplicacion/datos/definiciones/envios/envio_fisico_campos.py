#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Base general con atributos basicos
from librerias.datos.sql                    import sqalchemy_tipo_campos as tipos
from librerias.datos.base                   import globales

campos = {
    "radicado_id" : tipos.clave_obligatorio(propiedades={"titulo": "Radicado salida id", "longitud": 60}),  
    "nro_radicado": tipos.texto(propiedades={"titulo": "N�mero de radicado", "longitud": 50}),   
    "destinatario": tipos.texto(propiedades={"titulo": "Destinatario", "longitud": 512}), 
    # ORIGINAL,COPIA
    "tipo"        : tipos.texto_obligatorio(propiedades={"titulo": "Tipo de radicado", "longitud": 60}),         
    "direccion"   : tipos.texto(propiedades={"titulo": "Direcci�n", "longitud": 250}), 
    # Ciudad, departamento, pais
    "ubicacion"   : tipos.texto(propiedades={"titulo": "Ubicaci�n", "longitud": 250}), 
    "planilla_id" : tipos.clave(propiedades={"titulo": "Planilla id", "longitud": 60}),   
    # PENDIENTE,ENVIADO
    "estado"      : tipos.texto(propiedades={"titulo": "Estado envio", "longitud": 60, "defecto": "PENDIENTE"}),
    "guia_envio"  : tipos.texto(propiedades={"titulo": "Guia envio", "longitud": 60, "defecto": ""}),
    "fecha_envio" : tipos.fecha(propiedades={"titulo": "Fecha envio"}), 
    "guia_devolucion"  : tipos.texto(propiedades={"titulo": "Guia devoluci�n", "longitud": 60, "defecto": ""}),
    "fecha_devolucion" : tipos.fecha(propiedades={"titulo": "Fecha devoluci�n"}), 
    "motivo_devolucion": tipos.texto(propiedades={"titulo": "Motivo devoluci�n", "longitud": 250}), 
}