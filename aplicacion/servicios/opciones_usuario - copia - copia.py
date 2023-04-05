#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from datetime import datetime
import pprint

from librerias.datos.base import globales

continente = {
   "grid": {
      "id"        : "continente_grid",
      "ruta"      : "",
      "componente": "continente_grid",     
      "texto"     : "Continentes",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "id"        : "continente_forma",
      "ruta"      : "continente_forma",      
      "componente": "continente_forma",      
      "texto"     : "Manejo de continentes",
      "tipo"      : "importar"
   },
}

pais = {
   "grid": {
      "id"        : "pais_grid",
      "ruta"      : "pais",
      "componente": "pais_grid",     
      "texto"     : "Paises",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "id"        : "pais_forma",
      "ruta"      : "pais_forma",      
      "componente": "pais_forma",      
      "texto"     : "Manejo de paises",
      "tipo"      : "importar"
   },
}

departamento = {
   "grid": {
      "id"        : "departamento_grid",
      "ruta"      : "departamento",
      "componente": "departamento_grid",     
      "texto"     : "Departamentos",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "id"        : "departamento_forma",
      "ruta"      : "departamento_forma",      
      "componente": "departamento_forma",      
      "texto"     : "Manejo de Departamentos",
      "tipo"      : "importar"
   },
}

ciudad = {
   "grid": {
      "id"        : "ciudad_grid",
      "ruta"      : "ciudad",
      "componente": "ciudad_grid",     
      "texto"     : "Ciudades",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "id"        : "ciudad_forma",
      "ruta"      : "ciudad_forma",      
      "componente": "ciudad_forma",      
      "texto"     : "Manejo de Ciudades",
      "tipo"      : "importar"
   },
}

plantilla = {
   "grid": {
      "id"        : "plantilla_grid",
      "ruta"      : "plantilla",
      "componente": "plantilla_grid",     
      "texto"     : "Plantillas",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "id"        : "plantilla_forma",
      "ruta"      : "plantilla_forma",      
      "componente": "plantilla_forma",      
      "texto"     : "Manejo de Plantillas",
      "tipo"      : "importar"
   },
}

# UBICACIONES
ubicacion = {
  "grid": {
      "id"        : "ubicacion_grid",
      "ruta"      : "ubicacion",
      "componente": "ubicacion_grid",     
      "texto"     : "Ubicaciones geograficas",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "id"        : "ubicacion_forma",
      "ruta"      : "ubicacion_forma",      
      "componente": "ubicacion_forma",      
      "texto"     : "Manejo de ubicaciones",
      "tipo"      : "importar"
   }
}


# GRUPO
grupo = {
   "grid": {
      "id"        : "grupo_grid",
      "ruta"      : "grupo",
      "componente": "grupo_grid",     
      "texto"     : "Grupos",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "id"        : "grupo_forma",
      "ruta"      : "grupo_forma",      
      "componente": "grupo_forma",      
      "texto"     : "Manejo de grupos",
      "tipo"      : "importar"
   }
}

# CONSECUTIVO
consecutivo = {
   "grid": {
      "id"        : "consecutivo_grid",
      "ruta"      : "consecutivo",
      "componente": "consecutivo_grid",     
      "texto"     : "Consecutivos",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "id"        : "consecutivo_forma",
      "ruta"      : "consecutivo_forma",      
      "componente": "consecutivo_forma",      
      "texto"     : "Manejo de consecutivos",
      "tipo"      : "importar"
   }
}

# FESTIVOS
festivo = {
   "grid": {
      "id"        : "festivo_grid",
      "ruta"      : "festivo",
      "componente": "festivo_grid",     
      "texto"     : "Festivos",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "id"        : "festivo_forma",
      "ruta"      : "festivo_forma",      
      "componente": "festivo_forma",      
      "texto"     : "Manejo de festivos",
      "tipo"      : "importar"
   }
}

