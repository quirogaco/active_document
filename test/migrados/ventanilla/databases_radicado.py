#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import __builtin__
import pprint
from datetime import datetime

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base, synonym_for
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import Column, Integer, String, Unicode, ForeignKey,  DateTime, Date, Index, asc, desc, event
from sqlalchemy.orm import sessionmaker, relationship, backref

#from sqlalchemy_utils import UUIDType
import uuid

from utils import utils
from library.utils import utils
from utils.utils import JsonPathStr

from library.data  import fulltext, pyes_base, sql_globals

#/* Clase de ENTRADAS */
sessionEntrada = SQLSession()
class ENTRADA(Base):
    __tablename__  = 'd_entrada'
    __id__         = 'id'
    
    # Datos Basicos Radicado
    radicador_id    = Column('radicador_id',    Unicode(55), index=True, nullable=False, default=u'')
    radicado_en_id  = Column('radicado_en_id',  Unicode(55), index=True, nullable=False, default=u'')
    nro_radicado    = Column('nro_radicado',    Unicode(50), unique=True, nullable=False)
    fecha_radicado  = Column('fecha_radicado',  DateTime, index=True, nullable=False, default=utils.getOnlyDateTime)
    fecha_documento = Column('fecha_documento', DateTime, index=True, nullable=False, default=utils.getOnlyDateTime)
    nro_origen      = Column('nro_origen',      Unicode(30), index=True, nullable=True)
    nro_guia        = Column('nro_guia',        Unicode(30), index=True, nullable=True)
    folios          = Column('folios',          Integer, nullable=False, default=1)
    anexos          = Column('anexos',          Unicode(512),  nullable=True)
    asunto          = Column('asunto',          Unicode(1024), nullable=False)
    referenciados   = Column('referenciados',   Unicode(512), nullable=True)
    concopia        = Column('concopia',        Unicode(256), nullable=True)
    concopiaotros   = Column('concopiaotros',   Unicode(256), nullable=True)
    medio_id        = Column('medio_id',        Unicode(50),  ForeignKey('d_medio.id'), nullable=False, default=u'')
    medio_rel       = relationship("MEDIO", foreign_keys=medio_id, lazy="joined" )
    medio_name      = association_proxy('medio_rel', 'name')
    contestado_con  = Column('contestado_con',  Unicode(50), nullable=True)
    fecha_recorrido = Column('fecha_recorrido', DateTime, index=True, nullable=False, default=utils.getOnlyDateTime)
    recorrido       = Column('recorrido',       Integer, index=True, nullable=False, default=0)
    impreso         = Column('impreso',         Integer, index=True, nullable=False, default=0)
    copiamasivo     = Column('copiamasivo',     Unicode(20),  nullable=True)
    
    #informacion del tercero
    nit       = Column('nit',       Unicode(50),  index=True, nullable=True)
    name      = Column('name',      Unicode(120), index=True, nullable=False)
    address   = Column('address',   Unicode(120), nullable=True)
    phone     = Column('phone',     Unicode(50),  nullable=True)
    email     = Column('email',     Unicode(120),  nullable=True)
    cargo     = Column('cargo',     Unicode(150),  nullable=True)
    sender    = Column('sender',    Unicode(120), index=True, nullable=True)
    
    # Vinculos Pais    
    pais_id            = Column('pais_id', Unicode(50), ForeignKey('d_pais.id'), nullable=False, default=u'')
    pais_rel           = relationship("PAIS", foreign_keys=pais_id, lazy="joined" )
    pais_name          = association_proxy('pais_rel', 'name')
        
    departamento_id   = Column('departamento_id', Unicode(50), ForeignKey('d_departamento.id'), nullable=False, default=u'')
    departamento_rel  = relationship("DEPARTAMENTO", foreign_keys=departamento_id, lazy="joined" )
    departamento_name = association_proxy('departamento_rel', 'name')
    
    ciudad_id         = Column('ciudad_id', Unicode(50), ForeignKey('d_ciudad.id'), nullable=False, default=u'')
    ciudad_rel        = relationship("CIUDAD", foreign_keys=ciudad_id, lazy="joined")
    ciudad_name       = association_proxy('ciudad_rel', 'full_name')
    
    # valores de control  
    id                 = Column('id', Unicode(50), default=utils.UuidStr, primary_key=True, index=True )
    status             = Column('status',      Unicode(25),  default=u'ACTIVO', index=True, nullable=False)
    _created_at        = Column('_created_at', DateTime, index=True, nullable=False, default=utils.getOnlyDateTime)
    _updated_at        = Column('_updated_at', DateTime, index=True, nullable=False, default=utils.getOnlyDateTime, onupdate=utils.getOnlyDateTime)
    _unit_code         = Column('_unit_code', Unicode(20), index=True, nullable=False, default=u'*')
    _organization_code = Column('_organization_code', Unicode(20), index=True, nullable=False, default=organization_default)
    
    datainstancias     = None
    ##########################
    # BASE
    @property
    def tiporecord(self):
        return 'ENTRADA'
    
    # SITIO DE RADICACION
    @property
    def radicado_en(self):
        if (self.radicador_id in [None, '']):
            return ''
        else:
            q = sessionEntrada.query(SITIO).filter(SITIO.id == self.radicado_en_id)
            try:
                sitio = q.one()
                name  = sitio.name
            except:
                name  = ''
        
        return name
    
    # NOMBRE RADICADOR
    @property
    def radicado_por(self):
        if (self.radicador_id in [None, '']):
            return ''
        else:
            q = sessionEntrada.query(USUARIO).filter(USUARIO.id == self.radicador_id)
            try:
                usuario = q.one()
                name    = usuario.name
            except:
                name  = ''
        
        return name
    
    # SI TIENE IMAGEN ESCANEDA O NO
    @property
    def escaneada(self):
        # Si tiene imagen escaneada formato PDF
        # ver database relations
        total = len(self.r_scan)
        
        return 'N' if total == 0 else 'S'
    
    # Unifica nombre entidad de campo para consultas ENTRADA, SALIDA, INTERNO
    @property
    def enviadopor(self):
        return self.name
    
    # Unifica nombre persona de campo para consultas ENTRADA, SALIDA, INTERNO
    @property
    def sender_universal(self):
        return self.sender
    
    #####################
    # COPIAS
    @property
    def copia_terceros(self):
        #ini = datetime.now()
        copiasTer    = sessionEntrada.query(COPIATERCEROS).filter_by(documento_id=self.id).all()        
        tercerosList = []
        try:
            for copia in copiasTer:
                tercero = sessionEntrada.query(TERCERO).filter_by(id=copia.concopia_a_id).one()
                tercerosList.append({'id'    : tercero.id,
                                     'name'  : tercero.name,
                                     'sender': tercero.sender,
                                     'ciudad_full_name': tercero.ciudad_full_name
                                     })
        except:
            pass
        #print 'copia_terceros:', datetime.now() - ini, len(tercerosList)             
        return tercerosList
    
    @property
    def copia_funcionarios(self):
        #ini = datetime.now()
        copiasUsu    = sessionEntrada.query(COPIAUSUARIOS).filter_by(documento_id=self.id).all()        
        usuariosList = []
        try:
            for copia in copiasUsu:
                usuario = sessionEntrada.query(USUARIO).filter_by(id=copia.concopia_a_id).one()            
                usuariosList.append({'id'        : usuario.id,
                                     'name'      : usuario.name,
                                     'area_name' : usuario.area_name,
                                     'sitio_name': usuario.sitio_name
                                     })
        except:
            pass
        #print 'copia_funcionarios:', datetime.now() - ini, len(usuariosList)       
        return usuariosList
    
    @property
    def copia_grupos(self):
        #ini = datetime.now()
        copiasGru  = sessionEntrada.query(COPIAGRUPOS).filter_by(documento_id=self.id).all()        
        gruposList = []
        try:
            for copia in copiasGru:
                grupo = sessionEntrada.query(GRUPO).filter_by(id=copia.concopia_a_id).one()                           
                gruposList.append({'id'   : grupo.id,
                                   'name' : grupo.name
                                  })
        except:
            pass
        #print 'copia_grupos:', datetime.now() - ini, len(gruposList)   
        return gruposList                   
    
    #####################
    # ANEXOS
    @property
    def archivos_anexos(self):
        ini = datetime.now()
        anexos     = sessionEntrada.query(OS_OBJETO).filter_by(code=self.nro_radicado, status= u'ACTIVO').order_by(asc(OS_OBJETO._created_at)).all()
        #print 'archivos_anexos-0:', datetime.now() - ini, len(anexos)
        anexosList = []        
        for anexo in anexos:
            anexosList.append({'creado_en'  : anexo._created_at,
                               'versiones'  : anexo.versiones
                              })
        print 'archivos_anexos-1:', datetime.now() - ini, len(anexosList), self.nro_radicado
        return anexosList
    
    #####################
    # EXPEDIENTES ARCHIVO GESTION
    @property
    def expedientes(self):
        #ini = datetime.now()
        DE             = DOCUMENTOEXPEDIENTE
        documentos     = sessionEntrada.query(DE).filter(DE.documento_id==self.id).order_by(asc(DE._created_at)).all()
        documentoslist = []
        for documento in documentos:
            documentoslist.append(documento.expediente)
        #print 'expedientes:', datetime.now() - ini, len(documentoslist)        
        return documentoslist
    
    ##########################################
    # TAREAS - PROCESOS    
    # ESTADO GENERAL DEL RADICADO
    @property
    def estado_label(self):
        """
        # Retorna el numero de tareas activas asociadas al radicado
        # ver database relations
        total = self.pro_status
        
        return u'FINALIZADO' if total == 0 else u'ACTIVO'
        """
        return u'ACTIVO'
    
    # INSTANCIAS ASOCIADAS AL RADICADO  
    datainstancias = None
    @property
    def instancias(self):
        if self.datainstancias == None:
            #ini = datetime.now()
            self.datainstancias = []
            q = sessionEntrada.query(INSTANCIA).filter_by(wf_nro_radicado=self.nro_radicado).order_by(asc(INSTANCIA._created_at))            
            instancias = q.all()
            for instancia in instancias:
                self.datainstancias.append(instancia.instancia)               
                
            #print 'instancias:', datetime.now() - ini, len( self.datainstancias )    
        return self.datainstancias
    
    # persona responsable, primera tarea de la primera intancia
    @property
    def responsable_inicial(self):
        filtro = JsonPathStr("$.[0]['tareas'][0]['responsable_name']")
        #print 'responsable_inicial:', filtro, utils.getPathValue(filtro, self.instancias)
        return utils.getPathValue(filtro, self.instancias)
    
    # Para grid de consulta
    @property
    def destinatario(self):        
        return self.responsable_inicial
    
    # id persona responsable, primera tarea de la primera intancia
    @property
    def responsable_id_inicial(self):
        filtro = JsonPathStr("$.[0]['tareas'][0]['responsable_id']")
        #print "responsable_id_inicial:", len(self.datainstancias)
        return utils.getPathValue(filtro, self.instancias)
    
    # Dependencia responsable, primera tarea de la primera intancia
    @property
    def dependencia_inicial(self):
        filtro = JsonPathStr("$.[0]['tareas'][0]['dependencia_name']")
        #print "dependencia_inicial:", len(self.datainstancias)
        return utils.getPathValue(filtro, self.instancias)
    
    # Id Dependencia responsable, primera tarea de la primera intancia
    @property
    def dependencia_id_inicial(self):
        filtro = JsonPathStr("$.[0]['tareas'][0]['dependencia_id']")        
       
        return utils.getPathValue(filtro, self.instancias)
            
    # Primera actividad, primera tarea de la primera intancia
    @property
    def actividad_inicial(self):
        filtro = JsonPathStr("$.[0]['tareas'][0]['actividad_name']")
        
        return utils.getPathValue(filtro, self.instancias)
    
    # Id Primera actividad, primera tarea de la primera intancia
    @property
    def actividad_id_inicial(self):
        filtro = JsonPathStr("$.[0]['tareas'][0]['actividad']")
        
        return utils.getPathValue(filtro, self.instancias)
    
    # Primera tarea de la primera intancia
    @property
    def tramite_inicial(self):
        filtro = JsonPathStr("$.[0]['proceso_name']")
        
        return utils.getPathValue(filtro, self.instancias)
    
    # Id Primera tarea de la primera intancia
    @property
    def tramite_id_inicial(self):
        filtro = JsonPathStr("$.[0]['proceso_id']")
        
        return utils.getPathValue(filtro, self.instancias)
    
    @property
    def responsables_todos(self):
        keys      = ['responsable_id','responsable_name','dependencia_id','dependencia_name']
        filtrostr = ( "$.[*]['tareas'][*]%s" % ( str(keys).replace(' ', '') ) )
        filtro    = JsonPathStr( filtrostr )
        value     = utils.getPathValue(filtro, self.instancias, one=False, default=[])
        value     = [dict(zip(keys, v)) for v in utils.split_seq(value, 4)]
        
        return value
    
    @property
    def responsables_activos(self):
        keys      = ['responsable_id','responsable_name','dependencia_id','dependencia_name']
        filtrostr = ( "$.[*]['tareas'][?(@.estado==u'ACTIVO')]%s" % ( str(keys).replace(' ', '') ) )
        filtro    = JsonPathStr( filtrostr )
        value     = utils.getPathValue(filtro, self.instancias, one=False, default=[])
        value     = [dict(zip(keys, v)) for v in utils.split_seq(value, 4)]
        
        return value                
        
