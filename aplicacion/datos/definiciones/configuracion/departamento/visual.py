#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.base import globales

from . import departamento

grid_definicion_01 = {
    "tipo"    : "grid",
    "ruta"    : "dependencia",
    "id"      : "grid1", 
    "fuente"  : "terceros",   
    "columnas":[
        {
            "caption": "EMPLEADO",
            "width": 230,
            "fixed": True,
        }, 
        {
            "dataField": "NACIDO",
            "dataType": "date"
        }, 
        {
            "dataField": "FECHA CONTRATO",
            "dataType": "date"
        }, 
        {
            "dataField": "Position",
            "alignment": "right",
        }, 
        { 
            "dataField": "Address",
            "width": 230,
        }, 
        "City", "State", 
        {
            "dataField": "Zipcode",
            "visible": False
        }
    ],
};
globales.carga_definicion_visual("pais", (grid_definicion_01["ruta"] + "_" + grid_definicion_01["id"]), grid_definicion_01)



grid_definicion_02 = {
    "tipo"    : "grid",
    "ruta"    : "dependencia",
    "id"      : "grid2", 
    "fuente"  : "terceros",   
    "columnas":[ 
        { 
            "dataField": "Address",
            "width": 230,
        }, 
        "City", "State", 
        {
            "dataField": "Zipcode",
            "visible": False
        }
    ],
};
globales.carga_definicion_visual("pais", (grid_definicion_02["ruta"] + "_" + grid_definicion_02["id"]), grid_definicion_02)


grid_definicion_03 = {
    "tipo"    : "grid",
    "ruta"    : "dependencia",
    "id"      : "grid3", 
    "fuente"  : "terceros",   
    "columnas":[
        {
            "caption": "EMPLEADO",
            "width": 230,
            "fixed": True,
        }, 
        {
            "dataField": "NACIDO",
            "dataType": "date"
        }, 
        {
            "dataField": "Zipcode",
            "visible": False
        }
    ],
};

globales.carga_definicion_visual("pais", (grid_definicion_03["ruta"] + "_" + grid_definicion_03["id"]), grid_definicion_03)