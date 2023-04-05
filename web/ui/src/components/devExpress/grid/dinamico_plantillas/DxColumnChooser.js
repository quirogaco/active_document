

//const complejos = {
//};

// Filtra los atributos complejos del componente
const filtra_complejos = function(atributos={}, complejos={}) {
    let simples = {};
    for (const atributo in atributos) {
        if (complejos[atributo] == undefined) {
            simples[atributo] = atributos[atributo]
        }
    }

    return simples;
};

// Plantillas y diccionarios de atributos internos del componente
const plantilla_complejos = function(atributos={}, complejos={}) {
    let internos_data = {};
    let funcion, complejo;
    for (const atributo in atributos) {
        funcion = complejos[atributo];
        if (funcion !== undefined) {
            complejo = funcion(atributos[atributo]);
            internos_data[atributo] = complejo;
        }
    }

    return internos_data;
};

const plantilla = function(atributos) {
    // Plantillas y diccionarios de atributos complejos
    let complejos_data     = plantilla_complejos(atributos);
    // filtrar atributos complejos
    let atributos_simples = filtra_complejos(atributos);

    console.log("complejos_data:", complejos_data, "- atributos_simples:", atributos_simples)
};

export default {
    plantilla: plantilla
}