EntradaPro = {
    # Datos basicos
    'id'                : pyes_base.uuid_text,         # id del registro
    'tiporecord'        : pyes_base.base_multiple('tiporecord'),
    'radicador_id'      : pyes_base.uuid_text,
    'radicado_por'      : pyes_base.base_multiple('radicado_por'),
    'radicado_en_id'    : pyes_base.uuid_text,
    'radicado_en'       : pyes_base.base_multiple('radicado_en'),
    'nro_radicado'      : pyes_base.base_multiple('nro_radicado'),
    'fecha_radicado'    : pyes_base.base_multiple_date('fecha_radicado'),
    'fecha_documento'   : pyes_base.base_multiple_date('fecha_documento'),
    'nro_origen'        : pyes_base.base_multiple('nro_origen'),
    'nro_guia'          : pyes_base.base_multiple('nro_guia'),
    'folios'            : pyes_base.base_integer,
    'anexos'            : pyes_base.base_text,
    'asunto'            : pyes_base.base_text,
    'referenciados'     : pyes_base.base_text,
    'medio_id'          : pyes_base.uuid_text,
    'medio_name'        : pyes_base.base_multiple('medio_name'), 
    'contestado_con'    : pyes_base.base_multiple('contestado_con'), 
    'escaneada'         : pyes_base.base_multiple('escaneada'),    
    'fecha_recorrido'   : pyes_base.base_multiple_date('fecha_recorrido'),
    'recorrido'         : pyes_base.base_text,
    'impreso'           : pyes_base.base_text,    
    'copiamasivo'       : pyes_base.base_multiple('copiamasivo'),
    'enviadopor'        : pyes_base.base_multiple('enviadopor'), # Para grid de sort
    
    # Informacion del tercero
    'nit'               : pyes_base.base_multiple('nit'),
    'name'              : pyes_base.base_multiple('name'),
    'address'           : pyes_base.base_multiple('address'),
    'phone'             : pyes_base.base_multiple('phone'),
    'email'             : pyes_base.base_multiple('email'),
    'sender'            : pyes_base.base_multiple('sender'),
    'cargo'             : pyes_base.base_multiple('cargo'),
    'sender_universal'  : pyes_base.base_multiple('sender_universal'),
    'pais_id'           : pyes_base.uuid_text,
    'pais_name'         : pyes_base.base_multiple('pais_name'), 
    'departamento_id'   : pyes_base.uuid_text,
    'departamento_name' : pyes_base.base_multiple('departamento_name'), 
    'ciudad_id'         : pyes_base.uuid_text,
    'ciudad_name'       : pyes_base.base_multiple('ciudad_name'),
    
    # COPIAS
    'copia_terceros'    : {"properties" :
                                {'id'              : pyes_base.uuid_text,
                                 'name'            : pyes_base.base_text,
                                 'sender'          : pyes_base.base_text,
                                 'ciudad_full_name': pyes_base.base_text,
                                }
                          },
        
    'copia_funcionarios': {"properties" :
                                {'id'              : pyes_base.uuid_text,
                                 'name'            : pyes_base.base_text,
                                 'area_name'       : pyes_base.base_text,
                                 'sitio_name'      : pyes_base.base_text                                 
                                }
                          },
        
    'copia_grupos': {"properties" :
                                {'id'              : pyes_base.uuid_text,
                                 'name'            : pyes_base.base_text                                                           
                                }
                    },
     
    # ANEXOS
    'archivos_anexos'   : {"properties" :
                                {"creado_en" : pyes_base.base_text,
                                 "versiones" : {
                                     "properties" : {
                                            'descripcion': pyes_base.base_text,
                                            'filetype'   : pyes_base.base_text,
                                            'ocr'        : pyes_base.base_text,
                                            'path'       : pyes_base.base_text,
                                            'idFile'     : pyes_base.uuid_text,
                                            'version'    : pyes_base.base_text                             
                                        }
                                    }
                                }
                          },
    
    # EXPEDIENTES ARCHIVO GESTION
    'expedientes'      : {"properties" :
                                {'expediente_id'   : pyes_base.uuid_text,
                                 'expediente_name' : pyes_base.base_text,
                                 'expediente_trd'  : pyes_base.base_text,
                                 'carpeta_id'      : pyes_base.uuid_text,
                                 'carpeta_numero'  : pyes_base.base_integer,                                 
                                 'tipo_id'         : pyes_base.uuid_text,
                                 'tipo_name'       : pyes_base.uuid_text
                                }
                        },
        
    # Procesos
    'estado_label'      : pyes_base.base_multiple('estado_label'),    
    'instancias'        : {"properties" :
                                {"descripcion" : pyes_base.base_text,
                                 "proceso_id"  : pyes_base.uuid_text,
                                 "proceso_name": pyes_base.base_text,
                                 "tareas"      : {"properties" :
                                                    {'id'              : pyes_base.uuid_text,
                                                     # Responsable actual
                                                     'responsable_id'  : pyes_base.uuid_text,
                                                     'responsable_name': pyes_base.base_text,
                                                     'dependencia_id'  : pyes_base.uuid_text,
                                                     'dependencia_name': pyes_base.base_text,
                                                     # Dependencia que envia
                                                     'envia_id'        : pyes_base.uuid_text,
                                                     'envia_name'      : pyes_base.base_text,
                                                     'enviaDep_id'     : pyes_base.uuid_text,
                                                     'enviaDep_name'   : pyes_base.base_text,
                                                     'recibido_en'     : pyes_base.base_date,
                                                     'envia_tarea'     : {"properties" :
                                                                            {'de_ActividadId'   : pyes_base.uuid_text,
                                                                             'de_ActividadName' : pyes_base.base_text,
                                                                             'comentario'       : pyes_base.base_text,
                                                                             'creado'           : pyes_base.base_date,
                                                                            }                                                                            
                                                                         },
                                                     # Informacion de la Actividad
                                                     'actividad'       : pyes_base.uuid_text,
                                                     'actividad_name'  : pyes_base.base_text,
                                                     # Estado y alertas
                                                     'comentario'      : pyes_base.base_text,
                                                     'vence_en'        : pyes_base.base_date,
                                                     'wf_statusWItem'  : pyes_base.base_text,                                               
                                                     'estado'          : pyes_base.base_text,
                                                     'alertado'        : pyes_base.base_text,
                                                     'notificado'      : pyes_base.base_text                                                     
                                                    }                                                          
                                                  }
                                }
                          },
    
    'responsable_inicial'   : pyes_base.base_multiple('responsable_inicial'),
    'destinatario'          : pyes_base.base_multiple('destinatario'),
    'responsable_id_inicial': pyes_base.uuid_text,    
    'dependencia_inicial'   : pyes_base.base_multiple('dependencia_inicial'),
    'dependencia_id_inicial': pyes_base.uuid_text,    
    'actividad_inicial'     : pyes_base.base_multiple('actividad_inicial'),
    'actividad_id_inicial'  : pyes_base.uuid_text,    
    'tramite_inicial'       : pyes_base.base_multiple('tramite_inicial'),
    'tramite_id_inicial'    : pyes_base.uuid_text,    
    'responsables_todos': {"properties" :
                                {'responsable_id'  : pyes_base.uuid_text,
                                 'responsable_name': pyes_base.base_multiple('responsable_name'),
                                 'dependencia_id'  : pyes_base.uuid_text,
                                 'dependencia_name': pyes_base.base_multiple('dependencia_name'),}                                
                          },
        
    'responsables_activos': {"properties" :
                                {'responsable_id'  : pyes_base.uuid_text,
                                 'responsable_name': pyes_base.base_text,
                                 'dependencia_id'  : pyes_base.uuid_text,
                                 'dependencia_name': pyes_base.base_text}                                
                            },
    
    # Control
    'status'            : pyes_base.base_multiple('status'),
    '_created_at'       : pyes_base.base_multiple_date('_created_at'),
    '_updated_at'       : pyes_base.base_multiple_date('_updated_at'),
    '_unit_code'        : pyes_base.base_multiple('_unit_code'),
    '_organization_code': pyes_base.base_multiple('_organization_code'),
}
fulltext.createFullDB(entity=ENTIDAD_FTX, db='entrada'.lower(), idx='radicacion', properties=EntradaPro)
classDB['entrada'.lower()] = ENTRADA
__builtin__.ENTRADA = ENTRADA


