import basicos      from './basicos.js'
import eventos      from './eventos.js'
import validaciones from './validaciones.js'

const archivo = function(id, atributos) {
    let titulo        = $librerias.cargaAtributo(atributos, 'titulo', "")
    let eventos_campo = eventos.eventos(atributos)
    let validadores   = validaciones.validaciones(atributos)
    
    let editorOptions = {
        "accept"               : $librerias.cargaAtributo(atributos, 'aceptar', []),
        "allowedFileExtensions": $librerias.cargaAtributo(atributos, 'extensiones', []),
        "disabled"             : $librerias.cargaAtributo(atributos, 'habilitado', false),
        'height'               : $librerias.cargaAtributo(atributos, 'alto',  undefined),
        "hint"                 : $librerias.cargaAtributo(atributos, 'ayuda', titulo),  
        "labelText"            : $librerias.cargaAtributo(atributos, 'soltar_titulo', "Soltar archivo aqui"),  
        "maxFileSize"          : $librerias.cargaAtributo(atributos, 'tamano_maximo', 0),  
        "minFileSize"          : $librerias.cargaAtributo(atributos, 'tamano_minimo', 0),  
        "multiple"             : $librerias.cargaAtributo(atributos, 'multiple', false),  
        'readOnly'             : $librerias.cargaAtributo(atributos, 'lectura', false),
        "selectButtonText"     : $librerias.cargaAtributo(atributos, 'selecciona_titulo', "Seleccionar archivo"),
        "showFileList"         : $librerias.cargaAtributo(atributos, 'mostrar_lista', true),
        "uploadCustomData"     : $librerias.cargaAtributo(atributos, 'data_personalizada', {}),
        "uploadMethod"         : $librerias.cargaAtributo(atributos, 'metodo_carga', "POST"),
        "uploadMode"           : $librerias.cargaAtributo(atributos, 'modo_carga', "useButtons"), // css que oculta boton, debe estar
        "uploadUrl"            : $librerias.cargaAtributo(atributos, 'direccion_carga', "/"),
        "allowCanceling"       : $librerias.cargaAtributo(atributos, 'cancelar', true),
        'value'                : $librerias.cargaAtributo(atributos, 'valor', []),
        'width'                : $librerias.cargaAtributo(atributos, 'ancho',  undefined),
        'elementAttr'          : {
            "autocomplete": "off"
        }
    }
    let opciones_totales = Object.assign(editorOptions, eventos_campo)

    let campo = {
        'dataField'      : id,
        'editorType'     : "dxFileUploader",
        'label'          : basicos.label(atributos),  
        'itemType'       : 'simple',
        'name'           : $librerias.cargaAtributo(atributos, 'nombre', id),
        'visible'        : $librerias.cargaAtributo(atributos, 'visible', true),  
        'editorOptions'  : opciones_totales,
        "validationRules": validadores
    }

    return campo
}

export default {
    campo: archivo
}