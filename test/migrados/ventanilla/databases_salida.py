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