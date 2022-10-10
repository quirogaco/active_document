import { reactive, ref } from "vue";

let estados = {
    tramite_detalle: "Certificado de notas - Asignación", 
    tramite_inicio: (new Date()).toDateString(), 
    tramite_estado_terminos: "En terminos",
    tramite_dias_transcurridos: 13,
    tramite_dias_vencer: 5,
    tramite_vence_en: (new Date()).toDateString()
}

export default {
    estados: estados
}