#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import pprint

from librerias.datos.base import globales

############################
# RADICACIN CONFIGURACION #
############################

configura_radicacion_canales = {
   "definicion": {
      "id"    : "14",
      "nombre": "CONFIGURACIÓN - Parametros generales"
   },

   "forma": {
      "componente": "configura_parametros_generales",     
      "texto"     : "Parametros generales",
      "navegar"   : "si",
      "padre"     : "Configuración",
      "tipo"      : "importar",
   }
}

# Plantilla
plantillas = {
   "definicion": {
      "id"    : "15",
      "nombre": "CONFIGURACIÓN PQRS-VENTANILLA - Plantillas del sistema"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "plantilla_grid",     
      "texto"     : "Plantillas del sistema",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Configuración PQRS-VENTANILLA",
      "tipo"      : "importar",
   },

   "forma": {
      "componente": "pantalla_plantilla",      
      "texto"     : "Pantalla de plantilla",
      "tipo"      : "importar",
   }
}

# CONSECUTIVOS
consecutivos = {
   "definicion": {
      "id"    : "16",
      "nombre": "CONFIGURACIÓN PQRS-VENTANILLA - Consecutivos"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "consecutivos_grid",     
      "texto"     : "Consecutivos",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración PQRS-VENTANILLA",
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "consecutivos_forma",      
      "texto"     : "Consecutivos",
      "tipo"      : "importar"
   }
}

# MOTIVOS DEVOLUCIÓN
motivos_devolucion = {
   "definicion": {
      "id"    : "16",
      "nombre": "CONFIGURACIÓN PQRS-VENTANILLA - Motivos devolución"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "motivo_devolucion_grid",     
      "texto"     : "Motivos devolución",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración PQRS-VENTANILLA",
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "motivo_devolucion_forma",      
      "texto"     : "Motivos devolución",
      "tipo"      : "importar"
   }
}

# Tipo de identificacion
tipo_identificaciones = {
   "definicion": {
      "id"    : "17",
      "nombre": "CONFIGURACIÓN PQRS-VENTANILLA - Tipo identificaciÓn"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "tipo_identificaciones_grid",     
      "texto"     : "Tipo identificación",
      "icon"      : "",
      "navegar"   : "si",
      "padre"     : "Configuración PQRS-VENTANILLA",
      "tipo"      : "remota"
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "tipo_identificaciones_forma",      
      "texto"     : "Tipo identificación",
      "tipo"      : "remota"
   }
}

# Genero
genero = {
   "definicion": {
      "id"    : "18",
      "nombre": "CONFIGURACIÓN PQRS-VENTANILLA - Tipo Genero"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "genero_grid",     
      "texto"     : "Genero personas",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Configuración PQRS-VENTANILLA",
      "tipo"      : "remota"
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "genero_forma",      
      "texto"     : "Genero",
      "tipo"      : "remota"
   }
}

# Tipo entidad
tipo_entidad = {
   "definicion": {
      "id"    : "19",
      "nombre": "CONFIGURACIÓN - Tipo entidad"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "tipo_entidad_grid",     
      "texto"     : "Tipo entidad",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "tipo_entidad_forma",      
      "texto"     : "Tipo entidad",
      "tipo"      : "importar"
   }
}

# Tipo de poblacion
tipo_poblacion = {
   "definicion": {
      "id"    : "20",
      "nombre": "CONFIGURACIÓN PQRS-VENTANILLA - Tipo poblaciÓn"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "tipo_poblacion_grid",     
      "texto"     : "Tipo población",
      "icon"      : "",
      "tipo"      : "remota",
      "navegar"   : "si",
      "padre"     : "Configuración PQRS-VENTANILLA",
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "tipo_poblacion_forma",      
      "texto"     : "Tipo población",
      "tipo"      : "remota"
   }
}

# Rangos de edad
rango_edad = {
   "definicion": {
      "id"    : "21",
      "nombre": "CONFIGURACIÓN PQRS-VENTANILLA - Rango de edad"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "rango_edad_grid",     
      "texto"     : "Rango de edad",
      "icon"      : "",
      "tipo"      : "remota",
      "navegar"   : "si",
      "padre"     : "Configuración PQRS-VENTANILLA",
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "rango_edad_forma",      
      "texto"     : "Rango de edad",
      "tipo"      : "remota"
   }
}

# Discapacidad
discapacidad = {
   "definicion": {
      "id"    : "22",
      "nombre": "CONFIGURACIÓN PQRS-VENTANILLA - Tipo de discapacidad"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "discapacidad_grid",     
      "texto"     : "Tipo de discapacidad",
      "icon"      : "",
      "navegar"   : "si",
      "padre"     : "Configuración PQRS-VENTANILLA",
      "tipo"      : "remota"
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "discapacidad_forma",      
      "texto"     : "Tipo de discapacidad",
      "tipo"      : "remota"
   }
}

