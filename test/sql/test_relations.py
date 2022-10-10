
#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, sys
import os, builtins

from sqlalchemy.orm import joinedload, immediateload, relationship, join
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.future import select
from sqlalchemy import func     
from sqlalchemy.sql.expression import and_

import configuracion_base

from librerias.datos.base import globales
from librerias.datos.sql  import sqalchemy_comunes
from librerias.flujos     import flujos_leer_sql

""
DEPENDENCIAS_CLASE = globales.lee_clase("config_dependencias")
USUARIOS_CLASE     = globales.lee_clase("global_base_general")
RELACIONES_CLASE   = globales.lee_clase("global_base_relacion_estructura")

print("DEPENDENCIAS_CLASE:", DEPENDENCIAS_CLASE)
print("USUARIOS_CLASE:",     USUARIOS_CLASE)
print("RELACIONES_CLASE:",   RELACIONES_CLASE)

sesion = sqalchemy_comunes.nuevaSesion('base')

#pprint.pprint(dir(DEPENDENCIAS_CLASE.metadata))
pprint.pprint(dir(DEPENDENCIAS_CLASE))
#print( RELACIONES_CLASE.__table__)

#"""
filtro_primario   = and_(DEPENDENCIAS_CLASE.id       == RELACIONES_CLASE.origen_id)
filtro_secundario = and_(RELACIONES_CLASE.destino_id == USUARIOS_CLASE.id)
relacion = relationship(
    USUARIOS_CLASE,
    primaryjoin  = filtro_primario,
    foreign_keys = [DEPENDENCIAS_CLASE.id, RELACIONES_CLASE.destino_id ],
    remote_side  = RELACIONES_CLASE.origen_id,
    
    secondaryjoin = filtro_secundario,    
    secondary     = RELACIONES_CLASE.__table__,
        
    uselist      = True,
    lazy         = False  
)
DEPENDENCIAS_CLASE.relacion       = relacion
DEPENDENCIAS_CLASE.nombre_usuario = association_proxy(
    'relacion', 
    'nombre'
)

resultado = sesion.query(DEPENDENCIAS_CLASE).all()
print("")
print("")
#pprint.pprint( dir(resultado[0].tipo_relacion) )
print( resultado[0].nombre_usuario )

#"""

"""
print("")
print("")
print("RADICADO_CLASE:", RADICADO_CLASE)
print("TRAZA_CLASE:", TRAZA_CLASE)

filtro_primario   = and_(RADICADO_CLASE.id == TRAZA_CLASE.requ_id, TRAZA_CLASE.traz_estado == "RESUELTO")

RADICADO_CLASE.trazas_rel = relationship(
    TRAZA_CLASE,
    primaryjoin    = filtro_primario,
    foreign_keys = RADICADO_CLASE.id,
    remote_side  = TRAZA_CLASE.requ_id,
    uselist      = True,
    lazy         = False  
)

RADICADO_CLASE.traza_asuntos = association_proxy(
    'trazas_rel', 
    'traz_descripcion', 
    creator=lambda traza:
        traza  
    )

q = sesion.query(RADICADO_CLASE).filter(RADICADO_CLASE.id == 1000)
print(q)
resultado = q.all()

print("")
print("")
pprint.pprint( resultado[0].traza_asuntos )

print("")
print("")
print("resultado:")
for r in resultado:
    print("")
    for indice, asunto in enumerate(r.traza_asuntos):
        print("")
        print(indice)        
        pprint.pprint( asunto )

#pprint.pprint(dict(resultado[0].trazas_rel[0].to_dict()))

print("")
print("")
#pprint.pprint( dir( resultado[0] ) )
pprint.pprint( dict(resultado[0].to_dict()) )

"""


sesion.commit()