#/* Clase de INTERNOS */
sessionInterno = SQLSession()
class INTERNO(Base): 
    __tablename__  = 'd_interno'
    __id__         = "id"
    
    # datos basicos radicado    
    radicador_id    = Column('radicador_id',    Unicode(55), index=True, nullable=False, default=u'')
    radicado_en_id  = Column('radicado_en_id',  Unicode(55), index=True, nullable=False, default=u'')
    nro_radicado    = Column('nro_radicado',    Unicode(50), unique=True, nullable=False)
    fecha_radicado  = Column('fecha_radicado',  DateTime, index=True, nullable=False, default=utils.getOnlyDateTime)
    fecha_documento = Column('fecha_documento', DateTime, index=True, nullable=False, default=utils.getOnlyDateTime)
    nro_origen      = Column('nro_origen',      Unicode(30), index=True, nullable=True)    
    folios          = Column('folios',          Integer, nullable=False, default=1)
    anexos          = Column('anexos',          Unicode(512), nullable=True)    
    asunto          = Column('asunto',          Unicode(1024), index=True, nullable=False)
    referenciados   = Column('referenciados',   Unicode(512), nullable=True)
    intencion       = Column('intencion',       Unicode(10),  default=u'FINALIZA', nullable=False)
    concopia        = Column('concopia',        Unicode(256), nullable=True)
    concopiaotros   = Column('concopiaotros',   Unicode(256), nullable=True)
    contestado_con  = Column('contestado_con',  Unicode(50), nullable=True)
    fecha_recorrido = Column('fecha_recorrido', DateTime, index=True, nullable=False, default=utils.getOnlyDateTime)
    recorrido       = Column('recorrido',       Integer, index=True, nullable=False, default=0)
    sincopia        = Column('sincopia',        Integer, index=True, nullable=False, default=0)
    impreso         = Column('impreso',         Integer, index=True, nullable=False, default=0)
    copiamasivo     = Column('copiamasivo',     Unicode(20),  nullable=True)
    
    # envia informacion
    area_sender_id   = Column('area_sender_id',  Unicode(50),  ForeignKey('d_seccion.id'), nullable=False, default=u'')
    area_sender_rel  = relationship("SECCION", foreign_keys=area_sender_id)
    area_sender_name = association_proxy('area_sender_rel', 'name')
    
    sender_id   = Column('sender_id', Unicode(50),  ForeignKey('d_users.id'), nullable=False, default=u'')
    sender_rel  = relationship("USUARIO", foreign_keys=sender_id)
    sender_name = association_proxy('sender_rel', 'name')
    
    # recibe informacion
    area_target_id   = Column('area_target_id',  Unicode(50),  ForeignKey('d_seccion.id'), nullable=False, default=u'')
    area_target_rel  = relationship("SECCION", foreign_keys=area_target_id)
    area_target_name = association_proxy('area_target_rel', 'name')
    
    target_id   = Column('target_id', Unicode(50),  ForeignKey('d_users.id'), nullable=False, default=u'')
    target_rel  = relationship("USUARIO", foreign_keys=target_id)
    target_name = association_proxy('target_rel', 'name')
      
    # valores de control  
    id                 = Column('id', Unicode(50), default=utils.UuidStr, primary_key=True)
    status             = Column('status',      Unicode(25),  default=u'ACTIVO', index=True, nullable=False)
    _created_at        = Column('_created_at', DateTime, nullable=False, default=utils.getOnlyDateTime)
    _updated_at        = Column('_updated_at', DateTime, nullable=False, default=utils.getOnlyDateTime, onupdate=utils.getOnlyDateTime)
    _unit_code         = Column('_unit_code', Unicode(20), index=True, nullable=False, default=u'*')
    _organization_code = Column('_organization_code', Unicode(20), index=True, nullable=False, default=organization_default)

    ##########################
    # BASE
    @property
    def tiporecord(self):
        return 'INTERNO'
    
    # SITIO DE RADICACION
    @property
    def radicado_en(self):
        if (self.radicador_id in [None, '']):
            return ''
        else:
            q = sessionInterno.query(SITIO).filter(SITIO.id == self.radicado_en_id)
            try:
                sitio = q.one()
                name  = sitio.name
            except:
                name  = ''
        
        return name
    
    # NOMBRE RADICADOR
    @property
    def radicado_por(self):
        if (self.radicador_id in [None, '']):
            return ''
        else:
            q = sessionInterno.query(USUARIO).filter(USUARIO.id == self.radicador_id)
            try:
                usuario = q.one()
                name    = usuario.name
            except:
                name  = ''
        
        return name
    
    # SI TIENE IMAGEN ESCANEDA O NO
    @property
    def escaneada(self):
        # Si tiene imagen escaneada formato PDF
        # ver database relations
        total = len(self.r_scan)
        
        return 'N' if total == 0 else 'S'
    
    # Unifica nombre de campo para consultas ENTRADA, SALIDA, INTERNO
    @property
    def enviadopor(self):
        return self.area_sender_name
    
    # Unifica nombre de campo para consultas ENTRADA, SALIDA, INTERNO
    @property
    def destinatario(self):
       return self.responsable_inicial
    
    # Unifica nombre de campo para consultas ENTRADA, SALIDA, INTERNO
    @property
    def sender_universal(self):
       return self.sender_name
    
    # Unifica nit ENTRADA, SALIDA, INTERNO
    @property
    def nit(self):
       return ''
    
    #####################
    # COPIAS
    @property
    def copia_terceros(self):
        copiasTer    = sessionInterno.query(COPIATERCEROS).filter_by(documento_id=self.id).all()        
        tercerosList = []
        try:
            for copia in copiasTer:
                tercero = sessionInterno.query(TERCERO).filter_by(id=copia.concopia_a_id).one()
                tercerosList.append({'id'    : tercero.id,
                                     'name'  : tercero.name,
                                     'sender': tercero.sender,
                                     'ciudad_full_name': tercero.ciudad_full_name
                                     })
        except:
            pass
        
        return tercerosList
    
    @property
    def copia_funcionarios(self):
        copiasUsu    = sessionInterno.query(COPIAUSUARIOS).filter_by(documento_id=self.id).all()        
        usuariosList = []
        try:
            for copia in copiasUsu:
                usuario = sessionInterno.query(USUARIO).filter_by(id=copia.concopia_a_id).one()            
                usuariosList.append({'id'        : usuario.id,
                                     'name'      : usuario.name,
                                     'area_name' : usuario.area_name,
                                     'sitio_name': usuario.sitio_name
                                     })
        except:
            pass
        
        return usuariosList
    
    @property
    def copia_grupos(self):
        copiasGru  = sessionInterno.query(COPIAGRUPOS).filter_by(documento_id=self.id).all()        
        gruposList = []
        try:
            for copia in copiasGru:
                grupo = sessionInterno.query(GRUPO).filter_by(id=copia.concopia_a_id).one()                           
                gruposList.append({'id'   : grupo.id,
                                   'name' : grupo.name
                                  })
        except:
            pass
                 
        return gruposList                   
    
    #####################
    # ANEXOS
    @property
    def archivos_anexos(self):
        q          = sessionInterno.query(OS_OBJETO).filter_by(code=self.nro_radicado, status=u'ACTIVO').order_by(asc(OS_OBJETO._created_at))
        anexosList = []
        anexos     = q.all()
        for anexo in anexos:
            anexosList.append({'creado_en'  : anexo._created_at,
                               'versiones'  : anexo.versiones
                              })
        
        return anexosList
    
    #####################
    # EXPEDIENTES ARCHIVO GESTION
    @property
    def expedientes(self):
        DE             = DOCUMENTOEXPEDIENTE
        documentos     = sessionInterno.query(DE).filter(DE.documento_id==self.id).order_by(asc(DE._created_at)).all()
        documentoslist = []
        for documento in documentos:
            documentoslist.append(documento.expediente)
                
        return documentoslist
    
    ##########################################
    # TAREAS - PROCESOS    
    # ESTADO GENERAL DEL RADICADO
    @property
    def estado_label(self):
        """
        # Retorna el numero de tareas activas asociadas al radicado
        # ver database relations
        total = self.pro_status
        
        return u'FINALIZADO' if total == 0 else u'ACTIVO'
        """
        return u'ACTIVO'
    
    # INSTANCIAS ASOCIADAS AL RADICADO
    datainstancias = []
    @property
    def instancias(self):
        if (len(self.datainstancias) == 0):
            self.datainstancias = []
            try:
                q = sessionInterno.query(INSTANCIA).filter_by(wf_nro_radicado=self.nro_radicado).order_by(asc(INSTANCIA._created_at))
                instancias = q.all()
                for instancia in instancias:
                    self.datainstancias.append(instancia.instancia)
            except Exception, e:
                pass
            
        return self.datainstancias
    
    # persona responsable, primera tarea de la primera intancia
    @property
    def responsable_inicial(self):
        filtro = JsonPathStr("$.[0]['tareas'][0]['responsable_name']")
        
        return utils.getPathValue(filtro, self.instancias)
        
    # id persona responsable, primera tarea de la primera intancia
    @property
    def responsable_id_inicial(self):
        filtro = JsonPathStr("$.[0]['tareas'][0]['responsable_id']")
        
        return utils.getPathValue(filtro, self.instancias)
    
    # Dependencia responsable, primera tarea de la primera intancia
    @property
    def dependencia_inicial(self):
        filtro = JsonPathStr("$.[0]['tareas'][0]['dependencia_name']")
        
        return utils.getPathValue(filtro, self.instancias)
    
    # Id Dependencia responsable, primera tarea de la primera intancia
    @property
    def dependencia_id_inicial(self):
        filtro = JsonPathStr("$.[0]['tareas'][0]['dependencia_id']")
        
        return utils.getPathValue(filtro, self.instancias)
    
    # Primera actividad, primera tarea de la primera intancia
    @property
    def actividad_inicial(self):
        filtro = JsonPathStr("$.[0]['tareas'][0]['actividad_name']")
        
        return utils.getPathValue(filtro, self.instancias)
    
    # Id Primera actividad, primera tarea de la primera intancia
    @property
    def actividad_id_inicial(self):
        filtro = JsonPathStr("$.[0]['tareas'][0]['actividad']")
        
        return utils.getPathValue(filtro, self.instancias)
    
    # Primera tarea de la primera intancia
    @property
    def tramite_inicial(self):
        filtro = JsonPathStr("$.[0]['proceso_name']")
        
        return utils.getPathValue(filtro, self.instancias)
    
    # Id Primera tarea de la primera intancia
    @property
    def tramite_id_inicial(self):
        filtro = JsonPathStr("$.[0]['proceso_id']")
        
        return utils.getPathValue(filtro, self.instancias)
    
    @property
    def responsables_todos(self):
        keys      = ['responsable_id','responsable_name','dependencia_id','dependencia_name']
        filtrostr = ( "$.[*]['tareas'][*]%s" % ( str(keys).replace(' ', '') ) )
        filtro    = JsonPathStr( filtrostr )
        value     = utils.getPathValue(filtro, self.instancias, one=False, default=[])
        value     = [dict(zip(keys, v)) for v in utils.split_seq(value, 4)]
        
        return value
    
    @property
    def responsables_activos(self):
        keys      = ['responsable_id','responsable_name','dependencia_id','dependencia_name']
        filtrostr = ( "$.[*]['tareas'][?(@.estado==u'ACTIVO')]%s" % ( str(keys).replace(' ', '') ) )
        filtro    = JsonPathStr( filtrostr )
        value     = utils.getPathValue(filtro, self.instancias, one=False, default=[])
        value     = [dict(zip(keys, v)) for v in utils.split_seq(value, 4)]
        
        return value
    
