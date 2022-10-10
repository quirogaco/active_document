#!/usr/bin/python
# -*- coding: UTF-8 -*-

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, pprint, tempfile, base64

import xlsxwriter
from operator import itemgetter

from librerias.utilidades import basicas  

"""
        {
            'campo' : 'dependencia_nombre',
            'titulo': 'DEPENDENCIA',
            'ancho' : '35'
        }, 
"""       

# Crea archivo Excel, con los titulos de la columna
def crear_excel_base( datos ):  
    archivo_destino = tempfile.gettempdir() + os.sep + basicas.uuidTexto() + ".xlsx" 
    columnas        = [
        {
            'campo' : 'consecutivo',
            'titulo': 'NÚMERO DE ORDEN',
            'ancho' : '25'
        },

        {
            'campo' : 'codigo',
            'titulo': 'CODIGO',
            'ancho' : '15'
        },

        {
            'campo' : 'serie_nombre',
            'titulo': 'SERIE',
            'ancho' : '30'
        },

        {
            'campo' : 'subserie_nombre',
            'titulo': 'SUBSERIE',
            'ancho' : '30'
        },

        {
            'campo' : 'nombre',
            'titulo': 'ASUNTO',
            'ancho' : '30'
        },

        {
            'campo' : '#',
            'titulo': 'CONSECUTIVO',
            'ancho' : '10'
        }, 

        {
            'campo' : 'fecha_inicial',
            'titulo': 'FECHA INICIAL',
            'ancho' : '15'
        },

        {
            'campo' : 'fecha_final',
            'titulo': 'FECHA FINAL',
            'ancho' : '15'
        },

        {
            'campo' : 'carpetas',
            'titulo': 'CARPETA',
            'ancho' : '10'
        },

        {
            'campo' : 'carpetas',
            'titulo': 'TOMO',
            'ancho' : '10'
        },

        {
            'campo' : 'caja',
            'titulo': 'CAJA',
            'ancho' : '10'
        },

        {
            'campo' : '#',
            'titulo': 'OTRO',
            'ancho' : '10'
        }, 

        {
            'campo' : 'folios_fisicos',
            'titulo': 'FOLIOS FISICOS',
            'ancho' : '25'
        },

        {
            'campo' : 'folios_electronicos',
            'titulo': 'FOLIOS ELECTRÓNICOS',
            'ancho' : '25'
        },

        {
            'campo' : 'tipo_expediente',
            'titulo': 'SOPORTE',
            'ancho' : '25'
        },
        
    ]  
    columnas_nombre = [columna['campo'] for columna in columnas]
    
    # Tamano
    contador = 0
    for item in datos:
        item["#"] = ""
        contador += 1
        valores = itemgetter(*columnas_nombre)( item )
        for index, valor in enumerate( valores ):
            if valor in ["None", None]: valor = ""
            ancho = int( len( str(valor) ) * 1.2 )
            if ancho > int(columnas[index]["ancho"]):       
                columnas[index]["ancho"] = ancho
    
    workbook  = xlsxwriter.Workbook( archivo_destino )
    worksheet = workbook.add_worksheet()
    # Titulos     
    worksheet.insert_image( 'A1', "D:/gestor_2021_vite/aplicacion/expedientes/logo-esap.png" )

    # Formatos 
    formato = workbook.add_format({'bold': True, 'font_color': 'black', 'font': {'size': 20}})
    worksheet.write( 'D2', "FORMATO ÚNICO DE INVENTARIO DOCUMENTAL", formato )
    worksheet.write( 'B4', "DOCUMENTOS DE REFERENCIA:  DC-A-GD-01 / PT-A-GD-05 / PT-A-GD-04", formato )
    worksheet.write( 'E5', "Hoja No.", formato )
    worksheet.write( 'F5', "de", formato )

    worksheet.write( 'A6', "ENTIDAD PRODUCTORA", formato)
    worksheet.write( 'E6', "AÑO", formato )
    worksheet.write( 'F6', "MES", formato )
    worksheet.write( 'G6', "DIA", formato )
    worksheet.write( 'H6', "N.T.", formato )

    worksheet.write( 'B6', "Escuela Superior de Administración Pública")
    worksheet.write( 'A7', "UNIDAD ADMINISTRATIVA", formato)
    worksheet.write( 'A8', "OFICINA PRODUCTORA", formato )
    worksheet.write( 'A9', "OBJETO", formato )
    
    # Titulos de las columnas
    fila = 12
    for index, columna in enumerate( columnas ):
        letra = xlsxwriter.utility.xl_col_to_name( index )
        letra = letra + ':' + letra
        worksheet.set_column( letra, int(columna["ancho"]) )
        worksheet.write( fila, index, columna["titulo"], formato )    
    
    return workbook, worksheet, columnas, archivo_destino

# Imprime datos 
def salva_excel( workbook, worksheet, columnas, items ):
    fila = 13
    for item in items:  
        for indice, columna in enumerate( columnas ):
            campo = columna["campo"]    
            valor = ""
            if campo != "#":        
                valor = str(item.get( campo, "" ))
            if valor in ["None", None]: valor = ""
            worksheet.write( fila, indice, valor )
        fila += 1

    formato = workbook.add_format({'bold': True, 'font_color': 'black', 'font': {'size': 20}})
    worksheet.write(fila+1, 0, "ELABORADO POR:", formato )
    worksheet.write(fila+1, 3, "ENTREGADO POR:", formato )
    worksheet.write(fila+1, 6, "RECIBIDO POR:", formato )
    
    worksheet.write(fila+2, 0, "CARGO:", formato )
    worksheet.write(fila+2, 3, "CARGO:", formato )
    worksheet.write(fila+2, 6, "CARGO:", formato )

    worksheet.write(fila+3, 0, "FIRMA:", formato )
    worksheet.write(fila+3, 3, "FIRMA:", formato )
    worksheet.write(fila+3, 6, "FIRMA:", formato )

    worksheet.write(fila+3, 0, "FECHA:", formato )
    worksheet.write(fila+3, 3, "FECHA:", formato )
    worksheet.write(fila+3, 6, "FECHA:", formato )

    worksheet.write(fila+4, 0, "Nota: Parte sombreada para uso exclusivo de los funcionarios  del Archivo Central")

def genera_excel(expedientes=[]):
    # Lee EXPEDIENTES
    #expedientes = sqalchemy_leer.leer_todos("base", "agn_expedientes_trd", desde=0, hasta=1000)
    pprint.pprint(expedientes)

    consecutivo = 0
    for item in expedientes:  
        consecutivo += 1
        item["consecutivo"]   = consecutivo
        item["fecha_inicial"] = str(item["fecha_inicial"])[0:10]
        item["fecha_final"]   = str(item["fecha_final"])[0:10]

    # Crea excel
    workbook, worksheet, columnas, nombre_archivo = crear_excel_base( expedientes )    
    salva_excel( workbook, worksheet, columnas, expedientes )
    workbook.close()
    
    return nombre_archivo

def imprimir_fuid(accion, datos={}, archivo=[], id_tarea=""):
    expedientes = datos['datos']['expedientes']
    nombre_archivo = genera_excel(expedientes)
    nombre_byte     = nombre_archivo.encode('ascii')
    nombre_64       = base64.b64encode( nombre_byte )
    nombre_64_texto = str(nombre_64, 'utf-8')

    return nombre_64_texto