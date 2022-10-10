#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import typing, pprint, types

from sqlalchemy.orm        import object_session
from sqlalchemy            import event
from librerias.datos.sql   import sqalchemy_declarativa_base as dbase
from librerias.datos.base  import globales
from .                     import sqalchemy_tipo_campos, sqalchemy_columnas_dinamicas, sqalchemy_relaciones

# Manejo de eventos
def asigna_evento(CLASE, evento, funcion):
    event.listen(CLASE, evento, funcion)

# Imprime error y termina ejecución
def reporte_error(mensaje, imprimir):
    print("")
    print("******************************************")
    print(mensaje)
    pprint.pprint(imprimir)
    raise "ERROR ***-->"

# Valida nombre del campo
def valide_columna(clase, campo_nombre, campo_definicion):   
    campo_nombre = campo_nombre.lower()
    # Longitud
    longitud           = len(campo_nombre)
    if longitud > 30:
        reporte_error("----> CAMPO CON LONGITUD MAYOR QUE 30 ** campo: " + str(clase + " " + campo_nombre) + " - longitud:" + str(longitud), campo_definicion)

    # Nombre del campo
    error_nombre       = False
    caracteres_validos = 'abcdefghijklmnopqrstuvwxyz_'
    for letra in campo_nombre:
        if caracteres_validos.find(letra) < 0:         
            error_nombre = True
    if error_nombre == True:
        reporte_error("----> CAMPO CON NOMBRE INVALIDO ** campo: " + str(clase + " " + campo_nombre), campo_definicion)

    # Tipo de campo
    error_tipo = False
    tipo       = campo_definicion.get("tipo", "")
    error_tipo = sqalchemy_tipo_campos.diccionario_tipos.get(tipo, True)      
    if error_tipo == True:
        reporte_error("----> CAMPO CON TIPO INVALIDO ** campo: " + str(clase + " " + campo_nombre), campo_definicion)

# Valida la definición de la tabla
def valida_definicion(clase, tabla, columnas):
    for campo_nombre, campo_definicion in columnas.items():
        columna = campo_definicion.get("columna", "si")
        if columna == "si":
            valide_columna(clase, campo_nombre, campo_definicion) 

# Valida elementos basicos
def valida_basicos_clase(definicion):
    clase    = definicion.get('clase', False)
    tabla    = definicion.get('clase', False)
    columnas = definicion.get('campos', False)
    if   clase == False:
        reporte_error("----> ERROR REGISTRO DE DB CLASE, SIN **>> CLASE", definicion)

    elif tabla == False:
        reporte_error("----> ERROR REGISTRO DE DB CLASE, SIN **>> TABLA", definicion)

    elif (columnas == False) or not isinstance(columnas, typing.Dict):
        reporte_error("----> ERROR REGISTRO DE DB CLASE, SIN **>> COLUMNAS", definicion)

    return clase, tabla, columnas

def crea_relaciones_proxy():
    for clase_nombre, relaciones in CONFIGURACION_GENERAL["RELACIONES_SQL"].items():
        for relacion in relaciones:
            contenido_en = relacion.get('contenido_en', None)
            if contenido_en is None:
                externa = relacion.get('externa', None)
                if externa is None:
                    sqalchemy_relaciones.relacion_base(clase_nombre, relacion)
                else:
                    sqalchemy_relaciones.relacion_externa(clase_nombre, relacion)

# Crea relaciones a otras tablas
def prepara_relaciones_proxy(clase_nombre, referencias, columnas):        
    relaciones = []
    for referencia in referencias:
        # Campos local
        campo_referencia = referencia.get('campoReferencia', None)
        columna          = columnas.get(campo_referencia, None)
        if columna == None:
            print("")
            print("********************************************")
            print("ERROR...................")
            print(clase_nombre, " ---> REFERENCIA NO EXISTE")
            print("campo_referencia:", campo_referencia)
            print("")
            print("")            
            exit(0)

        estructura_destino = referencia.get('estructuraDestino', None)
        relacion = {
            # Datos destino
            "estructura_destino": estructura_destino,
            "campo_destino"     : referencia.get('campoDestino', 'id'),

            # Datos origen
            "campo_referencia"    : campo_referencia,
            "atributos_referencia": referencia.get('atributosReferencia', None),
            "contenido_en"        : referencia.get('contenido_en', None),
            "modo"                : referencia.get('modo', "simple"),
            "externa"             : referencia.get('externa', None)
        }
        relaciones.append(relacion)
        
    if len(relaciones) > 0:
        CONFIGURACION_GENERAL["RELACIONES_SQL"][clase_nombre] = relaciones

    return relaciones

# SERIALIZAR
def campos_serializa(columnas):
    serializar = []
    for campo_nombre, campo_definicion in columnas.items():
        serializa = campo_definicion.get("serializa", "si")
        if serializa == "si":
            serializar.append(campo_nombre)

    return serializar

