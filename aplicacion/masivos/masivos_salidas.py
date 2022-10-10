#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, random 

from librerias.datos.sql         import sqalchemy_modificar, sqalchemy_leer, sqalchemy_insertar, sqalchemy_borrar
from librerias.datos.elastic     import elastic_operaciones
from librerias.flujos            import flujos_insertar_sql
from librerias.utilidades        import basicas  
from librerias.datos.estructuras import estructura_operaciones


def salvar_listado(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    datos_listado = {
        "origen"        : datos["datos"]["origen"], 
        "dependencia_id": datos["datos"]["dependencia_id"],   
        "detalle"       : datos["datos"]["detalle"],        
        "destinatarios" : datos["datos"]["destinatarios"]
    }
    resultado = sqalchemy_insertar.insertar_registro_estructura("destinatarios_listado", datos_listado)
    elastic_operaciones.indexar_registro("destinatarios_listado", resultado["id"])
    
    return resultado

def modificar_listado(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    listado_id    = datos["datos"]["listado_id"]
    datos_listado = {
        "dependencia_id": datos["datos"]["dependencia_id"],   
        "detalle"       : datos["datos"]["detalle"],        
        "destinatarios" : datos["datos"]["destinatarios"]
    }
    resultado = sqalchemy_modificar.modificar_un_registro("destinatarios_listado", listado_id, datos_listado)
    elastic_operaciones.indexar_registro("destinatarios_listado", resultado["id"])
    
    return resultado

def borrar_listado(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    listado_id = datos["datos"]["listado_id"]
    resultado  = sqalchemy_borrar.borrar_un_registro("destinatarios_listado", listado_id)
    elastic_operaciones.eliminar_registro("destinatarios_listado", listado_id)
    
    return resultado

def generar_masivo(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    print("")
    print("")
    print("**************************************************************")
    print("MASIVO SALIDA")
    pprint.pprint(datos)
    print("")
    print("")   
    listado_id    = datos["datos"]["listado_id"]
    listado       = sqalchemy_leer.leer_un_registro("destinatarios_listado", listado_id)
    destinatarios = listado["destinatarios"] 
    print("destinatarios:")
    pprint.pprint(destinatarios)

    resultado     = {}
    lista_salidas = []

    radicado = "S-2021-" + str(random.randint(0, 10000))
    datos["nro_radicado"]   = radicado
    datos["fecha_radicado"] = datetime.datetime.now()

    for destinatario in destinatarios:
        salida_datos = {
            # BASICOS
            "fecha_radicado"         : datetime.datetime.now(),
            "fecha_documento"        : datetime.datetime.now(),
            "nro_radicado"           : radicado,
            "asunto"                 : datos["datos"]['asunto'],
            "nro_folios"             : datos["datos"]['nro_folios'],
            "tipo_firma"             : datos["datos"]['tipo_firma'],
            "reserva"                : "NO",
            "medio_notificacion"     : datos["datos"]['medio_notificacion'],
            "dependencia_responde_id": datos["datos"]['dependencia_responde_id'],
            "funcionario_responde_id": datos["datos"]['funcionario_responde_id'],
            # TERCERO
            "tercero_nro_identificacion"    : datos["datos"].get("nro_identificacion", ""),  
            "tercero_razon_social"          : datos["datos"].get("razon_social", ""),  
            "tercero_cargo"                 : datos["datos"].get("cargo", ""),   
            "tercero_nombres"               : datos["datos"].get("nombre_completo", ""),           
            "tercero_apellidos"             : datos["datos"].get("apellidos", ""),            
            "tercero_correo_electronico"    : datos["datos"].get("correo_electronico", ""),  
            "tercero_direccion"             : datos["datos"].get("direccion", ""),  
            "tercero_codigo_postal"         : datos["datos"].get("codigo_postal", ""),  
            "tercero_telefono"              : datos["datos"].get("telefono", ""),    
            "tercero_telefono_movil"        : datos["datos"].get("telefono_movil", ""),  
            "tercero_fax"                   : datos["datos"].get("fax", ""),   
            "tercero_ciudad_id"             : datos["datos"].get("ciudad_id", ""),          }
        lista_salidas.append(salida_datos)
    
    for salida_datos in lista_salidas:        
        uuid       = basicas.uuidTexto()
        resultado  = flujos_insertar_sql.ejecutar("base", "radicados_salida", salida_datos, uuid)
        estructura_operaciones.indexaEstructura("radicados_salida", resultado, True)
                
    return resultado

def generar_masivo_interno(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    print("")
    print("")
    print("**************************************************************")
    print("MASIVO INTERNO")
    pprint.pprint(datos)
    print("")
    print("")    
    listado_id    = datos["datos"]["listado_id"]
    listado       = sqalchemy_leer.leer_un_registro("destinatarios_listado", listado_id)
    destinatarios = listado["destinatarios"] 
    print("generar_masivo_interno - destinatarios:")
    pprint.pprint(destinatarios)

    resultado      = {}
    lista_internos = []

    radicado = "I-2021-" + str(random.randint(0, 10000))
    datos["nro_radicado"]   = radicado
    datos["fecha_radicado"] = datetime.datetime.now()

    for destinatario in destinatarios:
        funcionario_id = destinatario["id_registro"]
        funcionario    = sqalchemy_leer.leer_un_registro("usuarios", funcionario_id)
        print(funcionario)  

        print("destintario")
        print(destinatario)
        interno_datos = {
            # BASICOS
            "fecha_radicado"         : datetime.datetime.now(),
            "nro_radicado"           : radicado,
            "asunto"                 : datos["datos"]['asunto'],
            #"nro_folios"             : datos["datos"]['nro_folios'],
            #"tipo_firma"             : datos["datos"]['tipo_firma'],
            #"reserva"                : "NO",
            #"medio_notificacion"     : datos["datos"]['medio_notificacion'],
            "dependencia_envia_id"  : datos["datos"]['dependencia_envia_id'],
            "funcionario_envia_id"  : datos["datos"]['funcionario_envia_id'],
            "dependencia_recibe_id" : funcionario['dependencia_id'],
            "funcionario_recibe_id" : funcionario_id
        }
        lista_internos.append(interno_datos)
    
    
    for interno_datos in lista_internos:        
        uuid       = basicas.uuidTexto()
        resultado  = flujos_insertar_sql.ejecutar("base", "radicados_interno", interno_datos, uuid)
        estructura_operaciones.indexaEstructura("radicados_interno", resultado, True)
                

    return resultado

acciones_funcion = {
    "salvar"         : salvar_listado,
    "modificar"      : modificar_listado,
    "borrar"         : borrar_listado,
    "generar"        : generar_masivo,
    "generar_interno": generar_masivo_interno
}

def acciones_ejecuta(datos={}, archivos=[], id_tarea=""):
    accion = datos["accion"]
    print("")
    print("")
    print("------------------------------------------------")
    print('/acciones_ejecuta:', id_tarea) 
    print('datos:')
    pprint.pprint(datos)   
    print('archivos:', archivos)
    
    funcion   = acciones_funcion[accion]
    resultado = funcion(accion, datos, archivos, id_tarea)
    print("------------------------------------------------")
    print("")
    print("")

    return resultado
