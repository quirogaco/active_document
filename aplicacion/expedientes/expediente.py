#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pprint, datetime, random, base64, builtins, tempfile, os
import requests

from librerias.datos.sql             import sqalchemy_modificar, sqalchemy_insertar, sqalchemy_borrar, sqalchemy_leer
from librerias.datos.elastic         import elastic_operaciones
from librerias.documentos.conversion import conversion
from librerias.utilidades            import basicas 
from aplicacion.trd                  import logs

# TRD
def crear_expediente(accion, datos={}, archivo=[], id_tarea=""):
    # Expediente
    caja                  = datos["datos"].get("caja", 0)
    if caja is None:
        caja = 0
    ubicacion_topografica = datos["datos"].get("ubicacion_topografica", "")  
    datos_expediente = {
        "tabla"      : "TRD", 
        "serie_id"   : datos["datos"]["serie_id"], 
        "subserie_id": datos["datos"]["subserie_id"], 
        "nombre"     : datos["datos"]["nombre"],
        "observacion": datos["datos"].get("observacion", ""),
        "caja"       : caja,
        "ubicacion_topografica": ubicacion_topografica  
    }
    resultado = sqalchemy_insertar.insertar_registro_estructura("agn_expedientes_trd", datos_expediente)    
    logs.log_trd("agn_expedientes_trd", resultado["id"], "CREACIÓN DE EXPEDIENTE", "CREACION", id_tarea) 

    # Carpeta
    datos_carpeta = {
        "expediente_id"        : resultado["id"], 
        "caja"                 : caja,
        "ubicacion_topografica": ubicacion_topografica,
        "carpeta_nro"          : 1,
        "tomo"                 : 1
    }
    carpeta = sqalchemy_insertar.insertar_registro_estructura("agn_carpetas_trd", datos_carpeta)
    elastic_operaciones.indexar_registro("agn_carpetas_trd", carpeta["id"])

    # Indexa EXPEDIENTE
    elastic_operaciones.indexar_registro("agn_expedientes_trd", resultado["id"])

    resultado["accion"] = accion    

    return resultado

def modificar_expediente(accion, datos={}, archivo=[], id_tarea=""):
    expediente_id = datos["datos"]["id"]
    datos_expediente = {
        "serie_id"   : datos["datos"]["serie_id"], 
        "subserie_id": datos["datos"]["subserie_id"], 
        "nombre"     : datos["datos"]["nombre"],
        "caja"       : datos["datos"].get("caja", 0),
        "observacion": datos["datos"].get("observacion", ""),
        "ubicacion_topografica": datos["datos"].get("ubicacion_topografica", "")  
    }
    resultado = sqalchemy_modificar.modificar_un_registro("agn_expedientes_trd", expediente_id, datos_expediente)
    elastic_operaciones.indexar_registro("agn_expedientes_trd", resultado["id"])
    logs.log_trd("agn_expedientes_trd", resultado["id"], "MODIFICACIÓN DE EXPEDIENTE", "MODIFICACION", id_tarea) 
    
    resultado["accion"] = accion    

    return resultado

def borrar_expediente(accion, datos={}, archivo=[], id_tarea=""):
    expediente_id = datos["datos"]["id"]
    resultado  = sqalchemy_borrar.borrar_un_registro("agn_expedientes_trd", expediente_id)
    elastic_operaciones.eliminar_registro("agn_expedientes_trd", expediente_id)
    logs.log_trd("agn_expedientes_trd", resultado["id"], "BORRAR DE EXPEDIENTE", "BORRADO", id_tarea) 

    resultado["accion"] = accion
    
    return resultado

def cerrar_expediente(accion, datos={}, archivo=[], id_tarea=""):
    expediente_id = datos["datos"]["expediente_id"]
    datos_expediente = {
        "estado": "CERRADO" 
    }
    for id in expediente_id:
        resultado = sqalchemy_modificar.modificar_un_registro("agn_expedientes_trd", id, datos_expediente)
        elastic_operaciones.indexar_registro("agn_expedientes_trd", resultado["id"])
        logs.log_trd("agn_expedientes_trd", resultado["id"], "CERRAR DE EXPEDIENTE", "CERRAR", id_tarea) 

    resultado["accion"] = accion    

    return resultado

def abrir_expediente(accion, datos={}, archivo=[], id_tarea=""):
    expediente_id = datos["datos"]["expediente_id"]
    datos_expediente = {
        "estado": "ABIERTO" 
    }
    for id in expediente_id:
        resultado = sqalchemy_modificar.modificar_un_registro("agn_expedientes_trd", id, datos_expediente)
        elastic_operaciones.indexar_registro("agn_expedientes_trd", resultado["id"])
        logs.log_trd("agn_expedientes_trd", resultado["id"], "ABRIR DE EXPEDIENTE", "ABRIR", id_tarea) 
    resultado["accion"] = accion    

    return resultado

