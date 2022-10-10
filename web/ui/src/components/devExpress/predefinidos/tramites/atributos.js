import { reactive, ref } from "vue";

import visores_atributos     from "./atributos_visuales/visores_atributos.js";
import estado_atributos      from "./atributos_visuales/estado_atributos.js";
import visores_herramientas  from "./barra_herramientas/visores_herramientas.js";
import fijas_herramientas    from "./barra_herramientas/fijas_herramientas.js";
import acciones_herramientas from "./barra_herramientas/acciones_herramientas.js";

// HERRAMIENTAS
let lista_herramientas = visores_herramientas.herramientas.concat(fijas_herramientas.acciones);
lista_herramientas = lista_herramientas.concat(acciones_herramientas.acciones);

let herramientas = {
    "barra_herramientas": {
        "items": lista_herramientas
    }
}

let ventana_emergente = {
    opciones_emergente: ref({
        visible           : false,
        emergente_key     : 0,
        componente_visible: null 
    })  
}

let atributos = {
    ...visores_atributos.visores,
    ...estado_atributos.estados,
    ...herramientas,
    ...ventana_emergente
}

export default {
    atributos: atributos
}