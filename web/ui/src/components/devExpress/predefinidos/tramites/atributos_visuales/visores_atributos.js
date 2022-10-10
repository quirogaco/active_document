import { reactive, ref } from "vue";

// ************************ //
// VISORES DATOS, PDF, WORD //
// ************************ //
let visores = {
    // Contenedor datos formulario
    atributos_datos: reactive({
        id   : "visor_formulario",
        class: "col-sm shadow-sm p-3 mb-1 border border-2 rounded vh-80",
        show : true,
    }),

    // *******************
    // Contenedor visor pdf
    atributos_pdf: reactive({
        id   : "visor_pdf",
        class: "col-sm shadow-sm p-3 mb-1 border border-2 rounded vh-80",
        show : true
    }),

    // Visor PDF
    visor_pdf   : ref(),
    repintar_pdf: 0,
    pdf_existe  : false,   
    opciones_pdf: {
        nombrePdf: "mmmm.pdf"
    },

    // *********************
    // Contenedor editor word
    atributos_borrador: reactive({
        id   : "visor_borrador",
        class: "col-sm shadow-sm p-3 mb-1 border border-2 rounded vh-80",
        show : true
    }),

    // Borrador word
    repintar_onlyoffice: 0,
    borrador_existe    : false,
    opciones_editor: {
        documento: {
            lectura_url: "word"
        }
    }
}

export default {
    visores: visores
}