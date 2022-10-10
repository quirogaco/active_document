#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, sys
import datetime

sys.path.append('D:\gestor_2021_vite')

from librerias.utilidades import vencimientos

fechas   = ["2021-06-16", "2021-06-21", "2021-07-05"]
festivos = [datetime.datetime.strptime(fecha, '%Y-%m-%d').date() for fecha in fechas]
hoy      = datetime.datetime.now(datetime.timezone.utc) 
dias     = 12

proxima  = vencimientos.siguiente_fecha_habil_dias(hoy, dias, festivos)

print("Proxima fecha habil:", dias, hoy, proxima)

print("")
print("")

despues    = hoy + datetime.timedelta(2)
diferencia = vencimientos.diferencia_en_dias_habiles( despues, proxima, festivos )
print("Diferencia dias habiles:", despues, diferencia)


"""
despues = hoy + datetime.timedelta(2)
print("dia semana:", hoy, despues.weekday())
print("datetime.timedelta(0) :", datetime.timedelta(0) )
"""