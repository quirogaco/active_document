import fuenteDatos                       from '../components/devExpress/remoto/fuenteDatos.js';
import componentes_llamados_crud_comunes from './componentes_llamados_crud_comunes.js';

// #####################
//         GRID        #
// #####################

// Titulo barra superior 
const tituloCrud = function(titulo) {
    let titulo_objeto = {
        location    : "left",
        locateInMenu: "never",
        text        : titulo
    }

    return titulo_objeto
}

// BOTON CREA GRID #
// Boton de creación llama formulario
const botonCrud = function(titulo, estructura, llamador, llamado, datos=null, regresar=null) {        
    let boton = {
        location    : "after",                    
        widget      : "dxButton",
        locateInMenu: "never",
        options     : {
            text       : titulo,
            type       : 'success',
            stylingMode: 'contained',
            icon       : 'add',
            onClick    : () => {                  
                // JSON.parse(JSON.stringify(datos)), pasa objeto por valor y no por referencia, asi no se modifca internamente
                // Si se pasa objeto regresa el valor del registro creado, y no el original                
                componentes_llamados_crud_comunes.llamarComponenteCrud(estructura, llamador, llamado, JSON.parse(JSON.stringify(datos)), "crear", regresar);
            }              
        }
    }

    return boton
}

// DOBLE CLICK GRID #
const dobleClickGrid = function(estructura, llamador, llamado, regresar=null) {
    
    async function dclick(e) {            
        let opcionesCarga = {
            searchExpr     : "id",
            searchOperation: "=",
            searchValue    : e.data.id
        }
        
        //componente.loadIndicatorVisible = true;    // JCR!! NO ESTA FUNCIONANDO          
        // Trarea datos del registro del GRID
        async function traeDatos() { 
            let datos = await fuenteDatos.cargaDatosConsulta(opcionesCarga, "grid", llamador, estructura);
            let resultado = datos;

            return resultado;
        }
        // JCR !! Validar error
        let datos = await traeDatos(); // datos.data es un array  
        if (datos.data.length > 0) {
            componentes_llamados_crud_comunes.llamarComponenteCrud(estructura, llamador, llamado, JSON.parse(JSON.stringify(datos.data[0])),  "modificar", regresar);   
        }
        else {
            console.log("REGISTRO NO ENCONTRADO:", estructura, e.data.id)
        }        
    }

    return dclick
}

export default {
    // Visuales GRID
    tituloCrud                  : tituloCrud,
    botonCrud                   : botonCrud, 
    dobleClickGrid              : dobleClickGrid
} 