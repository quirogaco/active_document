#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import pprint, builtins

from . import crea_celery_app

radicados_app = crea_celery_app.aplicacion_celery('radicados_app', 'radicados')

# Crea ventanilla gestión 
from aplicacion.especificos.radicados.gestion import gestion
@radicados_app.task(name='radicados_app_ventanilla_gestion')
def ventanilla_gestion(**parametros):
    gestion.asigna_ventnailla(**parametros)

# Crea ventanilla gestión  
from aplicacion.especificos.radicados.gestion import gestion
@radicados_app.task(name='radicados_app_pqrs_gestion')
def pqrs_gestion(**parametros):
    gestion.asigna_pqrs(**parametros)

# Crea logs
from aplicacion.logs import crea_logs
# Crea log historico
@radicados_app.task(name='radicados_app_crea_log')
def radicados_app_crea_log(**parametros):
    #print("radicados_app_crea_log:")
    #pprint.pprint(parametros)
    crea_logs.crea_log(**parametros)

# Crea copia
from aplicacion.copias import crea_copias
# Crea copias radicado
@radicados_app.task(name='radicados_app_crea_copia')
def crea_copia(**parametros):
    crea_copias.crea_copia(**parametros) 

# Tercero - log
from aplicacion.comunes import tercero_log
# Log de manejo de terceros
@radicados_app.task(name='radicados_app_tercero_log')
def tercero_log(**parametros):
    tercero_log.crea_tercero_log(**parametros)


##########################################
# Crea Tercero - Archivos - Log - Copias #
##########################################
from aplicacion.especificos.radicados.comunes import radicado_global
@radicados_app.task(name='radicados_app_tercero_log_anexos_copias')
def radicados_app_tercero_log_anexos_copias(**parametros):
    radicado_global.crea_tercero_log_anexos_copias(**parametros)

#####################################
# Envia correo notificando radicado #
#####################################
from aplicacion.comunes import pdf_envia
@radicados_app.task(name='radicados_app_radicado_pdf_envia')
def radicados_app_radicado_pdf_envia(**parametros):
    pdf_envia.enviar_correo_radicado(**parametros)

###############################################
# Envia correo notificando asigancion gestión #
###############################################
from aplicacion.especificos.radicados.gestion import notifica_gestion
@radicados_app.task(name='radicados_app_notifica_gestion')
def radicados_app_notifica_gestion(**parametros):
    notifica_gestion.notifica(**parametros)