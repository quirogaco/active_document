#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, pprint, tempfile, base64

import xlsxwriter
from operator import itemgetter

from librerias.utilidades import basicas  

# Crea archivo Excel, con los titulos de la columna
def crear_excel_base( datos ):  
    archivo_destino = tempfile.gettempdir() + os.sep + basicas.uuidTexto() + ".xlsx" 
    columnas        = [
        {
            'campo' : 'fecha_creacion',
            'titulo': 'FECHA',
            'ancho' : '32'
        },

        {
            'campo' : 'detalle',
            'titulo': 'DESCRIPCIÓN',
            'ancho' : '40'
        },

        {
            'campo' : 'tipo',
            'titulo': 'TIPO DOCUMENTAL',
            'ancho' : '40'
        },

        {
            'campo' : 'fecha_creacion',
            'titulo': 'FECHA DE CREACIÓN',
            'ancho' : '30'
        },

        {
            'campo' : 'fecha_incorporado',
            'titulo': 'FECHA DE INCORPORACIÓN',
            'ancho' : '30'
        },

        {
            'campo' : 'soporte',
            'titulo': 'SOPORTE',
            'ancho' : '30'
        },

         {
            'campo' : 'tamano',
            'titulo': 'TAMAÑO',
            'ancho' : '30'
        },

        {
            'campo' : 'folios_electronicos',
            'titulo': 'FOLIO(S)',
            'ancho' : '15'
        },

        {
            'campo' : 'observacion',
            'titulo': 'OBSERVACIÓN',
            'ancho' : '40'
        },
    ]  
    columnas_nombre = [columna['campo'] for columna in columnas]

    # Tamano
    contador = 0
    for item in datos["documentos"]:
        contador += 1
        valores  = itemgetter(*columnas_nombre)( item )
        for index, valor in enumerate( valores ):
            if valor  in ["None", None]: valor = ""
            ancho = int( len( str(valor) ) * 1.2 )
            if ancho > int(columnas[index]["ancho"]):       
                columnas[index]["ancho"] = ancho
    
    workbook  = xlsxwriter.Workbook( archivo_destino )
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True, 'font_color': 'black', 'font': {'size': 40} })
    #bold = {'bold': True, 'font_color': 'black', 'font': {'size': 40}, 'bg_color': '#33CCCC' }
    
    # Titulos     
    worksheet.insert_image( 'A1', "D:/gestor_2021_vite/aplicacion/expedientes/logo-esap.png" )
    titulo_formato = workbook.add_format({
        'bottom': 6, 
        #'bg_color': '#33CCCC',
        'bold': True, 
        'font_color': 'black', 
        'font': {'size': 40}
    })
    worksheet.write( 'B2', "INDICE ELECTRÓNICO", bold )
    worksheet.write( 'C2', "", bold )
    
    # Version
    worksheet.write( 'A4', "Versión", bold )
    worksheet.write( 'B4', datos["serie_version"] )
    
    # Fecha
    worksheet.write( 'C4', "Fecha", bold )
    worksheet.write( 'D4', "" )
    
    # Codigo formato
    worksheet.write( 'E4', "Codigo", bold )

    # Codigo expediente
    worksheet.write( 'A5', "Codigo expediente", bold )
    worksheet.write( 'B5', datos["codigo"] )

    # Nombre
    worksheet.write( 'C5', "Asunto:", bold )
    worksheet.write( 'D5', datos["nombre"] )

    # Generales
    worksheet.write( 'A6', "Dependencia:", bold )
    worksheet.write( 'B6', datos["dependencia_nombre"] )
    worksheet.write( 'D6', "Serie/Subserie:", bold )
    worksheet.write( 'E6', datos["serie_subserie"] )
    
    # Titulos de las columnas
    fila = 7
    for index, columna in enumerate( columnas ):
        letra = xlsxwriter.utility.xl_col_to_name( index )
        letra = letra + ':' + letra
        worksheet.set_column( letra, int(columna["ancho"]) )
        worksheet.write( fila, index, columna["titulo"], bold )    
    
    return workbook, worksheet, columnas, archivo_destino

# Imprime datos 
def salva_excel( workbook, worksheet, columnas, items ):
    fila = 8
    for item in items:  
        if item["soporte"] in ["ELECTRONICO", "DIGITALIZADO"]:
            for indice, columna in enumerate( columnas ):            
                campo = columna["campo"]            
                valor = str(item.get( campo, "" ))
                if valor in ["None", None]: valor = ""
                worksheet.write( fila, indice, valor )
            fila += 1

    formato = workbook.add_format({'bold': True, 'font_color': 'black', 'font': {'size': 40}})    
    fila += 1
    worksheet.write( fila, 1, "RESPONSABLES DE MANEJAR EL EXPEDIENTE", formato )
    worksheet.write( fila+1, 0, "FIRMA:" )
    worksheet.write( fila+2, 0, "NOMBRE:" )
    worksheet.write( fila+3, 0, "PERIODO:" )
    
def genera_excel(dato):    
    workbook, worksheet, columnas, nombre_archivo = crear_excel_base( dato )    
    salva_excel( workbook, worksheet, columnas, dato["documentos"] )
    workbook.close()
    
    return nombre_archivo

def imprimir_indice(accion, datos={}, archivo=[], id_tarea=""):
    expediente = datos['datos']['expediente']
    documentos = expediente["documentos"]
    lista      = []
    for documento in documentos:
        if documento["soporte"] in ["FISICO", "DIGITALIZADO"]:
            documento["fecha_creacion"] = str(documento["fecha_creacion"])[0:10]
            lista.append(documento)
        
    expediente["documentos"] = lista

    nombre_archivo = genera_excel(expediente)
    nombre_byte     = nombre_archivo.encode('ascii')
    nombre_64       = base64.b64encode( nombre_byte )
    nombre_64_texto = str(nombre_64, 'utf-8')

    return nombre_64_texto