def consulta_expediente(accion, datos={}, archivo=[], id_tarea=""):
    pprint.pprint(datos["datos"])
    expediente_id = datos["datos"]["id"]
    logs.log_trd("agn_expedientes_trd", expediente_id, "CONSULTA DE EXPEDIENTE", "CONSULTA", id_tarea) 
    resultado = {"accion": accion}    

    return resultado

def actualiza_caja_anotacion(accion, datos={}, archivo=[], id_tarea=""):
    datos              = datos["datos"]
    expediente_id      = datos["expediente_id"]    
    actualiza          = {}
    caja_transferencia = datos.get("caja_transferencia", None) 
    anotacion          = datos.get("anotacion", None) 
    if (caja_transferencia != None):
        actualiza = {
          "caja_transferencia": caja_transferencia  
        }
    if (anotacion != None):
        actualiza = {
          "anotacion": anotacion  
        }
    
    resultado = sqalchemy_modificar.modificar_un_registro("agn_expedientes_trd", expediente_id, actualiza)
    elastic_operaciones.indexar_registro("agn_expedientes_trd", resultado["id"])
    logs.log_trd("agn_expedientes_trd", resultado["id"], "ASIGNA CAJA/ANOTACIÓN", "CAJA/ANOTACION", id_tarea) 
    
    resultado["accion"] = accion

    return resultado

def asignar_anotacion(accion, datos={}, archivo=[], id_tarea=""):
    datos = datos["datos"]
    
    expediente_id    = datos["expediente_id"]
    datos_expediente = {
        "anotacion": datos["anotacion"] 
    }
    resultado = sqalchemy_modificar.modificar_un_registro("agn_expedientes_trd", expediente_id, datos_expediente)
    elastic_operaciones.indexar_registro("agn_expedientes_trd", resultado["id"])
    logs.log_trd("agn_expedientes_trd", resultado["id"], "ASIGNA ANOTACIÓN TRANSFERENCIA", "ANOTACIÓN", id_tarea) 
    
    resultado["accion"] = accion

    return resultado

def permite_eliminar(accion, datos={}, archivo=[], id_tarea=""):
    datos = datos["datos"]    
    for expediente_id in datos["expediente_id"]:
        datos_expediente = {
            "eliminar": "SI"
        }
        resultado = sqalchemy_modificar.modificar_un_registro("agn_expedientes_trd", expediente_id, datos_expediente)
        elastic_operaciones.indexar_registro("agn_expedientes_trd", resultado["id"])
        logs.log_trd("agn_expedientes_trd", resultado["id"], "AUTORIZA ELMIMINACIÓN EN DISPOSICIÓN FINAL", "ELIMINACIÓN", id_tarea) 
    
    resultado["accion"] = accion

    return resultado

def no_permite_eliminar(accion, datos={}, archivo=[], id_tarea=""):
    datos = datos["datos"]    
    for expediente_id in datos["expediente_id"]:
        datos_expediente = {
            "eliminar": "NO"
        }
        resultado = sqalchemy_modificar.modificar_un_registro("agn_expedientes_trd", expediente_id, datos_expediente)
        elastic_operaciones.indexar_registro("agn_expedientes_trd", resultado["id"])
        logs.log_trd("agn_expedientes_trd", resultado["id"], "AUTORIZA ELMIMINACIÓN EN DISPOSICIÓN FINAL", "ELIMINACIÓN", id_tarea) 
    
    resultado["accion"] = accion

    return resultado

def disposicion_final(accion, datos={}, archivo=[], id_tarea=""):
    datos = datos["datos"] 
    resultado = {}   
    for expediente in datos["expedientes"]:
        expediente = sqalchemy_leer.leer_un_registro("agn_expedientes_trd", expediente["id"])
        print("")
        print("************************************************")
        pprint.pprint(expediente)
        print("")
        print("")

        datos_expediente = {
            "disposicion_fecha": datetime.date.today()
        }
        resultado = sqalchemy_modificar.modificar_un_registro("agn_expedientes_trd", expediente["id"], datos_expediente)
        elastic_operaciones.indexar_registro("agn_expedientes_trd", resultado["id"])
        logs.log_trd("agn_expedientes_trd", resultado["id"], "APLICA DISPOSICIÓN FINAL - " + expediente["disposicion_final"], "DISPOSICIÓN", id_tarea) 
        
    resultado["accion"] = accion

    return resultado

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
        Tipologia_Documental.text = DocumentoIndizado["tipo_detalle"]
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