INTERNOPro = {
    # Datos basicos
    'id'                : pyes_base.uuid_text,         # id del registro
    'tiporecord'        : pyes_base.base_multiple('tiporecord'),
    'radicador_id'      : pyes_base.uuid_text,
    'radicado_por'      : pyes_base.base_multiple('radicado_por'),
    'radicado_en_id'    : pyes_base.uuid_text,
    'radicado_en'       : pyes_base.base_multiple('radicado_en'),
    'nro_radicado'      : pyes_base.base_multiple('nro_radicado'),
    'fecha_radicado'    : pyes_base.base_multiple_date('fecha_radicado'),
    'fecha_documento'   : pyes_base.base_multiple_date('fecha_documento'),
    'nro_origen'        : pyes_base.base_multiple('nro_origen'),
    'folios'            : pyes_base.base_integer,
    'anexos'            : pyes_base.base_text,
    'asunto'            : pyes_base.base_text,
    'referenciados'     : pyes_base.base_text,
    'intencion'         : pyes_base.base_text, 
    'contestado_con'    : pyes_base.base_multiple('contestado_con'), 
    'escaneada'         : pyes_base.base_multiple('escaneada'),    
    'fecha_recorrido'   : pyes_base.base_multiple_date('fecha_recorrido'),
    'recorrido'         : pyes_base.base_text,
    'impreso'           : pyes_base.base_text,
    'copiamasivo'       : pyes_base.base_multiple('copiamasivo'),
    'enviadopor'        : pyes_base.base_multiple('enviadopor'), # Para grid de sort
    'sincopia'          : pyes_base.base_text,
    
    # Remitente
    'area_sender_id'    : pyes_base.uuid_text,
    'area_sender_name'  : pyes_base.base_multiple('area_sender_name'),    
    'sender_id'         : pyes_base.uuid_text,
    #'sender'            : pyes_base.base_multiple('sender'),
    'sender_universal'  : pyes_base.base_multiple('sender_universal'),
    
    # Destinatario
    'area_target_id'    : pyes_base.uuid_text,
    'area_target_name'  : pyes_base.base_multiple('area_target_name'), 
    'target_id'         : pyes_base.uuid_text,
    'target_name'       : pyes_base.base_multiple('target_name'),
    
    'destinatario'      : pyes_base.base_multiple('destinatario'), # Para grid de sort
    'enviadopor'        : pyes_base.base_multiple('enviadopor'), # Para grid de sort
   
    # COPIAS
    'copia_terceros'    : {"properties" :
                                {'id'              : pyes_base.uuid_text,
                                 'name'            : pyes_base.base_text,
                                 'sender'          : pyes_base.base_text,
                                 'ciudad_full_name': pyes_base.base_text,
                                }
                          },
        
    'copia_funcionarios': {"properties" :
                                {'id'              : pyes_base.uuid_text,
                                 'name'            : pyes_base.base_text,
                                 'area_name'       : pyes_base.base_text,
                                 'sitio_name'      : pyes_base.base_text                                 
                                }
                          },
        
    'copia_grupos': {"properties" :
                                {'id'              : pyes_base.uuid_text,
                                 'name'            : pyes_base.base_text                                                           
                                }
                    },
     
    # ANEXOS
    'archivos_anexos'   : {"properties" :
                                {"creado_en" : pyes_base.base_text,
                                 "versiones" : {"properties" :
                                                    {'descripcion': pyes_base.base_text,
                                                     'filetype'   : pyes_base.base_text,
                                                     'ocr'        : pyes_base.base_text,
                                                     'path'       : pyes_base.base_text,
                                                     'idFile'     : pyes_base.uuid_text,
                                                     'version'    : pyes_base.base_text                             
                                                    }
                                               }
                                }
                          },
    
    # EXPEDIENTES ARCHIVO GESTION
    'expedientes'      : {"properties" :
                                {'expediente_id'   : pyes_base.uuid_text,
                                 'expediente_name' : pyes_base.base_text,
                                 'expediente_trd'  : pyes_base.base_text,
                                 'carpeta_id'      : pyes_base.uuid_text,
                                 'carpeta_numero'  : pyes_base.base_integer,                                 
                                 'tipo_id'         : pyes_base.uuid_text,
                                 'tipo_name'       : pyes_base.uuid_text
                                }
                        },
        
    # Procesos
    'estado_label'      : pyes_base.base_multiple('estado_label'),  
    'instancias'        : {"properties" :
                                {"descripcion" : pyes_base.base_text,
                                 "proceso_id"  : pyes_base.uuid_text,
                                 "proceso_name": pyes_base.base_text,
                                 "tareas"      : {"properties" :
                                                    {'id'              : pyes_base.uuid_text,
                                                     # Responsable actual
                                                     'responsable_id'  : pyes_base.uuid_text,
                                                     'responsable_name': pyes_base.base_text,
                                                     'dependencia_id'  : pyes_base.uuid_text,
                                                     'dependencia_name': pyes_base.base_text,
                                                     # Dependencia que envia
                                                     'envia_id'        : pyes_base.uuid_text,
                                                     'envia_name'      : pyes_base.base_text,
                                                     'enviaDep_id'     : pyes_base.uuid_text,
                                                     'enviaDep_name'   : pyes_base.base_text,
                                                     'recibido_en'     : pyes_base.base_date,
                                                     'envia_tarea'     : {"properties" :
                                                                            {'de_ActividadId'   : pyes_base.uuid_text,
                                                                             'de_ActividadName' : pyes_base.base_text,
                                                                             'comentario'       : pyes_base.base_text,
                                                                             'creado'           : pyes_base.base_date,
                                                                            }                                                                            
                                                                         },
                                                     # Informacion de la Actividad
                                                     'actividad'       : pyes_base.uuid_text,
                                                     'actividad_name'  : pyes_base.base_text,
                                                     # Estado y alertas
                                                     'comentario'      : pyes_base.base_text,
                                                     'vence_en'        : pyes_base.base_date,
                                                     'wf_statusWItem'  : pyes_base.base_text,                                               
                                                     'estado'          : pyes_base.base_text,
                                                     'alertado'        : pyes_base.base_text,
                                                     'notificado'      : pyes_base.base_text                                                     
                                                    }                                                          
                                                  }
                                }
                          },
    
    'responsable_inicial'   : pyes_base.base_multiple('responsable_inicial'),
    'responsable_id_inicial': pyes_base.uuid_text,    
    'dependencia_inicial'   : pyes_base.base_multiple('dependencia_inicial'),
    'dependencia_id_inicial': pyes_base.uuid_text,    
    'actividad_inicial'     : pyes_base.base_multiple('actividad_inicial'),
    'actividad_id_inicial'  : pyes_base.uuid_text,    
    'tramite_inicial'       : pyes_base.base_multiple('tramite_inicial'),
    'tramite_id_inicial'    : pyes_base.uuid_text,    
    'responsables_todos': {"properties" :
                                {'responsable_id'  : pyes_base.uuid_text,
                                 'responsable_name': pyes_base.base_multiple('responsable_name'),
                                 'dependencia_id'  : pyes_base.uuid_text,
                                 'dependencia_name': pyes_base.base_multiple('dependencia_name'),}                                
                          },
        
    'responsables_activos': {"properties" :
                                {'responsable_id'  : pyes_base.uuid_text,
                                 'responsable_name': pyes_base.base_text,
                                 'dependencia_id'  : pyes_base.uuid_text,
                                 'dependencia_name': pyes_base.base_text}                                
                            },
    
    # Control
    'status'            : pyes_base.base_multiple('status'),
    '_created_at'       : pyes_base.base_multiple_date('_created_at'),
    '_updated_at'       : pyes_base.base_multiple_date('_updated_at'),
    '_unit_code'        : pyes_base.base_multiple('_unit_code'),
    '_organization_code': pyes_base.base_multiple('_organization_code'),
}
fulltext.createFullDB(entity=ENTIDAD_FTX, db='INTERNO'.lower(), idx='radicacion', properties=INTERNOPro)
classDB['INTERNO'.lower()] = INTERNO
__builtin__.INTERNO = INTERNO
                                                                                

#/* Clase de SALIDAS */
sessionSalida = SQLSession()
class SALIDA(Base):
    __tablename__  = 'd_salida'
    __id__         = 'id'
    
    # datos basicos radicado    
    radicador_id    = Column('radicador_id',    Unicode(55), index=True, nullable=False, default=u'')
    radicado_en_id  = Column('radicado_en_id',  Unicode(55), nullable=False, default=u'')
    nro_radicado    = Column('nro_radicado',    Unicode(50), unique=True, nullable=False)
    fecha_radicado  = Column('fecha_radicado',  DateTime, index=True, nullable=False, default=utils.getOnlyDateTime)
    fecha_documento = Column('fecha_documento', DateTime, index=True, nullable=False, default=utils.getOnlyDateTime)
    nro_origen      = Column('nro_origen',      Unicode(30), index=True, nullable=True)
    nro_guia        = Column('nro_guia',        Unicode(30), index=True, nullable=True)
    folios          = Column('folios',          Integer, nullable=False, default=1)
    anexos          = Column('anexos',          Unicode(512), nullable=True)
    asunto          = Column('asunto',          Unicode(1024), index=True, nullable=False)
    fecha_recorrido = Column('fecha_recorrido', DateTime, index=True, nullable=False, default=utils.getOnlyDateTime)
    recorrido       = Column('recorrido',       Integer, index=True, nullable=False, default=0)
    fecha_copia     = Column('fecha_copia',     DateTime, index=True, nullable=True, default=None)
    recorrido_copia = Column('recorrido_copia', Integer, index=True, nullable=True, default=None)
    impreso         = Column('impreso',         Integer, index=True, nullable=False, default=0)
    copiamasivo     = Column('copiamasivo',     Unicode(20),  nullable=True)
    medio_id        = Column('medio_id',        Unicode(50),  ForeignKey('d_medio.id'), nullable=False, default=u'')
    medio_rel       = relationship("MEDIO", foreign_keys=medio_id)
    medio_name      = association_proxy('medio_rel', 'name')    
    referenciados   = Column('referenciados',   Unicode(512), nullable=True)
    intencion       = Column('intencion',       Unicode(10),  default=u'FINALIZA', nullable=False)
    concopia        = Column('concopia',        Unicode(256), nullable=True)
    concopiaotros   = Column('concopiaotros',   Unicode(256), nullable=True)
    peso            = Column('peso',            Integer,  nullable=True, default=0)
    vinculada_cor   = Column('vinculada_cor',  Unicode(10),  default=u'NO', index=True, nullable=False)
        
    #informacion del tercero
    nit       = Column('nit',       Unicode(50),  nullable=True)
    name      = Column('name',      Unicode(120), index=True, nullable=False)
    address   = Column('address',   Unicode(120), nullable=True)
    phone     = Column('phone',     Unicode(50),  nullable=True)
    email     = Column('email',     Unicode(120),  nullable=True)
    sender    = Column('sender',    Unicode(120), index=True, nullable=True)
    cargo     = Column('cargo',     Unicode(150),  nullable=True)
     
    # Vinculos Pais
    pais_id            = Column('pais_id', Unicode(50), ForeignKey('d_pais.id'), nullable=False, default=u'')
    pais_rel           = relationship("PAIS", foreign_keys=pais_id)
    pais_name          = association_proxy('pais_rel', 'name')
        
    departamento_id   = Column('departamento_id', Unicode(50), ForeignKey('d_departamento.id'), nullable=False, default=u'')
    departamento_rel  = relationship("DEPARTAMENTO", foreign_keys=departamento_id)
    departamento_name = association_proxy('departamento_rel', 'name')
    
    ciudad_id         = Column('ciudad_id', Unicode(50), ForeignKey('d_ciudad.id'), nullable=False, default=u'')
    ciudad_rel        = relationship("CIUDAD", foreign_keys=ciudad_id)
    ciudad_name       = association_proxy('ciudad_rel', 'full_name')
    
    # envia informacion
    area_sender_id   = Column('area_sender_id',  Unicode(50),  ForeignKey('d_seccion.id'), nullable=False, default=u'')
    area_sender_rel  = relationship("SECCION", foreign_keys=area_sender_id)
    area_sender_name = association_proxy('area_sender_rel', 'name')
    
    sender_id   = Column('sender_id', Unicode(50),  ForeignKey('d_users.id'), nullable=False, default=u'')
    sender_rel  = relationship("USUARIO", foreign_keys=sender_id)
    sender_name = association_proxy('sender_rel', 'name')
    
    # respuesta
    response       = Column('response',        Unicode(10),  index=True, default=u'SI', nullable=False)
    fecha_response = Column('fecha_response',  Date, index=True, nullable=True)
    isresponse     = Column('isresponse',      Unicode(10),  index=True, default=u'NO', nullable=False)
    
    # valores de control  
    id                 = Column('id', Unicode(50), default=utils.UuidStr, primary_key=True)
    status             = Column('status',      Unicode(25),  default=u'ACTIVO', index=True, nullable=False)
    _created_at        = Column('_created_at', DateTime, nullable=False, default=utils.getOnlyDateTime)
    _updated_at        = Column('_updated_at', DateTime, nullable=False, default=utils.getOnlyDateTime, onupdate=utils.getOnlyDateTime)
    _unit_code         = Column('_unit_code', Unicode(20), index=True, nullable=False, default=u'*')
    _organization_code = Column('_organization_code', Unicode(20), index=True, nullable=False, default=organization_default)    
    
    @property
    def tiporecord(self):
        return 'SALIDA'
    
    @property
    def copia_terceros(self):
        copiasTer    = sessionSalida.query(COPIATERCEROS).filter_by(documento_id=self.id).all()        
        tercerosList = []
        try:
            for copia in copiasTer:
                tercero = sessionSalida.query(TERCERO).filter_by(id=copia.concopia_a_id).one()
                tercerosList.append({'id'    : tercero.id,
                                     'name'  : tercero.name,
                                     'sender': tercero.sender,
                                     'ciudad_full_name': tercero.ciudad_full_name
                                     })
        except:
            pass
                           
        return tercerosList
    
    @property
    def copia_funcionarios(self):
        copiasUsu    = sessionSalida.query(COPIAUSUARIOS).filter_by(documento_id=self.id).all()        
        usuariosList = []
        try:
            for copia in copiasUsu:
                usuario = sessionSalida.query(USUARIO).filter_by(id=copia.concopia_a_id).one()            
                usuariosList.append({'id'        : usuario.id,
                                     'name'      : usuario.name,
                                     'area_name' : usuario.area_name,
                                     'sitio_name': usuario.sitio_name
                                     })
        except:
            pass
        
        return usuariosList
    
    @property
    def copia_grupos(self):
        copiasGru  = sessionSalida.query(COPIAGRUPOS).filter_by(documento_id=self.id).all()        
        gruposList = []
        try:
            for copia in copiasGru:
                grupo = sessionSalida.query(GRUPO).filter_by(id=copia.concopia_a_id).one()                           
                gruposList.append({'id'   : grupo.id,
                                   'name' : grupo.name
                                  })
        except:
            pass
        
        return gruposList    
    
    @property
    def copiaAmarilla(self):
        prueba = ""
        for r in self.r_copia_amarilla:
            prueba = 'Rad: ' + r.nro_radicado_ext + ' - De:' + str(r.fecha_documento) + '\n'
        return prueba
    
    @property
    def radicado_en(self):
        if (self.radicado_en_id in [None, '']):
            return ''
        else:
            q = sessionSalida.query(SITIO).filter(SITIO.id == self.radicado_en_id)
            try:
                sitio = q.one()
                name  = sitio.name
            except:
                name  = ''
      
        return name
    
    @property
    def radicado_por(self):
        if (self.radicador_id in [None, '']):
            return ''
        else:
            q = sessionSalida.query(USUARIO).filter(USUARIO.id == self.radicador_id)            
            try:
                usuario = q.one()
                name    = usuario.name
                
            except Exception, e:
                name  = ''
            
        return name       
    
    escaneada = Column('escaneada', Unicode(10))
    
    @synonym_for('escaneada')
    @property    
    def escaneada_(self):
        total = len(self.r_scan)
        
        return u'N' if total == 0 else u'S'
    
    @property
    def archivos_anexos(self):
        q          = sessionSalida.query(OS_OBJETO).filter_by(code=self.nro_radicado, status=u'ACTIVO').order_by(asc(OS_OBJETO._created_at))
        anexosList = []
        anexos     = q.all()
        for anexo in anexos:
            anexosList.append({'creado_en'  : anexo._created_at,
                               'versiones'  : anexo.versiones                              
                              })
        return anexosList
    
    @property
    def expedientes(self):
        DE             = DOCUMENTOEXPEDIENTE
        documentos     = sessionSalida.query(DE).filter(DE.documento_id==self.id).order_by(asc(DE._created_at)).all()
        documentoslist = []
        for documento in documentos:
            documentoslist.append(documento.expediente)
        
        return documentoslist
    
    @property
    def destinatario(self):
        data = self.name
        
        return data
    
    @property
    def enviadopor(self):
        return self.area_sender_name
    
    
    # Unifica nombre de campo para consultas ENTRADA, SALIDA, INTERNO
    @property
    def sender_universal(self):
        return self.sender_name
    
    #Unifica nombre de campo para consultas ENTRADA, SALIDA, INTERNO
    @property
    def estado_label(self):
        #print 'FINALIZADO'
        return 'FINALIZADO'
    
