#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from minio import Minio
from parent_import import parentdir
globales     = parentdir.parentdir.librerias.datos.base.globales

#pprint.pprint(dir(Minio))

client = Minio(    
    "172.24.153.161:9000",
    access_key="minio",
    secret_key="minio123",
    secure=False,
)
#print("client:", client)
#client.

"""
# Make 'asiatrip' bucket if not exist.
client.make_bucket('encriptado')
ENC_CONFIG = {
    'ServerSideEncryptionConfiguration': {
        'Rule': [
            {
                'ApplyServerSideEncryptionByDefault': {
                    'SSEAlgorithm': 'AES256'
                }
            }
        ]
    }
}

client.put_bucket_encryption('encriptado', ENC_CONFIG)
"""

#"""
gestor = "gestor.uno.dos"
found = client.bucket_exists(gestor)
if not found:
    client.make_bucket(gestor)


objects = client.list_objects(gestor, recursive=True)
for obj in objects:
    #pprint.pprint(dir(obj))
    print(obj.is_dir, obj.object_name)

client.fput_object(
    gestor, 
    "mas/menos/sigue/que/Activiti_User_Guide.pdf", "d:/Activiti_User_Guide.pdf",
)

print("")
print("")
datos = client.stat_object(gestor, "mas/menos/sigue/que/Activiti_User_Guide.pdf")
for key in dir(datos):
    print(key, getattr(datos, key))

#pprint.pprint(dir(datos))
#print(datos.version)
#"""
