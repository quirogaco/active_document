#!/usr/bin/python
# -*- coding: utf-8 -*-

import builtins
import pprint

from librerias.utilidades import basicas  

# Definiciones sql
from librerias.datos.sql                 import sqalchemy_declarativa_base as dbase

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base import base_general
from librerias.datos.sql                 import sqalchemy_tipo_campos as tipos

from librerias.datos.base                import globales
from librerias.datos.validacion          import valida 
from librerias.datos.elastic             import elastic_utilidades
from librerias.datos.elastic             import elastic_operaciones
from librerias.datos.sql                 import sqalchemy_operaciones

################################
#              CLASE           #
# MIGRADO PQRS, Clase RADICADO #
################################

class DB_MIGRADO_RADICADO_PQRS(base_general.DB_BASE_SIMPLE, globales.CLASE_BASE_SQL):
    # Serializar esos campos a diccionario
    __serialization__ = dbase.serializa([
        'id', 
        'tipo_radicado',
        'fecha_radicado', 
        'nro_radicado',
        'fecha_documento', 
        'folios',
        'asunto', 
        'id_tabla_asunto',
        'asunto_form_web', 
    ])

    # Campos fijos de la tabla
    __basicos__ = [
        'id', 
        'tipo_radicado',
        'fecha_radicado', 
        'nro_radicado',
        'fecha_documento', 
        'folios',
        'asunto', 
        'id_tabla_asunto',
        'asunto_form_web',
    ]
     
    id                  = dbase.Column( dbase.Unicode(50),  default=basicas.uuidTexto, primary_key=True) 
    tipo_radicado       = dbase.Column( dbase.Unicode(60),  index=True, nullable=True )
    fecha_radicado      = dbase.Column( dbase.DateTime,     nullable=True)
    nro_radicado        = dbase.Column( dbase.Unicode(50),  index=True, nullable=True )
    fecha_documento     = dbase.Column( dbase.DateTime,     nullable=True)
    folios              = dbase.Column( dbase.Integer,      index=True, nullable=True )
    asunto              = dbase.Column( dbase.Text(),       nullable=True )
    id_tabla_asunto     = dbase.Column( dbase.Unicode(50),  index=True, nullable=True ) 
    asunto_form_web     = dbase.Column( dbase.Unicode(60),  index=True, nullable=True )

globales.carga_clase("db_migrado_radicado_pqrs", DB_MIGRADO_RADICADO_PQRS)


##################################
#           ESTRUCTURA           #
##################################

campos = {
    "id": tipos.id(), 
    "tipo_radicado"  : tipos.texto_obligatorio(propiedades={"titulo": "Tipo de radicado", "longitud": 60}), 
    "fecha_radicado" : tipos.fecha_obligatorio(propiedades={"titulo": "Fecha del radicado"}), 
    "nro_radicado"   : tipos.texto_obligatorio(propiedades={"titulo": "Número de radicado", "longitud": 60}),         
    "fecha_documento": tipos.fecha_obligatorio(propiedades={"titulo": "Fecha del documento"}),         
    "folios"         : tipos.entero(propiedades={"titulo": "Número de folios"}),     
    "asunto"         : tipos.texto_base(propiedades={"titulo": "Asunto"}), 
    "id_tabla_asunto": tipos.clave(propiedades={"titulo": "Id Tabla asunto"}), 
    "asunto_form_web": tipos.clave(propiedades={"titulo": "Forma web"})
}
#campos.update(base_general_campos.campos)