SALIDAPro = {
    'id'                : pyes_base.uuid_text,         # id del registro
    'tiporecord'        : pyes_base.base_multiple('tiporecord'),
    'radicador_id'      : pyes_base.uuid_text,
    'radicado_por'      : pyes_base.base_multiple('radicado_por'),
    'radicado_en_id'    : pyes_base.uuid_text,
    'radicado_en'       : pyes_base.base_multiple('radicado_en'),
    'nro_radicado'      : pyes_base.base_multiple('nro_radicado'),
    'fecha_radicado'    : pyes_base.base_multiple_date('fecha_radicado'),    
    'fecha_documento'   : pyes_base.base_multiple_date('fecha_documento'),
    'nro_origen'        : pyes_base.base_multiple('nro_origen'),
    'nro_guia'          : pyes_base.base_multiple('nro_guia'),
    'folios'            : pyes_base.base_integer,
    'nro_guia'          : pyes_base.base_multiple('nro_guia'),
    'anexos'            : pyes_base.base_text,
    'asunto'            : pyes_base.base_text,
    'referenciados'     : pyes_base.base_text,
    'medio_id'          : pyes_base.uuid_text,
    'medio_name'        : pyes_base.base_multiple('medio_name'),    
    'intencion'         : pyes_base.base_text,
    'concopia'          : pyes_base.base_text,
    'concopiaotros'     : pyes_base.base_text,
    'peso'              : pyes_base.base_text,
    'fecha_recorrido'   : pyes_base.base_multiple_date('fecha_recorrido'),
    'recorrido'         : pyes_base.base_text,
    'impreso'           : pyes_base.base_text,
    'escaneada'         : pyes_base.base_multiple('escaneada'),
    'vinculada_cor'     : pyes_base.base_text,
    'response'          : pyes_base.base_text,
    'fecha_response'    : pyes_base.base_text,
    'isresponse'        : pyes_base.base_text,
    'fecha_copia'       : pyes_base.base_text,
    'recorrido_copia'   : pyes_base.base_text,
    'recorrido'         : pyes_base.base_text,
    'copiamasivo'       : pyes_base.base_multiple('copiamasivo'),    
    
    # Destinatario
    'nit'               : pyes_base.base_multiple('nit'),
    'name'              : pyes_base.base_multiple('name'),
    'address'           : pyes_base.base_multiple('address'),
    'phone'             : pyes_base.base_multiple('phone'),
    'email'             : pyes_base.base_multiple('email'),
    'sender'            : pyes_base.base_multiple('sender'),
    'cargo'             : pyes_base.base_multiple('cargo'),
    'sender_universal'  : pyes_base.base_multiple('sender_universal'),    
    'pais_id'           : pyes_base.uuid_text,
    'pais_name'         : pyes_base.base_multiple('pais_name'), 
    'departamento_id'   : pyes_base.uuid_text,
    'departamento_name' : pyes_base.base_multiple('departamento_name'), 
    'ciudad_id'         : pyes_base.uuid_text,
    'ciudad_name'       : pyes_base.base_multiple('ciudad_name'),
    
    # Remitente      
    'area_sender_id'    : pyes_base.uuid_text,
    'area_sender_name'  : pyes_base.base_multiple('area_sender_name'),    
    'sender_id'         : pyes_base.uuid_text,
    'sender_name'       : pyes_base.base_multiple('sender_name'),
    
    'archivos_anexos'   : {"properties" :
                                {"creado_en" : pyes_base.base_text,
                                 "versiones" : {"properties" :
                                                    {'descripcion': pyes_base.base_text,
                                                     'filetype'   : pyes_base.base_text,
                                                     'ocr'        : pyes_base.base_text,
                                                     'path'       : pyes_base.base_text,
                                                     'idFile'     : pyes_base.uuid_text,
                                                     'version'    : pyes_base.base_text                             
                                                    }
                                               }
                                }
                          },
        
    'expedientes'      : {"properties" :
                                {'expediente_id'   : pyes_base.uuid_text,
                                 'expediente_name' : pyes_base.base_text,
                                 'expediente_trd'  : pyes_base.base_text,
                                 'carpeta_id'      : pyes_base.uuid_text,
                                 'carpeta_numero'  : pyes_base.base_integer,                                 
                                 'tipo_id'         : pyes_base.uuid_text,
                                 'tipo_name'       : pyes_base.uuid_text
                                }
                        },
    'destinatario'      : pyes_base.base_multiple('destinatario'), # Para grid de sort
    'enviadopor'        : pyes_base.base_multiple('enviadopor'), # Para grid de sort
    'estado_label'      : pyes_base.base_multiple('estado_label'),  
    
    'copia_terceros'    : {"properties" :
                                {'id'              : pyes_base.uuid_text,
                                 'name'            : pyes_base.base_text,
                                 'sender'          : pyes_base.base_text,
                                 'ciudad_full_name': pyes_base.base_text,
                                }
                          },
        
    'copia_funcionarios': {"properties" :
                                {'id'              : pyes_base.uuid_text,
                                 'name'            : pyes_base.base_text,
                                 'area_name'       : pyes_base.base_text,
                                 'sitio_name'      : pyes_base.base_text                                 
                                }
                          },
        
    'copia_grupos': {"properties" :
                                {'id'              : pyes_base.uuid_text,
                                 'name'            : pyes_base.base_text                                                           
                                }
                    },
    
    'status'            : pyes_base.base_multiple('status'),
    '_created_at'       : pyes_base.base_multiple_date('_created_at'),
    '_updated_at'       : pyes_base.base_multiple_date('_updated_at'),
    '_unit_code'        : pyes_base.base_multiple('_unit_code'),
    '_organization_code': pyes_base.base_multiple('_organization_code'),
}
fulltext.createFullDB(entity=ENTIDAD_FTX, db='SALIDA'.lower(), idx='radicacion', properties=SALIDAPro)
classDB['SALIDA'.lower()] = SALIDA
__builtin__.SALIDA = SALIDA

# BASE DE DATOS PARA BUSCAR SOBRE TODOS LOS RADICADOS, NO ES ALIAS; TRABAJO SOBRE UN SOLO INDICE
typesRadicados = ','.join( [ fulltextDB['entrada']['TYPE'], fulltextDB['salida']['TYPE'], fulltextDB['interno']['TYPE'] ] )
idxs = ','.join( [ fulltextDB['entrada']['INDEX'], fulltextDB['salida']['INDEX'], fulltextDB['interno']['INDEX'] ] )
fulltext.createFullDB(entity=ENTIDAD_FTX, db='RADICADOS'.lower(), idx=idxs,
                      properties=SALIDAPro, typesF = typesRadicados, multiple = True)

