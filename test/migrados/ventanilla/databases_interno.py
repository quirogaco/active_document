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
                                                                                