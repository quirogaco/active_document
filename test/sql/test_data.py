#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, sys, random
import os, builtins

import configuracion_base

from librerias.utilidades import basicas  
from librerias.flujos     import flujos_insertar_sql
from librerias.datos.sql  import sqalchemy_comunes

def entero(maximo):
    return random.randint(0, maximo)

def ano_suma():
    lista = [
        "2018",
        "2019",
        "2020",
        "2021",
    ]
    indice = entero(len(lista)-1)

    return lista[ indice ]

def mes_suma():
    lista = [
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
    ]
    indice = entero(len(lista)-1)

    return lista[ indice ]

def dia_suma():
    lista = [
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26",
        "27",
        "28"
    ]
    indice = entero(len(lista)-1)

    return lista[ indice ]


def fuente_dato():
    lista = [
        "PQRS",
        "VENTANILLA"
    ]
    indice = entero(len(lista)-1)

    return lista[ indice ]

def radicado_dato():
    lista = [
        "8fb770a6-cad6-11eb-9166-006073b60f8a",
        "51c7f09b-cad6-11eb-946f-006073b60f8a",
        "35a6ce28-cad6-11eb-aa0d-006073b60f8a",
        "8fb770a6-cad6-11eb-9166-006073b60f8a",
        "b74c7b93-cad5-11eb-bff6-006073b60f8a",
        "0fbc14ae-ca0c-11eb-96de-006073b60f8a",
        "dcc559da-ca0a-11eb-846f-006073b60f8a",
        "fd11546d-ca09-11eb-bc33-006073b60f8a",
        "e4b4468d-ca09-11eb-89a6-006073b60f8a",
        "19963612-ca06-11eb-8884-006073b60f8a",
        "09e45152-ca06-11eb-ad5a-006073b60f8a",
        "c6714163-ca05-11eb-866b-006073b60f8a",
        "7c1bb18d-ca05-11eb-9373-006073b60f8a",
        "a2418fe4-ca04-11eb-a1b4-006073b60f8a",
        "92011104-ca04-11eb-841e-006073b60f8a",
        "693c1a57-ca04-11eb-bbe7-006073b60f8a",
        "f7372a5c-ca03-11eb-a3c0-006073b60f8a",
        "4966e3e2-ca03-11eb-bea4-006073b60f8a",
        "06d51d7a-ca03-11eb-a1d8-006073b60f8a",
        "bebc49a2-ca02-11eb-b1e2-006073b60f8a",
        "4f30a45a-ca02-11eb-aadb-006073b60f8a",
        "3a151d53-ca02-11eb-8db7-006073b60f8a",
        "1b7c727d-ca02-11eb-820b-006073b60f8a",
        "d41c1377-ca01-11eb-ba65-006073b60f8a",
        "947d8cfb-ca01-11eb-9ee1-006073b60f8a",
        "4544b71b-ca01-11eb-87c9-006073b60f8a",
        "ff0b48a7-ca00-11eb-9803-006073b60f8a",
        "c30edabb-ca00-11eb-8c77-006073b60f8a",
        "03141a85-c9fb-11eb-be3b-006073b60f8a",
        "2b54c8a5-c9f9-11eb-860b-006073b60f8a",
        "ce119b59-c9ea-11eb-8331-006073b60f8a",
        "96cd5eb6-c9ea-11eb-b079-006073b60f8a",
        "87738afe-c9ea-11eb-a104-006073b60f8a",
        "0af400eb-c9e9-11eb-855a-006073b60f8a",
        "0841d39a-c9e6-11eb-b243-006073b60f8a",
        "75dcebac-c9e4-11eb-8cc6-006073b60f8a",
        "b19deb98-c9e3-11eb-bf38-006073b60f8a"
    ]
    indice = entero(len(lista)-1)

    return lista[ indice ]

