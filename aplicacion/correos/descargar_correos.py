#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import sys, pprint, builtins

#########################
# Variables de ambiente #
#########################
from dotenv import dotenv_values


try:
    _ambiente_ = dotenv_values(".env") 
except:
    pass

if len(_ambiente_.keys()) == 0:    
    _ambiente_ = dotenv_values("../../.env") 
    
print( "ambiente  TRABAJDADOR >>>>>>>>>>>>>>")
pprint.pprint(_ambiente_)
builtins._appServicios = _ambiente_['CFG_SERVICIOS_URL']
builtins._appAnfitrion = _ambiente_['CFG_DATA_HOST']
builtins._appPuerto    = _ambiente_['CFG_DATA_PORT']

sys.path.append('D:/gestor_2021_vite')
import rutaGlobal
rutaGlobal.publicaRutas(builtins._appServicios)

import carga_inicial


# APLICACION
from email.parser import BytesParser, Parser

import email, getpass, imaplib, os, re, pprint
from datetime import datetime
from email.header import Header, decode_header, make_header

from librerias.datos.sql     import sqalchemy_insertar
from librerias.datos.elastic import elastic_operaciones
from aplicacion.comunes      import manejo_archivos


#####################
# Manejo de correos #  
#####################
from subprocess import *
def jarWrapper(*args):
  #process = Popen(['java', '-jar']+list(args), stdout=PIPE, stderr=PIPE)
  process = Popen(['java', '-jar']+list(args) )
  ret     = []
  return ret

def conectarCorreo( data ):
  """
  'oficial_usuario' : '',
  'oficial_clave'   : '',
  'oficial_url'     : '',
  'oficial_puerto'  : 0,
  """
  mailserver = imaplib.IMAP4_SSL( data["oficial_url"] )
  mailserver.login( data["oficial_usuario"], data["oficial_clave"] )
  mailserver.select('Inbox')
    
  return mailserver

def buscarCorreos( mailserver, cuales='(UNSEEN)' ):
  status, response = mailserver.status('INBOX', "(UNSEEN)")
  print( 'buscarCorreos:') #, status, response )  
  typ, data = mailserver.search( None, cuales)
    
  return data

def descargaCorreo( mailserver, ruta, numCorreo ):
  print( '------------- descargaCorreo:', numCorreo, int(numCorreo) )# int(numCorreo), str(numCorreo).decode() )
  # Lee un archivo
  nombreEml = None
  try:
    typ, data = mailserver.fetch( str( int(numCorreo) ), '(RFC822)' )
    parse = email.parser.BytesFeedParser()
    parse.feed( data[0][1] )
    correo = parse.close()
    texto = correo.as_string().strip()
    nombreEml = str( '%s/%s.eml' %( ruta, str( int(numCorreo) ) ) )
    f = open( nombreEml, 'w' )
    f.write( texto  )
    f.close()
  except Exception as e:
    print( 'error descargaCorreo:', numCorreo, str(e) )
    pass
  
  return nombreEml

def extraeAnexos( nombreEml, ruta, numCorreo, cual ):
  anexos = []
  correo = None
  if nombreEml != None:
    correo = email.message_from_file( open( nombreEml ) )
    print( 'extraeAnexos-nombreEml:', nombreEml )
    imagenes = ["jpg", "jpeg", "png", "gif"]  
    for anexo in correo.get_payload():
      if ( type( anexo) != str ):
        filename = anexo.get_filename()          
        if filename != None:
          if ( anexo.get_content_disposition() != "inline" ):                
            maintype      = anexo.get_content_maintype()
            subtype       = anexo.get_content_subtype()
            es_imagen     = ( subtype in imagenes )
            content_id    = str( anexo.get("Content-Id") )
            imagen_inline = False
            if es_imagen:
              # Trata de validar que no sean imagenes inline no detectadas
              for imagen in imagenes:
                imagen_inline = ( content_id.find( "."+imagen+"@" ) > -1 )
                if imagen_inline: break
              
            if not imagen_inline:
              try:
                # error nombre de anexo, si tiene varias cuentas numcorreo se puede duplicar, es consecutivo por cuenta.
                filename = ruta + os.sep + cual + "-" + str( int(numCorreo) ) + '_' +  filename
                #print( 'filename:', filename )
                open( filename, 'wb').write( anexo.get_payload(decode=True) )
                anexos.append( filename )
              except Exception as e:
                print("FAX extraeAnexos:", str(e))
            
  return anexos, correo

