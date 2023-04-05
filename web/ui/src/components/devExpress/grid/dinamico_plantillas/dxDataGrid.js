import atributos_validacion      from '../../librerias/atributos_validacion.js';
import plantillas                from '../../plantillas/plantillas.js';
import atributos_DxColumnChooser from './atributos_DxColumnChooser.js';

const complejos = {
    "columnChooser": {
        componente: "DxColumnChooser",
        atributos : atributos_DxColumnChooser
    },

    "columns": {
        componente: "DxColumn",
        atributos : []
    },

};

const genera_plantilla = function(atributos) {
    // filtrar atributos complejos
    let atributos_simples = atributos_validacion.filtra_complejos(atributos, complejos);

    // Nombres, id y ruta del componente
    let idNombre = atributos_validacion.idNombre(atributos_simples, atributos);

    // Asigna nombre y id del elemento para definición de componente
    atributos_validacion.componenteAtributos(atributos_simples, idNombre);

    // Valores globales que se necesitan para configurar y manipular desde la forma
    atributos.idComponente = idNombre.id;
    atributos.id_original  = idNombre.id_original;

    // Limpiar atributos
    let nuevos_atributos = atributos_validacion.valida_atributos("dxDataGrid", {}, atributos_simples);

    // Genera texto interno grilla
    let textoInterno = plantillas.plantillaDosPuntosDiccionario(nuevos_atributos, idNombre.id_original, "");

    // Genera texto cuerpo complejos
    let complejo_data = plantillas.plantilla_complejos(atributos, complejos);
    let textoCuerpo   = atributos_validacion.unifica_complejos_texto(complejo_data);

    // Genera diccionario complejos   
    let diccionario_base = atributos_validacion.unifica_complejos_diccionario(complejo_data);
    
    // Genera diccionario grilla
    let diccionario_grilla = plantillas.diccionarioComponente(nuevos_atributos);

    // Genera plantilla y diccionario total
    let texto       = plantillas.plantillaCompleta("DxDataGrid", textoInterno, textoCuerpo);
    let diccionario = Object.assign(diccionario_grilla, diccionario_base);
    
    return {
        "texto"      : texto,
        "diccionario": diccionario
    }
};

export default {
    genera_plantilla: genera_plantilla,

}