npm run dev -- --port 3000
npm run dev -- --port 3000 --https

uvicorn servidor:_app --host=192.168.1.144 --port=9100 --log-level critical --workers=2 -nodo=001 -celery=SI

uvicorn servidor:_app --host=192.168.1.144 --port=9100 --workers=2
uvicorn servidor:_app --host=192.168.1.99 --port=9100 --workers=2
uvicorn servidor:_app --host=172.16.202.58 --port=9100 --workers=4
uvicorn servidor:_app --host=172.16.202.58 --port=9100 --workers=4 --ssl-keyfile=./localhost.key --ssl-certfile=./localhost.crt
uvicorn servidor:_app --host=172.16.202.9 --port=9100 --workers=4
uvicorn servidor:_app --host=127.0.0.1 --port=9100 --workers=2

uvicorn servidor:_app --host=127.0.0.1 --port=9100 --workers=2 --ssl-keyfile=./localhost+4-key.pem --ssl-certfile=./localhost+4.pem
uvicorn servidor:_app --host=127.0.0.1 --port=9100 --workers=2 --ssl-keyfile=./localhost.key --ssl-certfile=./localhost.crt

# TRABAJADORES
python3.10 active_document/aplicacion/trabajadores/llama_trabajadores.py

screen -localhost
python aplicacion/trabajadores/llama_trabajadores.py

openssl x509 -in raiz.cer -inform DER -outform PEM  >> consolidate.pem

curl https://activedocumentv2.esap.edu.co/

entrar a docker  >>> docker exec -it 816e098e781a bash

docker exec -it 816e098e781a /var/www/onlyoffice/documentserver/npm/node_modules/.bin/json -f /etc/onlyoffice/documentserver/default.json -I -e 'this.services.CoAuthoring.requestDefaults.rejectUnauthorized=false'

 bash -c "/var/www/onlyoffice/documentserver/npm/json -f /etc/onlyoffice/documentserver/default.json -I -e 'this.services.CoAuthoring.requestDefaults.rejectUnauthorized=false' bash /app/onlyoffice/run-document-server.sh"

docker exec 816e098e781a node -v


desde /active_document

python aplicacion/trabajadores/llama_trabajadores.py

or
python D:\gestor_2021_vite\aplicacion\trabajadores\llama_trabajadores.py


# DESCARGA CORREOS
python  D:\gestor_2021_vite\aplicacion\correos/descargar_correos.py
or
python3.10 /active_document/aplicacion/correos/descargar_correos.py


python configurar.py -services=172.21.155.69
python3.10 configurar.py -services=172.16.202.58