#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.base import globales

# Radicados migrados
radicado_migrado  = {
   "definicion": {
      "id"    : "30",
      "nombre": "MIGRACIÓN - Radicados migrados Pqrs"
   },

   "grid": {
      "componente": "radicado_pqr_grid",     
      "texto"     : "Radicados migrados Pqrs",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "MigraciÓn",
   },

   "forma": {
      "componente": "radicado_pqr_forma",      
      "texto"     : "Radicados migrados Pqrs",
      "tipo"      : "importar"
   }
}

#############################
# HISTORICO ARCHIVO MIGRADO #
#############################
archivo_historico_migrado = {
   "definicion": {
      "id"    : "31",
      "nombre": "MIGRACIÓN - Archivo historico"
   },

   "grid": {
      "componente": "archivo_historico_migrado_grid",     
      "texto"     : "Archivo historico",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "MigraciÓn",
   }
}

################################
# VENTANILLA RADICADO ENETRADA #
################################
entradas_ventanilla_migrado = {
   "definicion": {
      "id"    : "32",
      "nombre": "MIGRACIÓN - Entradas Migrados Ventanilla"
   },

   "grid": {
      "componente": "entradas_ventanilla_grid",     
      "texto"     : "Entradas Migrados Ventanilla",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "MigraciÓn",
   },

   "forma": {
      "componente": "entradas_ventanilla_forma",      
      "texto"     : "Entradas radicados Ventanilla",
      "tipo"      : "importar"
   }
}

internos_ventanilla_migrado = {
   "definicion": {
      "id"    : "33",
      "nombre": "MIGRACIÓN - Internos Migrados Ventanilla"
   },

   "grid": {
      "componente": "internos_ventanilla_grid",     
      "texto"     : "Internos Migrados Ventanilla",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "MigraciÓn",
   },

   "forma": {
      "componente": "internos_ventanilla_forma",      
      "texto"     : "Internos radicados Ventanilla",
      "tipo"      : "importar"
   }
}

salidas_ventanilla_migrado = {
   "definicion": {
      "id"    : "34",
      "nombre": "MIGRACIÓN - Salidas Migrados Ventanilla"
   },

   "grid": {
      "componente": "salidas_ventanilla_grid",     
      "texto"     : "Salidas Migrados Ventanilla",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "MigraciÓn",
   },

   "forma": {
      "componente": "salidas_ventanilla_forma",      
      "texto"     : "Salidas radicadas  Ventanilla",
      "tipo"      : "importar"
   }
}

opciones = [
   # RADICADOS PQRS MIGRADOS
   radicado_migrado,

   # Archivo historico migrado
   archivo_historico_migrado,

   # VENTANILLA RADICADOS ENTRADAS MIGRADOS
   entradas_ventanilla_migrado,

   # VENTANILLA INTERNOS ENTRADAS MIGRADOS
   internos_ventanilla_migrado,

   # VENTANILLA SALIDAS ENTRADAS MIGRADOS
   salidas_ventanilla_migrado
]