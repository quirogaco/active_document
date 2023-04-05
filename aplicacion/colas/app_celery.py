#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import builtins

# Celery
from celery import Celery
from kombu import Queue, Exchange

def add_preload_options(parser):
    print("0 - ******************************>>>> add_preload_options")
    parser.add_argument('-SERVICIOS_CELERY')
    parser.add_argument('-NODO')
    parser.add_argument('-ip')
    parser.add_argument('-port')

def base_celery(nombreGeneral, nombreQE):
    redisDireccion = 'redis://' + trabajador_inicio.leerNodo(builtins.zk, builtins.nsBase+"redis/direccion") + '/'
    amqpUsuario    = trabajador_inicio.leerNodo(zk, builtins.nsBase+"amqp/usuario")
    amqpDireccion  = 'pyamqp://' + amqpUsuario + '@' + trabajador_inicio.leerNodo(builtins.zk, builtins.nsBase+"amqp/direccion")  + '//'  
    appCelery      = Celery(nombreGeneral, backend=redisDireccion, broker=amqpDireccion)
    appCelery.user_options['preload'].add(add_preload_options)

    return appCelery

def simple_celery(nombreGeneral, nombreQE=None):
    return base_celery(nombreGeneral, nombreQE)

def aplicacion_celery(nombreGeneral, nombreQE):
    appCelery = base_celery(nombreGeneral, nombreQE)
    appCelery.conf.update(
        task_serializer          = 'json',
        accept_content           = ['json'] , 
        result_serializer        = 'json',
        enable_utc               = True,
        timezone                 = 'America/Bogota',
        broker_transport_options = {'confirm_publish': True},
        broker_heartbeat         = 30,
        result_persistent        = True
    )

    appCelery.conf.task_queues = (
        Queue(nombreQE, exchange=Exchange(nombreQE), routing_key=nombreQE),
    )

    return appCelery

# Caraga variables de entorno y argumentos
from . import trabajador_inicio