class COPIAAMARILLA(Base):
    __tablename__  = 'd_copia_am'
    __id__         = "id"
        
    # datos basicos radicado    
    radicador_id        = Column('radicador_id',    Unicode(55), nullable=False, default=u'')
    radicado_en_id      = Column('radicado_en_id',  Unicode(55), nullable=False, default=u'')
    nro_radicado        = Column('nro_radicado',    Unicode(50), nullable=False )
    nro_radicado_ext    = Column('nro_radicado_ext',Unicode(55), nullable=False, default=u'')
    fecha_radicado      = Column('fecha_radicado',  DateTime, nullable=False, default=utils.getOnlyDateTime)
    fecha_documento     = Column('fecha_documento', DateTime, nullable=False, default=utils.getOnlyDateTime)
    referenciados       = Column('referenciados',   Unicode(150),  nullable=True)
    
    # recibe informacion
    area_target_id  = Column('area_target_id',  Unicode(50),  ForeignKey('d_seccion.id'), nullable=False, default=u'')
    target_id = Column('target_id', Unicode(50),  ForeignKey('d_users.id'), nullable=False, default=u'')

    fecha_recorrido = Column('fecha_recorrido', DateTime, nullable=False, default=utils.getOnlyDateTime)
    recorrido       = Column('recorrido',       Integer, nullable=False, default=0)

    r_area_target = relationship(SECCION, foreign_keys = [area_target_id],  primaryjoin = area_target_id  == SECCION.id, lazy=False)
    r_target      = relationship(USUARIO, foreign_keys = [target_id],       primaryjoin = target_id       == USUARIO.id, lazy=False)
    r_radicado    = relationship( SALIDA
                                 ,primaryjoin  = "COPIAAMARILLA.referenciados == SALIDA.nro_radicado"
                                 ,lazy         = False
                                 ,foreign_keys = "COPIAAMARILLA.referenciados")

   # valores de control  
    id                 = Column('id', Unicode(50), default=utils.UuidStr, primary_key=True)
    status             = Column('status',      Unicode(10),  default=u'ACTIVO', index=True, nullable=False)
    _created_at        = Column('_created_at', DateTime, nullable=False, default=utils.getOnlyDateTime)
    _updated_at        = Column('_updated_at', DateTime, nullable=False, default=utils.getOnlyDateTime, onupdate=utils.getOnlyDateTime)
    _unit_code         = Column('_unit_code', Unicode(20), index=True, nullable=False, default=u'*')
    _organization_code = Column('_organization_code', Unicode(20), index=True, nullable=False, default=organization_default)
    
COPIAAMARILLAPRO = {
    'id'                : pyes_base.uuid_text,         # id del registro
    
    'radicador_id'      : pyes_base.uuid_text,        
    'radicado_en_id'    : pyes_base.uuid_text,           
    'nro_radicado'      : pyes_base.base_multiple('nro_radicado'),
    'nro_radicado_ext'  : pyes_base.base_multiple('nro_radicado_ext'),
    
    'fecha_radicado'    : pyes_base.base_multiple_date('fecha_radicado'),
    'fecha_documento'   : pyes_base.base_multiple_date('fecha_documento'),
    'referenciados'     : pyes_base.uuid_text,
    
    'area_target_id'    : pyes_base.uuid_text,
    'target_id'         : pyes_base.uuid_text,  
    
    'fecha_recorrido'   : pyes_base.base_text,
    'recorrido'         : pyes_base.base_text,    
    
    'status'            : pyes_base.base_multiple('status'),
    '_created_at'       : pyes_base.base_multiple_date('_created_at'),
    '_updated_at'       : pyes_base.base_multiple_date('_updated_at'),
    '_unit_code'        : pyes_base.base_multiple('_unit_code'),
    '_organization_code': pyes_base.base_multiple('_organization_code'),
}
fulltext.createFullDB(entity=ENTIDAD_FTX, db='COPIAAMARILLA'.lower(), idx='radicacion', properties=COPIAAMARILLAPRO)
classDB['COPIAAMARILLA'.lower()] = COPIAAMARILLA
__builtin__.COPIAAMARILLA = COPIAAMARILLA


class COPIAAMARILLARELATION(Base): 
    __tablename__  = 'd_copia_am_rel'
    __id__         = "id"
    
    radicado_id         = Column('radicado_id',    Unicode(50), ForeignKey('d_salida.id'), nullable=False)
    copia_am_id        = Column('copia_am_id',    Unicode(50), ForeignKey('d_copia_am.id'), nullable=False)

   # valores de control  
    id                 = Column('id', Unicode(50), default=utils.UuidStr, primary_key=True)
    status             = Column('status',      Unicode(10),  default=u'ACTIVO', index=True, nullable=False)
    _created_at        = Column('_created_at', DateTime, nullable=False, default=utils.getOnlyDateTime)
    _updated_at        = Column('_updated_at', DateTime, nullable=False, default=utils.getOnlyDateTime, onupdate=utils.getOnlyDateTime)
    _unit_code         = Column('_unit_code', Unicode(20), index=True, nullable=False, default=u'*')
    _organization_code = Column('_organization_code', Unicode(20), index=True, nullable=False, default=organization_default)
    
COPIAAMARILLARELATIONPRO = {
    'id'                : pyes_base.uuid_text,         # id del registro
    'radicado_id'       : pyes_base.uuid_text,         # id del radicado
    'copia_am_id'       : pyes_base.uuid_text,         # id del tercero referenciado        
    
    'status'            : pyes_base.base_multiple('status'),
    '_created_at'       : pyes_base.base_multiple_date('_created_at'),
    '_updated_at'       : pyes_base.base_multiple_date('_updated_at'),
    '_unit_code'        : pyes_base.base_multiple('_unit_code'),
    '_organization_code': pyes_base.base_multiple('_organization_code'),
}
fulltext.createFullDB(entity=ENTIDAD_FTX, db='COPIAAMARILLARELATION'.lower(), idx='radicacion', properties=COPIAAMARILLARELATIONPRO)
classDB['COPIAAMARILLARELATION'.lower()] = COPIAAMARILLARELATION
__builtin__.COPIAAMARILLARELATION = COPIAAMARILLARELATION

class COPIAUSUARIOS(Base):  
    __tablename__  = 'd_copia_usuarios'
    __id__         = "id"
    
    documento_id  = Column(Unicode(55), index=True, nullable=False, default=u'')
    concopia_a_id = Column(Unicode(50), ForeignKey('d_users.id'), index=True, nullable=False, default=None)
    source        = Column(Unicode(10), index=True, nullable=False, default=u'')
    leido         = Column('leido',     Integer,   nullable=False, default=0)

    fecha_recorrido = Column('fecha_recorrido', DateTime, index=True, nullable=False, default=utils.getOnlyDateTime)
    recorrido       = Column('recorrido',       Integer, index=True, nullable=False, default=0)
    impreso         = Column('impreso',         Integer, index=True, nullable=False, default=0)
    
    @property
    def documento(self):
        session    = SQLSession()
        documentodic = {}
        try:
            doc = False
            if   self.source == 'ENTRADA':                
                doc = session.query(ENTRADA).filter(ENTRADA.id == self.documento_id).one()
            elif self.source == 'SALIDA':                
                doc = session.query(SALIDA).filter(SALIDA.id == self.documento_id).one()
            elif self.source == 'INTERNO':                
                doc = session.query(INTERNO).filter(INTERNO.id == self.documento_id).one()    
            
            if doc:  
                documentodic = {'id'            : doc.id,
                                'source'        : self.source,
                                'nro_radicado'  : doc.nro_radicado,
                                'fecha_radicado': doc.fecha_radicado,
                                'asunto'        : doc.asunto,
                                }
        except:
            pass
        session.close()
        
        return documentodic       
    
    # valores de control  
    id                 = Column('id', Unicode(50), default=utils.UuidStr, primary_key=True)
    status             = Column('status',      Unicode(10),  default=u'ACTIVO', index=True, nullable=False)
    _created_at        = Column('_created_at', DateTime, nullable=False, default=utils.getOnlyDateTime)
    _updated_at        = Column('_updated_at', DateTime, nullable=False, default=utils.getOnlyDateTime, onupdate=utils.getOnlyDateTime)
    _unit_code         = Column('_unit_code', Unicode(20), index=True, nullable=False, default=u'*')
    _organization_code = Column('_organization_code', Unicode(20), index=True, nullable=False, default=organization_default)

COPIAUSUARIOSPRO = {
    'id'                : pyes_base.uuid_text,         # id del registro
    'documento_id'      : pyes_base.uuid_text,         # id del radicado
    'concopia_a_id'     : pyes_base.uuid_text,         # id del usuario referenciado        
    'source'            : pyes_base.base_multiple('source'), # tipo 'ENTRADA', 'INTERNO'
    'fecha_recorrido'   : pyes_base.base_multiple_date('fecha_recorrido'),
    'recorrido'         : pyes_base.base_text,
    'leido'             : pyes_base.base_text,
    'impreso'           : pyes_base.base_text,
    
    'documento'       : {"properties" :
                                {'id'            : pyes_base.uuid_text,
                                 'source'        : pyes_base.base_multiple('source'),
                                 'nro_radicado'  : pyes_base.base_multiple('nro_radicado'),
                                 'fecha_radicado': pyes_base.base_multiple_date('fecha_radicado'),
                                 'asunto'        : pyes_base.base_text
                                }
                        },
    # ??? FALTARIA NOMBRE DEL MEDIO PARA INDEXAR FULL
    
    'status'            : pyes_base.base_multiple('status'),
    '_created_at'       : pyes_base.base_multiple_date('_created_at'),
    '_updated_at'       : pyes_base.base_multiple_date('_updated_at'),
    '_unit_code'        : pyes_base.base_multiple('_unit_code'),
    '_organization_code': pyes_base.base_multiple('_organization_code'),
}
fulltext.createFullDB(entity=ENTIDAD_FTX, db='COPIAUSUARIOS'.lower(), idx='radicacion', properties=COPIAUSUARIOSPRO)
classDB['COPIAUSUARIOS'.lower()] = COPIAUSUARIOS
__builtin__.COPIAUSUARIOS = COPIAUSUARIOS

event.listen(COPIAUSUARIOS, 'after_update', sql_globals.after_update_listener)
event.listen(COPIAUSUARIOS, 'after_insert', sql_globals.after_insert_listener)
event.listen(COPIAUSUARIOS, 'after_delete', sql_globals.after_delete_listener) 

    
class COPIATERCEROS(Base):
    __tablename__  = 'd_copia_terceros'
    __id__         = 'id'
    
    documento_id  = Column(Unicode(55), index=True, nullable=False, default=u'')
    
    concopia_a_id = Column(Unicode(50), ForeignKey('d_tercero.id'), index=True, nullable=False, default=u'')    
    source        = Column(Unicode(10), index=True, nullable=False, default=u'')
        
    fecha_recorrido = Column('fecha_recorrido', DateTime, index=True, nullable=False, default=utils.getOnlyDateTime)
    recorrido       = Column('recorrido',       Integer, index=True, nullable=False, default=0)
    medio_id        = Column('medio_id',        Unicode(50),  ForeignKey('d_medio.id'), nullable=False, default=u'')
    
    # ??? CREAR ENLACE A TERCERO Y A MEDIO DIRECTAMENTE
    
    # valores de control  
    id                 = Column('id', Unicode(50), default=utils.UuidStr, primary_key=True)
    status             = Column('status',      Unicode(10),  default=u'ACTIVO', index=True, nullable=False)
    _created_at        = Column('_created_at', DateTime, nullable=False, default=utils.getOnlyDateTime)
    _updated_at        = Column('_updated_at', DateTime, nullable=False, default=utils.getOnlyDateTime, onupdate=utils.getOnlyDateTime)
    _unit_code         = Column('_unit_code', Unicode(20), index=True, nullable=False, default=u'*')
    _organization_code = Column('_organization_code', Unicode(20), index=True, nullable=False, default=organization_default)
    
