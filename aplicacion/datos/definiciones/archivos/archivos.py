#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint

# Base general con atributos basicos
from librerias.datos.sql                    import sqalchemy_tipo_campos as tipos
from aplicacion.datos.definiciones._comunes import elementos_comunes
from librerias.datos.sql                    import sqalchemy_clase_dinamica

# Texto del PDF
def texto_archivo(r_):
    texto = ['']
    
    return texto

campos = {
    "id"               : tipos.clave(propiedades={"titulo": "Id registro"}),
    # Atributo de MINIO
    "cubeta"           : tipos.texto(propiedades={"titulo": "Cubeta del archivo", "longitud": 60}),     
    # Nombre del archivo, objeto para MINIO
    "nombre"           : tipos.texto(propiedades={"titulo": "Objeto minio", "longitud": 60}),    
    # Detalle
    "detalle"          : tipos.texto(propiedades={"titulo": "Detalle", "longitud": 512}),    
    # Ruta del archivo
    "ruta"             : tipos.texto(propiedades={"titulo": "Ruta", "longitud": 512}),    
    # Tipo pdf, docx
    "tipo_archivo"     : tipos.texto(propiedades={"titulo": "Razon social", "longitud": 64}),
    # Tamano del archivo
    "tamano"           : tipos.entero(propiedades={"titulo": "Tama�o del archivo"}),
    # Folios
    "folios"           : tipos.entero(propiedades={"titulo": "Folios del archivo"}),
    # Texto extraido
    "texto_extraido"   : tipos.texto(propiedades={"titulo": "Texto extraido", "longitud": 64}),
    # Convertido a PDF/A
    "pdf_a"            : tipos.texto(propiedades={"titulo": "Convertido a PDF/A", "longitud": 64}),
    # Archivo base, ej. Es el PDF del radicado
    "base"             : tipos.texto(propiedades={"titulo": "Archivo base", "longitud": 64}),
    # Texto a indexar
    "texto"            : tipos.texto(propiedades={"columna": "no", "titulo": "Texto del archivo", "propiedad": texto_archivo}),
    # Usuario creador
    "creado_por_id"    : tipos.clave(propiedades={"titulo": "Creado por id"}),
    "creado_por_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Creado por"}),       
    # Creación
     "creado_en_"      : tipos.fecha(propiedades={"titulo": "Creado en"}),      
     "actualizado_en_" : tipos.fecha(propiedades={"titulo": "Actualizado en"})           
}  
camposElastic = campos.copy()

referencias = [
    # Usuario que creo
    {
        "campoReferencia"    : "creado_por_id",
        "atributosReferencia": [{
            "creado_por_nombre": "nombre"
        }],
        "estructuraDestino": "usuarios"
    }
]

definicion = {
    "descripcion" : "Archivos del sistema",
    "clase"       : "global_base_archivo_electronico",
    "estructura"  : "archivos_anexos",    
    "campos"      : campos,
    "referencias" : referencias,
    "campoIndice" : "id",
    "indexa"      : "no",
    "indexamiento": {}
}

# Crea relacion y campos proxy para esta estructura ya que no es dinamica
sqalchemy_clase_dinamica.prepara_relaciones_proxy(definicion["clase"], definicion["referencias"], definicion["campos"])

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)

# PROCESAMIENTO ESTRUCTURA
elementos_comunes.procesaBaseGeneral(definicion)