# Campos elastic
camposIndexamiento = {   
    "nombre"           : tipos.texto(propiedades={"titulo": "Nombre"}), 
    "nroidentificacion": tipos.texto(propiedades={"titulo": "Identificación"}), 
    "direccion"        : tipos.texto(propiedades={"titulo": "Dirección"}), 
    "correoelectronico": tipos.texto(propiedades={"titulo": "Correo electronico"}), 
    "telefonofijo"     : tipos.texto(propiedades={"titulo": "Telefono fijo"}), 
    "telefonomovil"    : tipos.texto(propiedades={"titulo": "Telefono movil"}), 
    'logs': {
        "tipoElastic": {
            'tipo'       : 'anidados',
            'propiedades': {
                'id'             : tipos.clave(propiedades={"titulo": "Id"}),
                'accionante'     : tipos.texto(propiedades={"titulo": "Accionante"}), 
                'destinatario'   : tipos.texto(propiedades={"titulo": "Destinatario"}), 
                'estado'         : tipos.texto(propiedades={"titulo": "Estado"}),
                'fecha'          : tipos.texto(propiedades={"titulo": "Fecha"}),
                'descripcion'    : tipos.texto_base(propiedades={"titulo": "Descripci�n"}), 
                'tipo_accionante': tipos.texto(propiedades={"titulo": "Tipo accionante"}),
            }
        }
    },

    'anexos': {
        "tipoElastic": {
            'tipo'       : 'anidados',
            'propiedades': {
                'id'             : tipos.clave(propiedades={"titulo": "Id"}),
                'archivo_nombre' : tipos.clave(propiedades={"titulo": "Archivo"}),
                'tipo_archivo'   : tipos.clave(propiedades={"titulo": "Tipo archivo"}),
                'tipo_documento' : tipos.texto(propiedades={"titulo": "Tipo documento"}), 
                'accionante'     : tipos.texto(propiedades={"titulo": "Usuario"}),
                'fecha'          : tipos.texto(propiedades={"titulo": "Fecha"})
            }
        }
    }  
}

camposElastic = campos.copy()
camposElastic.update(camposIndexamiento)

definicion = {
    "descripcion" : "Radicados PQRS",
    "clase"       : "db_migrado_radicado_pqrs",
    "estructura"  : "radicado_pqr",    
    # Campos de la estructura
    "campos"      : campos,
    "camposIndexamiento": camposIndexamiento,

    # Referencias a otras estructuras
    "referencias" : [
        {
            "campoReferencia"    : "logs",
            "funcion"            : "busca_tramitelog",
        },

        {
            "campoReferencia"    : "anexos",
            "funcion"            : "busca_archivos_todos",
        },

        {
            "campoReferencia"    : "remitente",
            "funcion"            : "busca_remitente",
        },

        
    ],

    "campoIndice" : "id",
    "indexa"      : "si",

    "indexamiento": {}
}

# Publica definicion de estructura
globales.carga_definicion(definicion["estructura"], definicion)

##### VALIDACIÓN #######
# Genera modelo de validación
validador = valida.definirModelo(definicion["estructura"], definicion["campos"])
# Publica modelo de validacion
globales.carga_validador(definicion["estructura"], validador)

##### ELASTIC #######
# Genera modelo de elastic
elastic_modelo, runtime, querytime = elastic_utilidades.generaModelo(camposElastic, definicion["indexamiento"], definicion["estructura"])

# Registra modelo de elastic
elastic_utilidades.registraModelo(
    definicion["estructura"], 
    elastic_modelo, 
    definicion["indexamiento"], 
    definicion.get("campoIndice", "id") 
)
elastic_operaciones.creaIndice(definicion["estructura"], "base")

# Funciones referemcia
def valida_none(valor):
    if valor == None:
        return ""
    else:
        return str(valor).strip()

def trae_remitente_datos(remitente_id):
    datos             = {}
    remite_nombre     = ""
    nroidentificacion = ""
    direccion         = ""
    correoelectronico = ""
    telefonofijo      = ""
    telefonomovil     = ""
    filtro            = [ "id", "=", remitente_id ]
    remitente = sqalchemy_operaciones.filtrarOrdena("base", "tercero_pqr", [ filtro ], [], True)
    if len(remitente) > 0:
        remitente = remitente[0]
        if remitente["nombres"] not in ["", None]:
            remite_nombre = remitente["nombres"]
        else:
            remite_nombre = (valida_none(remitente["primer_nombre"]) + " " + valida_none(remitente["segundo_nombre"]) + " "  + 
                             valida_none(remitente["primer_apellido"]) + " "  + valida_none(remitente["segundo_apellido"]))
        
        remite_nombre.replace("   ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ")
        nroidentificacion = valida_none(remitente["nroidentificacion"])
        direccion         = valida_none(remitente["direccion"])
        correoelectronico = valida_none(remitente["correoelectronico"])
        telefonofijo      = valida_none(remitente["telefonofijo"])
        telefonomovil     = valida_none(remitente["telefonomovil"])

    datos = {
        'nombre'           : remite_nombre,
        'nroidentificacion': nroidentificacion,
        'direccion'        : direccion,
        'correoelectronico': correoelectronico,
        'telefonofijo'     : telefonofijo,
        'telefonomovil'    : telefonomovil,
        ## Pais, ciudad, depeartamento
    }

    return datos