# MENSAJERIA
mensajeria = {
   "grid": {
      "id"        : "mensajeria_grid",
      "ruta"      : "mensajeria",
      "componente": "mensajeria_grid",     
      "texto"     : "Empresas de mensajeria",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "id"        : "mensajeria_forma",
      "ruta"      : "mensajeria_forma",      
      "componente": "mensajeria_forma",      
      "texto"     : "Manejo de Empresas de mensajeria",
      "tipo"      : "importar"
   }
}

# MEDIO ENVIO
medio_envio = {
   "grid": {
      "id"        : "medio_envio_grid",
      "ruta"      : "medio_envio",
      "componente": "medio_envio_grid",     
      "texto"     : "Medios de envio de correspondencia",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "id"        : "medio_envio",
      "ruta"      : "medio_envio_forma",      
      "componente": "medio_envio_forma",      
      "texto"     : "Manejo de Medios de envio de correspondencia",
      "tipo"      : "importar"
   }
}

# MOTIVOS_DEVOLUCION
motivo_devolucion = {
   "grid": {
      "id"        : "motivo_devolucion_grid",
      "ruta"      : "motivo_devolucion",
      "componente": "motivo_devolucion_grid",     
      "texto"     : "Motivos devolución de correspondencia",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "id"        : "motivo_devolucion",
      "ruta"      : "motivo_devolucion_forma",      
      "componente": "motivo_devolucion_forma",      
      "texto"     : "Motivos devolución de correspondencia",
      "tipo"      : "importar"
   }
}

usuario = {
   "grid": {
      "id"        : "usuario_grid",
      "ruta"      : "usuario",
      "componente": "usuario_grid",     
      "texto"     : "Usuarios del Sistema",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "id"        : "usuario",
      "ruta"      : "usuario_forma",      
      "componente": "usuario_forma",      
      "texto"     : "Usuarios del Sistema",
      "tipo"      : "importar"
   }
}

# DEPENDENCIAS
dependencia = {
   "grid": {
      "id"        : "dependencia_grid",
      "ruta"      : "dependencia",
      "componente": "dependencia_grid",     
      "texto"     : "Dependencias",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "id"        : "dependencia",
      "ruta"      : "dependencia_forma",      
      "componente": "dependencia_forma",      
      "texto"     : "Dependencias",
      "tipo"      : "importar"
   }
}

# PETICION
peticion = {
   "grid": {
      "id"        : "peticion_grid",
      "ruta"      : "peticion",
      "componente": "peticion_grid",     
      "texto"     : "Peticiones",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "id"        : "peticion",
      "ruta"      : "peticion_forma",      
      "componente": "peticion_forma",      
      "texto"     : "Peticiones",
      "tipo"      : "importar"
   }
}

# CORREO
correo = {
   "grid": {
      "id"        : "correo_grid",
      "ruta"      : "correo",
      "componente": "correo_grid",     
      "texto"     : "Correos",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "id"        : "correo",
      "ruta"      : "correo_forma",      
      "componente": "correo_forma",      
      "texto"     : "Correos",
      "tipo"      : "importar"
   }
}

# ROLE
role = {
   "grid": {
      "id"        : "role_grid",
      "ruta"      : "role",
      "componente": "role_grid",     
      "texto"     : "Roles",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "id"        : "role",
      "ruta"      : "role_forma",      
      "componente": "role_forma",      
      "texto"     : "Roles",
      "tipo"      : "importar"
   }
}

# ACCIONES
accion = {
   "grid": {
      "id"        : "accion_grid",
      "ruta"      : "accion",
      "componente": "accion_grid",     
      "texto"     : "Acciones",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "id"        : "accion",
      "ruta"      : "accion_forma",      
      "componente": "accion_forma",      
      "texto"     : "Acciones",
      "tipo"      : "importar"
   }
}

# Tipos de identificacion
tipo_identificacion = {
   "grid": {
      "id"        : "tipo_identificacion_grid",
      "ruta"      : "tipo_identificacion",
      "componente": "tipo_identificacion_grid",     
      "texto"     : "Tipos de identificación",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "id"        : "tipo_identificacion",
      "ruta"      : "tipo_identificacion_forma",      
      "componente": "tipo_identificacion_forma",      
      "texto"     : "Tipos de identificación",
      "tipo"      : "importar"
   }
}

