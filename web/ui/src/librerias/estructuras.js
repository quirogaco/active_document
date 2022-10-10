
import fuenteDatos  from '../components/devExpress/remoto/fuenteDatos.js';

async function leer_registro_id(estructura, id, componente="grid") {          
    let opcionesCarga = {
        searchExpr     : "id",
        searchOperation: "=",
        searchValue    : id
    }
    
    // Trarea datos del registro del GRID
    async function traeDatos() { 
        let datos = await fuenteDatos.cargaDatosConsulta(opcionesCarga, componente, null, estructura);
        let resultado = datos;

        return resultado;
    }
    
    let datos = await traeDatos();
    if (datos.data.length > 0) {
        datos = JSON.parse(JSON.stringify(datos.data[0]))
    }
    else {
        console.log("REGISTRO NO ENCONTRADO:", estructura, id)
    }

    return datos;
}

export default {
    leer_registro_id: leer_registro_id
}