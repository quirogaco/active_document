#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint

import configuracion_base

from librerias.datos.elastic import elastic_operaciones
from librerias.datos.sql import sqalchemy_leer
from librerias.datos.base import globales
from librerias.datos.archivos import leer_archivo

conexion = globales.lee_conexion_elastic("base")

def recuperar(conexion, estructura):
    modelo = globales.lee_modelo_elastic(estructura)
    definicion = globales.lee_definicion(estructura) 

    # desde  = 0
    # resultado = sqalchemy_leer.leer_todos(
    #     "base", 
    #     estructura, 
    #     desde=0, 
    #     hasta=10000
    # )

    total = sqalchemy_leer.contar_registros("base", estructura)
    paso = 100
    resultado = []
    for posicion in range(0, total, paso):
        print("")
        print(estructura, posicion, (posicion+paso), total, end=' - ')
        resultado = sqalchemy_leer.leer_rango(
            "base", 
            estructura, 
            desde=posicion, 
            hasta=(posicion+paso), 
            retornar="diccionario"
        )
        bulk = elastic_operaciones.bulk_indexar(
            conexion, 
            modelo["modelo"], 
            modelo["indice"], 
            resultado
        )
        # for r in resultado:
        #     print(r["dependencia_nombre"], r["nombre"], "D:", r["dependencia_id"])        
            #print(r["trd_nombre"], r["nombre"], "U:", r["ubicaciones_gestion"])# "D:", r["dependencias_gestion"],            
            # print(r["atributos_"], r["nro_respuesta"])
            # print(r["nro_respuesta"])

    print("")
    
    print("RESULTADO>>>" + estructura, total)    
    print("")

    pprint.pprint(resultado)

    # Peticiones
    # for r in resultado:
    #     print(r["tipo_radicado"], r["funcionarios_id"])

    # for r in resultado:
    #     print("")
    #     print("....................")
    #     print(r["nro_radicado"], r["clase_radicado"], r["gestion_asignada_peticion"])

        
        # for archivo in r["archivos"]:
        #     nombre_archivo = leer_archivo.salva_archivo_minio(archivo["id"])  
        #     print(r["nro_radicado"], nombre_archivo)

    # Usuarios, Dependencias
    # for r in resultado:
    #     if r.get("coordinadores_ids", []):
    #         pprint.pprint(r)

    # # Usuarios
    # for r in resultado:
    #     if r["roles_especificos"]:
    #         pprint.pprint(r)

    # # nombre_archivo = leer_archivo.salva_archivo_minio(archivos[0]["id"])
    # print("")

# CONFIGURACIÓN
# recuperar(conexion, "configuracion_general")
# recuperar(conexion, "canales_comunicacion")
# recuperar(conexion, "roles")
# recuperar(conexion, "ubicaciones")
# recuperar(conexion, "usuarios")
# recuperar(conexion, "dependencias")
# recuperar(conexion, "continentes")
# recuperar(conexion, "paises")
# recuperar(conexion, "departamentos")
# recuperar(conexion, "ciudades")
# recuperar(conexion, "grupo_usuarios")
# recuperar(conexion, "festivos")
# recuperar(conexion, "reportes_dinamicos")
# recuperar(conexion, "plantillas")
# recuperar(conexion, "consecutivos")cls
# recuperar(conexion, "tipo_identificaciones")
# recuperar(conexion, "genero")
# recuperar(conexion, "tipo_poblacion")
# recuperar(conexion, "rango_edad")
# recuperar(conexion, "discapacidad")
# recuperar(conexion, "tipo_terceros")
# recuperar(conexion, "terceros")
# recuperar(conexion, "tipo_peticiones")
# recuperar(conexion, "temas")
# recuperar(conexion, "subtemas")
# recuperar(conexion, "empresas_mensajeria")
# recuperar(conexion, "motivos_devolucion")
# recuperar(conexion, "permisos_archivo")

#recuperar(conexion, "global_base_general")
#recuperar(conexion, "tipo_peticiones")
#recuperar(conexion, "tramites")


#"""
# RADICACION GESTION
# recuperar(conexion, "radicados_entrada")
# recuperar(conexion, "radicados_salida")
# recuperar(conexion, "radicados_interno")
# recuperar(conexion, "peticiones")
# recuperar(conexion, "copias")
recuperar(conexion,"correos_descargados")
#"""

#"""
# ARCHIVO
# recuperar(conexion, "agn_fondo_documental")
# recuperar(conexion, "agn_trd")
# recuperar(conexion, "agn_dependencia_trd")
# recuperar(conexion, "agn_serie_trd")
# recuperar(conexion, "agn_subserie_trd")
# recuperar(conexion, "agn_expedientes_trd")
# recuperar(conexion, "agn_tipo_documental_trd")
# recuperar(conexion, "agn_documentos_trd")

#recuperar(conexion, "datos_formularios_dinamicos")
#"""

#recuperar(conexion, "peticiones")
#recuperar(conexion, "radicados_entrada")

#recuperar(conexion, "agn_documentos_trd")
#recuperar(conexion, "agn_dependencia_trd")
#recuperar(conexion, "agn_serie_trd")
# recuperar(conexion, "agn_expedientes_trd")
#recuperar(conexion, "dependencias")
#recuperar(conexion, "agn_prestamos_trd")

#recuperar(conexion, "logs")