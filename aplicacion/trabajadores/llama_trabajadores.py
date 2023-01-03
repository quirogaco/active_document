#!/usr/bin/env python3
# -*- coding: ISO-8859-15 -*-  

from subprocess import Popen

DETACHED_PROCESS         = 0x00000008
CREATE_NEW_PROCESS_GROUP = 0x00000200

####################
# Colas de trabajo #
####################
trabajadores = {
    'generales': [
        'celery', '-A', 'aplicacion.trabajadores_base.generales_celery',  
        'worker',  '-Q', 'generales',         
        '--concurrency=1', 
        '-Ofair', 
        '-n', 'worker1.%h',
        '--loglevel', 'info'
    ],

    'radicados': [
        'celery', '-A', 'aplicacion.trabajadores_base.radicados_celery',  
        'worker',  '-Q', 'radicados',         
        '--concurrency=1', 
        '-Ofair', 
        '-n', 'worker2.%h',
        '--loglevel', 'info'
    ],

    # TRABAJADORES PROGRAMADOS BEAT
    'programadas_beat': [
        'celery', '-A', 'aplicacion.trabajadores_base.programadas_beat',  
        'beat'
    ],

    'conversion_pdf': [
        'celery', '-A', 'aplicacion.trabajadores_base.conversion_pdf',  
        'worker',  '-Q', 'conversion_pdf',         
        '--concurrency=1', 
        '-Ofair', 
        '-n', 'worker3.%h',
        '--loglevel', 'info'
    ],

}

def invoca_trabajadores():
    global DETACHED_PROCESS, CREATE_NEW_PROCESS_GROUP

    comando = trabajadores['radicados']  
    process = Popen( comando, shell=False, stdin=None, stdout=None, stderr=None, close_fds=True) #, creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP )

    comando = trabajadores['generales']  
    process = Popen( comando, shell=False, stdin=None, stdout=None, stderr=None, close_fds=True) #, creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP )    

    # TRABAJADORES PROGRAMADOS BEAT 
    # Beat general  
    comando = trabajadores['programadas_beat']  
    process = Popen( comando, shell=False, stdin=None, stdout=None, stderr=None, close_fds=True) #, creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP )   

    comando = trabajadores['conversion_pdf']  
    process = Popen( comando, shell=False, stdin=None, stdout=None, stderr=None, close_fds=True) #, creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP ) 

print("")
print("***************************************************************************************************************************")
print("LLAMANDO TRABAJADORES")
invoca_trabajadores()