def clase_serializar(clase_nombre, columnas):
    # Columnas a serializar
    CLASE       = globales.lee_clase(clase_nombre)
    
    # Serializacion actual
    __basicos__ = getattr(CLASE, "__basicos__", [])
    
    # Actualiza serializacion
    serializar  = campos_serializa(columnas)
    serializar.extend(__basicos__)
    serializar_ = dbase.serializa_base(serializar)
    setattr(CLASE, "__serialization__", serializar_)

# PROPIEDADES CON VALORES DENTRO DE CAMPOS JSON: atributos_
def crea_propiedad_no_columna(contenido_en, campo_referencia, columna_destino, columna_leer):
    # Propiedad QUERY
    def propiedad(self):
        contenedor         = getattr(self, contenido_en, {})
        columna_destino_id = contenedor.get(campo_referencia, None)
        valor              = None # deberia existir un valor defecto        
        if columna_destino_id is not None:
            valor = object_session(self).query(columna_leer).filter(columna_destino == columna_destino_id).first()
            if valor is not None:
                valor = valor[0]

        return valor

    return propiedad

def clase_propiedades_no_columna(clase_nombre):
    CLASE      = globales.lee_clase(clase_nombre)
    relaciones = CONFIGURACION_GENERAL["RELACIONES_SQL"][clase_nombre]
    for relacion in relaciones:
        #################
        # Datos destino #
        #################
        estructura_destino = relacion["estructura_destino"]
        definicion_destino = globales.lee_definicion(estructura_destino)
        CLASE_DESTINO      = globales.lee_clase(definicion_destino['clase']) # Clase
        campo_destino      = relacion["campo_destino"]                   # Campo para filtro de relación
        columna_destino    = getattr(CLASE_DESTINO, campo_destino, None) # Columna para relación

        ################
        # Datos origen #
        ################
        campo_referencia     = relacion["campo_referencia"]          # Campo local que cruza con campo destino       
        contenido_en         = relacion['contenido_en']
        atributos_referencia = relacion["atributos_referencia"]      
        modo                 = relacion["modo"]
        if contenido_en != None:
            for referencia in atributos_referencia: 
                for local, remota in referencia.items():      
                    columna_remota = getattr(CLASE_DESTINO, remota, None) # Columna para leer         
                    propiedad      = property( fget=crea_propiedad_no_columna(contenido_en, campo_referencia, columna_destino, columna_remota) )
                    setattr(CLASE, local, propiedad)
            
# PROPIEDADES
def crea_propiedad( propiedad ):    
    # Es funcion
    if isinstance(propiedad, types.FunctionType):
        return property(fget=propiedad)    

def campos_propiedades(CLASE, columnas):
    for campo_nombre, campo_definicion in columnas.items():
        propiedad = campo_definicion.get("propiedad", None)
        if (propiedad != None):
            setattr(CLASE, campo_nombre, crea_propiedad( propiedad ) )

def clase_propiedades(clase_nombre, columnas):
    CLASE = globales.lee_clase(clase_nombre)
    campos_propiedades(CLASE, columnas)

# Crea clase dinamica
def crea_clase_dinamica(clase_nombre, tabla, columnas, propiedades, definicion, clasesBase=(), extendida=True):      
    # diccionario de atributos de la clase
    atributos  = {}
    serializar = []
    
    # Creación de columnas dinamicas
    # Adiciona campos base
    if extendida == True:
        columnas.update(sqalchemy_columnas_dinamicas.campos_generales)

    for campo_nombre, campo_definicion in columnas.items():
        columna   = campo_definicion.get("columna", "si")
        propiedad = campo_definicion.get("propiedad", None)
        # Es columna sql de tabla
        if (columna == "si") and (propiedad == None):
            atributos[campo_nombre] = sqalchemy_columnas_dinamicas.crea_columna(campo_nombre, campo_definicion)

        if (propiedad != None):
            atributos[campo_nombre] = crea_propiedad( propiedad )
        
    serializar = campos_serializa(columnas)
    # Creación de diccionarios serialización
    __serialization__ = dbase.serializa(serializar)

    # Crea referencias a clases externa
    referencias = definicion.get("referencias", [])
    relaciones = prepara_relaciones_proxy(clase_nombre, referencias, columnas)
    
    if len(atributos.keys()) > 0:
        atributos['__tablename__']     = tabla
        atributos['__id__']            = "id"
        atributos['__serialization__'] = __serialization__
        atributos.update(propiedades)
        CLASE = type(clase_nombre, clasesBase, atributos)     
    else:
        reporte_error("----> ERROR DEFINICIÓN DE CLASE SIN ATRIBUTO: " + clase_nombre, columnas)

    return CLASE

# Crea clase SQLALCHEMY de manera dinamica
def crea_clase(definicion, clasesBase, extendida=True):
    clase, tabla, columnas = valida_basicos_clase(definicion)    
    valida_definicion(clase, tabla, columnas)

    # Crea clase mapeo dinamico
    propiedades = definicion.get('propiedades', {})
    CLASE       = crea_clase_dinamica(clase, tabla, columnas, propiedades, definicion, clasesBase, extendida)

    return CLASE