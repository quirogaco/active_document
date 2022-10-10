#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, sys

from prettytable import PrettyTable

sys.path.append('D:\gestor_2021_vite')

from librerias.email import email

direccion_smtp = "smtp.gmail.com"
puerto_smtp    = 587

de        = "quirogaco@gmail.com"
clave     = "sreojrjewsjkxnml"
para      = ["quirogaco@gmail.com", "fabigonz@esap.edu.co", "viveros.60@gmail.com"]
para      = ["quirogaco@gmail.com"]
archivos  = []

# Para jefe del area
asunto    = "Vencimientos radicados resumen por dependencia"     

# Contenido
tabla = PrettyTable(format=True, border=True, header=True, padding_width=2)
tabla.field_names = ["Responsable", "Radicado", "Fecha radicado", "Vence en", "Estado"]
tabla.add_row(["Alberto Jimenez", "E-2021-7488", "2021-05-10", "2021-05-28", "VENCIDO"])
tabla.add_row(["Alberto Jimenez", "E-2021-5466", "2021-04-02", "2021-04-22", "VENCIDO"])
tabla.add_row(["Alberto Jimenez", "E-2021-2790", "2021-03-10", "2021-03-28", "VENCIDO"])
tabla.add_row(["ANTONIO MACHADO", "E-2021-9655", "2021-06-01", "2021-06-15", "VENCIDO"])

contenido = tabla.get_html_string()

mensaje = email.mensaje_html(
    de, 
    para, 
    asunto,
    contenido, 
    archivos
)

email.enviar_mensaje_smtp(
    mensaje, 
    de, 
    clave, 
    para, 
    direccion_smtp, 
    puerto_smtp
)

# Para funcionario
asunto    = "Vencimientos radicados resumen por funcionario"     

# Contenido
tabla = PrettyTable(format=True, border=True, header=True, padding_width=2)
tabla.field_names = ["Responsable", "Radicado", "Fecha radicado", "Vence en", "Estado"]
tabla.add_row(["Alberto Jimenez", "E-2021-7488", "2021-05-10", "2021-05-28", "VENCIDO"])
tabla.add_row(["Alberto Jimenez", "E-2021-5466", "2021-04-02", "2021-04-22", "VENCIDO"])
tabla.add_row(["Alberto Jimenez", "E-2021-2790", "2021-03-10", "2021-03-28", "VENCIDO"])

contenido = tabla.get_html_string()

mensaje = email.mensaje_html(
    de, 
    para, 
    asunto,
    contenido, 
    archivos
)

email.enviar_mensaje_smtp(
    mensaje, 
    de, 
    clave, 
    para, 
    direccion_smtp, 
    puerto_smtp
)

