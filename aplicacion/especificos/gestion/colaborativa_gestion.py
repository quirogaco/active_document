#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, builtins, base64

from aplicacion.especificos.radicados.gestion import crea_gestion_base

# Crea petición COLABORATIVA
def crea_colaborativa(accion, datos={}, archivo=[], id_tarea=""):  
    peticiones_id = datos["peticiones"]
    crea_gestion_base.crea_gestion_colaborativa(datos, peticiones_id[0], id_tarea)  

    return {}