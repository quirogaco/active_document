#!/usr/bin/python
# -*- coding: utf-8 -*- 

import pprint

from librerias.datos.base import globales

# Opciones de menu del sistema
"""
opciones_sistema_onfiguracion = {
   "grid": {
      "clase"     : "grid",
      "componente": "opciones_sistema_grid",     
      "texto"     : "Opciones Menu del Sistema",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Configuración",
      "tipo"      : "remota",
   },

   "forma": {
      "clase"     : "forma",
      "componente": "opciones_sistema_forma",      
      "texto"     : "Opciones Menu del Sistema",
      "tipo"      : "remota"
   }
}

# Acciones asociadas a a botones o links
acciones = {
   "grid": {
      "clase"     : "grid",
      "componente": "acciones_sistema_grid",     
      "texto"     : "Acciones del Sistema",
      "icon"      : "",
      "navegar"   : "si",
      "padre"     : "Configuración",
      "tipo"      : "remota"
   },

   "forma": {
      "clase"     : "forma",
      "componente": "acciones_sistema_forma",      
      "texto"     : "Acciones del Sistema",
      "tipo"      : "remota"
   }
}
"""

# ROLES
roles = {
   "definicion": {
      "id"    : "1",
      "nombre": "CONFIGURACIÓN - Roles del Sistema"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "roles_grid",     
      "texto"     : "Roles del Sistema",
      "icon"      : "",
      "navegar"   : "si",
      "padre"     : "Configuración",
      "tipo"      : "importar",
   },

   "forma": {
      "clase"     : "forma",
      "componente": "roles_formulario",      
      "texto"     : "Roles del Sistema",
      "tipo"      : "importar",
   }
}

# UBICACIONES
ubicaciones = {
   "definicion": {
      "id"    : "2",
      "nombre": "CONFIGURACIÓN - Ubicaciones geograficas"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "ubicaciones_grid",     
      "texto"     : "Ubicaciones geograficas",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Configuración",
      "tipo"      : "remota"
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "ubicaciones_forma",      
      "texto"     : "Manejo de ubicaciones",
      "tipo"      : "remota"
   }
}

# USUARIOS
usuarios = {
   "definicion": {
      "id"    : "3",
      "nombre": "CONFIGURACIÓN - Usuarios del Sistema"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "usuarios_grid",     
      "texto"     : "Usuarios del Sistema",
      "icon"      : "",
      "navegar"   : "si",
      "padre"     : "Configuración",
      "tipo"      : "remota"
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "usuarios_forma",      
      "texto"     : "Usuarios del Sistema",
      "tipo"      : "remota"
   }
}

# DEPENDENCIAS
dependencias = {
   "definicion": {
      "id"    : "4",
      "nombre": "CONFIGURACIÓN - Dependencias/Areas de la entidad"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "dependencias_grid",     
      "texto"     : "Dependencias",
      "icon"      : "",
      "navegar"   : "si",
      "padre"     : "Configuración",
      "tipo"      : "remota"
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "dependencias_forma",      
      "texto"     : "Dependencias",
      "tipo"      : "remota"
   }
}

# CONTINENTES
continentes = {
   "definicion": {
      "id"    : "5",
      "nombre": "CONFIGURACIÓN - Continentes"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "continentes_grid",     
      "texto"     : "Continentes",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Configuración",
      "tipo"      : "remota",
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "continentes_forma",      
      "texto"     : "Continentes",
      "tipo"      : "remota"
   }
}

# PAISES
paises = {
   "definicion": {
      "id"    : "6",
      "nombre": "CONFIGURACIÓN - Paises"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "paises_grid",     
      "texto"     : "Paises",
      "icon"      : "",
      "navegar"   : "si",
      "padre"     : "Configuración",
      "tipo"      : "remota",
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "paises_forma",      
      "texto"     : "Paises",
      "tipo"      : "remota",
   }
}

# DEPARTAMENTO
departamentos = {
   "definicion": {
      "id"    : "7",
      "nombre": "CONFIGURACIÓN - Departamentos"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "departamentos_grid",     
      "texto"     : "Departamentos",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Configuración",
      "tipo"      : "remota"
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "departamentos_forma",      
      "texto"     : "Departamentos",
      "tipo"      : "remota"
   }
}

# CIUDADES
ciudades = {
   "definicion": {
      "id"    : "8",
      "nombre": "CONFIGURACIÓN - Ciudades"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "ciudades_grid",     
      "texto"     : "Ciudades",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Configuración",
      "tipo"      : "remota"
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "ciudades_forma",      
      "texto"     : "Ciudades",
      "tipo"      : "remota"
   }
}

# GRUPOS USUARIOS
grupo_usuarios = {
   "definicion": {
      "id"    : "9",
      "nombre": "CONFIGURACIÓN - Grupos de usuarios"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "grupo_usuarios_grid",     
      "texto"     : "Grupos",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Configuración",
      "tipo"      : "remota"
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "grupo_usuarios_forma",      
      "texto"     : "Grupos",
      "tipo"      : "remota"
   }
}

# FESTIVO
dias_festivo = {
   "definicion": {
      "id"    : "10",
      "nombre": "CONFIGURACIÓN - Dias festivos"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "festivos_grid",     
      "texto"     : "Dias festivos",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Configuración",
      "tipo"      : "remota"
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "festivos_forma",      
      "texto"     : "Dias festivos",
      "tipo"      : "remota"
   }
}

"""
   # Opciones del sistema
   opciones_sistema_onfiguracion["grid"],
   opciones_sistema_onfiguracion["forma"],

   # Acciones del menu del sistema
   acciones["grid"],
   acciones["forma"],
"""

opciones = [
   # Roles del menu del sistema
   roles,

   # Ubicaciones geograficas
   ubicaciones,

   # Usuarios
   usuarios,

   # Dependencias
   dependencias,

   # Continentes
   continentes,

   # Paises
   paises,

   # Departamento
   departamentos,

   # Ciudades
   ciudades,

   # GRUPOS USUARIOS
   grupo_usuarios,

   # DIAS FESTIVOS
   dias_festivo
]