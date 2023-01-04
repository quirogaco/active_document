#!/usr/bin/python
# -*- coding: UTF-8 -*-

from aplicacion.datos.clases.clases_base import *
from aplicacion.datos.clases.genericas   import *
from librerias.datos.sql                 import sqalchemy_clase_dinamica

###################
# BASES GENERALES #
###################

######## ARCHIVOS ###########
# Archivos anexos generales
from aplicacion.datos.definiciones.genericas.archivo_electronico          import *
# Relación a arhivos anexos con las  estructuras
from aplicacion.datos.definiciones.genericas.archivo_electronico_relacion import *
# Estructura de archivo
from aplicacion.datos.definiciones.archivos import archivos


######## RELACIONES ###########
# Relaciones estructuras
from aplicacion.datos.definiciones.genericas.estructura_relacion import *

#################################
# PUBLICAR FUNCIONES GENERALES  #
#################################

# Manejo de envio de archivos
from aplicacion.archivos import *

# Relaciones a estructura
from aplicacion.relaciones import *

##############################
# CONFIGURACION Definiciones #
##############################
from aplicacion.datos.definiciones.configuracion.opciones_sistema      import *
from aplicacion.datos.definiciones.configuracion.acciones              import *
from aplicacion.datos.definiciones.configuracion.roles                 import *
from aplicacion.datos.definiciones.configuracion.ubicaciones           import *
from aplicacion.datos.definiciones.configuracion.usuarios              import *
from aplicacion.datos.definiciones.configuracion.dependencias          import *

from aplicacion.datos.definiciones.configuracion.paises                import *
from aplicacion.datos.definiciones.configuracion.continentes           import *
from aplicacion.datos.definiciones.configuracion.departamentos         import *
from aplicacion.datos.definiciones.configuracion.ciudades              import *
from aplicacion.datos.definiciones.configuracion.grupos                import *
from aplicacion.datos.definiciones.configuracion.consecutivos          import *
from aplicacion.datos.definiciones.configuracion.tipo_identificacion   import *
from aplicacion.datos.definiciones.configuracion.genero                import *
from aplicacion.datos.definiciones.configuracion.tipo_poblacion        import *
from aplicacion.datos.definiciones.configuracion.rango_edad            import *
from aplicacion.datos.definiciones.configuracion.discapacidad          import *
from aplicacion.datos.definiciones.configuracion.tipo_ciudadano        import *
from aplicacion.datos.definiciones.configuracion.tipo_entidad          import *
from aplicacion.datos.definiciones.configuracion.peticiones            import *
from aplicacion.datos.definiciones.configuracion.temas_subtemas        import *
from aplicacion.datos.definiciones.configuracion.tipo_terceros         import *
from aplicacion.datos.definiciones.configuracion.canales               import *
from aplicacion.datos.definiciones.configuracion.empresas_mensajeria   import *
from aplicacion.datos.definiciones.configuracion.festivos              import *
from aplicacion.datos.definiciones.configuracion.plantilla             import *
from aplicacion.datos.definiciones.configuracion.configuracion_general import *
from aplicacion.datos.definiciones.configuracion.reportes_dinamicos    import *
from aplicacion.datos.definiciones.configuracion.formularios_dinamicos import *
from aplicacion.datos.definiciones.configuracion.tramites              import *
from aplicacion.datos.definiciones.configuracion.logs_ingreso          import *
from aplicacion.datos.definiciones.configuracion.permisos_archivo      import *
from aplicacion.datos.definiciones.configuracion.motivo_devolucion     import *

# Tablas especificas de pqrs, ventanilla, gestión
from aplicacion.datos.definiciones.terceros import *

# Log de eventos
from aplicacion.datos.definiciones.logs import *

#######################
# ENVIOS Definiciones #
#######################
from aplicacion.datos.definiciones.envios import *

#######################
# MASIVO Definiciones #
#######################
from aplicacion.datos.definiciones.masivos import *

"""
from aplicacion.datos.definiciones.configuracion.mensajeria          import *
from aplicacion.datos.definiciones.configuracion.medio_envio         import *
"""

########################
# GESTIóN Definiciones #
########################
from aplicacion.datos.definiciones.gestion.gestion import *
from aplicacion.datos.definiciones.gestion.gestion_relaciones import *

######################
# MIGRACIóN DE DATOS #
######################
## ESTA PENDIENTE
from aplicacion.datos.definiciones.migrados.historico import *
from aplicacion.datos.definiciones.migrados.pqrs import *
from aplicacion.datos.definiciones.migrados.ventanilla import *

##############
# RADICACIóN #
##############
from aplicacion.datos.definiciones.radicados import *
from aplicacion.datos.definiciones.salidas import *
from aplicacion.datos.definiciones.internos import *
from aplicacion.datos.definiciones.correos import *
from aplicacion.datos.definiciones.copias import *

###################
# DATOS Dinamicos #
###################
from aplicacion.datos.definiciones.datos_dinamicos import *


###############
# AGN ARCHIVO #
###############

# TRD
from aplicacion.datos.definiciones.agn.fondo              import *
from aplicacion.datos.definiciones.agn.trd                import *
from aplicacion.datos.definiciones.agn.trd_dependencias   import *
from aplicacion.datos.definiciones.agn.trd_series         import *
from aplicacion.datos.definiciones.agn.trd_subseries      import *
from aplicacion.datos.definiciones.agn.trd_tipos          import *
from aplicacion.datos.definiciones.agn.trd_expedientes    import *
from aplicacion.datos.definiciones.agn.trd_documentos     import *
from aplicacion.datos.definiciones.agn.trd_accesos        import *
from aplicacion.datos.definiciones.agn.trd_prestamos      import *
from aplicacion.datos.definiciones.agn.trd_transferencias import *

# TVD
from aplicacion.datos.definiciones.agn.tvd                import *
from aplicacion.datos.definiciones.agn.tvd_dependencias   import *
from aplicacion.datos.definiciones.agn.tvd_series         import *
from aplicacion.datos.definiciones.agn.tvd_subseries      import *
from aplicacion.datos.definiciones.agn.tvd_expedientes    import *
from aplicacion.datos.definiciones.agn.tvd_documentos     import *
from aplicacion.datos.definiciones.agn.tvd_accesos        import *
from aplicacion.datos.definiciones.agn.tvd_prestamos      import *

########################
# FUNCIONES PRE Y POST #
########################
import aplicacion.estructuras

###########################
# CREA REALCION DE CLASES #
###########################
sqalchemy_clase_dinamica.crea_relaciones_proxy()

########################
# FNCIONES ESPECIFICAS #
########################
from aplicacion.especificos.radicados.gestion  import *

#########
# LOGS  #  
#########
from aplicacion.logs import *

######################
# TAREAS ESPECIFICAS #
######################
# EJ.Manejo de TERCEROS
from aplicacion.tareas_especificas import * 

#######################################
# PUBLICACION DE FUNCIONES A EJECUTAR #
######################################
from aplicacion.ejecucion import publicar

from aplicacion.trd import *
from aplicacion.expedientes import *