#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint, datetime

# Definiciones sql
from librerias.datos.base                import globales

# Base general con atributos basicos
from librerias.datos.base                   import globales
from aplicacion.datos.definiciones._comunes import elementos_comunes
from librerias.datos.sql                    import sqalchemy_clase_dinamica

from . import interno_campos
from . import interno_referencias
from . import interno_propiedades

# Campos elastic
camposElastic      = interno_campos.campos.copy()
camposIndexamiento = interno_campos.indexamiento.copy()
camposElastic.update(camposIndexamiento)

definicion = {
    "descripcion" : "Radicados Interno",
    "clase"       : "gestor_radicados_interno",
    "estructura"  : "radicados_interno",    
    "campos"      : interno_campos.campos,    
    "camposIndexamiento": camposIndexamiento,
    "archivos"    : {
        "cardinalidad" : "multiple",
        "tipo_relacion": "ANEXOS RADICADO",
        "cubeta"       : "radicados_repositorio"
    },
    # Referencias a otras estructuras
    "referencias" : interno_referencias.referencias,
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
    # print("INTERNO")
    interno_propiedades.archivos_nombres(context.session, target)
    interno_propiedades.pdf_base(context.session, target)
    interno_propiedades.logs(context.session, target)
    
sqalchemy_clase_dinamica.asigna_evento(CLASE, "load", al_cargar)


# Procesos pre, post, ultimo
from . import interno_procesamiento

# Normalizaci�n
from . import interno_estructura_funciones