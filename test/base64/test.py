#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, base64

pdf_id                = "QzpcVXNlcnNccXVpcm9cQXBwRGF0YVxMb2NhbFxUZW1wXDQ1MmVjZTA5LTRlM2EtMTFlYy1iZGQ1LTA4NjI2NmI1MzljMS5wZGY"
archivo_nombre_byte   = bytes(pdf_id, 'utf8')
#archivo_nombre_byte   = pdf_id
print("*** pdf_disco-0 **:", type(archivo_nombre_byte), archivo_nombre_byte)
# Base 64 a texto original
#decodificado          = base64.b64decode( archivo_nombre_byte.decode('ascii') )
decodificado          = base64.b64decode( archivo_nombre_byte + b'==' )
print("*** pdf_disco-1 **:", type(archivo_nombre_byte), archivo_nombre_byte)
# Byte a texto
archivo_nombre        = str( decodificado, 'utf-8')

print("")
print("")
    
print("")
print("")
print("********************* pdf_disco-1 *******************************:", archivo_nombre)
print("")
print("")