COPIATERCEROSPRO = {
    'id'                : pyes_base.uuid_text,         # id del registro
    'documento_id'      : pyes_base.uuid_text,         # id del radicado
    'concopia_a_id'     : pyes_base.uuid_text,         # id del tercero referenciado        
    'source'            : pyes_base.base_multiple('source'), # tipo 'ENTRADA', 'INTERNO'
    'fecha_recorrido'   : pyes_base.base_multiple_date('fecha_recorrido'),
    'recorrido'         : pyes_base.base_text,
    'medio_id'          : pyes_base.uuid_text,         # id del medio
    # ??? FALTARIA NOMBRE DEL MEDIO PARA INDEXAR FULL
    
    'status'            : pyes_base.base_multiple('status'),
    '_created_at'       : pyes_base.base_multiple_date('_created_at'),
    '_updated_at'       : pyes_base.base_multiple_date('_updated_at'),
    '_unit_code'        : pyes_base.base_multiple('_unit_code'),
    '_organization_code': pyes_base.base_multiple('_organization_code'),
}
fulltext.createFullDB(entity=ENTIDAD_FTX, db='copiaterceros', idx='radicacion', properties=COPIATERCEROSPRO)
classDB['copiaterceros'] = COPIATERCEROS
__builtin__.COPIATERCEROS = COPIATERCEROS

class COPIAGRUPOS(Base):  
    __tablename__  = 'd_copia_grupos'
    __id__         = "id"
    
    documento_id  = Column(Unicode(55), index=True, nullable=False, default=u'')
    concopia_a_id = Column(Unicode(50), ForeignKey('d_grupos.id'), index=True, nullable=False, default=u'')
    source        = Column(Unicode(10), index=True, nullable=False, default=u'')
    
    # valores de control  
    id                 = Column('id', Unicode(50), default=utils.UuidStr, primary_key=True)
    status             = Column('status',      Unicode(10),  default=u'ACTIVO', index=True, nullable=False)
    _created_at        = Column('_created_at', DateTime, nullable=False, default=utils.getOnlyDateTime)
    _updated_at        = Column('_updated_at', DateTime, nullable=False, default=utils.getOnlyDateTime, onupdate=utils.getOnlyDateTime)
    _unit_code         = Column('_unit_code', Unicode(20), index=True, nullable=False, default=u'*')
    _organization_code = Column('_organization_code', Unicode(20), index=True, nullable=False, default=organization_default)

COPIAGRUPOSPRO = {
    'id'                : pyes_base.uuid_text,         # id del registro
    'documento_id'      : pyes_base.uuid_text,         # id del radicado
    'concopia_a_id'     : pyes_base.uuid_text,         # id del usuario referenciado        
    'source'            : pyes_base.base_multiple('source'), # tipo 'ENTRADA', 'INTERNO'
    
    'status'            : pyes_base.base_multiple('status'),
    '_created_at'       : pyes_base.base_multiple_date('_created_at'),
    '_updated_at'       : pyes_base.base_multiple_date('_updated_at'),
    '_unit_code'        : pyes_base.base_multiple('_unit_code'),
    '_organization_code': pyes_base.base_multiple('_organization_code'),
}
fulltext.createFullDB(entity=ENTIDAD_FTX, db='COPIAGRUPOS'.lower(), idx='radicacion', properties=COPIAGRUPOSPRO)
classDB['COPIAGRUPOS'.lower()] = COPIAGRUPOS
__builtin__.COPIAGRUPOS = COPIAGRUPOS

class PENDIENTEDIST(Base):
    __tablename__  = 'd_pen_dis'
    __id__         = "id"
    
    documento_id    = Column('documento_id',  Unicode(50),   ForeignKey('d_entrada.id'), index=True, nullable=False, default=u'')
    responsable_id  = Column('responsable_id',  Unicode(50),   ForeignKey('d_users.id'), index=True, nullable=False, default=u'')
    sent            = Column('sent',      Integer,   nullable=False, default=0)
    
    # valores de control  
    id                 = Column('id', Unicode(50), default=utils.UuidStr, primary_key=True)
    status             = Column('status',      Unicode(10),  default=u'ACTIVO', index=True, nullable=False)
    _created_at        = Column('_created_at', DateTime, nullable=False, default=utils.getOnlyDateTime)
    _updated_at        = Column('_updated_at', DateTime, nullable=False, default=utils.getOnlyDateTime, onupdate=utils.getOnlyDateTime)
    _unit_code         = Column('_unit_code', Unicode(20), index=True, nullable=False, default=u'*')
    _organization_code = Column('_organization_code', Unicode(20), index=True, nullable=False, default=organization_default)

PENDIENTEDISTPRO = {
    'id'                : pyes_base.uuid_text,         # id del registro
    'documento_id'      : pyes_base.uuid_text,         # id del radicado
    'responsable_id'    : pyes_base.uuid_text,         # id del usuario responsable
    'sent'              : pyes_base.base_integer,      # Bandera de envio
    
    'status'            : pyes_base.base_multiple('status'),
    '_created_at'       : pyes_base.base_multiple_date('_created_at'),
    '_updated_at'       : pyes_base.base_multiple_date('_updated_at'),
    '_unit_code'        : pyes_base.base_multiple('_unit_code'),
    '_organization_code': pyes_base.base_multiple('_organization_code'),
}
fulltext.createFullDB(entity=ENTIDAD_FTX, db='PENDIENTEDIST'.lower(), idx='radicacion', properties=PENDIENTEDISTPRO)
classDB['PENDIENTEDIST'.lower()] = PENDIENTEDIST
__builtin__.PENDIENTEDIST = PENDIENTEDIST

# Devoluciones 
class DEVOLUCION(Base):
    __tablename__  = 'd_devolucion'
    __id__         = "id"
    
    # datos basicos radicado    
    radicador_id        = Column('radicador_id',    Unicode(55), nullable=False, default=u'')
    radicado_en_id      = Column('radicado_en_id',  Unicode(55), nullable=False, default=u'')
    nro_radicado        = Column('nro_radicado',    Unicode(50), nullable=False )
    motivo_dev_id       = Column('motivo_dev_id', Unicode(50), ForeignKey('d_motivo_dev.id'), nullable=False, default=u'')
    r_motivo            = relationship(MOTIVODEVOLUCION, foreign_keys = [motivo_dev_id],  primaryjoin = (motivo_dev_id  == MOTIVODEVOLUCION.id))
    motivo_name         = association_proxy('r_motivo', 'name')
    
    sitio_name = association_proxy('sitio_rel', 'name')
    
    fecha_radicado      = Column('fecha_radicado',  DateTime, nullable=False, default=utils.getOnlyDateTime)
    fecha_documento     = Column('fecha_documento', DateTime, nullable=False, default=utils.getOnlyDateTime)
    referenciados       = Column('referenciados',   Unicode(150), nullable=True)
    
    # recibe informacion
    area_target_id      = Column('area_target_id',  Unicode(50),  ForeignKey('d_seccion.id'), nullable=False, default=u'')
    r_area_target       = relationship(SECCION, foreign_keys = [area_target_id],  primaryjoin = area_target_id == SECCION.id)
    area_target_name    = association_proxy('r_area_target', 'name')
    
    target_id           = Column('target_id', Unicode(50),  ForeignKey('d_users.id'), nullable=False, default=u'')    
    r_target            = relationship(USUARIO, foreign_keys = [target_id],  primaryjoin = target_id == USUARIO.id)
    target_name         = association_proxy('r_target', 'name')

    fecha_recorrido     = Column('fecha_recorrido', DateTime, nullable=False, default=utils.getOnlyDateTime)
    recorrido           = Column('recorrido',       Integer, nullable=False, default=0)
    
    # valores de control  
    id                 = Column('id', Unicode(50), default=utils.UuidStr, primary_key=True)
    status             = Column('status',      Unicode(10),  default=u'ACTIVO', index=True, nullable=False)
    _created_at        = Column('_created_at', DateTime, nullable=False, default=utils.getOnlyDateTime)
    _updated_at        = Column('_updated_at', DateTime, nullable=False, default=utils.getOnlyDateTime, onupdate=utils.getOnlyDateTime)
    _unit_code         = Column('_unit_code', Unicode(20), index=True, nullable=False, default=u'*')
    _organization_code = Column('_organization_code', Unicode(20), index=True, nullable=False, default=organization_default)    
    
    @property
    def radicado_en(self):
        session    = SQLSession()
        if (self.radicado_en_id in [None, '']):
            return ''
        else:
            q = session.query(SITIO).filter(SITIO.id == self.radicado_en_id)
            try:
                sitio = q.one()
                name  = sitio.name
            except:
                name  = ''
        session.close()
        
        return name
    
    # NOMBRE RADICADOR
    @property
    def radicado_por(self):
        session    = SQLSession()
        if (self.radicador_id in [None, '']):
            return ''
        else:
            q = session.query(USUARIO).filter(USUARIO.id == self.radicador_id)
            try:
                usuario = q.one()
                name    = usuario.name
            except:
                name  = ''
        session.close()
        
        return name
    
    @property
    def radicado_salida(self):
        session  = SQLSession()
        radicado = ''
        if (self.referenciados not in [None, '']):            
            try:
                salida   = session.query(SALIDA).filter(SALIDA.id == self.referenciados).one()            
                radicado = salida.nro_radicado                
            except Exception, e:
                pass
        
        session.close()
        
        return radicado      

DEVOLUCIONPRO = {
    'id'                : pyes_base.uuid_text,         # id del registro
    
    'radicador_id'      : pyes_base.uuid_text,         # id del radicador
    'radicado_en_id'    : pyes_base.uuid_text,         # id del sitio de radicacion
    'radicado_por'      : pyes_base.base_multiple('radicado_por'),
    'radicado_en'       : pyes_base.base_multiple('radicado_en'),
    'nro_radicado'      : pyes_base.base_multiple('nro_radicado'), # numero de radicado
    'motivo_dev_id'     : pyes_base.uuid_text,         # id del motivo de devolucion    
    'motivo_name'       : pyes_base.base_multiple('motivo_name'),
    'referenciados'     : pyes_base.base_multiple('referenciados'), # numero de radicado
    'radicado_salida'   : pyes_base.base_multiple('radicado_salida'), # numero de radicado   
    
    'fecha_radicado'    : pyes_base.base_multiple_date('fecha_radicado'),
    'fecha_documento'   : pyes_base.base_multiple_date('fecha_documento'),
    'area_target_id'    : pyes_base.uuid_text,         # id del area a devolver
    'area_target_name'  : pyes_base.base_multiple('area_target_name'),
    'target_id'         : pyes_base.uuid_text,         # id de la persona a devolver
    'target_name'       : pyes_base.base_multiple('target_name'),
    'fecha_recorrido'   : pyes_base.base_multiple_date('fecha_recorrido'),    
    'recorrido'         : pyes_base.base_integer,      # Numero de recorrido
    
    'status'            : pyes_base.base_multiple('status'),
    '_created_at'       : pyes_base.base_multiple_date('_created_at'),
    '_updated_at'       : pyes_base.base_multiple_date('_updated_at'),
    '_unit_code'        : pyes_base.base_multiple('_unit_code'),
    '_organization_code': pyes_base.base_multiple('_organization_code'),
}

event.listen(DEVOLUCION, 'after_update', sql_globals.after_update_listener)
event.listen(DEVOLUCION, 'after_insert', sql_globals.after_insert_listener)
event.listen(DEVOLUCION, 'after_delete', sql_globals.after_delete_listener)

fulltext.createFullDB(entity=ENTIDAD_FTX, db='DEVOLUCION'.lower(), idx='radicacion', properties=DEVOLUCIONPRO)
classDB['DEVOLUCION'.lower()] = DEVOLUCION
__builtin__.DEVOLUCION = DEVOLUCION

