#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import datetime, uuid

########
# GRID #
########

def filtrar_columna(campo, tipoElastic):
   filtrar_tipos = ["texto", "fecha", "clave"]
   filtrar       = 'no'
   if tipoElastic in filtrar_tipos:
      filtrar = 'si'

   return filtrar

def ordenar_columna(campo, tipoElastic):
   ordenar_tipos = ["texto", "fecha", "clave"]
   ordenar       = 'no'
   if tipoElastic in ordenar_tipos:
      ordenar = 'si'

   return ordenar

def adaptador_columna_grid(campo, atributos_base={}, atributos_especificos={}):
   tipoElastic = atributos_base.get('tipoElastic', 'sin tipo')
   atributos_columna = {
      'tipo'  : atributos_base.get('tipo', 'texto'),
      'campo' : campo,
      'titulo': atributos_base.get('titulo', 'sin titulo'),
      'ancho' : (atributos_base.get('longitud', 50) * 2),
      'filtra': filtrar_columna(campo, tipoElastic),
      'ordena': ordenar_columna(campo, tipoElastic) 
   }
   atributos_columna.update(atributos_especificos)

   return atributos_columna

def adaptador_grid(estructura, columnas, titulo, atributos_especificos={}):  
   atributos_grid = {
      'estructura': estructura,
      'columnas'  : columnas,
      'titulos'  : {
         'principal': titulo,
         'crear'    : atributos_especificos.get('crear', '>.')  
      }   
   }
   atributos_grid.update(atributos_especificos)

   return atributos_grid

#########
# FORMA #
#########
def adaptador_campo_forma(campo, atributos_base={}, atributos_especificos={}):
   """
   editable   -> "si", "no" -> defecto "si"
   modo       -> "text", "date", "email" -> defecto "text" 
   expandir   -> "si" -> defecto null
   editorType -> ""   -> defecto -> "dxTextBox"
   """
   atributos_campo = {
      'tipo'       : atributos_base.get('tipo', 'texto'),
      'tipoeditor' : atributos_base.get('tipo', 'texto'),
      'modo'       : atributos_base.get('modo', 'text'),
      'campo'      : campo,
      'obligatorio': atributos_base.get('obligatorio', 'no'),
      'titulo'     : atributos_base.get('titulo', 'sin titulo'),
      'maximo'     : atributos_base.get('longitud', None),
      
      # Datos para select, tag
      'fuente'     : atributos_base.get('fuente', None),
      'filtros'    : atributos_base.get('filtros', None),
   }
   atributos_campo.update(atributos_especificos)

   return atributos_campo

def adaptador_forma(estructura, campos, titulo, atributos_especificos={}):  
   """
      'estructura'   : 'radicado_pqr',
      "titulo"       : "Información del Radicado PQRS",
      'campos'       : campos,
      'ajustaPalabra': 'si',
      'lectura'   : 'si',
      'columnas'  : 2,
      'botones'   : {
         crea    : false, 
         modifica: false, 
         elimina : false, 
         regresa : true
      },
      "metodos"   : {
         "cambiaDatosEvento": function(forma, datos) {
               // Grid de logs
               window.scroll(0,0);
               let gridLog   = window.$ns["radicado_pqr_logs"]
               let datosLog  = datos["logs"];            
               let fuenteLog = new ArrayStore({
                  data: datosLog,
                  key : 'id'
               })
               gridLog.option('dataSource', fuenteLog);
               
               // Grid de anexos
               let gridAnexo   = window.$ns["radicado_pqr_anexos"]
               let datosAnexo  = datos["anexos"];            
               let fuenteAnexo = new ArrayStore({
                  data: datosAnexo,
                  key : 'id'
               })
               gridAnexo.option('dataSource', fuenteAnexo);
         }
      }
   }
   """

   atributos_forma = {
      'estructura': estructura,
      'campos'    : campos,
      'titulo'    : titulo
   }
   atributos_forma.update(atributos_especificos)
   
   return atributos_forma