def responsable_dato():
    lista = [
        "39d612d6-acff-11eb-b928-006073b60f8a",
        "5628ab27-acff-11eb-a7e7-006073b60f8a",
        "4b3f5765-cddc-11eb-9f34-acfdce646f0d",
        "5d32cdcd-cddc-11eb-82db-acfdce646f0d",
        "980fb258-cddc-11eb-8dc8-acfdce646f0d",
        "e1770e07-cddc-11eb-846b-acfdce646f0d",
        "f3277c2d-cddc-11eb-bc11-acfdce646f0d",
        "0a83bbe0-cddd-11eb-bc8f-acfdce646f0d",
        "335f30af-cddd-11eb-8ccc-acfdce646f0d",
        "43ddde7d-cddd-11eb-a65e-acfdce646f0d"
    ]
    indice = entero(len(lista)-1)

    return lista[ indice ]

def dependencia_dato():
    lista = [
        "4aabc042-ac3d-11eb-b431-006073b60f8a",
        "a97564a7-adb0-11eb-bc14-006073b60f8a",
        "49409802-af81-11eb-b616-006073b60f8a",
        "d46a3fa2-af81-11eb-92af-006073b60f8a",
        "f23fa856-cdd2-11eb-bddc-acfdce646f0d",
        "037723cf-cdd3-11eb-b888-acfdce646f0d",
        "27d8eada-cdd3-11eb-bfce-acfdce646f0d",
        "3e3ee93a-cdd3-11eb-8717-acfdce646f0d",
        "a11a269c-cdd3-11eb-a3bf-acfdce646f0d",
        "b1f6bdc5-cdd3-11eb-93e5-acfdce646f0d",
        "c0739bbf-cdd3-11eb-8d73-acfdce646f0d",
        "09d71d25-cdd4-11eb-b9e4-acfdce646f0d",
        "155c28aa-cdd4-11eb-9bcd-acfdce646f0d",
        "d105f0bd-cdd4-11eb-9416-acfdce646f0d"
    ]
    indice = entero(len(lista)-1)

    return lista[ indice ]

def peticion_dato():
    lista = [
        "e6289306-b5b0-11eb-a79d-006073b60f8a",
        "03913e81-b5b1-11eb-88ea-006073b60f8a",
        "3d0fcf20-cdf8-11eb-be4e-acfdce646f0d",
        "a1cd4cea-cdf8-11eb-9b6c-acfdce646f0d",
        "b1d3ae0f-cdf8-11eb-85a6-acfdce646f0d"
    ]
    indice = entero(len(lista)-1)

    return lista[ indice ]

def tiempo_dato():
    tiempo = entero(20)

    return tiempo

def horasdias_dato():
    lista = [
        "HORAS",
        "DIAS"
    ]
    indice = entero(len(lista)-1)

    return lista[ indice ]

def prioridad_dato():
    lista = [
        "ALTA",
        "MEDIA",
        "BAJA",
    ]
    indice = entero(len(lista)-1)

    return lista[ indice ]

def fecha_hora():
    ano_valor   = ano_suma()
    mes_valor   = mes_suma()
    dia_valor   = dia_suma()
    fecha_valor = ano_valor + "-" + mes_valor + "-" + dia_valor
    fecha       = datetime.datetime.strptime(fecha_valor, '%Y-%m-%d').date()

    return fecha

def crea_registro():
    data_registro = {
        'creado_por_id'  : "*",
        'fuente'         : fuente_dato(),
        'tipo'           : "ENTRADA",
        'origen_id'      : radicado_dato(),
        "responsable_id" : responsable_dato(),
        "dependencia_id" : dependencia_dato(),
        "gestion_inicio" : fecha_hora(),
        "peticion_id"    : peticion_dato(),
        "total_tiempo"   : tiempo_dato(),
        "horas_dias"     : horasdias_dato(),
        "prioridad"      : prioridad_dato()
    }

    return data_registro 



#PETICION_CLASE = globales.lee_clase("peticion")

# Crear registro GESTIÓN    

sesion = sqalchemy_comunes.nuevaSesion('base')

for i in range(0, 5000):
    print("")
    datos = crea_registro()
    #pprint.pprint( datos )
    resultado = flujos_insertar_sql.ejecutar("base", "peticiones", datos)
    print("")

sesion.commit()