def busca_remitente(registro):
    datos          = {}
    radicado_id    = registro["id"]
    filtroRadicado = [ "requ_id", "=", radicado_id ]
    filtroEstado   = [ "traz_estado", "=", "RADICADO" ]

    traza = sqalchemy_operaciones.filtrarOrdena("base", "traza_pqr", [ filtroRadicado, filtroEstado ], [], True)
    if len(traza) > 0:
        traza = traza[0]
        datos = trae_remitente_datos(traza["usua_idejecutor"])    
    else:
        datos = {
            'nombre'           : "",
            'nroidentificacion': "",
            'direccion'        : "",
            'correoelectronico': "",
            'telefonofijo'     : "",
            'telefonomovil'    : "",
            ## Pais, ciudad, depeartamento
        }

    registro['nombre']            = datos['nombre']
    registro['nroidentificacion'] = datos['nroidentificacion']
    registro['direccion']         = datos['direccion']
    registro['correoelectronico'] = datos['correoelectronico']
    registro['telefonofijo']      = datos['telefonofijo']
    registro['telefonomovil']     = datos['telefonomovil']

    return datos

globales.carga_funcion_referencia(definicion["estructura"], "busca_remitente", busca_remitente)

###############################################
# FUNCIONES LOCALES DE OPERACI�N E INDEXACI�N #
###############################################

def busca_remitente_nombre(remitente_id):
    datos = trae_remitente_datos(remitente_id)

    return datos.get('nombre', '')

def busca_funcionario(funcionario_id):
    nombre      = ""
    filtro      = [ "id", "=", funcionario_id ]
    funcionario = sqalchemy_operaciones.filtrarOrdena("base", "funcionario_pqr", [ filtro ], [], True)
    if len(funcionario) > 0:
        funcionario = funcionario[0]
        nombre      = valida_none(funcionario["func_primernombre"]) + " " + valida_none(funcionario["func_primerapellido"])

    return nombre

def data_log(log):
    accionante      = ""
    destinatario    = ""
    tipo_accionante = "FUNCIONARIO"
    if   log["traz_estado"] == "EN TRAMITE":
            # FUNCIONARIO EL MISMO
            accionante   = busca_funcionario(log["usua_idejecutor"])
            destinatario = accionante

    elif log["traz_estado"] == "NO TRAMITADO":
            # FUNCIONARIO EL MISMO
            accionante   = busca_funcionario(log["usua_idejecutor"])
            destinatario = accionante

    elif log["traz_estado"] == "RADICADO":
            # TERCERO EL MISMO
            accionante      = busca_remitente_nombre(log["usua_idejecutor"])
            destinatario    = accionante
            tipo_accionante = "TERCERO"

    elif log["traz_estado"] == "RECHAZADO":
            # FUNCIONARIO EL MISMO
            accionante   = busca_funcionario(log["usua_idejecutor"])
            destinatario = accionante

    elif log["traz_estado"] == "RESUELTO":
            # FUNCIONARIO EL MISMO
            accionante   = busca_funcionario(log["usua_idejecutor"])
            destinatario = accionante

    elif log["traz_estado"] == "TRAMITADO":
            # FUNCIONARIO EL MISMO
            accionante   = busca_funcionario(log["usua_idejecutor"])
            destinatario = accionante

    elif log["traz_estado"] == "TRASLADO":
            # FUNCIONARIO DISTINTO
            accionante   = busca_funcionario(log["usua_idejecutor"])
            destinatario = busca_funcionario(log["usua_idasignado"])

    data = {
        'id'             : log["id"],
        'accionante'     : accionante,
        'destinatario'   : destinatario,
        'estado'         : log["traz_estado"],
        'fecha'          : log["traz_fecha"],
        'descripcion'    : log["traz_descripcion"],
        'tipo_accionante': tipo_accionante
    }

    return data     

def busca_tramitelog(registro):
    datos       = []
    #print(registro["id"])
    radicado_id = registro["id"]
    filtro      = [ "requ_id", "=", radicado_id ]
    ordenar     = [ "descendente", "traz_fecha" ]
    logs = sqalchemy_operaciones.filtrarOrdena("base", "traza_pqr", [ filtro ], [ordenar], True)
    # logs        = session.query( TRAZA_CLASE ).filter_by( requ_id = radicado_id).order_by( desc( TRAZA_CLASE.traz_fecha) ).all()
    for log in logs:
        data = data_log(log)
        datos.append(data)
   
    return datos
