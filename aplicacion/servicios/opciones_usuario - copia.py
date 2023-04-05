#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.base import globales

#################
# CONFIGURACION #
#################

configura_radicacion_canales = {
   "forma": {
      "componente": "configura_radicacion_canales",     
      "texto"     : "Radicación Canales",
      "navegar"   : "si",
      "padre"     : "Configuración",
      "tipo"      : "importar",
   }
}

# Plantilla
plantillas = {
   "grid": {
      "clase"     : "grid",
      "componente": "plantilla_grid",     
      "texto"     : "Plantillas del sistema",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Configuración",
      "tipo"      : "importar",
   },

   "forma": {
      "componente": "pantalla_plantilla",      
      "texto"     : "Pantalla de plantilla",
      "tipo"      : "importar",
   }
}

# Opciones de menu del sistema
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

# ROLES
roles = {
   "grid": {
      "clase"     : "grid",
      "componente": "roles_grid",     
      "texto"     : "Roles del Sistema",
      "icon"      : "",
      "navegar"   : "si",
      "padre"     : "Configuración",
      "tipo"      : "remota"   
   },

   "forma": {
      "clase"     : "forma",
      "componente": "roles_forma",      
      "texto"     : "Roles del Sistema",
      "tipo"      : "remota"
   }
}