# Genero de identidad sexual
genero = {
   "grid": {
      "id"        : "genero_grid",
      "ruta"      : "genero",
      "componente": "genero_grid",     
      "texto"     : "Genero",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "id"        : "genero",
      "ruta"      : "genero_forma",      
      "componente": "genero_forma",      
      "texto"     : "Genero",
      "tipo"      : "importar"
   }
}

# Tipos de entidades
tipo_entidad = {
   "grid": {
      "id"        : "tipo_entidad_grid",
      "ruta"      : "tipo_entidad",
      "componente": "tipo_entidad_grid",     
      "texto"     : "Tipos de entidades",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "id"        : "tipo_entidad",
      "ruta"      : "tipo_entidad_forma",      
      "componente": "tipo_entidad_forma",      
      "texto"     : "Tipos de entidades",
      "tipo"      : "importar"
   }
}

#############################
# FORMULARIOS WEB RADICADOS #
#############################

# Persona juridica
fweb_juridica = {
   "grid": {
      "id"        : "fweb_juridica_grid",
      "ruta"      : "fweb_juridica",
      "componente": "fweb_juridica_grid",     
      "texto"     : "PERSONA JURIDICA",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Formularios Web",
   },

   "forma": {
      "id"        : "fweb_juridica",
      "ruta"      : "fweb_juridica_forma",      
      "componente": "fweb_juridica_forma",      
      "texto"     : "PERSONA JURIDICA",
      "tipo"      : "importar"
   }
}

#################
# CONFIGURACION #
#################
opciones_sistema_onfiguracion = {
   "grid": {
      "clase"     : "grid",
      "id"        : "opciones_sistema_grid",
      "ruta"      : "opciones_sistema_grid",
      "componente": "opciones_sistema_grid",     
      "texto"     : "Opciones Menu del Sistema",
      "icon"      : "",
      "tipo"      : "remota",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "clase"     : "forma",
      "id"        : "opciones_sistema_forma",
      "ruta"      : "opciones_sistema_forma",      
      "componente": "opciones_sistema_forma",      
      "texto"     : "Opciones Menu del Sistema",
      "tipo"      : "remota"
   }
}


#########################
# PQRS RADICADO MIGRADO #
#########################
# Radicados migrados
radicado_migrado  = {
   "grid": {
      "id"        : "radicado_pqr_grid",
      "ruta"      : "radicado_pqr",
      "componente": "radicado_pqr_grid",     
      "texto"     : "Radicados migrados Pqrs",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Migración",
   },

   "forma": {
      "id"        : "radicado_pqr",
      "ruta"      : "radicado_pqr_forma",      
      "componente": "radicado_pqr_forma",      
      "texto"     : "Radicados migrados Pqrs",
      "tipo"      : "importar"
   }
}

#############################
# HISTORICO ARCHIVO MIGRADO #
#############################
archivo_historico_migrado = {
   "grid": {
      "id"        : "archivo_historico_migrado_grid",
      "ruta"      : "archivo_historico_migrado",
      "componente": "archivo_historico_migrado_grid",     
      "texto"     : "Archivo historico",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Migración",
   }
}

################################
# VENTANILLA RADICADO ENETRADA #
################################
entradas_ventanilla_migrado = {
   "grid": {
      "id"        : "entradas_ventanilla_grid",
      "ruta"      : "entradas_ventanilla",
      "componente": "entradas_ventanilla_grid",     
      "texto"     : "Entradas Migrados Ventanilla",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Migración",
   },

   "forma": {
      "id"        : "entradas_ventanilla",
      "ruta"      : "entradas_ventanilla_forma",      
      "componente": "entradas_ventanilla_forma",      
      "texto"     : "Entradas radicados Ventanilla",
      "tipo"      : "importar"
   }
}

