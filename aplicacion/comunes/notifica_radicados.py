#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.sql      import sqalchemy_filtrar 
from librerias.datos.archivos import leer_archivo

def notifica(datos):
    """
    print("")
    print("")
    print("")
    print("*******------->>> NOTIFICA:--->")    
    pprint.pprint(datos)
    """
    # Mezcla datos
    ruta_archivo   = builtins.rutaBase + 'temporal' + os.sep + "entrada.docx" 
    ruta_salida    = builtins.rutaBase + 'temporal' + os.sep + "salida.docx" 
    nombre_archivo = word_plantilla.mezcla_plantilla_archivos(ruta_archivo, ruta_salida, datos=datos)    
    
    # Inicia conversión
    ini = datetime.datetime.now()    
    #url = "http://" + str(builtins._appAnfitrion) + ":" + str(builtins._appPuerto) + '/entregar_archivo_disco/salida.docx' # + nombre_archivo    
    #url = "http://" + str(builtins._appAnfitrion) + ":8000" + '/entregar_archivo_disco/salida.docx'
    url = "http://" + str(builtins._appAnfitrion) + ":" + str(builtins._appPuerto) + '/entregar_archivo_disco/salida.docx' # + nombre_archivo    
    print("url:", url)
    print("builtins._appServicios:", builtins._appServicios)
    parametros = {
        "filetype"  : "docx",
        "title"     : "convertido",
        "url"       : url
    }
            
    ruta_destino  = conversion.a_pdfa(str(builtins._appServicios), "80", parametros)    
    jpg_ruta      = conversion.a_jpg(str(builtins._appServicios), "80", parametros)    

    print("")
    print("---------------------------------------------------")
    print("termina:", datetime.datetime.now()-ini)
    print("---------------------------------------------------")
    print("")

    de        = "quirogaco@gmail.com"
    clave     = "sreojrjewsjkxnml"
    #para      = ["quirogaco@gmail.com", "fabigonz@esap.edu.co", "viveros.60@gmail.com"]
    para      = ["quirogaco@gmail.com"]
    asunto    = "Notificación de radicado [E-2021-474755]"     
    archivos  = [ruta_destino]

    direccion_smtp = "smtp.gmail.com"
    puerto_smtp    = 587

    #mensaje = email.mensaje_texto(
    mensaje = email.mensaje_imagen(
        de, 
        para, 
        asunto, 
        jpg_ruta, 
        archivos=archivos
    )

    email.enviar_mensaje_smtp(
        mensaje, 
        de, 
        clave, 
        para, 
        direccion_smtp, 
        puerto_smtp
    )

    return {"ruta_destino": ruta_destino}