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
archivo = open("D:/ventanilla_datos_esap/entradas.pkl", 'rb')
datos   = pickle.load(archivo)
archivo.close()

longitud = len(datos)
print(len(datos))

pprint.pprint(datos[longitud-2000])

"""        
sesion = sqalchemy_comunes.nuevaSesion('base')

# ENTRADAS RADICADOS
contador      = 0
ENTRADA_CLASE = globales.lee_clase("db_migrado_entrada_ventanilla")
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
      'nro_guia'          : dato['nro_guia'],
      'anexos'            : dato['anexos'],
      'asunto'            : dato['asunto'],      

      # Información remitente
      'nit'              : dato['nit'],
      'name'             : dato['name'],
      'address'          : dato['address'],
      'phone'            : dato['phone'],
      'email'            : dato['email'],
      'cargo'            : dato['cargo'],
      'sender'           : dato['sender'],
      'pais_name'        : dato['pais_name'],
      'departamento_name': dato['departamento_name'],
      'ciudad_name'      : dato['ciudad_name'],    

      # Tramite
      'tramite_inicial'      : dato['tramite_inicial'],    
      'responsable_inicial'  : dato['responsable_inicial'],    
      'dependencia_inicial'  : dato['dependencia_inicial'],    

      'atributos_internos': dato
    }

    sqalchemy_insertar.insertar(sesion, ENTRADA_CLASE, data, False)
    sesion.commit()
    if contador > 2000:
        sesion.commit()
        contador = 0
        print(indice

sesion.commit()
"""    
    