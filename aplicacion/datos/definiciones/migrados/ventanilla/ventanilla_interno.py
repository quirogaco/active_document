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

####################
#     CLASE        #
# MIGRADO INTERNO  #
####################

class DB_MIGRADO_INTERNO_VENTANILLA(base_general.DB_BASE_SIMPLE, globales.CLASE_BASE_SQL):
    # Serializar esos campos a diccionario
    __serialization__ = dbase.serializa([
        'id', 
        'radicado_en',
        'radicado_por',
        'nro_radicado',
        'fecha_radicado',
        'nro_origen',
        'anexos',
        'asunto',
        'area_sender_name',
        'sender_name',
        'area_target_name',
        'target_name',
        'atributos_internos'
    ])

    # Campos fijos de la tabla
    __basicos__ = [
        'id', 
        'radicado_en',
        'radicado_por',
        'nro_radicado',
        'fecha_radicado',
        'nro_origen',
        'anexos',
        'asunto',
        'area_sender_name',
        'sender_name',
        'area_target_name',
        'target_name',
        'atributos_internos'
    ]
     
    id                 = dbase.Column( dbase.Unicode(50),  default=basicas.uuidTexto, primary_key=True)

    # Base
    radicado_en        = dbase.Column( dbase.Unicode(120),   nullable=True, default='')
    radicado_por       = dbase.Column( dbase.Unicode(120),   nullable=True, default='')
    nro_radicado       = dbase.Column( dbase.Unicode(60),  index=True, nullable=True )
    fecha_radicado     = dbase.Column( dbase.DateTime,     nullable=True)
    nro_origen         = dbase.Column( dbase.Unicode(60),   nullable=True, default='')
    anexos             = dbase.Column( dbase.Unicode(512),  nullable=True, default='')    
    asunto             = dbase.Column( dbase.Unicode(1024), nullable=True, default='')    
    
    # Remitente
    area_sender_name   = dbase.Column( dbase.Unicode(120),   nullable=True, default='')    
    sender_name        = dbase.Column( dbase.Unicode(120),  nullable=True, default='')    
    
    # Destinatario
    area_target_name   = dbase.Column( dbase.Unicode(120),   nullable=True, default='')    
    target_name        = dbase.Column( dbase.Unicode(120),  nullable=True, default='')        

    # Tramite
    tramite_inicial     = dbase.Column( dbase.Unicode(120),  nullable=True, default='')  
    
    atributos_internos = dbase.Column( dbase.json.JSONType, default={} )    
    
globales.carga_clase("db_migrado_interno_ventanilla", DB_MIGRADO_INTERNO_VENTANILLA)


##################################
#           ESTRUCTURA           #
##################################

campos = {
    "id"               : tipos.id(), 
    "radicado_en"      : tipos.texto_obligatorio(propiedades={"titulo": "Radicado en"}), 
    "radicado_por"     : tipos.texto_obligatorio(propiedades={"titulo": "Radicado por"}), 
    "fecha_radicado"   : tipos.fecha_obligatorio(propiedades={"titulo": "Fecha del radicado"}), 
    "nro_radicado"     : tipos.texto_obligatorio(propiedades={"titulo": "Nónmero de radicado", "longitud": 60}),
    "nro_origen"       : tipos.texto_obligatorio(propiedades={"titulo": "Nónmero de origen", "longitud": 60}),    
    "anexos"           : tipos.texto_obligatorio(propiedades={"titulo": "Anexos", "longitud": 256}),    
    "asunto"           : tipos.texto_obligatorio(propiedades={"titulo": "Asunto", "longitud": 1024}), 

    "area_sender_name" : tipos.texto_obligatorio(propiedades={"titulo": "Dependencia envia", "longitud": 120}), 
    "sender_name"      : tipos.texto_obligatorio(propiedades={"titulo": "Funcionario envia", "longitud": 120}),  
    
    "area_target_name" : tipos.texto_obligatorio(propiedades={"titulo": "Dependencia recibe", "longitud": 120}), 
    "target_name"      : tipos.texto_obligatorio(propiedades={"titulo": "Funcionario recibe", "longitud": 120}),  
    
    "tramite_inicial"    : tipos.texto_obligatorio(propiedades={"titulo": "Tramite"})   
}
#campos.update(base_general_campos.campos)

