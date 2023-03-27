
#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, random 

from librerias.datos.sql import sqalchemy_modificar, sqalchemy_insertar
from librerias.datos.sql import sqalchemy_borrar, sqalchemy_leer
from librerias.datos.sql import sqalchemy_filtrar 

from librerias.datos.elastic import elastic_operaciones

from aplicacion.trd import logs

from . import indexar_datos

# ARCHIVOS
def salvar_archivo(accion, datos={}, archivos=[], id_tarea=""): 
    expediente_id = datos['expediente_id']
    # Carpeta id
    filtros = [ [ "expediente_id", "=", expediente_id ] ]
    carpetas = sqalchemy_filtrar.filtrarOrdena(estructura="agn_carpetas_trd", filtros=filtros)
    carpeta_id = carpetas[0]['id']
    soporte = datos["datos"]['soporte']    
    datos_archivos = {
        "padre_id": datos["datos"].get("padre_id", ""),
        "tabla": "TRD", 
        "carpeta_id": carpeta_id, 
        "expediente_id": expediente_id, 
        "detalle": datos["datos"]["detalle"], 
        "observacion": datos["datos"].get("observacion", ""), 
        "fecha_creacion": datos["datos"]["fecha_creacion"], 
        "tipo_id": datos["datos"]["tipo_id"],
        "fecha_funcion": "RSA-MD5",
        "soporte": soporte
    }
    # Atributos por soporte
    datos_archivos["folios_fisicos"] = 0
    if soporte in ["DIGITALIZADO", "FISICO"]:
        datos_archivos["folios_fisicos"] = datos["datos"]["folios_fisicos"]        
    resultado = sqalchemy_insertar.insertar_registro_estructura("agn_documentos_trd", datos_archivos)
    logs.log_trd("agn_expedientes_trd", expediente_id, "ADICIONA DOCUMENTO", ("ADICIONA DOCUMENTO" + datos["datos"]["detalle"]), id_tarea)
    indexar_datos.salvar_anexos("insertar", {"id": resultado["id"]}, archivos, id_tarea)    
    
    # indexa documentos y expediente
    indexar_datos.indexar("agn_documentos_trd", resultado["id"], expediente_id)    
    resultado["accion"] = accion    

    return resultado

def modificar_archivo(accion, datos={}, archivos=[], id_tarea=""):
    expediente_id  = datos['expediente_id']
    archivo_id     = datos["datos"]['id']
    soporte        = datos["datos"]['soporte']    
    datos_archivos = {
        "tabla"         : "TRD", 
        "expediente_id" : expediente_id, 
        "detalle"       : datos["datos"]["detalle"], 
        "observacion"   : datos["datos"].get("observacion", ""),         
        "fecha_creacion": datos["datos"]["fecha_creacion"], 
        "tipo_id"       : datos["datos"]["tipo_id"],
        "fecha_funcion" : "RSA-MD5",
        "soporte"       : soporte
    }
    # Atributos por soporte
    datos_archivos["folios_fisicos"] = 0
    if soporte in ["DIGITALIZADO", "FISICO"]:
        datos_archivos["folios_fisicos"] = datos["datos"]["folios_fisicos"]        
    
    resultado = sqalchemy_modificar.modificar_un_registro("agn_documentos_trd", archivo_id, datos_archivos)
    logs.log_trd("agn_expedientes_trd", expediente_id, "MODIFICACION DOCUMENTO", ("MODIFICA DOCUMENTO: " + datos["datos"]["detalle"]), id_tarea)
    # Indexa registros y anexos, falta indexar expediente
    indexar_datos.salvar_anexos("insertar", {"id": archivo_id}, archivos, id_tarea)
    indexar_datos.indexar("agn_documentos_trd", archivo_id, expediente_id)    
    
    resultado["accion"] = accion    

    return resultado

def borrar_archivo(accion, datos={}, archivos=[], id_tarea=""):
    archivo_id = datos["datos"]["id"]
    expediente_id = datos['expediente_id']
    resultado  = sqalchemy_borrar.borrar_un_registro("agn_documentos_trd", archivo_id)
    logs.log_trd("agn_expedientes_trd", expediente_id, "BORRA DOCUMENTO" , ("BORRA DOCUMENTO: " + datos["datos"]["detalle"]), id_tarea)
    elastic_operaciones.eliminar_registro("agn_documentos_trd", archivo_id)
    indexar_datos.indexar("agn_documentos_trd", archivo_id, expediente_id)   
    resultado["accion"] = accion
    
    return resultado

# Crea archivo xml para indice
def genera_xml(expediente, data_expediente, nombreArchivo):
    print("XML --------------------------------")
    indice = ET.Element('TipoDocumentoFoliado')
    indice.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    for DocumentoIndizado in data_expediente['documentos_ie']:
        elemento = ET.SubElement(indice, 'DocumentoIndizado')
        # Id
        id       = ET.SubElement(elemento, 'id')
        id.text  = DocumentoIndizado["id"]
        # Nombre_Documento
        Nombre_Documento      = ET.SubElement(elemento, 'Nombre_Documento')
        Nombre_Documento.text = DocumentoIndizado["nombre_documento"]
        # Tipologia_Documental
        Tipologia_Documental      = ET.SubElement(elemento, 'Tipologia_Documental')
        Tipologia_Documental.text = DocumentoIndizado["tipologia_documental"]
        # Fecha_Creacion_Documento
        Fecha_Creacion_Documento      = ET.SubElement(elemento, 'Fecha_Creacion_Documento')
        Fecha_Creacion_Documento.text = DocumentoIndizado["fecha_creacion_documento"]
        # Fecha_Creacion_Documento
        Fecha_Incorporacion_Expediente      = ET.SubElement(elemento, 'Fecha_Incorporacion_Expediente')
        Fecha_Incorporacion_Expediente.text = DocumentoIndizado["fecha_incorporacion_expediente"]
        # Valor_Huella
        Valor_Huella      = ET.SubElement(elemento, 'Valor_Huella')
        Valor_Huella.text = DocumentoIndizado["valor_huella"]
        # Funcion_Resumen
        Funcion_Resumen      = ET.SubElement(elemento, 'Funcion_Resumen')
        Funcion_Resumen.text = DocumentoIndizado["funcion_resumen"]
        # Orden_Documento_Expediente
        Orden_Documento_Expediente      = ET.SubElement(elemento, 'Orden_Documento_Expediente')
        Orden_Documento_Expediente.text = str(DocumentoIndizado["orden_documento_expediente"])
        # Pagina_Inicio
        Pagina_Inicio      = ET.SubElement(elemento, 'Orden_Documento_Expediente')
        Pagina_Inicio.text = str(DocumentoIndizado["pagina_inicio"])
        # Pagina_Fin
        Pagina_Fin      = ET.SubElement(elemento, 'Pagina_Fin')
        Pagina_Fin.text = str(DocumentoIndizado["pagina_fin"])
        # Formato
        Formato      = ET.SubElement(elemento, 'Formato')
        Formato.text = str(DocumentoIndizado["formato"])
        # Tamano
        Tamano      = ET.SubElement(elemento, 'Tamano')
        Tamano.text = str(DocumentoIndizado["tamano"])    
    tree = ET.ElementTree(indice)
    tree.write(nombreArchivo)
  
    return nombreArchivo