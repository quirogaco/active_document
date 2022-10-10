#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint, builtins

# Celery
from celery import Celery
from kombu  import Queue, Exchange
from click  import Option

def base_celery(nombreGeneral):
    redisDireccion = 'redis://' + builtins._appServicios + ':6379/'
    amqpUsuario    = "guest"
    amqpDireccion  = 'pyamqp://' + amqpUsuario + '@' + builtins._appServicios + ':5672/' 
    #amqpDireccion  = 'pyamqp://' + amqpUsuario + '@' + "0.0.0.0" + ':5672/'
    #amqpDireccion  = 'pyamqp://' + amqpUsuario + '@' + "127.0.0.1" + ':5672/'
    #amqpDireccion  = 'pyamqp://' + amqpUsuario + '@' + "172.17.8.27" + ':5672'
    #amqpDireccion  = 'pyamqp://guest@localhost//'
    appCelery      = Celery(nombreGeneral, backend=redisDireccion, broker=amqpDireccion)

    appCelery.user_options['preload'].add(
        Option(('-Z', '--host'),
        default='localhost',
        help='ip de la maquina')
    )

    appCelery.user_options['preload'].add(
        Option(('-Z', '--port'),
        default='80',
        help='puerto de la maquina')
    )

    return appCelery

def simple_celery(nombreGeneral):
    return base_celery(nombreGeneral)

def aplicacion_celery(nombreGeneral, nombreQE):
    appCelery = base_celery(nombreGeneral)
    
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

    #appCelery.control.purge()
    
    return appCelery

# Carga variables de entorno y argumentos
from . import trabajador_inicio