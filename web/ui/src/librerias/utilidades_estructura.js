import fuenteDatos from '../components/devExpress/remoto/fuenteDatos.js';

// Leer registro remoto por id
async function leer_registro_id(estructura, id=null, regresar=null) {
    let datos = null;                  
    let opcionesCarga = {
        searchExpr     : "id",
        searchOperation: "=",
        searchValue    : id
    }
    
    async function traeDatos() { 
        let resultado = await fuenteDatos.cargaDatosConsulta(opcionesCarga, "", null, estructura);
        if (resultado.length > 0) {
            resultado = resultado[0]  
        }
        else {
            console.log("REGISTRO NO ENCONTRADO:", estructura, id);
            resultado = null;
        }  
        
        return resultado;
    }
    
    if (id != null) {
        datos = await traeDatos(); // datos.data es un array 
    }

    return datos
}

export default {
    leer_registro_id: leer_registro_id
} 