"""
# Tipos de ciudadanos
tipo_ciudadano = {
   "definicion": {
      "id"    : "23",
      "nombre": "CONFIGURACIÓN - Tipo de ciudadano"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "tipo_ciudadano_grid",     
      "texto"     : "Tipo de ciudadano",
      "icon"      : "",
      "navegar"   : "si",
      "padre"     : "Configuración",
      "tipo"      : "importar"
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "tipo_ciudadano_forma",      
      "texto"     : "Tipo de ciudadano",
      "tipo"      : "importar"
   }
}

# Tipos de terceros
tipo_terceros = {
   "definicion": {
      "id"    : "24",
      "nombre": "CONFIGURACIÓN PQRS-VENTANILLA - Tipo de terceros"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "tipo_terceros_grid",     
      "texto"     : "Tipo de terceros",
      "icon"      : "",
      "tipo"      : "remota",
      "navegar"   : "si",
      "padre"     : "Configuración PQRS-VENTANILLA",
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "tipo_terceros_forma",      
      "texto"     : "Tipo de terceros",
      "tipo"      : "remota"
   }
}
"""

# TIPO DE PETICION
tipo_peticiones = {
   "definicion": {
      "id"    : "25",
      "nombre": "CONFIGURACIÓN PQRS-VENTANILLA - Tipos de Peticiones"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "tipo_peticiones_grid",     
      "texto"     : "Tipos de Peticiones",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Configuración PQRS-VENTANILLA",
      "tipo"      : "remota"
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "tipo_peticiones_forma",      
      "texto"     : "Tipos de Peticiones",
      "tipo"      : "remota"
   }
}

# TEMAS POR DEPENDENCIA
temas = {
   "definicion": {
      "id"    : "26",
      "nombre": "CONFIGURACIÓN PQRS-VENTANILLA - Temas por dependencia"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "temas_grid",     
      "texto"     : "Temas por dependencia",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Configuración PQRS-VENTANILLA",
      "tipo"      : "remota"
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "temas_forma",      
      "texto"     : "Temas por dependencia",
      "tipo"      : "remota"
   }
}

# SUBTEMAS POR DEPENDENCIA
subtemas = {
   "definicion": {
      "id"    : "27",
      "nombre": "CONFIGURACIÓN PQRS-VENTANILLA - Subtemas por Tema"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "subtemas_grid",     
      "texto"     : "Subtemas por Tema",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Configuración PQRS-VENTANILLA",
      "tipo"      : "remota"
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "subtemas_forma",      
      "texto"     : "Subtemas por Tema",
      "tipo"      : "remota"
   }
}

# CANALES DE COMUNICACIóN
canales_comunicacion = {
   "definicion": {
      "id"    : "28",
      "nombre": "CONFIGURACIÓN - Canales de comunicación"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "canales_comunicacion_grid",     
      "texto"     : "Canales de comunicación",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Configuración",
      "tipo"      : "remota"
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "canales_comunicacion_forma",      
      "texto"     : "Canales de comunicación",
      "tipo"      : "remota"
   }
}

# EMPRESA DE MENSAJERIA
empresas_mensajeria = {
   "definicion": {
      "id"    : "29",
      "nombre": "CONFIGURACIÓN PQRS-VENTANILLA - Empresas de mensajeria"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "empresas_mensajeria_grid",     
      "texto"     : "Empresas de mensajeria",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Configuración PQRS-VENTANILLA",
      "tipo"      : "remota"
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "empresas_mensajeria_forma",      
      "texto"     : "Empresas de mensajeria",
      "tipo"      : "remota"
   }
}

opciones = [
   # Canales de radicación configuración
   configura_radicacion_canales,

   # Plantillas del sistema
   plantillas,

   # Consecutivos
   consecutivos,

   # Tipo identificación
   tipo_identificaciones,

   # Genero
   genero,

   # Tipo entidad
   #tipo_entidad,

   # Tipo poblacion
   tipo_poblacion,

   # Rango de edad
   rango_edad,

   # Discapacidad
   discapacidad,

   # Tipo de ciudadano
   #tipo_ciudadano,

   # TIPO TERCEROS
   #tipo_terceros,

   # Tipos de peticiones
   tipo_peticiones,

   # TEMAS POR DEPENDENCIA
   temas,

   # SUBTEMAS POR TEMA
   subtemas,
   
   # CANALES DE COMUNICACIóN
   canales_comunicacion,

   # EMPRESAS DE MENSAJERIA
   empresas_mensajeria,

   # MOTIVOS DEVOLUCIóN
   motivos_devolucion
]