internos_ventanilla_migrado = {
   "grid": {
      "id"        : "internos_ventanilla_grid",
      "ruta"      : "internos_ventanilla_grid",
      "componente": "internos_ventanilla_grid",     
      "texto"     : "Internos Migrados Ventanilla",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Migración",
   },

   "forma": {
      "id"        : "internos_ventanilla_grid",
      "ruta"      : "internos_ventanilla_forma",      
      "componente": "internos_ventanilla_forma",      
      "texto"     : "Internos radicados Ventanilla",
      "tipo"      : "importar"
   }
}

salidas_ventanilla_migrado = {
   "grid": {
      "id"        : "salidas_ventanilla_grid",
      "ruta"      : "salidas_ventanilla_grid",
      "componente": "salidas_ventanilla_grid",     
      "texto"     : "Salidas Migrados Ventanilla",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Migración",
   },

   "forma": {
      "id"        : "salidas_ventanilla_forma",
      "ruta"      : "salidas_ventanilla_forma",      
      "componente": "salidas_ventanilla_forma",      
      "texto"     : "Salidas radicadas  Ventanilla",
      "tipo"      : "importar"
   }
}


"""
   # CONTINENTES
   continente["grid"],
   continente["forma"],
  
   # PAISES
   pais["grid"],
   pais["forma"],

   # DEPARTAMENTOS
   departamento["grid"],
   departamento["forma"],

   # CIUDAD
   ciudad["grid"],
   ciudad["forma"],

   # PLANTILLA
   plantilla["grid"],
   plantilla["forma"],

   # Ubicaciones geograficas
   ubicacion["grid"],
   ubicacion["forma"],

   # Grupos de usuarios
   grupo["grid"],
   grupo["forma"],

   # Consecutivo
   consecutivo["grid"],
   consecutivo["forma"],

   # Festivos
   festivo["grid"],
   festivo["forma"],

   # MENSAJERIA
   mensajeria["grid"],
   mensajeria["forma"],

   # MEDIO ENVIO
   medio_envio["grid"],
   medio_envio["forma"],

   # MOTIVO_DEVOLUCION
   motivo_devolucion["grid"],
   motivo_devolucion["forma"],

   # USUARIO
   usuario["grid"],
   usuario["forma"],

   # DEPENDENCIAS
   dependencia["grid"],
   dependencia["forma"],

   # PETICION
   peticion["grid"],
   peticion["forma"],

   # CORREO
   correo["grid"],
   correo["forma"],

   # ROLE
   role["grid"],
   role["forma"],

   # ACCIONES
   accion["grid"],
   accion["forma"],

   # Tipos de identificacion
   tipo_identificacion["grid"],
   tipo_identificacion["forma"],

   # Generos
   genero["grid"],
   genero["forma"],

   # Tipos de entidades
   tipo_entidad["grid"],
   tipo_entidad["forma"],

   # Persona juridica
   fweb_juridica["grid"],
   fweb_juridica["forma"],
"""

opciones_usuario = [
   # Opciones del sistema
   opciones_sistema_onfiguracion["grid"],
   opciones_sistema_onfiguracion["forma"],

   # Archivo historico migrado
   archivo_historico_migrado["grid"],

   # RADICADOS PQRS MIGRADOS
   radicado_migrado["grid"],
   radicado_migrado["forma"],

   # VENTANILLA RADICADOS ENTRADAS MIGRADOS
   entradas_ventanilla_migrado["grid"],
   entradas_ventanilla_migrado["forma"],

   # VENTANILLA INTERNOS ENTRADAS MIGRADOS
   internos_ventanilla_migrado["grid"],
   internos_ventanilla_migrado["forma"],

   # VENTANILLA SALIDAS ENTRADAS MIGRADOS
   salidas_ventanilla_migrado["grid"],
   salidas_ventanilla_migrado["forma"],
]

def ejecutar(parametros):
   resultado = {
      "datos"     : {},      
      "usuario_id": ""
   }
   accion    = parametros["__accion__"]
   if accion == "leer":
      usuario_id              = parametros["usuario_id"]
      resultado["datos"]      = opciones_usuario
      resultado["usuario_id"] = usuario_id

   return resultado