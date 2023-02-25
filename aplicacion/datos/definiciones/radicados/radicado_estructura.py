#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint, datetime

# Definiciones sql
from librerias.datos.base import globales

# Base general con atributos basicos
from librerias.datos.base                   import globales
from aplicacion.datos.definiciones._comunes import elementos_comunes
from librerias.datos.sql                    import sqalchemy_clase_dinamica

from . import radicado_campos
from . import radicado_referencias
from . import radicado_propiedades

# Campos elastic
camposElastic      = radicado_campos.campos.copy()
camposIndexamiento = radicado_campos.indexamiento.copy()
camposElastic.update(camposIndexamiento)

definicion = {
    "descripcion" : "Radicados Entrada",
    "clase"       : "gestor_radicados_entrada",
    "estructura"  : "radicados_entrada",    
    "campos"      : radicado_campos.campos,    
    "camposIndexamiento": camposIndexamiento,
    "archivos"    : {
        "cardinalidad" : "multiple",
        "tipo_relacion": "ANEXOS RADICADO",
        "cubeta"       : "radicados_repositorio"
    },
    # Referencias a otras estructuras
    "referencias" : radicado_referencias.referencias,
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {},
    "reporte"     : "SI" # Fuente de datos para REPORTES
}

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)

# Crea relacion y campos proxy para esta estructura ya que no es dinamica
sqalchemy_clase_dinamica.prepara_relaciones_proxy(definicion["clase"], definicion["referencias"], definicion["campos"])
sqalchemy_clase_dinamica.clase_serializar(definicion["clase"], definicion["campos"])
sqalchemy_clase_dinamica.clase_propiedades(definicion["clase"], definicion["campos"])
sqalchemy_clase_dinamica.clase_propiedades_no_columna(definicion["clase"])

# Evento al cargar
CLASE = globales.lee_clase(definicion["clase"])

# Eventos de clase y objeto
def al_cargar(target, context):
    # Primero trae Id de gestión para logs
    # print("")
    # print("................")    
    # print("ENTRADA")
    radicado_propiedades.gestion_asignada_peticion(context.session, target)
    radicado_propiedades.logs(context.session, target)
    radicado_propiedades.archivos_nombres(context.session, target)
    radicado_propiedades.archivos_total(context.session, target)
    radicado_propiedades.pdf_base(context.session, target)
    radicado_propiedades.relacionados(context.session, target)
    radicado_propiedades.con_copia(context.session, target)    
    
sqalchemy_clase_dinamica.asigna_evento(CLASE, "load", al_cargar)