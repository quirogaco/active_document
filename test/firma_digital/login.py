
import pprint

import requests
import json

url  = "https://8uw10ruhfj.execute-api.us-east-2.amazonaws.com/qa/authentication/api/Login"
data = {
    'usuario': 'esapuser',
    'clave'  : '7v40RK5C'
}
#respuesta = requests.post(url, data=json.dumps(d))
respuesta = requests.post(url, json = data)

pprint.pprint(dir(respuesta))

print("")
print("....")
print("json:")
pprint.pprint(respuesta.json())
print("status_code:", respuesta.status_code)