# Convierte indice electronico
def convierte_indice_electronico(nombre_archivo):
    nombre_byte     = nombre_archivo.encode('ascii')
    nombre_64       = base64.b64encode( nombre_byte )
    nombre_64_texto = str(nombre_64, 'utf-8')
    url             = "http://" + str(builtins._appAnfitrion) + ":" + str(builtins._appPuerto) + '/entregar_archivo_base64/' + nombre_64_texto    
    parametros = {
        "filetype"  : "xml",
        "title"     : "convertido",
        "url"       : url
    }                
    nombre_archivo = conversion.a_pdfa(str(builtins._appServicios), "80", parametros)  

    return nombre_archivo

import xml.etree.ElementTree as ET

"""
def expediente_indice_firmar(accion, datos={}, archivo=[], id_tarea=""):
    pprint.pprint(datos)
    expediente_id   = datos["datos"][0]
    data_expediente = sqalchemy_leer.leer_un_registro("agn_expedientes_trd", expediente_id)
    archivo_indice  = tempfile.gettempdir() + os.sep + basicas.uuidTexto() + ".xml"
    genera_xml(data_expediente, archivo_indice)
    nombre_indice   = convierte_indice_electronico(archivo_indice)
    nombre_pdf      = firmar_documento(nombre_indice)

    nombre_byte     = nombre_pdf.encode('ascii')
    nombre_64       = base64.b64encode( nombre_byte )
    nombre_64_texto = str(nombre_64, 'utf-8')

    return {"nombre_archivo": nombre_64_texto}
"""

def expediente_indice(accion, datos={}, archivo=[], id_tarea=""):
    pprint.pprint(datos)
    expediente_id   = datos["datos"][0]
    data_expediente = sqalchemy_leer.leer_un_registro("agn_expedientes_trd", expediente_id)
    archivo_indice  = tempfile.gettempdir() + os.sep + basicas.uuidTexto() + ".xml"
    genera_xml(data_expediente, archivo_indice)
    nombre_indice   = convierte_indice_electronico(archivo_indice)
    nombre_byte     = nombre_indice.encode('ascii')
    nombre_64       = base64.b64encode( nombre_byte )
    nombre_64_texto = str(nombre_64, 'utf-8')

    return {"nombre_archivo": nombre_64_texto}

def firmar_salvar(url_firma, encabezado, data):
    # Firma documento
    respuesta = requests.post(url_firma, headers=encabezado, json=data)

    # Respuesta  
    respuesta_json = respuesta.json()
    # str obliga a que json compolete la descarga
    # si no se hace genera None
    pdf_64         = str(respuesta_json["documentoFirmado"])

    # Salva pdf
    ruta_destino = tempfile.gettempdir() + os.sep + basicas.uuidTexto() + "." + "pdf"
    pdf_bytes    = base64.b64decode(pdf_64, validate=True)
    f = open(ruta_destino, 'wb')
    f.write(pdf_bytes)
    f.close()

    return ruta_destino

def firmar_leer(pdf_nombre):
    with open(pdf_nombre, "rb") as pdf_file:
        pdf_base64 = base64.b64encode(pdf_file.read())
    print("FIRMA LEER:", pdf_nombre)
    return pdf_base64
    
def firmar_documento(pdf_nombre):
    #########
    # LOGIN #
    #########
    # Url firma
    url_login  = "https://8uw10ruhfj.execute-api.us-east-2.amazonaws.com/qa/authentication/api/Login"
    # Información usuario PRUEBAS
    data = {
        'usuario': 'esapuser',
        'clave'  : '7v40RK5C'
    }
    # Login para token de firma
    respuesta = requests.post(url_login, json = data)
    token     = respuesta.json()["token"]

    #########
    # FIRMA #
    #########
    # Url firma
    url_firma  = "https://8uw10ruhfj.execute-api.us-east-2.amazonaws.com/qa/signature/api/sign/pades"
    # Encabezado de autenticacón
    bearer     = "Bearer " + token
    encabezado = {'Authorization': bearer}
    # Información firma
    pdf_base64 = firmar_leer(pdf_nombre)

    # Datos envio
    data = {
        'numeroDocumento': '52412',        # Documento certificado que me entregan despues de registrar formalmente el certificado
        'base64'         : pdf_base64,
        'clave'          : 'Escuela11', # Clave certificado que me entregan despues de registrar formalmente el certificado
        "conLTV"         : False,
        "conEstampa"     : False,
        "conEstampa"     : False,
        "firmaVisible"   : False
    }

    firmado = firmar_salvar(url_firma, encabezado, data)

    print("firmado:", firmado)

    return firmado

def test(accion, datos={}, archivo=[], id_tarea=""):
    print("")
    print("------------------------ test", id_tarea)
    pprint.pprint(datos)
    pprint.pprint(archivo)
    print("")
    print("")
    
    1/0
    return {}