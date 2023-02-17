    #!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint
from librerias.datos.base import globales

#################
# Agrupamientos #
#################

import pandas as pd

def gruposRespuesta(grupos, datos):
    #print("")
    #print("grupoRespuesta")
    #pprint.pprint(grupos)
    # Campos para agrupar
    campos   = [ grupo["selector"] for grupo in grupos]
    expandir = {}
    for grupo in grupos:
      expandir[(grupo["selector"])] = grupo["isExpanded"]
    #pprint.pprint(expandir)
    
    # Lista de registros a dataframe
    df  = pd.DataFrame(datos)
    dfg = df.groupby(campos[0])

    # Grupos superios
    grupos_primer_nivel = dfg.ngroups
   
    # data por grupo    
    diccionario_grupos = dict(tuple(dfg))
    keys               = diccionario_grupos.keys()
    data               = []
    for key in keys:
        items = diccionario_grupos[key]
        #print("--------->>>>")
        #print("items:", key)
        #for k in items.keys():
        #  print("k:", k, type(k))
        #pprint.pprint(diccionario_grupos[key])
        if key not in ["", None, "None"]:
            item = {
                "key"  : key,
                #"items": diccionario_grupos[key],
                "items": None,
                "count": len(diccionario_grupos[key])   ,
                #"summary": no aplica por ahora  
            }        
            data.append(item)

    resultado = {
        "data"      : data,
        "groupCount": grupos_primer_nivel,
        "totalCount": len(datos),      
        "agrupado"  : True # indicar agrupaci�n               
    }     
    pprint.pprint(resultado['data'])
    print("NUMERO DE ITEMS>>>>>>>>>>>>>:", len(resultado['data']))
    return resultado