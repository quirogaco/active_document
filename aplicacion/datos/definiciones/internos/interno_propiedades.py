#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint

from librerias.datos.sql import sqalchemy_comunes
from librerias.datos.base import globales

# Si esta firmado
def esta_firmado(r_):
    firmado = "NO"
    if "DIGITAL" in r_.tipo_firma:
        firmado = "SI"
    # FALTA VALIDAR POR FIRMA FISICA O ELECTRONICA

    return firmado