import ArrayStore from 'devextreme/data/array_store'
import DataSource from 'devextreme/data/data_source'

function check_string(x) {
    return x.every(i => (typeof i === "string"));
}

const fuente_arreglo = function(datos, key="id") {        
    if (check_string(datos) == true) {
        datos = datos.map(function(text) {
            return {
                "id"    : text,
                "nombre": text
            }
         });
    };

    // Tienda de datos
    const tienda = new ArrayStore({
        'key' : key,
        'data': datos
    })

    // Fuente de datos
    let fuente = new DataSource({
        store: tienda
    })

    return fuente
}

const fuente_datos = function(tipo, atributos, filtros=[], eventos=[]) {
    let fuente = null;
    let key = $librerias.cargaAtributo(atributos, 'valor_expresion',"id");
    let fuente_definicion = $librerias.cargaAtributo(atributos, 'fuente', []); 
    let fuente_orden = $librerias.cargaAtributo(atributos, 'fuente_orden', []);    

    if ( Array.isArray(fuente_definicion) ) {
        fuente = fuente_arreglo(fuente_definicion, key);
    }
    else {
        fuente = $sistema["fuenteDatos"].creaFuenteDatosConsulta(
            tipo, 
            null, 
            fuente_definicion, 
            fuente_definicion, 
            filtros, 
            eventos, 
            fuente_orden
        );
    }

    return fuente
}

export default {
    fuente_arreglo: fuente_arreglo,
    fuente_datos  : fuente_datos
}