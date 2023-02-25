<template >

    <DxLoadPanel
        v-model:visible = "indicador_visible" 
        message         = "Por favor espere"               
        shading-color   = "rgba(0,0,0,0.4)"
    />


        <div class="full-width-content ">
            <div class="dx-fieldset">
                <div class="dx-field">
                    <div class="dx-field-label">Comentario:</div>
                    <div class="dx-field-value">
                        <DxTextArea
                            :height       = "90"
                            v-model:value = "comentario"
                        />
                    </div>
                </div>

            </div>

        </div>  

        <DxToolbar>
            <DxItem
                :options = "accion_opciones"
                location = "after"
                widget   = "dxButton"
            />
        </DxToolbar>


</template>

<script>
import { DxLoadPanel } from 'devextreme-vue/load-panel'
import DxTextArea from 'devextreme-vue/text-area'
import DxToolbar, { DxItem } from 'devextreme-vue/toolbar'
import DxButton from 'devextreme-vue/button'
import notify from 'devextreme/ui/notify'
import { locale, loadMessages, formatMessage } from 'devextreme/localization'

import fuenteDatos from '../../../remoto/fuenteDatos.js'

let comentario_gestion =  {
    name: 'comentario_gestion',

    created() {
        locale("es")
    },

    components: {
        DxLoadPanel,
        DxTextArea,       
        DxButton,
        DxToolbar,
        DxItem
    },

    created() {},

    props: {
        datos: {
            type: Object,
            default: () => {
                return {}
            }
        },  
    },

    mounted() {},

    methods: {
        retorna: function() {
            this.indicador_visible = false
            this.$parent.$parent.$_instance.hide() 
            let acciones_refresca = ["DEVOLVER_DEPENDENCIA"]
            let acciones_cierra   = [
                "DEVOLVER_DEPENDENCIA",
                "DEVOLVER_ASIGNADOR", 
                "ENVIAR_VISTO_BUENO", 
                "DEVOLVER_REVISION", 
                "APROBAR_RADICAR", 
                "FINALIZAR_MANUAL",
                "CREA_BORRADOR_SALIDA",
                "CREA_BORRADOR_INTERNO"
            ]        
            let grid = window.$grid_gestion;
            console.log("this.datos.accion:", this.datos.accion) 
            if (acciones_cierra.indexOf(this.datos.accion) > -1) { 
                console.log("REFESCAS")               
                this.$router.push({path: "gestion_basica_grid"})
                grid.refresh()
            }                       
            if (acciones_refresca.indexOf(this.datos.accion) > -1) {                
                grid.refresh()                    
            }
        }
    },

    data() {
        return {
            indicador_visible: false,
            fuente: fuenteDatos.creaFuenteDatosUniversal(
                "select", 
                "usuario", 
                "usuarios", 
                null, 
                [], 
                []
            ),
            comentario: null,
            usuario: null,
            accion_opciones: {
                text: this.datos.boton_mensaje,
                type: "success",
                onClick: () => {                
                        let parametros = {
                            comentario: this.comentario,
                            peticiones: this.datos.elementos,
                            accion: this.datos.accion
                        }
                        //console.log("parametrod comentarios:", parametros)
                        this.indicador_visible = true
                        let urlCompleta = (
                            window.$direcciones.servidorDatos + 
                            '/gestion_acciones'
                        )
                        window.$f["http"].llamadoRestPost( 
                            urlCompleta, 
                            parametros, 
                            this.retorna, 
                            ""
                        )   
                        this.$parent.$_instance.option("disabled", true);                                          
                   // }
                }
            }
        }
    }
}

export default comentario_gestion;

</script>