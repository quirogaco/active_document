#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint, datetime

# Definiciones sql
from librerias.datos.base                import globales

# Base general con atributos basicos
from librerias.datos.base                   import globales
from aplicacion.datos.definiciones._comunes import elementos_comunes
from librerias.datos.sql                    import sqalchemy_clase_dinamica

from . import salida_campos
from . import salida_referencias
from . import salida_propiedades

# Campos elastic
camposElastic      = salida_campos.campos.copy()
camposIndexamiento = salida_campos.indexamiento.copy()
camposElastic.update(camposIndexamiento)

definicion = {
    "descripcion" : "Radicados Salida",
    "clase"       : "gestor_radicados_salida",
    "estructura"  : "radicados_salida",    
    "campos"      : salida_campos.campos,    
    "camposIndexamiento": camposIndexamiento,
    "archivos"    : {
        "cardinalidad" : "multiple",
        "tipo_relacion": "ANEXOS RADICADO",
        "cubeta"       : "radicados_repositorio"
    },
    # Referencias a otras estructuras
    "referencias" : salida_referencias.referencias,
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {}
}

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)

# Crea relacion y campos proxy para esta estructura ya que no es dinamica
sqalchemy_clase_dinamica.prepara_relaciones_proxy(definicion["clase"], definicion["referencias"], definicion["campos"])
sqalchemy_clase_dinamica.clase_serializar(definicion["clase"], definicion["campos"])
sqalchemy_clase_dinamica.clase_propiedades(definicion["clase"], definicion["campos"])

# Evento al cargar
CLASE = globales.lee_clase(definicion["clase"])

# Eventos de clase y objeto
def al_cargar(target, context):
    # print("")
    # print("................")
    # print("SALIDA")
    salida_propiedades.archivos_nombres(context.session, target)
    salida_propiedades.pdf_base(context.session, target)
    salida_propiedades.logs(context.session, target)
    
sqalchemy_clase_dinamica.asigna_evento(CLASE, "load", al_cargar)

# Procesos pre, post, ultimo
#from . import salida_procesamiento

# Normalización
#from . import salida_estructura_funciones


# # Eventos de clase y objeto
# COPIA DE ENTRADA
# def al_cargar(target, context):
#     # Primero trae Id de gestión para logs
#     radicado_propiedades.gestion_asignada_peticion(context.session, target)
#     radicado_propiedades.logs(context.session, target)
#     radicado_propiedades.archivos_nombres(context.session, target)
#     radicado_propiedades.archivos_total(context.session, target)
#     radicado_propiedades.pdf_base(context.session, target)
#     radicado_propiedades.relacionados(context.session, target)
#     radicado_propiedades.con_copia(context.session, target)    
    
sqalchemy_clase_dinamica.asigna_evento(CLASE, "load", al_cargar)