#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, pprint, tempfile, base64

import xlsxwriter
from operator import itemgetter

from librerias.datos.sql  import sqalchemy_leer
from librerias.utilidades import basicas  

# Crea archivo Excel, con los titulos de la columna
def crear_excel_base( datos ):  
    archivo_destino = tempfile.gettempdir() + os.sep + basicas.uuidTexto() + ".xlsx" 
    columnas        = [
        {
            'campo' : 'codigo',
            'titulo': 'Codigo',
            'ancho' : '50'
        },

        {
            'campo' : 'nombre',
            'titulo': 'Nombre',
            'ancho' : '50'
        }, 

        {
            'campo' : 'tipo',
            'titulo': 'Tipo',
            'ancho' : '50'
        }
    ]  
    columnas_nombre = [columna['campo'] for columna in columnas]
    
    # Tamano
    contador = 0
    for item in datos["trd_arbol"]:
        contador += 1
        valores  = itemgetter(*columnas_nombre)( item )
        for index, valor in enumerate( valores ):
            if valor  in ["None", None]: valor = ""
            ancho = int( len( str(valor) ) * 1.2 )
            if ancho > int(columnas[index]["ancho"]):       
                columnas[index]["ancho"] = ancho
    
    workbook  = xlsxwriter.Workbook( archivo_destino )
    worksheet = workbook.add_worksheet()
    # Formatos 
    formato = workbook.add_format({'bold': True, 'font_color': 'black', 'font': {'size': 40}})
    bold    = workbook.add_format({'bold': True})    
    worksheet.write( 'A1', "Descripción" )
    worksheet.write( 'B1', datos["nombre"] )
    worksheet.write( 'A2', "Versión" )
    worksheet.write( 'B2', datos["version"] )
    
    # Titulos de las columnas
    fila = 3
    for index, columna in enumerate( columnas ):
        letra = xlsxwriter.utility.xl_col_to_name( index )
        letra = letra + ':' + letra
        worksheet.set_column( letra, int(columna["ancho"]) )
        worksheet.write( fila, index, columna["titulo"], bold )    
    
    return workbook, worksheet, columnas, archivo_destino

# Imprime datos 
def salva_excel( worksheet, columnas, items ):
    fila = 4
    for item in items:  
        blancos = ""  
        if item["tipo"] == "serie"   : blancos = "  "
        if item["tipo"] == "subserie": blancos = "      "
        if item["tipo"] == "tipo"    : blancos = "            "        
        for indice, columna in enumerate( columnas ):
            campo = columna["campo"]            
            valor = item.get( campo, "" )
            if valor in ["None", None]: valor = ""
            if campo in ["codigo", "nombre"]: valor = blancos + valor 
            worksheet.write( fila, indice, valor )
        fila += 1
    
def genera_excel(trd_id):
    # Lee TRD
    trd_registro = sqalchemy_leer.leer_un_registro("agn_trd", trd_id)

    # Crea excel
    workbook, worksheet, columnas, nombre_archivo = crear_excel_base( trd_registro )    
    salva_excel( worksheet, columnas, trd_registro["trd_arbol"] )
    workbook.close()
    
    return nombre_archivo

def exportar(accion, datos={}, archivo=[], id_tarea=""):
    trd_id = datos['datos']['trd_id'][0]
    print("")
    print("trd_id:")
    pprint.pprint(trd_id)
    print("")
    print("")
    nombre_archivo = genera_excel(trd_id)
    print("nombre_archivo:", nombre_archivo)
    nombre_byte     = nombre_archivo.encode('ascii')
    nombre_64       = base64.b64encode( nombre_byte )
    nombre_64_texto = str(nombre_64, 'utf-8')

    return nombre_64_texto