# Recorridos
class RECORRIDO(Base):
    __tablename__  = 'd_recorridos'
    __id__         = "id"
    
    # datos basicos reccorido 
    fecha_recorrido     = Column('fecha_recorrido', DateTime, nullable=False, default=utils.getOnlyDateTime)
    nro_recorrido       = Column('recorrido',       Integer, index=True, nullable=False, default=0)
    fecha_recibido      = Column('fecha_recibido',  DateTime, nullable=True)
    recibido_por        = Column('recibido_por',    Unicode(50), ForeignKey('d_users.id'), index=True, nullable=True)
    area_id             = Column('area_id',         Unicode(50), ForeignKey('d_seccion.id'), index=True, nullable=True)
    
    # Datos del radicado
    nro_radicado        = Column('nro_radicado',    Unicode(50), nullable=False )
    tipo_radicado       = Column('tipo_radicado',   Unicode(10), nullable=False)
    
    # valores de control  
    id                 = Column('id', Unicode(50), default=utils.UuidStr, primary_key=True)
    status             = Column('status',      Unicode(10),  default=u'ACTIVO', index=True, nullable=False)
    _created_at        = Column('_created_at', DateTime, nullable=False, default=utils.getOnlyDateTime)
    _updated_at        = Column('_updated_at', DateTime, nullable=False, default=utils.getOnlyDateTime, onupdate=utils.getOnlyDateTime)
    _unit_code         = Column('_unit_code', Unicode(20), index=True, nullable=False, default=u'*')
    _organization_code = Column('_organization_code', Unicode(20), index=True, nullable=False, default=organization_default)    
       
    @property
    def recibido_name(self):
        #ini = datetime.now()
        session = SQLSession()
        nombre  = ""
        try:
            usuario = session.query(USUARIO).filter(USUARIO.id == self.recibido_por).one()            
            nombre  = usuario.name                
        except Exception, e:
            #print e
            pass        
        session.close()
        #print nombre, self.recibido_por
        #print 'recibido_name:', datetime.now() - ini
        return nombre
    
    @property
    def area_name(self):
        #ini = datetime.now()
        # Area a la cual se traslado
        session = SQLSession()
        nombre  = ""
        try:
            area = session.query(SECCION).filter(SECCION.id == self.area_id).one()            
            nombre  = area.name                
        except Exception, e:
            pass        
        session.close()
        #print 'area_name:', datetime.now() - ini
        return nombre
    
    @property
    def radicado(self):
        #ini = datetime.now()
        session  = SQLSession()
    
        radicado = {}
        try:
            if (self.tipo_radicado == 'ENTRADA'):                            
                entrada  = session.query(ENTRADA).filter(ENTRADA.nro_radicado == self.nro_radicado).one()            
                radicado['fecha_radicado']     = entrada.fecha_radicado
                radicado['responsable']        = entrada.responsable_inicial
                radicado['dependencia']        = entrada.dependencia_inicial
                radicado['asunto']             = entrada.asunto
                radicado['persona_remite']     = entrada.sender
                radicado['entidad_remite']     = entrada.name
                radicado['copia_funcionarios'] = entrada.copia_funcionarios                
                
            elif (self.tipo_radicado == 'INTERNO'):
                interno  = session.query(INTERNO).filter(INTERNO.nro_radicado == self.nro_radicado).one()
                #print '1'
                radicado['fecha_radicado']     = interno.fecha_radicado
                #print '2'
                radicado['responsable']        = interno.responsable_inicial
                #print '3'
                radicado['dependencia']        = interno.dependencia_inicial
                #print '4'
                radicado['asunto']             = interno.asunto
                #print '5'
                radicado['persona_remite']     = interno.sender_universal
                #print '6'
                radicado['entidad_remite']     = interno.area_sender_name
                #print '7'
                radicado['copia_funcionarios'] = interno.copia_funcionarios                
                
        except Exception, e:
            pass
        
        session.close()
        #print 'radicado:', datetime.now() - ini, self.tipo_radicado 
        return radicado      

RECORRIDOPRO = {
    'id'                : pyes_base.uuid_text,         # id del registro
    
    'fecha_recorrido'   : pyes_base.base_multiple_date('fecha_recorrido'),
    'nro_recorrido'     : pyes_base.base_text,
    'fecha_recibido'    : pyes_base.base_multiple('fecha_recibido'),
    'recibido_por'      : pyes_base.uuid_text, 
    'recibido_name'     : pyes_base.base_multiple('recibido_name'),
    'area_id'           : pyes_base.uuid_text,
    'area_name'         : pyes_base.base_multiple('area_name'),
    
    'nro_radicado'      : pyes_base.base_multiple('nro_radicado'),  # numero de radicado
    'tipo_radicado'     : pyes_base.base_multiple('tipo_radicado'), # tipo radicado = ENTRADA, SALIDA, INTERNO
    'radicado'          : {"properties" :
                                {'fecha_radicado' : pyes_base.base_text,
                                 'responsable'    : pyes_base.base_multiple('radicado.responsable'),
                                 'dependencia'    : pyes_base.base_multiple('radicado.dependencia'),
                                 'asunto'         : pyes_base.base_text,
                                 'persona_remite' : pyes_base.base_text,                    
                                 'entidad_remite' : pyes_base.base_text,
                                 'copia_funcionarios': {"properties" :
                                        {'id'              : pyes_base.uuid_text,
                                         'name'            : pyes_base.base_text,
                                         'area_name'       : pyes_base.base_text,
                                         'sitio_name'      : pyes_base.base_text                                 
                                        }
                                  },
                                }
                           },
    
    
    
    'status'            : pyes_base.base_multiple('status'),
    '_created_at'       : pyes_base.base_multiple_date('_created_at'),
    '_updated_at'       : pyes_base.base_multiple_date('_updated_at'),
    '_unit_code'        : pyes_base.base_multiple('_unit_code'),
    '_organization_code': pyes_base.base_multiple('_organization_code'),
}

event.listen(RECORRIDO, 'after_update', sql_globals.after_update_listener)
event.listen(RECORRIDO, 'after_insert', sql_globals.after_insert_listener)
event.listen(RECORRIDO, 'after_delete', sql_globals.after_delete_listener)

fulltext.createFullDB(entity=ENTIDAD_FTX, db='RECORRIDO'.lower(), idx='radicacion', properties=RECORRIDOPRO)
classDB['RECORRIDO'.lower()] = RECORRIDO
__builtin__.RECORRIDO = RECORRIDO


# EMAILDATA registros
class EMAILDATA(Base):
    __tablename__  = 'd_email'
    __id__         = "id"
    
    id_email      = Column('id_email',      Unicode(256), index=True, nullable=False, unique = True)
    fecha_email   = Column('fecha_email',   DateTime, index=True, nullable=False, default=utils.getOnlyDateTime)
    from_email    = Column('from_email',    Unicode(256),  nullable=False)
    to_email      = Column('to_email',      Unicode(512),  nullable=False)
    cc_email      = Column('cc_email',      Unicode(512),  nullable=True, default=u'')
    subject_email = Column('subject_email', Unicode(512),  nullable=True, default=u'')
    body_email    = Column('body_email',    Unicode(1024), nullable=True, default=u'')
    filenames     = Column('filenames',     Unicode(500),  nullable=True, default=u'')
    nro_radicado  = Column('nro_radicado',  Unicode(20),   nullable=True, default=u'')
    
    # valores de control  
    id                 = Column('id', Unicode(50), default=utils.UuidStr, primary_key=True)
    status             = Column('status',      Unicode(10),  default=u'ACTIVO', index=True, nullable=False)
    _created_at        = Column('_created_at', DateTime, nullable=False, default=utils.getOnlyDateTime)
    _updated_at        = Column('_updated_at', DateTime, nullable=False, default=utils.getOnlyDateTime, onupdate=utils.getOnlyDateTime)
    _unit_code         = Column('_unit_code', Unicode(20), index=True, nullable=False, default=u'*')
    _organization_code = Column('_organization_code', Unicode(20), index=True, nullable=False, default=organization_default)    
       
EMAILDATAPRO = {
    'id'                : pyes_base.uuid_text,         # id del registro
    
    'id_email'          : pyes_base.base_text,    
    'fecha_email'       : pyes_base.base_multiple('fecha_email'),
    'from_email'        : pyes_base.base_text,
    'to_email'          : pyes_base.base_text,
    'cc_email'          : pyes_base.base_text,    
    'subject_email'     : pyes_base.base_text,    
    'body_email'        : pyes_base.base_text,    
    'filenames'         : pyes_base.base_text,
    'nro_radicado'      : pyes_base.base_multiple('nro_radicado'),
    
    'status'            : pyes_base.base_multiple('status'),
    '_created_at'       : pyes_base.base_multiple_date('_created_at'),
    '_updated_at'       : pyes_base.base_multiple_date('_updated_at'),
    '_unit_code'        : pyes_base.base_multiple('_unit_code'),
    '_organization_code': pyes_base.base_multiple('_organization_code'),
}

event.listen(EMAILDATA, 'after_update', sql_globals.after_update_listener)
event.listen(EMAILDATA, 'after_insert', sql_globals.after_insert_listener)
event.listen(EMAILDATA, 'after_delete', sql_globals.after_delete_listener)

fulltext.createFullDB(entity=ENTIDAD_FTX, db='EMAILDATA'.lower(), idx='radicacion', properties=EMAILDATAPRO)
classDB['EMAILDATA'.lower()] = EMAILDATA
__builtin__.EMAILDATA = EMAILDATA


# FAXDATA registros
class FAXDATA(Base):
    __tablename__  = 'd_faxdata'
    __id__         = "id"
    
    name           = Column('name',      Unicode(256))
    fecha_fax      = Column('fecha_fax',   DateTime, index=True, nullable=False, default=utils.getOnlyDateTime)    
    nro_radicado   = Column('nro_radicado',  Unicode(20),   nullable=True, default=u'')
    
    # valores de control  
    id                 = Column('id', Unicode(50), default=utils.UuidStr, primary_key=True)
    status             = Column('status',      Unicode(10),  default=u'ACTIVO', index=True, nullable=False)
    _created_at        = Column('_created_at', DateTime, nullable=False, default=utils.getOnlyDateTime)
    _updated_at        = Column('_updated_at', DateTime, nullable=False, default=utils.getOnlyDateTime, onupdate=utils.getOnlyDateTime)
    _unit_code         = Column('_unit_code', Unicode(20), index=True, nullable=False, default=u'*')
    _organization_code = Column('_organization_code', Unicode(20), index=True, nullable=False, default=organization_default)    
       
FAXDATAPRO = {
    'id'                : pyes_base.uuid_text,         # id del registro
    
    'name'              : pyes_base.base_text,    
    'fecha_fax'         : pyes_base.base_multiple('fecha_fax'),
    'nro_radicado'      : pyes_base.base_multiple('nro_radicado'),
    
    'status'            : pyes_base.base_multiple('status'),
    '_created_at'       : pyes_base.base_multiple_date('_created_at'),
    '_updated_at'       : pyes_base.base_multiple_date('_updated_at'),
    '_unit_code'        : pyes_base.base_multiple('_unit_code'),
    '_organization_code': pyes_base.base_multiple('_organization_code'),
}

event.listen(FAXDATA, 'after_update', sql_globals.after_update_listener)
event.listen(FAXDATA, 'after_insert', sql_globals.after_insert_listener)
event.listen(FAXDATA, 'after_delete', sql_globals.after_delete_listener)

fulltext.createFullDB(entity=ENTIDAD_FTX, db='FAXDATA'.lower(), idx='radicacion', properties=FAXDATAPRO)
classDB['FAXDATA'.lower()] = FAXDATA
__builtin__.FAXDATA = FAXDATA



