#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

#####################################
# Funci�n cuando termina el sistema #
#####################################
import platform
import atexit, signal

def al_salir(sig, func=None):
    print("al salir")
    termina()
    exit(0)

if platform.system() == "Linux":
    import signal
    signal.signal(signal.SIGTERM, al_salir)
elif platform.system() == "Darwin":
    pass
elif platform.system() == "Windows":
    import win32api
    win32api.SetConsoleCtrlHandler(al_salir, True)

# Funci�n de salida
def termina():  
    print("<--- TERMINA APLICACI�N --->")  

#atexit.register(termina)