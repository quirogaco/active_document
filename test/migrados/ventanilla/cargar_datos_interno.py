#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, sys, pickle
from datetime import datetime

import configuracion_base

from librerias.datos.sql  import sqalchemy_comunes
from librerias.datos.sql  import sqalchemy_insertar
from librerias.datos.base import globales

# Carga datos
archivo = open("D:/ventanilla_datos_esap/interno.pkl", 'rb')
datos   = pickle.load(archivo)
archivo.close()

longitud = len(datos)
pprint.pprint(datos[longitud-2000])

print(longitud)

#"""        
sesion = sqalchemy_comunes.nuevaSesion('base')

# INTERNOS RADICADOS
contador      = 0
INTERNO_CLASE = globales.lee_clase("db_migrado_interno_ventanilla")
for indice, dato in enumerate(datos):
    contador += 1        
    fecha = dato['fecha_radicado'].replace("T", " ")
    data = {
      'id'                : dato['id'],
      'radicado_en'       : dato['radicado_en'],
      'radicado_por'      : dato['radicado_por'],
    
      # Información base
      'fecha_radicado'    : datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S'),
      'nro_radicado'      : dato['nro_radicado'],
      'nro_origen'        : dato['nro_origen'],
      'anexos'            : dato['anexos'],
      'asunto'            : dato['asunto'],      

      # Tramite
      'tramite_inicial'      : dato['tramite_inicial'],    
      'area_sender_name'     : dato['area_sender_name'],    
      'sender_name'          : dato['sender_universal'],    
      'area_target_name'     : dato['area_target_name'],    
      'target_name'          : dato['target_name'],    
  
      'atributos_internos': dato
    }

    sqalchemy_insertar.insertar(sesion, INTERNO_CLASE, data, False)
    sesion.commit()
    if contador > 2000:
        sesion.commit()
        contador = 0
        print(indice)

sesion.commit()
#"""    
    