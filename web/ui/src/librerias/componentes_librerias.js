
import solicitar_servicios from './solicitar_servicios.js'
import rutas_predefinidos  from '../rutas/rutas_predefinidos.js'
import grid_prepara        from '../components/devExpress/grid/utilidades/grid_prepara.js'
import forma_prepara       from '../components/devExpress/forma/utilidades/forma_prepara.js'

// Traer un componente ya creado
const traeComponente = function(nombre_componente) {
    let componente = window._APLICACION_.component(nombre_componente);
    
    return componente;
};

// Crear componente
// La funcion de creacion de componente es la encargada de publicar el componente
// con app.component
const crearComponente = function(tipo, configuracion) {
    let funcion    = window.$componentes[tipo];
    let componente = funcion.creaComponente(configuracion);

    return componente;
};

// Crear componente basado en definición publicada, 
// Luego lo recupera y retorna el componente VUE. 
const crearComponenteDefinicion = function(idComponente) {
    let definicion = window.$componentesDef[idComponente];
    crearComponente(definicion.tipo, definicion);
    let componente = traeComponente(idComponente)

    return componente;
};

// Carga la definicion del componente en diccinario global
const cargaComponenteDefinicion = function(idComponente, definicion) {
    window.$componentesDef[idComponente] = definicion;
};

// Crear componente con informacion de ruta
const crearComponenteRuta = function(elemento, idComponente, importar="") {      
    let componente = null;     
    if (importar == "importar") {
        componente = rutas_predefinidos.rutas_componentes[idComponente]
    }
    else {    
        //console.log("crearComponenteRuta", elemento, idComponente, importar)
        componente = null;
        let definicion = solicitar_servicios.cargarDefinicion(elemento["clase"] , elemento["componente"])
        if (elemento["clase"] == "grid") {
            componente =  grid_prepara.grid_prepara(definicion) 
        }
        
        if (elemento["clase"] == "forma") {
            componente =  forma_prepara.forma_prepara(definicion) 
        }        
    }    

    return componente;
};

export default {
    cargaComponenteDefinicion: cargaComponenteDefinicion,
    traeComponente           : traeComponente,
    crearComponente          : crearComponente,
    crearComponenteDefinicion: crearComponenteDefinicion,
    crearComponenteRuta      : crearComponenteRuta
} 