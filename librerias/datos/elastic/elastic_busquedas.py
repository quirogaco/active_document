    #!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint
from elasticsearch_dsl import Search

from librerias.datos.base import globales

from . import elastic_ordenamientos
from . import elastic_agrupamientos
from . import elastic_filtros

##############
# Resultados #
##############
def procesaResultado(elementos, parametros):
    """
    print("......................")
    pprint.pprint(elementos)
    print("......................")
    """
    total      = elementos["total"]["value"] 
    hits       = elementos["hits"]   
    data       = [] 
    for hit in hits:        
        # hit internos
        item = hit["_source"]           
        """
        resaltados = []        
        inner_hits = hit.get('inner_hits', {})
        for campo, valor in inner_hits.items():
            inners = valor["hits"]["hits"]
            for inner in inners:          
                source_hit    = inner.get("_source", {})
                highlight_hit = inner.get("highlight", {})
                for campo, valor in highlight_hit.items():
                    texto =  "<br><div style='color:green;' >..................................</div><br>".join(valor)
                    resaltados.append({
                        'campo' : campo,
                        "tipo"  : "inner",
                        "valor" : texto,
                        "source": source_hit
                    }) 
        item["_resaltados_"] = resaltados
        """

        # campos de script
        campos = hit.get("fields", {})   
        for campo, valor in campos.items():
            item[campo] = valor[0]
                
        data.append(item)  

    # Agrupar resultados
    grupos = parametros.get("grupos", []) 
    if len(grupos) > 0:
        data = elastic_agrupamientos.gruposRespuesta(grupos, data)

    #print("total:", total)   
    resultado = {
        "total"     : total,
        "items"     : data
    }

    return resultado

from datetime import datetime
# Busqueda con parametros, genera query
def ejecutarBusqueda(estructura, parametros, definicion, id_tarea):
    querytime = globales.lee_modelo_querytime(estructura)
    parametros = parametros["params"]
    # Crea objeto de busqueda
    #"""
    # print("")
    # print("")    
    # print("BUSQUEDA PARAMETROS------------->", estructura)
    # pprint.pprint(parametros) 
    # #pprint.pprint(definicion)
    # #print("")
    # print("***************XXXXXXXXXXXXXXX**********************************")
    # print("")
    # print("")
    # print("")   
    #""" 
    #pprint.pprint(querytime)
    conexion  = globales.lee_conexion_elastic("base")
    busqueda  = Search(using=conexion, index=estructura)
    busqueda  = busqueda.extra(track_total_hits=True)

    # Ordenamientos sort
    busqueda = elastic_ordenamientos.prepararOrdenamiento(busqueda, estructura, parametros, definicion)

    # Querys y filtros
    resaltar = parametros.get('resaltar', [])
    definicion["resaltar"] = resaltar
    busqueda = elastic_filtros.prepararFiltros(busqueda, parametros, definicion)

    # Rango de busqueda 
    inicio   = parametros["desde"]
    final    = parametros["desde"] + parametros["hasta"]
    busqueda = busqueda[inicio:final]

    # Excluir
    indexamiento = definicion.get('indexamiento', {})
    excluir      = indexamiento.get('excluir', [])
    if ( len(excluir) > 0 ):
        busqueda = busqueda.source(excludes=excluir)

    # Incluir
    campos = parametros.get('campos', [])
    if ( len(campos) > 0 ):
        busqueda = busqueda.source(includes=campos)
        #busqueda = busqueda.fields(campos)
    else:
        busqueda = busqueda.source(includes=['*'])
        #busqueda = busqueda.fields(['*'])
    
    for campo, script in querytime.items():
        #print("**********", campo)
        #pprint.pprint(script)
        #busqueda = busqueda.script_fields(**{campo:script})
        pass

    # Ejecuta busqueda y procesa respuesta
    #"""
    # print("")
    # print("")
    # print("diccionario:")
    # pprint.pprint(busqueda.to_dict())
    # print("")
    # print("")
    #"""

    elementos      =  busqueda.execute().to_dict()["hits"] 
    resultado      = procesaResultado(elementos,  parametros)
    
    return resultado


# Busqueda query pregenerados
def crea_conexion_query(estructura):
    conexion  = globales.lee_conexion_elastic("base")
    busqueda  = Search(using=conexion, index=estructura)

    return busqueda

def ejecutar_querys(estructura, querys):
    # Crea objeto de busqueda
    #print("BUSQUEDA PARAMETROS------------->", estructura)
    conexion  = globales.lee_conexion_elastic("base")
    busqueda  = Search(using=conexion, index=estructura)
    busqueda  = busqueda.extra(track_total_hits=True)


    elementos = busqueda.execute().to_dict()["hits"]        
    resultado = elementos
    
    return resultado

def ejecutar(estructura, parametros, definicion, id_tarea):
    # print("")
    # print("")
    # print("********************************************************************")
    # print("estructura:", estructura)
    # #parametros = parametros["params"]
    # pprint.pprint(parametros) 
    # pprint.pprint(definicion)
    # #print("")
    # print("********************************************************************")

    resultado = ejecutarBusqueda(estructura, parametros, definicion, id_tarea)
    
    # print("")
    # print("")
    # print("resultado:") 
    # pprint.pprint(resultado)
    
    return resultado