# UBICACIONES
ubicaciones = {
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

# CONSECUTIVOS
consecutivos = {
   "grid": {
      "clase"     : "grid",
      "componente": "consecutivos_grid",     
      "texto"     : "Consecutivos",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "consecutivos_forma",      
      "texto"     : "Consecutivos",
      "tipo"      : "importar"
   }
}

# Tipo de identificacion
tipo_identificaciones = {
   "grid": {
      "clase"     : "grid",
      "componente": "tipo_identificaciones_grid",     
      "texto"     : "Tipo identificación",
      "icon"      : "",
      "navegar"   : "si",
      "padre"     : "Configuración",
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
   "grid": {
      "clase"     : "grid",
      "componente": "genero_grid",     
      "texto"     : "Genero",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "genero_forma",      
      "texto"     : "Genero",
      "tipo"      : "importar"
   }
}

# Tipo entidad
tipo_entidad = {
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
   "grid": {
      "clase"     : "grid",
      "componente": "tipo_poblacion_grid",     
      "texto"     : "Tipo población",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "tipo_poblacion_forma",      
      "texto"     : "Tipo población",
      "tipo"      : "importar"
   }
}

# Rangos de edad
rango_edad = {
   "grid": {
      "clase"     : "grid",
      "componente": "rango_edad_grid",     
      "texto"     : "Rango de edad",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "rango_edad_forma",      
      "texto"     : "Rango de edad",
      "tipo"      : "importar"
   }
}

# Discapacidad
discapacidad = {
   "grid": {
      "clase"     : "grid",
      "componente": "discapacidad_grid",     
      "texto"     : "Tipo de discapacidad",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "discapacidad_forma",      
      "texto"     : "Tipo de discapacidad",
      "tipo"      : "importar"
   }
}

# Tipos de ciudadanos
tipo_ciudadano = {
   "grid": {
      "clase"     : "grid",
      "componente": "tipo_ciudadano_grid",     
      "texto"     : "Tipo de ciudadano",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Configuración",
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
   "grid": {
      "clase"     : "grid",
      "componente": "tipo_terceros_grid",     
      "texto"     : "Tipo de terceros",
      "icon"      : "",
      "tipo"      : "remota",
      "navegar"   : "si",
      "padre"     : "Configuración",
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "tipo_terceros_forma",      
      "texto"     : "Tipo de terceros",
      "tipo"      : "remota"
   }
}

# TIPO DE PETICION
tipo_peticiones = {
   "grid": {
      "clase"     : "grid",
      "componente": "tipo_peticiones_grid",     
      "texto"     : "Tipos de Peticiones",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Configuración",
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
   "grid": {
      "clase"     : "grid",
      "componente": "temas_grid",     
      "texto"     : "Temas por dependencia",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Configuración",
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
   "grid": {
      "clase"     : "grid",
      "componente": "subtemas_grid",     
      "texto"     : "Subtemas por Tema",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Configuración",
      "tipo"      : "remota"
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "subtemas_forma",      
      "texto"     : "Subtemas por Tema",
      "tipo"      : "remota"
   }
}

# CANALES DE COMUNICACIÓN
canales_comunicacion = {
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
   "grid": {
      "clase"     : "grid",
      "componente": "empresas_mensajeria_grid",     
      "texto"     : "Empresas de mensajeria",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Configuración",
      "tipo"      : "remota"
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "empresas_mensajeria_forma",      
      "texto"     : "Empresas de mensajeria",
      "tipo"      : "remota"
   }
}

# FESTIVO
dias_festivo = {
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

#########################
# PQRS RADICADO MIGRADO #
#########################
# Radicados migrados
radicado_migrado  = {
   "grid": {
      "componente": "radicado_pqr_grid",     
      "texto"     : "Radicados migrados Pqrs",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Migración",
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
   "grid": {
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
      "componente": "entradas_ventanilla_grid",     
      "texto"     : "Entradas Migrados Ventanilla",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Migración",
   },

   "forma": {
      "componente": "entradas_ventanilla_forma",      
      "texto"     : "Entradas radicados Ventanilla",
      "tipo"      : "importar"
   }
}

internos_ventanilla_migrado = {
   "grid": {
      "componente": "internos_ventanilla_grid",     
      "texto"     : "Internos Migrados Ventanilla",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Migración",
   },

   "forma": {
      "componente": "internos_ventanilla_forma",      
      "texto"     : "Internos radicados Ventanilla",
      "tipo"      : "importar"
   }
}

salidas_ventanilla_migrado = {
   "grid": {
      "componente": "salidas_ventanilla_grid",     
      "texto"     : "Salidas Migrados Ventanilla",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Migración",
   },

   "forma": {
      "componente": "salidas_ventanilla_forma",      
      "texto"     : "Salidas radicadas  Ventanilla",
      "tipo"      : "importar"
   }
}

########
# PQRS #
########
radicado_web_juridico = {
   "grid": {
      "componente": "radicado_general_grid",     
      "texto"     : "Radicación Persona JURIDICA",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Formularios web",
   },

   "forma": {
      "componente": "radicado_juridica_forma",      
      "texto"     : "Entradas radicados Ventanilla",
      "tipo"      : "importar"
   }
}

radicado_web_natural = {
   "grid": {
      "componente": "natural_radicados_grid",     
      "texto"     : "Radicación Persona Natural",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Formularios web",
   },

   "forma": {
      "componente": "natural_web_forma",      
      "texto"     : "Entradas radicados Web",
      "tipo"      : "importar"
   }
}

radicado_web_anonimo = {
   "grid": {
      "componente": "anonimo_radicados_grid",     
      "texto"     : "Radicación Anonimo",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Formularios web",
   },

   "forma": {
      "componente": "anonimo_web_forma",      
      "texto"     : "Entradas radicados Web",
      "tipo"      : "importar"
   }
}

asignar_pqrs = {
   "grid": {
      "componente": "asignar_pqrs_grid",     
      "texto"     : "Asignación y traslado de radicados PQRS",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "PQRS",
      "tipo"      : "importar",
   },   

   "forma": {
      "componente": "asignar_pqrs_forma",      
      "texto"     : "Asignación y traslado de PQRS",
      "tipo"      : "importar"
   }
}

##############
# PETICIONES #
##############

gestion_basica = {
   "grid": {
      "componente": "gestion_basica_grid",     
      "texto"     : "Gestión de peticiones/tramites",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Gestión",
      "tipo"      : "importar",
   }
}

pqrs_radicado = {
   "grid": {
      "componente": "pqrs_radicado_grid",     
      "texto"     : "Radicación",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "PQRS",
   },

   "forma": {
      "componente": "pqrs_radicado_forma",      
      "texto"     : "Radicación PQRS",
      "tipo"      : "importar"
   }
}

tablero_general = {
   "grid": {
      "componente": "tablero_general",     
      "texto"     : "Gestión seguimiento general",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Gestión",
      "tipo"      : "importar",
   }
}

gestion_pantalla = {
   "forma": {
      "componente": "gestion_pantalla",     
      "texto"     : "Gestión peticiones",
      "tipo"      : "importar",
   }
}

#######################
# VENTANILLA RADICADO #
#######################
ventanilla_radicado = {
   "grid": {
      "componente": "ventanilla_radicado_grid",     
      "texto"     : "Radicación",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Ventanilla Radicación",
   },

   "forma": {
      "componente": "ventanilla_radicado_forma",      
      "texto"     : "Radicación Ventanilla",
      "tipo"      : "importar"
   }
}

ventanilla_radicado_consulta = {
   "forma": {
      "componente": "ventanilla_radicado_consulta",      
      "texto"     : "Consulta Radicados",
      "tipo"      : "importar"
   }
}

#####################
# VENTANILLA SALIDA #
#####################
ventanilla_salida = {
   "grid": {
      "componente": "ventanilla_salida_grid",     
      "texto"     : "Radicación Salida",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Ventanilla Radicación",
   },

   "forma": {
      "componente": "ventanilla_salida_forma",      
      "texto"     : "Radicación Ventanilla Salida",
      "tipo"      : "importar"
   }
}

ventanilla_salida_consulta = {
   "forma": {
      "componente": "ventanilla_salida_consulta",      
      "texto"     : "Consulta Radicados Salida",
      "tipo"      : "importar"
   }
}

######################
# VENTANILLA INTERNO #
######################
ventanilla_interno = {
   "grid": {
      "componente": "ventanilla_interno_grid",     
      "texto"     : "Radicación Interno",
      "icon"      : "",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Ventanilla Radicación",
   },

   "forma": {
      "componente": "ventanilla_interno_forma",      
      "texto"     : "Radicación Ventanilla Interno",
      "tipo"      : "importar"
   }
}

ventanilla_interno_consulta = {
   "forma": {
      "componente": "ventanilla_interno_consulta",      
      "texto"     : "Consulta Radicados Interno",
      "tipo"      : "importar"
   }
}

planilla_grid = {
   "grid": {
      "componente": "planilla_grid",     
      "texto"     : "Manejo de planillas de envio fisico",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Envios",
      "tipo"      : "importar",
   }
}

envios_grid = {
   "grid": {
      "componente": "envios_grid",     
      "texto"     : "Envios grid",
      "icon"      : "",      
      "navegar"   : "no",
      "padre"     : "Envios",
      "tipo"      : "importar",
   }
}

devoluciones_grid = {
   "grid": {
      "componente": "devoluciones_grid",     
      "texto"     : "Devoluciones grid",
      "icon"      : "",      
      "navegar"   : "no",
      "padre"     : "Envios",
      "tipo"      : "importar",
   }
}

envio_electronico_grid = {
   "grid": {
      "componente": "envio_electronico_grid",     
      "texto"     : "Envios electronicos",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Envios",
      "tipo"      : "importar",
   }
}

destinatarios_listado = {
   "grid": {
      "componente": "destinatarios_listado_grid",     
      "texto"     : "Listados destinatarios salidas",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Envios masivos",
      "tipo"      : "importar",
   },

   "forma": {
      "componente": "ventana_listado",      
      "texto"     : "Ventana listado",
      "navegar"   : "no",
      "tipo"      : "importar"
   }
}

ventanilla_masivos = {
   "forma": {
      "componente": "salida_masiva",      
      "texto"     : "Genera masivos de salida",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Envios masivos"
   }
}

destinatarios_listado_interno = {
   "grid": {
      "componente": "destinatarios_listado_interno_grid",     
      "texto"     : "Listados destinatarios internos",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Envios masivos",
      "tipo"      : "importar",
   },

   "forma": {
      "componente": "ventana_listado_interno",      
      "texto"     : "Ventana listado interno",
      "navegar"   : "no",
      "tipo"      : "importar"
   }
}

ventanilla_masivos_interno = {
   "forma": {
      "componente": "interno_masiva",      
      "texto"     : "Genera masivos de internos",
      "tipo"      : "importar",
      "navegar"   : "si",
      "padre"     : "Envios masivos"
   }
}

################
# AGN ARCHIVOS #
################
# FONDOS DOCUMENTALES
agn_fondos = {
   "grid": {
      "clase"     : "grid",
      "componente": "agn_fondo_documental_grid",     
      "texto"     : "Fondos Documentales",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Archivo",
      "tipo"      : "remota"
   },

   "forma": {
      "clase"     : "forma",     
      "componente": "agn_fondo_documental_forma",      
      "texto"     : "Manejo de fondos",
      "tipo"      : "remota"
   }
}

###########
# TRD AGN #
###########
# TRD GRID
trd_basica = {
   "grid": {
      "componente": "trd_basica_grid",     
      "texto"     : "Manejo de Tablas de Retención",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Archivo TRD",
      "tipo"      : "importar",
   }
}

trd_pantalla = {
   "forma": {
      "componente": "trd_pantalla",     
      "texto"     : "Pantalla  trd",
      "tipo"      : "importar",
   }
}

# EXPEDIENTE GRID
expediente_basica = {
   "grid": {
      "componente": "expediente_basica_grid",     
      "texto"     : "Manejo de Expedientes TRD",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Archivo TRD",
      "tipo"      : "importar",
   }
}

pantalla_expediente = {
   "forma": {
      "componente": "pantalla_expediente",     
      "texto"     : "Pantalla  Expediente",
      "tipo"      : "importar",
   }
}

# EXPEDIENTE CONSULTA GRID
expediente_consulta_basica = {
   "grid": {
      "componente": "expediente_consulta_basica_grid",     
      "texto"     : "Consulta Expedientes TRD",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Archivo TRD",
      "tipo"      : "importar",
   }
}

pantalla_consulta_expediente = {
   "forma": {
      "componente": "pantalla_consulta_expediente",     
      "texto"     : "Consulta Expediente",
      "tipo"      : "importar",
   }
}

# EXPEDIENTE PRESTAMO
prestamo_basica = {
   "grid": {
      "componente": "prestamo_basica_grid",     
      "texto"     : "Prestamo Expedientes",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Prestamos expedientes",
      "tipo"      : "importar",
   }
}

# TRANSFERENCIA GRID
transferencia_basica = {
   "grid": {
      "componente": "transferencia_basica_grid",     
      "texto"     : "Manejo de Transferencia Primaria",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Archivo TRD",
      "tipo"      : "importar",
   }
}

pantalla_transferencia = {
   "forma": {
      "componente": "pantalla_transferencia",     
      "texto"     : "Pantalla Transferencia Primaria",
      "tipo"      : "importar",
   }
}

###########
# TVD AGN #
###########
# TVD GRID
tvd_basica = {
   "grid": {
      "componente": "tvd_basica_grid",     
      "texto"     : "Manejo de Tablas de Valoración",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Archivo TVD",
      "tipo"      : "importar",
   }
}

tvd_pantalla = {
   "forma": {
      "componente": "tvd_pantalla",     
      "texto"     : "Pantalla  tvd",
      "tipo"      : "importar",
   }
}

# TVD EXPEDIENTE GRID
tvd_expediente_basica = {
   "grid": {
      "componente": "tvd_expediente_basica_grid",     
      "texto"     : "Manejo de Expedientes TVD",
      "icon"      : "",      
      "navegar"   : "si",
      "padre"     : "Archivo TVD",
      "tipo"      : "importar",
   }
}

tvd_pantalla_expediente = {
   "forma": {
      "componente": "tvd_pantalla_expediente",     
      "texto"     : "Pantalla  Expediente TVD",
      "tipo"      : "importar",
   }
}

#######################
# FORMULARIO DINAMICO #
#######################
formulario_constructor = {
   "forma": {
      "componente": "formulario_constructor",     
      "texto"     : "Formulario constructor",
      "padre"     : "Formularios dinamicos",
      "navegar"   : "si",
      "tipo"      : "importar",
   }
}

#########################
# DISEÑADOR DE REPORTES #
#########################
disenador_reportes = {
   "forma": {
      "componente": "disenador_reportes",     
      "texto"     : "Diseñador de reportes",
      "padre"     : "Diseñador de reportes",
      "navegar"   : "si",
      "tipo"      : "importar",
   }
}

opciones_usuario = [

   
   #################
   # CONFIGURACIÓN #
   #################

   # Canales de radicación configuración
   configura_radicacion_canales["forma"],

   # Plantillas del sistema
   plantillas["grid"],
   plantillas["forma"],

   # Opciones del sistema
   opciones_sistema_onfiguracion["grid"],
   opciones_sistema_onfiguracion["forma"],

   # Acciones del menu del sistema
   acciones["grid"],
   acciones["forma"],

   # Roles del menu del sistema
   roles["grid"],
   roles["forma"],

   # Ubicaciones geograficas
   ubicaciones["grid"],
   ubicaciones["forma"],

   # Usuarios
   usuarios["grid"],
   usuarios["forma"],

   # Dependencias
   dependencias["grid"],
   dependencias["forma"],

   # Continentes
   continentes["grid"],
   continentes["forma"],

   # Paises
   paises["grid"],
   paises["forma"],

   # Departamento
   departamentos["grid"],
   departamentos["forma"],

   # Ciudades
   ciudades["grid"],
   ciudades["forma"],

   # # GRUPOS USUARIOS
   grupo_usuarios["grid"],
   grupo_usuarios["forma"],

   # Consecutivos
   consecutivos["grid"],
   consecutivos["forma"],

   # Tipo identificación
   tipo_identificaciones["grid"],
   tipo_identificaciones["forma"],

   # Genero
   genero["grid"],
   genero["forma"],

   # Tipo entidad
   tipo_entidad["grid"],
   tipo_entidad["forma"],

   # Tipo poblacion
   tipo_poblacion["grid"],
   tipo_poblacion["forma"],

   # Rango de edad
   rango_edad["grid"],
   rango_edad["forma"],

   # Discapacidad
   discapacidad["grid"],
   discapacidad["forma"],

   # Tipo de ciudadano
   tipo_ciudadano["grid"],
   tipo_ciudadano["forma"],

   # Tipos de peticiones
   tipo_peticiones["grid"],
   tipo_peticiones["forma"],
   
   # TEMAS POR DEPENDENCIA
   temas["grid"],
   temas["forma"],

   # SUBTEMAS POR TEMA
   subtemas["grid"],
   subtemas["forma"],

   # TIPO TERCEROS
   tipo_terceros["grid"],
   tipo_terceros["forma"],
   
   # CANALES DE COMUNICACIÓN
   canales_comunicacion["grid"],
   canales_comunicacion["forma"],

   # EMPRESAS DE MENSAJERIA
   empresas_mensajeria["grid"],
   empresas_mensajeria["forma"],

   # DIAS FESTIVOS
   dias_festivo["grid"],
   dias_festivo["forma"],

   #############
   # MIGRACIÓN #
   #############
   
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

   #############
   # RADICADOS #
   #############
   radicado_web_juridico["grid"],
   radicado_web_juridico["forma"],

   radicado_web_natural["grid"],
   radicado_web_natural["forma"],

   radicado_web_anonimo["grid"],
   radicado_web_anonimo["forma"],

   asignar_pqrs["grid"],
   asignar_pqrs["forma"],

   ###########
   # GESTIÓN #
   ###########   
   gestion_basica["grid"],
   tablero_general["grid"],
   gestion_pantalla["forma"],

   ########
   # PQRS #
   ########
   pqrs_radicado["grid"],
   pqrs_radicado["forma"],
   
   #######################
   # VENTANILLA RADICADO #
   #######################
   ventanilla_radicado["grid"],
   ventanilla_radicado["forma"],
   ventanilla_radicado_consulta["forma"],

   #####################
   # VENTANILLA SALIDA #
   #####################
   ventanilla_salida["grid"],
   ventanilla_salida["forma"],
   ventanilla_salida_consulta["forma"],

   ######################
   # VENTANILLA INTERNO #
   ######################
   ventanilla_interno["grid"],
   ventanilla_interno["forma"],
   ventanilla_interno_consulta["forma"],

   ##################
   # ENVIOS FISICOS #
   ##################
   planilla_grid["grid"],
   envios_grid["grid"],
   devoluciones_grid["grid"],
   envio_electronico_grid["grid"],

   ##################
   # MASIVOS SALIDA #
   ##################
   destinatarios_listado["grid"],
   destinatarios_listado["forma"],
   ventanilla_masivos["forma"],

   ####################
   # MASIVOS INTERNOS #
   ####################
   destinatarios_listado_interno["grid"],
   destinatarios_listado_interno["forma"],
   ventanilla_masivos_interno["forma"],

   ###############
   # AGN ARCHIVO #
   ###############

   ###########
   # TRD AGN #
   ###########
   # FONDOS
   agn_fondos["grid"],
   agn_fondos["forma"],

   # TRD
   trd_basica["grid"],
   trd_pantalla["forma"],

   # EXPEDIENTE
   expediente_basica["grid"],
   pantalla_expediente["forma"],

   # CONSULTA EXPEDIENTE
   expediente_consulta_basica["grid"],
   pantalla_consulta_expediente["forma"],

   # EXPEDIENTE
   transferencia_basica["grid"],
   pantalla_transferencia["forma"],

   # PRESTAMOS EXPEDIENTES
   prestamo_basica["grid"],

   ###########
   # TVD AGN #
   ###########
   # TVD
   tvd_basica["grid"],
   tvd_pantalla["forma"],

   # EXPEDIENTE
   tvd_expediente_basica["grid"],
   tvd_pantalla_expediente["forma"],
   
   ##########################
   # FORMULARIO CONSTRUCTOR #
   ##########################
   formulario_constructor["forma"],

   #########################
   # DISEÑADOR DE REPORTES #
   #########################
   disenador_reportes["forma"]
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