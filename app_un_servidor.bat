npm run dev -- --port 3000
npm run dev -- --port 3000 --https

uvicorn servidor:_app --host=192.168.1.144 --port=9100 --log-level critical --workers=2 -nodo=001 -celery=SI

uvicorn servidor:_app --host=192.168.1.144 --port=9100 --workers=2
uvicorn servidor:_app --host=192.168.1.99 --port=9100 --workers=2
uvicorn servidor:_app --host=172.16.202.58 --port=9100 --workers=4
uvicorn servidor:_app --host=172.16.202.9 --port=9100 --workers=4
uvicorn servidor:_app --host=127.0.0.1 --port=9100 --workers=2

uvicorn servidor:_app --host=127.0.0.1 --port=9100 --workers=2 --ssl-keyfile=./localhost+4-key.pem --ssl-certfile=./localhost+4.pem
uvicorn servidor:_app --host=127.0.0.1 --port=9100 --workers=2 --ssl-keyfile=./localhost.key --ssl-certfile=./localhost.crt

localhost+4-key.pem
localhost+4.pem

# TRABAJADORES
python3.10 active_document/aplicacion/trabajadores/llama_trabajadores.py

python3.10 aplicacion/trabajadores/llama_trabajadores.py
python aplicacion/trabajadores/llama_trabajadores.py


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


viveros.60@gmail.com
karenv.rativa@esap.edu.co