globales.carga_funcion_referencia(definicion["estructura"], "busca_tramitelog", busca_tramitelog)

import os.path
def busca_anexos(registro):
    datos          = [] 
    radicado_id    = registro["id"]
    fecha_radicado = registro["fecha_radicado"]
    filtro         = [ "requ_id", "=", radicado_id ]
    ordenar        = [ "descendente", "adju_fechacambio" ]
    logs           = sqalchemy_operaciones.filtrarOrdena("base", "traza_anexo_pqr", [ filtro ], [ordenar], True)
    for log in logs:
        #print("log:", log)
        filtro = [ "id", "=", log["id"] ]
        anexos = sqalchemy_operaciones.filtrarOrdena("base", "anexo_pqr", [ filtro ], [], True) 
        for anexo in anexos:
            accionante = busca_funcionario(log["adju_registradopor"])
            if accionante == "":
                accionante = log["adju_registradopor"]
            
            nombre_archivo = anexo["adju_nombre"]
            extension      = os.path.splitext(nombre_archivo)[1].lower().replace(".", "")
            data = {
                'id'            : anexo["id"],
                'tipo_archivo'  : extension,
                'archivo_nombre': nombre_archivo,
                'tipo_documento': "ANEXO",
                'accionante'    : accionante, 
                'fecha'         : log["adju_fechacambio"],
                'idRadicado'    : radicado_id,
                'fechaRadicado' : fecha_radicado
            }              
            datos.append(data)

    return datos

def busca_anexos_traza(registro):
    datos          = [] 
    radicado_id    = registro["id"]
    fecha_radicado = registro["fecha_radicado"]
    trazas         = registro["logs"]
    for traza in trazas:
        filtro = [ "traz_id", "=", traza["id"] ]
        logs   = sqalchemy_operaciones.filtrarOrdena("base", "traza_anexo_pqr", [ filtro ], [], True) 
        for log in logs:
            filtro = [ "id", "=", log["id"] ]
            anexo  = sqalchemy_operaciones.filtrarOrdena("base", "anexo_pqr", [ filtro ], [], True) 
            if len(anexo) > 0:
                anexo      = anexo[0]
                accionante = busca_funcionario(log["adju_registradopor"])
                if accionante == "":
                    accionante = log["adju_registradopor"]

                nombre_archivo = anexo["adju_nombre"]
                extension      = os.path.splitext(nombre_archivo)[1].lower().replace(".", "")
                data = {
                    'id'            : anexo["id"],
                    'tipo_archivo'  : extension,
                    'archivo_nombre': nombre_archivo,
                    'tipo_documento': "RESPUESTA",
                    'accionante'    : accionante, 
                    'fecha'         : log["adju_fechacambio"],
                    'idRadicado'    : radicado_id,
                    'fechaRadicado' : fecha_radicado
                }              
                datos.append(data)

    return datos
    
def busca_archivos_todos(registro):
    datos  = []
    
    # anexos
    anexos = busca_anexos(registro)
    datos  = datos + anexos

    # anexos por traza
    anexos_traza = busca_anexos_traza(registro)
    datos        = datos + anexos_traza

    # ordena por fecha
    datos        = sorted(datos, key = lambda i: i['fecha'], reverse = True) 
    
    return datos
globales.carga_funcion_referencia(definicion["estructura"], "busca_archivos_todos", busca_archivos_todos)

def _indexar_primero_(self):
    session  = object_session(self)
    #print("")
    #print("RADICADO:", self.id)

    # Remitente
    remitente_data                = busca_remitente(self.id, session)
    #pprint.pprint(remitente_data)
    self.remite_nombre            = remitente_data['nombre']
    self.remite_nroidentificacion = remitente_data['nroidentificacion']
    self.direccion                = remitente_data['direccion']
    self.correoelectronico        = remitente_data['correoelectronico']
    self.telefonofijo             = remitente_data['telefonofijo']
    self.telefonomovil            = remitente_data['telefonomovil']
    self.pais                     = ''
    self.departamento             = ''
    self.ciudad                   = ''

    # Trazabilidad
    self.logs = busca_tramitelog(self.id, session)
    #pprint.pprint(logs)

    # Anexos
    self.anexos = busca_archivos_todos(self.id, self.fecha_radicado, self.logs, session)
  
    return ""