import json as jsonlib
def cargarCorreos():
  #correosConfig = ac_pathglobal + '/configuracion/correosConfig.json'
  datosCorreos  = {      
    'oficial_usuario' : 'quirogaco@gmail.com',
    'oficial_clave'   : 'sreojrjewsjkxnml',
    'oficial_url'     : 'imap.gmail.com',
    'oficial_puerto'  : 0,
        
    'fax_usuario'     : '',
    'fax_clave'       : '',
    'fax_url'         : '',
    'fax_puerto'      : 0,
          
    'notifica_usuario': '',
    'notifica_clave'  : '',
    'notifica_url'    : '',
    'notifica_puerto' : 0      
  }

  """ 
  print( correosConfig )

  try:
    with open( correosConfig ) as json_file:  
      data = jsonlib.load( json_file )         
  except Exception as e:
    print( 'Parametros:', str(e) )
    data = datosCorreos
    
  return data
  """ 

  return datosCorreos

def descargarCorreos( ruta, cuantos = 1, cual="email" ):
  ruta_basica = 'D:/gestor_2021_vite/'
  config     = cargarCorreos()
  mailserver = conectarCorreo( config )   
  count      = 0
  data       = buscarCorreos( mailserver, '(UNSEEN)' )[0].split()
  data.reverse()
  # Invertir el correo para que tome los mas recientes !!!!
  #data      = buscarCorreos( mailserver, '(SEEN)' )
  
  # Para cada correo
  for numCorreo in data:
    count += 1
    nombreEml       = descargaCorreo( mailserver, ruta, numCorreo )   
    anexos, message = extraeAnexos( nombreEml, ruta, numCorreo, cual )
    if message != None:
      From = message['From']
      print( count, numCorreo, From )
      if From != None:
        fromCorreo = re.findall( r'[\w\.-]+@[\w\.-]+', From )            
        if fromCorreo != None:
          From      = fromCorreo[0]
          Date      = message['Date'][5:25].strip()
          dt        = datetime.strptime( Date, '%d %b  %Y  %H:%M:%S')
          asunto    = str(make_header( decode_header(message['Subject']) ))
          
          # Listado de archivos
          archivos  = []
          for  nombre in anexos:
            data = {
              "nombre_completo": nombre,
              "nombre"         : os.path.basename( nombre )
            }
            archivos.append(data)

          # Arma correo                      
          dataTemporal = {}
          dataTemporal['correo_origen'] = From
          dataTemporal['asunto']        = asunto[0:1000]
          dataTemporal['fecha_correo']  = dt
          dataTemporal['estado']        = u'PENDIENTE'
          dataTemporal['radicado']      = u''
          print("")
          print("datos correo:", count)
          pprint.pprint(dataTemporal)
          resultado = sqalchemy_insertar.insertar_registro_estructura("correos_descargados", dataTemporal)
          elastic_operaciones.indexar_registro("correos_descargados", resultado["id"])
          print("")
          print("ANEXOS:")
          pprint.pprint(anexos)
          print("")
          print("")          
          manejo_archivos.manejo("correos", "insertar", {"id":resultado["id"]}, archivos, "", cubeta = "correos")
          
          print("")
          print("")
          
          """
          temporal = CORREO_ELECTRONICO_TEMPORAL( **dataTemporal )
          session.add( temporal )
          session.commit()                      
          fulltext.indexOneRecord( 'CORREO_ELECTRONICO_TEMPORAL', temporal, connPyes, flush=True)
          """
    if count > cuantos:
        break
                  
  mailserver.close()
  mailserver.logout()
  print("sale...................descarga")

descargarCorreos( "D:/gestor_2021_vite/aplicacion/correos", 1, cual="email" )