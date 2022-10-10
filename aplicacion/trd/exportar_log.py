#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, pprint, tempfile, base64

import xlsxwriter
from operator import itemgetter

from librerias.utilidades import basicas  
from librerias.datos.sql  import sqalchemy_filtrar 

# Crea archivo Excel, con los titulos de la columna
def crear_excel_base( datos ):  
    archivo_destino = tempfile.gettempdir() + os.sep + basicas.uuidTexto() + ".xlsx" 
    columnas        = [
        {
            'campo' : 'creado_en_',
            'titulo': 'Fecha',
            'ancho' : '50'
        },

        {
            'campo' : 'accionante_nombre',
            'titulo': 'Accionante',
            'ancho' : '100'
        },

        {
            'campo' : 'accion',
            'titulo': 'Accion',
            'ancho' : '100'
        }, 

        {
            'campo' : 'detalle',
            'titulo': 'Detalle',
            'ancho' : '100'
        }
    ]  
    columnas_nombre = [columna['campo'] for columna in columnas]
    
    # Tamano
    contador = 0
    for item in datos:
        contador += 1
        valores  = itemgetter(*columnas_nombre)( item )
        for index, valor in enumerate( valores ):
            if valor  in ["None", None]: valor = ""
            ancho = int( len( str(valor) ) * 1.2 )
            if ancho > int(columnas[index]["ancho"]):       
                columnas[index]["ancho"] = ancho
    
    workbook  = xlsxwriter.Workbook( archivo_destino )
    worksheet = workbook.add_worksheet()
    # Titulos de las columnas
    fila = 3
    for index, columna in enumerate( columnas ):
        letra = xlsxwriter.utility.xl_col_to_name( index )
        letra = letra + ':' + letra
        worksheet.set_column( letra, int(columna["ancho"]) )
        worksheet.write( fila, index, columna["titulo"] )    
    
    return workbook, worksheet, columnas, archivo_destino

# Imprime datos 
def salva_excel( worksheet, columnas, items ):
    fila = 4
    for item in items:  
        for indice, columna in enumerate( columnas ):
            campo = columna["campo"]            
            valor = item.get( campo, "" )
            if campo == "creado_en_": valor = str(valor)
            if valor in ["None", None]: valor = ""
            worksheet.write( fila, indice, valor )
        fila += 1
    
def genera_excel(fuente, fuente_id):
    # Lee datos logs
    ordenar = [ [ "descendente", "creado_en_" ] ]
    filtros = [ [ "fuente", "=", fuente ], [ "fuente_id", "=", fuente_id ] ]
    logs    = sqalchemy_filtrar.filtrarOrdena(estructura="logs", filtros=filtros, ordenamientos=ordenar)
    
    # Crea excel
    workbook, worksheet, columnas, nombre_archivo = crear_excel_base( logs )    
    salva_excel( worksheet, columnas, logs)
    workbook.close()
    
    return nombre_archivo

def exportar_log(accion, datos={}, archivo=[], id_tarea=""):
    fuente    = datos['datos']['fuente']
    fuente_id = datos['datos']['fuente_id'][0]
    print("")
    print("fuente:", fuente, fuente_id)
    print("")
    print("")
    nombre_archivo = genera_excel(fuente, fuente_id)
    nombre_byte     = nombre_archivo.encode('ascii')
    nombre_64       = base64.b64encode( nombre_byte )
    nombre_64_texto = str(nombre_64, 'utf-8')

    return nombre_64_texto