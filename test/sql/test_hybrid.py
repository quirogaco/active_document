#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, sys
import os, builtins

from sqlalchemy.orm import joinedload, immediateload, relationship, join
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.future import select
from sqlalchemy import func     

import configuracion_base

from librerias.datos.base import globales
from librerias.datos.sql  import sqalchemy_comunes
from librerias.flujos     import flujos_leer_sql


RADICADO_CLASE = globales.lee_clase("db_migrado_radicado_pqrs")

filtro = (RADICADO_CLASE.id == TRAZA_CLASE.requ_id)

RADICADO_CLASE.trazas_rel = relationship(
    TRAZA_CLASE,
    primaryjoin  = filtro,
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


sesion = sqalchemy_comunes.nuevaSesion('base')

# Join
#q = sesion.query(RADICADO_CLASE).filter(RADICADO_CLASE.id == 1000).join(TRAZA_CLASE, RADICADO_CLASE.id==TRAZA_CLASE.requ_id)
#q = sesion.query(RADICADO_CLASE, TRAZA_CLASE).join(TRAZA_CLASE, RADICADO_CLASE.id==TRAZA_CLASE.requ_id).filter(RADICADO_CLASE.id == 10001)
#q = sesion.query(RADICADO_CLASE).filter(RADICADO_CLASE.id == 1000)
#q = sesion.query(RADICADO_CLASE).join(TRAZA_CLASE, RADICADO_CLASE.id==TRAZA_CLASE.requ_id).filter(RADICADO_CLASE.id == 10001)

#q = sesion.query(RADICADO_CLASE, TRAZA_CLASE).select_from(RADICADO_CLASE).filter(RADICADO_CLASE.id == 1000).join(TRAZA_CLASE, RADICADO_CLASE.id==TRAZA_CLASE.requ_id)
#q = sesion.query(RADICADO_CLASE, TRAZA_CLASE.usua_idejecutor.label('content')).filter(RADICADO_CLASE.id == 1000)
#q = q.join(TRAZA_CLASE, RADICADO_CLASE.id==TRAZA_CLASE.requ_id)

#stmt      = select([RADICADO_CLASE, TRAZA_CLASE.traz_descripcion]).select_from(join(RADICADO_CLASE, TRAZA_CLASE, RADICADO_CLASE.id==TRAZA_CLASE.requ_id))
#print(stmt)
#resultado = sesion.execute(stmt).fetchall()

q = sesion.query(RADICADO_CLASE).filter(RADICADO_CLASE.id == 1000)
print(q)
resultado = q.all()

print("")
print("")
pprint.pprint( resultado[0].traza_asuntos )

"""
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