# Campos elastic
camposIndexamiento = { 
    'atributos_internos.copia_terceros': {
        "tipoElastic": {
            'tipo'       : 'anidados',
            'propiedades': {
                'id'              : tipos.clave(propiedades={"titulo": "Id"}),
                'name'            : tipos.texto(propiedades={"titulo": "Nombre"}), 
                'sender'          : tipos.texto(propiedades={"titulo": "Destinatario"}), 
                'ciudad_full_name': tipos.texto(propiedades={"titulo": "Ciudad"}),
            }
        }
    },

    'atributos_internos.copia_funcionarios': {
        "tipoElastic": {
            'tipo'       : 'anidados',
            'propiedades': {
                'id'        : tipos.clave(propiedades={"titulo": "Id"}),
                'name'      : tipos.texto(propiedades={"titulo": "Nombre"}), 
                'area_name' : tipos.texto(propiedades={"titulo": "Area"}), 
                'sitio_name': tipos.texto(propiedades={"titulo": "Ubicacion"}),
            }
        }
    },

    'atributos_internos.archivos_anexos'   : {
        "tipoElastic": {
            'tipo'       : 'anidados',
            "propiedades": {
                "creado_en" : tipos.texto(propiedades={"titulo": "Creado en"}),
                "versiones" : {
                    "tipoElastic": {
                        'tipo'        : 'anidados',
                        "propiedades" : {
                            'descripcion': tipos.texto(propiedades={"titulo": "Descripciónn"}),
                            'filetype'   : tipos.texto(propiedades={"titulo": "Tipo archivo"}),
                            'ocr'        : tipos.texto(propiedades={"titulo": "Ocr"}),
                            'path'       : tipos.texto(propiedades={"titulo": "Ruta"}),
                            'idFile'     : tipos.texto(propiedades={"titulo": "Id archivo"}),
                            'version'    : tipos.texto(propiedades={"titulo": "Versiónn"}),
                        }   
                    }                 
                }
            }
        }
    },

    # EXPEDIENTES ARCHIVO GESTION
    'atributos_internos.expedientes'      : {
        "tipoElastic": {
            'tipo'       : 'anidados',
            "propiedades": {
                'expediente_id'   : tipos.id(), 
                'expediente_name' : tipos.texto(propiedades={"titulo": "Descripciónn"}),
                'expediente_trd'  : tipos.texto(propiedades={"titulo": "Descripciónn"}),
                'carpeta_id'      : tipos.id(), 
                'carpeta_numero'  : tipos.entero(propiedades={"titulo": "Carpeta Nónmero"}),                             
                'tipo_id'         : tipos.id(), 
                'tipo_name'       : tipos.texto(propiedades={"titulo": "Nombre expediente"}),
            }
        }
    },

    'atributos_internos.instancias'        : {
        "tipoElastic": {
            'tipo'        : 'anidados',
            "propiedades" : {                
                "descripcion" : tipos.texto(propiedades={"titulo": "Descripciónn"}),
                "proceso_id"  : tipos.id(), 
                "proceso_name": tipos.texto(propiedades={"titulo": "Proceso"}),
                "tareas"      : {
                    "tipoElastic": {
                        'tipo'       : 'anidados',
                        "propiedades": {  
                            'id'              : tipos.id(), 
                            # Responsable actual
                            'responsable_id'  : tipos.id(), 
                            'responsable_name': tipos.texto(propiedades={"titulo": "Responsable"}),
                            'dependencia_id'  : tipos.id(), 
                            'dependencia_name': tipos.texto(propiedades={"titulo": "Dependencia"}),
                            # Dependencia que envia
                            'envia_id'        : tipos.id(), 
                            'envia_name'      : tipos.texto(propiedades={"titulo": "Dependencia envia"}),
                            'enviaDep_id'     : tipos.id(), 
                            'enviaDep_name'   : tipos.texto(propiedades={"titulo": "Envia"}),
                            'recibido_en'     : tipos.fecha(propiedades={"titulo": "Recibido"}),
                            'envia_tarea'     : {
                                "tipoElastic": {
                                    'tipo'       : 'anidados',
                                    "propiedades" : {                          
                                        'de_ActividadId'   : tipos.id(), 
                                        'de_ActividadName' : tipos.texto(propiedades={"titulo": "Actividad"}),
                                        'comentario'       : tipos.texto(propiedades={"titulo": "Comentario"}),
                                        'creado'           : tipos.fecha(propiedades={"titulo": "Creado"}),
                                    }
                                }                                                                            
                            },
                            # Informacion de la Actividad
                            'actividad'       : tipos.id(), 
                            'actividad_name'  : tipos.texto(propiedades={"titulo": "Actividad"}),
                            # Estado y alertas
                            'comentario'      : tipos.texto(propiedades={"titulo": "Comentario"}),
                            'vence_en'        : tipos.fecha(propiedades={"titulo": "Recibido"}),
                            'wf_statusWItem'  : tipos.texto(propiedades={"titulo": "Estado"}),                                         
                            'estado'          : tipos.texto(propiedades={"titulo": "Estado"}),
                            'alertado'        : tipos.texto(propiedades={"titulo": "Alertado"}),
                            'notificado'      : tipos.texto(propiedades={"titulo": "Notificado"}),                                                 
                        }
                    }
                }
            }
        }           
    },

    'atributos_internos.responsables_todos': {
        "tipoElastic": {
            'tipo'        : 'anidados',
            "propiedades" : {   
                'responsable_id'  : tipos.id(), 
                'responsable_name': tipos.texto(propiedades={"titulo": "Responsable Nombre"}),
                'dependencia_id'  : tipos.id(), 
                'dependencia_name': tipos.texto(propiedades={"titulo": "Dependencia"}),
            }
        }                                
    },
        
    'atributos_internos.responsables_activos': {
        "tipoElastic": {
            'tipo'        : 'anidados',
            "propiedades" : {                                                                                
                'responsable_id'  : tipos.id(), 
                'responsable_name': tipos.texto(propiedades={"titulo": "Responsable Nombre"}),
                'dependencia_id'  : tipos.id(), 
                'dependencia_name': tipos.texto(propiedades={"titulo": "Dependencia"})                      
            }
        }
    }
}

camposElastic = campos.copy()
camposElastic.update(camposIndexamiento)

definicion = {
    "descripcion" : "Internos Ventanilla",
    "clase"       : "db_migrado_interno_ventanilla",
    "estructura"  : "internos_ventanilla",    
    # Campos de la estructura
    "campos"      : campos,
    "camposIndexamiento": camposIndexamiento,

    # Referencias a otras estructuras
    "referencias" : [],

    "campoIndice" : "id",
    "indexa"      : "si",

    "indexamiento": {}
}

# Publica definicion de estructura
globales.carga_definicion(definicion["estructura"], definicion)

##### VALIDACIónN #######
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
