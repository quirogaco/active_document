import librerias            from '../../../../librerias/librerias.js'
import librerias_forma      from './librerias.js'
import forma_generador_crud from '../dinamico_parametros/forma_generador_crud.js'

// Simple item
import grupo_objeto         from './grupo_objeto.js'
import tab_panel_objeto     from './tab_panel_objeto.js'
import tab_objeto           from './tab_objeto.js'
import campo_objeto         from './campo_objeto.js'
import select_objeto        from './select_objeto.js'
import tag_objeto           from './tag_objeto.js'
import radio_objeto         from './radio_objeto.js'
import archivo_objeto       from './archivo_objeto.js'
import campos_mostrar       from './campos_mostrar.js'

// Plantillas
import contenido_objeto     from './contenido_objeto.js'

// Boton item
import boton_objeto         from './boton_objeto.js'

// Define y crea grid FORMA por atributos
const forma_objeto_crud = function(atributos={}) {
    let estructura   = librerias.cargaAtributo(atributos, "estructura",     "SIN_ESTRUCTURA")  
    let idForma      = librerias.cargaAtributo(atributos, "id",             "forma")   
    let titulo       = librerias.cargaAtributo(atributos, "titulo",         "SIN_TITULO")      
    let tipofuente   = librerias.cargaAtributo(atributos, "tipofuente",     "remota")
    let campos       = librerias.cargaAtributo(atributos, "campos",         [])
    let botones      = librerias.cargaAtributo(atributos, "botones",        {})
    let columnas     = librerias.cargaAtributo(atributos, "columnas",       1)
    let ancho        = librerias.cargaAtributo(atributos, 'ancho', "100%");
    let metodos      = librerias.cargaAtributo(atributos, "metodos",        {})
    let nombre_forma = librerias.cargaAtributo(atributos, "nombre_forma", null)
    let plantillaAtributos = librerias.cargaAtributo(atributos, "plantillaAtributos", {})
    let eventos           = window.$librerias.cargaAtributo(atributos, 'eventos', {}); 

    let lectura    = librerias.cargaAtributo(atributos, "lectura",       "no")
    lectura = lectura == "si" ? true : false;

    if (nombre_forma == null) nombre_forma = estructura + "_forma"
    let barraVisible = librerias.cargaAtributo(atributos, "barraVisible", true)
    let elementosBarra = window.$f.componentes_llamados_crud.botonesForma(nombre_forma, botones)

    // Definición FORMA
    let definicion = {
        'ruta'          : estructura,
        'id'            : idForma,
        'nombre_forma'  : nombre_forma,
        'lectura'       : lectura,
        'titulo'        : titulo,
        'fuente'        : estructura,
        'tipofuente'    : tipofuente,
        'campos'        : campos,
        'elementosBarra': elementosBarra,
        'barraVisible'  : barraVisible,
        "metodos"       : metodos,
        "columnasForma" : columnas,
        "ancho"         : ancho,
        "plantillaAtributos": plantillaAtributos,
        "eventos"       : eventos
    }

    let componente = forma_generador_crud.creaComponente(definicion);

    return componente;
}

export default {
    forma_objeto_crud: forma_objeto_crud,
    grupo_objeto     : grupo_objeto.grupo_objeto,
    tab_panel_objeto : tab_panel_objeto.tab_panel_objeto,
    tab_objeto       : tab_objeto.tab_objeto,    

    // Simple item
    campo_objeto     : campo_objeto.campo_objeto,
    select_objeto    : select_objeto.select_objeto,
    tag_objeto       : tag_objeto.tag_objeto,
    radio_objeto     : radio_objeto.radio_objeto,
    archivo_objeto   : archivo_objeto.archivo_objeto,

    // Plantillas
    contenido_objeto : contenido_objeto.contenido_objeto,

    // Boton item
    boton_objeto    : boton_objeto.boton_objeto,

    // Librarias
    plantillaAtributos: librerias_forma.plantillaAtributos,

    // Mostrar datos
    mostrar_datos: campos_mostrar.mostrar_datos
}