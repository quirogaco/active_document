<template>

    <div class="container-fluid ">
        <div class="row">
        
            <DxPopup
                ref                     = "popup"
                v-model:visible         = "opciones.visible"
                :drag-enabled           = "false"
                :close-on-outside-click = "true"
                :show-close-button      = "true"
                :show-title             = "true"
                width                  = "70%"
                height                 = "auto"
                :title                  = "opciones.titulo"
                container               = ".dx-viewport" 
            >
                
                <DataForma     
                    ref             = "form"  
                    :attributes     = "atributos_forma"
                />

                <div class="d-flex justify-content-center">
                    <ToolBar    
                        ref             = "barra"  
                        :attributes     = "atributos_barra"
                    />
                </div>

            </DxPopup>

        </div>
    </div>

</template>

<script>
import { getCurrentInstance, ref, onMounted } from "vue";
import { DxPopup } from 'devextreme-vue/popup'
import { DxScrollView } from 'devextreme-vue/scroll-view';

import forma_general from "../../comunes_vue/forma/forma.js"

import items_grupos from "./items_grupos";
import items_barra  from "./items_barra";

/*
let parametros = {
                            comentario: this.comentario,
                            tipo      : this.tipo,
                            peticiones: this.datos.elementos,
                            accion    : this.datos.accion
                        }
                        this.indicador_visible = true
                        let urlCompleta = window.$direcciones.servidorDatos + '/gestion_acciones'    
                        window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna, "")   
                        this.$parent.$_instance.option("disabled", true);               
*/

// Ventana emergente
let ventana =  {
    name: 'ventana_emergente_gestion',

    components: {
        DxPopup
    },

    props: {
        opciones: {
            type: Object,
            default: () => {
                return {}
            }
        }        
    },

    // setup(props, { attrs, slots, emit, expose })
    setup(props) {
        let that = getCurrentInstance().ctx;
        // refs
        let popup = ref(null);
        let form  = ref(null);
        let barra = ref(null);

        //*****************//
        // form attributes //
        //*****************//
        let atributos_forma = {
            id      : "forma_emergente_gestion",
            formData: {},
            items   : items_grupos.items(props.opciones.tipo_campos),
            colCount: 1,            
        }  

        //********************//
        // toolbar attributes //
        //********************//
        const retorna_remoto = function(retorna_datos) {
            $notify("Acción realizada exitosamente", "success") 
            props.opciones.visible = false;
        };

        const ejecutar_accion = function(accion) {
            if (accion == "salvar") {
                let dxForm = that.form.dxForm;
                if (forma_general.validar_datos(dxForm.instance) == true) {          
                    let datos = dxForm.formData;    
                    datos["tramite_id"] = "";
                    let parametros = {
                        'accion': that.opciones.tipo_campos,
                        'datos' : datos
                    };
                    console.log("parametros:", parametros);       
                    forma_general.envio_accion_notifica("tramite_acciones", parametros, retorna_remoto)                                 
                }
                //console.log("ejecutar_accion:", accion, that.opciones.tipo_campos, form.dxForm.formData)
            }
            else {
               props.opciones.visible = false
            }
        }

        let atributos_barra = {
            id      : "barra_emergente_gestion",
            items   : items_barra.items(props.opciones.titulo_accion, ejecutar_accion)
        }  

        onMounted(() => {  
            let that = getCurrentInstance().ctx;
        })

        return {
            form,
            atributos_forma,
            atributos_barra
        }
    }
}

export default ventana;
</script>