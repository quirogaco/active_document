#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import sqlalchemy 

from librerias.datos.sql  import sqalchemy_declarativa_base as dbase
from librerias.utilidades import basicas  
from .                    import sqalchemy_tipo_campos

# Tipos de columna
columnas_tipo = {
    'texto'  : sqlalchemy.Unicode,
    'fecha'  : sqlalchemy.DateTime,
    'entero' : sqlalchemy.Integer,
    'json'   : dbase.json.JSONType
}

# Valores por defecto
columnas_valor_defecto = {
    'fecha_hora': basicas.fechaHora,
    'uuid'      : basicas.uuidTexto,
    'entero'    : 0,
    'texto'     : u"",
    'json'      : {}
}

# Crea columna dinamica
def crea_columna(campo_nombre, campo_definicion):   
    """
        titulo     : comment
        obligatorio: "no",

    ->'tipo'         : 'unicode',
    ->'longitud'     : 20,
    ->'defecto'      : 'organizacion', // default=u''
    ->'actualiza'    : 'fecha_hora', // onupdate
    ->'obligatorio'  : 'no', // nullable=True, 
    ->'indexado      : 'si', // index=True, 
    ->'llavePrimaria': 'si', // primary_key=True
    ->'titulo'       : '', // comment
    ->'unico'        : 'si', // unique=True
    
    """   
    # diccionario de atributos del campo
    atributos = {}

    # Columna sqlalchemy
    columna = columnas_tipo[ campo_definicion['tipo'] ]

    # longitud
    longitud = campo_definicion.get('longitud', 0) 
    if longitud > 0:
        tipo = columna(longitud) 
    else:
        tipo = columna

    # default: valor por defecto cuando crea
    defecto = campo_definicion.get('defecto', False)
    if defecto != False:
        if not callable(defecto):
            # Si no existe valor por key defecto, el valor es defecto
            valor                = columnas_valor_defecto.get(str(defecto), defecto)
            atributos['default'] = valor
        else:
            atributos['default'] = defecto

    # onupdate: valor por defecto cuando actualiza
    actualiza = campo_definicion.get('actualiza', False)
    if actualiza != False:
        if not callable(actualiza):
            # Si no existe valor por key actualiza, el valor es actualiza
            valor                = columnas_valor_defecto.get(str(actualiza), actualiza)
            atributos['onupdate'] = valor
        else:
            atributos['onupdate'] = actualiza
    
    # obligatorio: si permite nulos
    obligatorio = campo_definicion.get('obligatorio', "no")
    if obligatorio == "si":
        atributos['nullable'] = False

    # indexado: si se indexa
    indexado = campo_definicion.get('indice', "no")
    if indexado == "si":
        atributos['index'] = True

    # primary_key: si es llave primaria
    llavePrimaria = campo_definicion.get('llavePrimaria', "no")
    if llavePrimaria == "si":
        atributos['primary_key'] = True

    # unique: si es llave primaria
    unico = campo_definicion.get('unico', "no")
    if unico == "si":
        atributos['unique'] = True

    # titulo
    titulo = campo_definicion.get('titulo', '') 
    if titulo != "":
        atributos['comment'] = titulo

    columna = sqlalchemy.Column(campo_nombre, tipo, **atributos)
    
    return columna

#######################
# Campos predefinidos #
#######################

id_ = sqalchemy_tipo_campos.id({
    'llavePrimaria': 'si', 
    'sistema'      : 'si'
})

estado_  = sqalchemy_tipo_campos.texto_obligatorio({
    'titulo'  : 'Estado', 
    'longitud': 20, 
    'defecto' : 'ACTIVO', 
    'indice'  : 'si', 
    'sistema' : 'si'
})

creado_en_ = sqalchemy_tipo_campos.fecha_obligatorio({
    'titulo' : 'Fecha de creación', 
    'indice' : 'si', 
    'sistema': 'si'
})

actualizado_en_ = sqalchemy_tipo_campos.fecha_obligatorio({
    'titulo' : 'Fecha de actualización', 
    'indice' : 'si', 
    'sistema': 'si'
})

codigo_unidad_ = sqalchemy_tipo_campos.texto_obligatorio({
    'titulo'  : 'Unidad', 
    'longitud': 20, 
    'defecto' : '*', 
    'indice'  : 'si', 
    'sistema' : 'si'
})

codigo_organizacion_ = sqalchemy_tipo_campos.texto_obligatorio({
    'titulo'  : 'Organización', 
    'longitud': 20, 
    'defecto' : '*', 
    'indice'  : 'si', 
    'sistema' : 'si'
})  

# Campos generales por tabla
campos_generales = {
    'id'                  : id_,
    'estado_'             : estado_,
    'creado_en_'          : creado_en_,
    'actualizado_en_'     : actualizado_en_,
    'codigo_unidad_'      : codigo_unidad_,
    'codigo_organizacion_': codigo_organizacion_
}