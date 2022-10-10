#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint

from librerias.datos.sql  import sqalchemy_comunes
from librerias.datos.base import globales

"""
def gestion_asignada_peticion(r_):
    asignada      = "NO"
    GESTION_CLASE = globales.lee_clase("gestor_peticiones")
    sesion        = sqalchemy_comunes.nuevaSesion("base") 
    peticion      = sesion.query(GESTION_CLASE).filter( GESTION_CLASE.origen_id == r_.id ).first()
    if peticion != None:
        asignada = "SI"
    sesion.close()
    
    return  asignada
"""