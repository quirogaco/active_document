#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

import xml.etree.ElementTree as ET

import configuracion_base

from librerias.datos.elastic import elastic_operaciones
from librerias.datos.base    import globales

from librerias.datos.sql         import sqalchemy_modificar, sqalchemy_leer, sqalchemy_insertar, sqalchemy_borrar
from librerias.datos.elastic     import elastic_operaciones
from librerias.flujos            import flujos_insertar_sql
from librerias.utilidades        import basicas  
from librerias.datos.estructuras import estructura_operaciones


conexion   = globales.lee_conexion_elastic("base")

# Crea archivo xml para indice
def genera_xml(data_expediente, nombreArchivo):
    print("XML --------------------------------")
    indice = ET.Element('TipoDocumentoFoliado')
    indice.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    contador = 0
    for DocumentoIndizado in data_expediente['documentos']:
        contador += 1
        elemento = ET.SubElement(indice, 'DocumentoIndizado')
        # Id
        id       = ET.SubElement(elemento, 'id')
        id.text  = DocumentoIndizado["id"]
        # Nombre_Documento
        Nombre_Documento      = ET.SubElement(elemento, 'Nombre_Documento')
        Nombre_Documento.text = DocumentoIndizado["detalle"]
        # Tipologia_Documental
        Tipologia_Documental      = ET.SubElement(elemento, 'Tipologia_Documental')
        Tipologia_Documental.text = DocumentoIndizado["tipo_nombre"]
        # Fecha_Creacion_Documento
        Fecha_Creacion_Documento      = ET.SubElement(elemento, 'Fecha_Creacion_Documento')
        Fecha_Creacion_Documento.text = str(DocumentoIndizado["fecha_creacion"])
        # Fecha_Creacion_Documento
        Fecha_Incorporacion_Expediente      = ET.SubElement(elemento, 'Fecha_Incorporacion_Expediente')
        Fecha_Incorporacion_Expediente.text = str(DocumentoIndizado["fecha_incorporado"])
        # Valor_Huella
        Valor_Huella      = ET.SubElement(elemento, 'Valor_Huella')
        Valor_Huella.text = DocumentoIndizado["valor_huella"]
        # Funcion_Resumen
        Funcion_Resumen      = ET.SubElement(elemento, 'Funcion_Resumen')
        Funcion_Resumen.text = str(DocumentoIndizado["fecha_funcion"])
        # Orden_Documento_Expediente
        Orden_Documento_Expediente      = ET.SubElement(elemento, 'Orden_Documento_Expediente')
        Orden_Documento_Expediente.text = str(contador)
        # Pagina_Inicio
        Pagina_Inicio      = ET.SubElement(elemento, 'Pagina_Inicio')
        Pagina_Inicio.text = str(0)
        # Pagina_Fin
        Pagina_Fin      = ET.SubElement(elemento, 'Pagina_Fin')
        Pagina_Fin.text = str(DocumentoIndizado["folios_electronicos"])
        # Formato
        Formato      = ET.SubElement(elemento, 'Formato')
        Formato.text = str(DocumentoIndizado["tipo_archivo"])
        # Tamano
        Tamano      = ET.SubElement(elemento, 'Tamano')
        Tamano.text = str(DocumentoIndizado["tamano"])    
    tree = ET.ElementTree(indice)
    tree.write(nombreArchivo)
  
    return nombreArchivo


def expediente_indice():
    data_expediente = sqalchemy_leer.leer_un_registro("agn_expedientes_trd", "27f4b68b-3fce-11ec-bdee-086266b539c1")
    pprint.pprint(data_expediente)
    genera_xml(data_expediente, "indice.xml")

expediente_indice()