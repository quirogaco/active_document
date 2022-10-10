import { DxFilterPanelTexts } from 'devextreme-vue/tree-list';
import notify from 'devextreme/ui/notify'

import librerias from '../../../../../librerias/librerias.js';

let montar_componente = function(componente) {
    const montar = function() {
        this.elemento       = componente
        this.forma          = this.$refs.forma.instance
        this.barra          = this.$refs.barra.instance
        this.notify         = notify
    }

    return  montar 
}

let metodos = {
    accion_retorno: function() {
        if (window.$ventana_emergente_archivos != undefined) {
            window.$ventana_emergente_archivos.opciones.visible = false
        }
    },
    
    retorna: function(parametros) {     
        this.indicador_visible = false;
        let mensaje = this.opciones.atributos.mensaje_retorno;
        this.notify(mensaje, "success");
        this.accion_retorno();       
    },

    boton_click(e) {
        let valido = this.forma.validate().isValid
        let datos  = this.forma.option("formData")
        if ( valido == true) {
            let parametros = {
                datos : datos,
                accion: "salvar_archivo"
            }               
            let urlCompleta        = window.$direcciones.servidorDatos + '/especifico_acciones'   
            this.indicador_visible = true 
            window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna, "")               
        }
        else {
            this.notify("Archivo(s) obligatorio", "error")     
        }
        
    },

    asigna_propiedades(propiedades) {
        this.propiedades = propiedades
    },

    'cargar_label':  function() {
        let atributos = this.opciones.atributos
        let label = librerias.cargaAtributo(atributos, "label", "Archivos")
        
        return label
    },

    'cargar_opciones':  function() {
        let atributos = this.opciones.atributos
        let opciones = {  
            //uploadMode           : "useButtons",
            multiple             : librerias.cargaAtributo(atributos, "multiple", false),
            //allowedFileExtensions: librerias.cargaAtributo(atributos, "permitidos", null),  
            allowedFileExtensions: [".pdf"],
            width                : "600px",
            height               : "150px"
        }
        
        return opciones
    },
}

let barra_botones = function(forma) {
    return  [       
        { 
            widget  : "dxButton",           
            options :{ //0
                icon       : 'fas fa-plus-square',
                hint       : 'salvar',
                type       : 'success',
                text       : forma.opciones.atributos.titulo_boton, 
                onClick    : forma.boton_click,
            } 
        }
    ]              
}

export default {
    metodos          : metodos,
    barra_botones    : barra_botones,
    montar_componente: montar_componente
}