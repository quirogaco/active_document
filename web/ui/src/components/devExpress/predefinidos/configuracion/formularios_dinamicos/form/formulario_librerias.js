import { on }             from 'devextreme/events'; 
import visores_archivo    from '../../../../../../librerias/visores_archivo.js';
import campos_constructor from './campos_constructor.js'

// Calcula la posicion del item que se acaba de soltar sobre la forma
const calcula_posiciones = function(forma, drop_x, drop_y) {
    let distancia = 999999;
    let posicion  = -1;
    let sobre     = false;
    for (const indice in forma.campos) { 
        let campo           = forma.campos[indice];
        let elemento_actual = document.getElementById(campo.uuid).getBoundingClientRect();  
        const x2 = elemento_actual.x + elemento_actual.width;
        const y2 = elemento_actual.y + elemento_actual.height;
        const x_distancia = drop_x - x2;
        const y_distancia = drop_y - y2;

        const distancia_actual = Math.sqrt(
            (x_distancia * x_distancia) + (y_distancia * y_distancia)
        )

        if (distancia_actual < distancia ) {
            sobre       = false;
            posicion    = indice;
            distancia   = distancia_actual;
            const ancho = elemento_actual.x + elemento_actual.width;
            const alto  = elemento_actual.y + elemento_actual.height;
            if ( (drop_x > elemento_actual.x ) &&  (drop_x < ancho ) ) {
                if ( (drop_y > elemento_actual.y ) &&  (drop_y < alto ) ) {
                    sobre = true
                }
            }
        }
    }    
    
    return {"distancia": distancia, "posicion": posicion, "sobre": sobre}
}

// Drop forma, cuando se suelta un elemento sobre la forma
const drop_forma = function(forma) {
    let forma_elemento = document.getElementById("constructor_forma_id")   

    on(
        forma_elemento, 
        "dxdrop", 
        { value: "SOBRE LA FORMA" }, 
        function (event, extraParameters) {
            let nombre_origen = event.draggingElement.id;
            let datos = calcula_posiciones(forma, event.screenX, event.screenY);            
            if (nombre_origen.search("_contiene_") > -1) {                
                campos_constructor.campo_mover(forma, nombre_origen, datos)
            }
            else {
                campos_constructor.campo_insertar(forma, datos)
            }   
        }
    )
}

//#####################//
// Componentes archivo //
//#####################//
let columnas = [
    {
        'dataField': 'detalle',
        'caption'  : 'Descripción',
        'width'    : 550,
    },
    {
        'dataField': 'tipo_archivo',
        'caption'  : 'Tipo',
        'width'    : 50,
    },
    {
        'dataField': 'creado_en_',
        'caption'  : 'Creado en',
        'width'    : 150,
    },     
    {
        'dataField': 'tamano',
        'caption'  : 'Tamaño bytes',
        'width'    : 100,
    },     
    {
        'dataField': 'folios',
        'caption'  : 'Folios',
        'width'    : 60,
    },  
    {
        'dataField': 'creado_por_nombre',
        'caption'  : 'Creado por',
        'width'    : 300,
    },     
];

let eventos = {
    'fila_doble_click':  function(e) {
        visores_archivo.ver_descarga_archivo({
            titulo_general: "Consulta de Anexos",
            archivo_id    : e.data.id, 
            tipo_documento: e.data.tipo_archivo, 
            titulo        : e.data.detalle,
            modo          : "leer",
            descarga      : 'evaluar'
        })               
    } 
};

// Lista de anexos del radicado
let grid_archivos = {
    'tipo'         : 'grid',
    'id'           : 'archivos',
    'modo'         : 'grid',
    'titulo'       : '',
    'registrar'    : 'si',
    'ajustaPalabra': 'si',
    'columnas'     : columnas,
    'eventos'      : eventos
};

let grupo_archivos = {
    'tipo'     : 'grupo',
    'titulo'   : 'Documento y anexos',
    'elementos': [
        grid_archivos
    ]
};

//####################//
// Crea item consulta //
//####################//
const item_informacion = function(campo, consulta=false) {
    let definicion = {
        "componente" : "campo", 
        "tipo"       : campo._tipo,               
        "id"         : campo.dataField,                
        "titulo"     : campo.label.text, 
        "obligatorio": campo.isRequired
    }
    switch (campo._tipo) {
        case "texto":
            break
        
        case "correo":
            break

        case "texto_area":
            break

        case "entero": 
            break

        case "fecha":            
            definicion.tipo_fecha = campo.editorOptions.type;
            definicion.formato    = campo.editorOptions.dateSerializationFormat;                             
            break
                        
        case "chequeo":
            definicion.valor = campo.editorOptions.text;         
            break

        case "radio":
            definicion.fuente = campo.editorOptions.items;   
            break

        case "seleccion":
            definicion.fuente = campo.editorOptions.items;   
            break

        case "etiqueta":
            definicion.fuente = campo.editorOptions.items;   
            break                        

        case "archivo":
            definicion.multiple = true;  
            break                
    }
    definicion["lectura"] = consulta; 

    return definicion;
};

const items_consulta = function(definiciones, consulta=false) {   
    // Campos de datos
    let campos_datos = [];
    let definicion   = {};
    for (const indice in definiciones) { 
        let campo  = definiciones[indice];            
        definicion = item_informacion(campo, consulta);
        if (campo._tipo != "archivo") {
            campos_datos.push(definicion);
        }
    };

    let grupo_datos = {
        'tipo'     : 'grupo',
        'titulo'   : 'Datos',
        'elementos': campos_datos
    };

    return [grupo_datos, grupo_archivos];
};

export default {   
    drop_forma    : drop_forma,
    items_consulta: items_consulta
}