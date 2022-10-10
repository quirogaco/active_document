// #########################################
// Crear rutas de navegacion menu pricipal #
// #########################################


import { 
    createWebHashHistory,
    createRouter 
} from "vue-router"


import componentes_librerias from './componentes_librerias.js'

const creaEnrutador = function(routes) {
    const enrutador = createRouter({
        history: createWebHashHistory(),
        routes
    })    

    return enrutador
}

// Encargado de crear todas las rutas, para cada componente de perfil del usuario
// Todos los componentes deben quedar asigando a una ruta,
// pero solo los componentes de menu deben estar en la opciones de navegación
// Los que no esten en opciones de navegación seran invocados por $router.push, 
// desde otro componente.
let contador_id = 0;
const creaRutasNavegacion = function(opciones) {
    let rutas             = [];
    let navegaciones      = [];
    let navegacionesLista = [];
    let padres            = [];
    let ruta, navegacion, elemento, nombre_componente;
    for (const opcion in opciones) {
        elemento = opciones[opcion]       
        // Crea ruta
        // elemento["estructura"], valor estrutura no existe.                
        nombre_componente = elemento["componente"]
        // Si no tiene ruta, la ruta es el nombre del componente
        // Un componente puede tener diferentes rutas
        ruta              = window.$librerias.cargaAtributo(elemento, "ruta", nombre_componente)   
        let componente = componentes_librerias.crearComponenteRuta(elemento, nombre_componente, elemento["tipo"])      
        ruta = {
            path     : ("/" + ruta),   
            name     : ruta, 
            component: componente, 
            props    : true           
        }        
        rutas.push(ruta)               

        // Crea navegacion
        if (elemento["navegar"] == "si") {
            contador_id += 1;
            let id    = window.$librerias.cargaAtributo(elemento, 'id', contador_id);;
            let texto = elemento["texto"];
            let icon  = elemento["icon"];            
            let padre = elemento["padre"];  
            if (padre == undefined) {
                // Insertar elementos primer nivel
                navegacion = {
                    id  : id,
                    text: texto,
                    icon: icon,
                    path: ruta,              
                }
                navegaciones.push(navegacion)
            }
            else {
                // Insertar elementos segundo nivel
                if (padres[padre] == undefined) {
                    padres[padre] = {
                        text : padre,
                        items: []
                    }
                }
                padres[padre]["items"].push({
                    id  : id,
                    text: texto,
                    icon: icon,
                    path: ruta,               
                })
            }
        }
    }
    
    // Actualiza navegación con elementos de dos niveles primero
    for (const padre in padres) {
        const elemento = padres[padre];
        navegacionesLista.push(elemento)
    }

    // Actualiza navegación con elementos un nivel segundo
    for (const navegacion in navegaciones) {
        const elemento = navegaciones[navegacion];
        navegacionesLista.push(elemento)
    }

    let resultado = {
        ruta        : creaEnrutador(rutas),
        navegaciones: navegacionesLista
    }

    return resultado;
}

export default {
    creaRutasNavegacion: creaRutasNavegacion,
    creaEnrutador      : creaEnrutador
};