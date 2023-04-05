#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Base general con atributos basicos
from librerias.datos.sql                    import sqalchemy_tipo_campos as tipos
from librerias.datos.base                   import globales

campos = {
    "detalle": tipos.texto(propiedades={"titulo": "Detalle", "longitud": 512}), 
}

indexamiento = {}