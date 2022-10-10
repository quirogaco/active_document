import campos_constructor   from './campos_constructor.js';
import formulario_librerias from './formulario_librerias.js';
import fuente               from "../../../comunes_vue/forma/fuente.js";

// Retorna a llamador
const retorna_grid = function() {
    $lib.llamar_componente("formularios_dinamicos_grid", {});
}

// Retorna de envio post de datos
const retorna_envio = function(retorna_datos) {
    retorna_grid();
}

const enviar_datos = function(forma, modo) {
    let campos = forma.campos;
    let validacion = forma.forma_datos.validateData();
    if (validacion.isValid == true) {
        if ( (campos.length > 0) || (modo == "borrar") ) {
            // Parametros 
            let datos = validacion.formData;
            datos["diseno"] = campos;
            let parametros = {
                "datos" : datos,
                "accion": modo
            }
            $forma.envio_accion_notifica("formularios_dinamicos", parametros, retorna_envio)               
        }
        else {
            $notify("Forma dinamica sin campos", "warning")   
        }
    }    
}

// JCR ELIMINAR
import temporal_campos from './temporal_campos.js';
let datos_formulario = {};

let metodos = {
    // ***********************//
    // Metodos forma de datos //
    // ***********************//
    // Funcion llamada por evento mounted DataForma base 
    async dataBaseFormaMounted(DataForma) {},

    forma_datos_lista(objeto) {},

    // *********************//
    // Metodos forma diseño //
    // *********************//
    forma_lista(objeto) {},

    // metodos para diseño/prevista
    en_definicion() {
        return (this.definicion == true)
    },

    en_prevista() {
        return (this.prevista == true)
    },

    // Borrar esto JCR!!
    is_viewer() {
        return (this.viewer == true)
    },

    // Borrar esto JCR!!
    async viewer_mounted(DataForma) {       
        DataForma.repaint();
        DataForma.formData(datos_formulario);       
        // Archivos
        let archivos      = datos_formulario['archivos'];
        let fuente_anexos = fuente.fuente_arreglo(archivos);
        $forma.asigna_fuente(DataForma.instance, "archivos", fuente_anexos);  
    },

    // Funcion llamada por evento mounted DataForma
    async dataFormaMounted(DataForma) {
        window.$forma_prevista = DataForma;   
        window.$forma_prevista.repaint();
        window.$forma_prevista.formData(datos_formulario);
        // Archivos
        let archivos      = datos_formulario['archivos'];
        let fuente_anexos = fuente.fuente_arreglo(archivos);
        $forma.asigna_fuente(DataForma.instance, "archivos", fuente_anexos);               
    },

    // Bara botones
    async click_botones(e, modo) {
        switch (modo) {
            case "consulta":  
                // Datos de consulta                 
                let datos = await $lib.leer_registro_id("datos_formularios_dinamicos", "83a9639d-aef6-11ec-8bb7-086266b539c1");
                datos_formulario = datos["actuales"];
                datos_formulario['archivos'] = datos['archivos'];  
               
                this.definicion = false;
                this.prevista = false;

                // Muestra forma                
                let definiciones = temporal_campos.campos;
                let campos = formulario_librerias.items_consulta($lib.clone(definiciones));                
                this.viewer_attributes.items = campos;
                this.viewer_attributes.formData = datos_formulario;
                this.viewer_attributes.colCount = 1;
                this.viewer = true;
                this.viewer_key += 1;  
                break;

            case "prevista":
                this.prevista = !this.prevista;
                if (this.prevista) {
                    datos_formulario = {};
                    let campos = formulario_librerias.items_consulta(this.campos);               
                    this.atributos_forma.items = campos;
                    this.prevista_key = this.prevista_key + 1;
                    e.component.option("text", "Diseño formulario");                                                           
                }
                else {
                    e.component.option("text", "Prevista formulario");                    
                }
                break;

            case "regresar":
                retorna_grid();
                break;
            
            default:
                enviar_datos(this, modo);
        }  
    },

    calcula_forma_tamano() {
        let clase_base = "container-fluid border border-2 p-1 col-sm-";
        let columnas   = 7;
        // Si muestra tipos de campos
        if (this.muestra_elementos == false) columnas += 2;
        // Si muestra atributos de campos
        if (this.muestra_atributos == false) columnas += 3;
        this.clase_forma = (clase_base + columnas);
    },

    // Asigna eventos drag-drop a tipos de campos
    grupo_botones_listo(objeto) {
        for (const indice in this.campos_tipo) {
            let campo = this.campos_tipo[indice];
            campos_constructor.drag_eventos(this, campo.elementAttr.id, campo);     
        }
    },

    // Busca un campo por indice en la forma
    buscar_campo(uuid) {
        let campo = null;
        for (const indice in this.campos) {            
            if (this.campos[indice].editorOptions.uuid == uuid) {
                campo = this.campos[indice];
            }
        }

        return campo
    },

    // Cambia campo por indice en la forma
    cambia_campo(datos) {
        for (const indice in this.campos) {
            if (this.campos[indice].editorOptions.uuid == datos.uuid) {
                this.campos[indice] = datos;
            }
        }
    },

    click_editar(e) {
        let dataField = e.dataField;
        let campo     = this.buscar_campo(e.editorOptions.uuid);
        let accion    = campos_constructor.click_campo_accion(this, "editar", campo);
        accion();
    },

    click_borrar(e) {
        let dataField = e.dataField;
        let campo     = this.buscar_campo(e.editorOptions.uuid);
        let accion    = campos_constructor.click_campo_accion(this, "borrar", campo);
        accion();
    }
}    

export default {
    metodos   : metodos,
    drop_forma: formulario_librerias.drop_forma
}