<template >
    <DxLoadPanel
        v-model:visible = "indicador_visible" 
        message         = "Por favor espere"               
        shading-color   = "rgba(0,0,0,0.4)"
    />

    <div class="bg_tab_panel">

        <div class="full-width-content ">
            <div class="dx-fieldset">

                <div class="dx-field">
                    <div class="dx-field-label">Usuario:</div>
                    <div class="dx-field-value">
                        <DxSelectBox
                            :data-source    = "fuente"
                            v-model:value   = "usuario"
                            display-expr    = "nombre"
                            value-expr      = "id"
                            search-enabled   = "true"
                            :showClearButton = "true"
                        >
                            <DxValidator>
                                <DxRequiredRule />                            
                            </DxValidator>
                        </DxSelectBox>
                        
                    </div>
                </div>

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

    </div>  

</template>

<script>
import { DxLoadPanel } from 'devextreme-vue/load-panel'
import DxTextArea from 'devextreme-vue/text-area'
import DxToolbar, { DxItem } from 'devextreme-vue/toolbar'
import DxButton from 'devextreme-vue/button'
import DxSelectBox from 'devextreme-vue/select-box'
import DxValidator, {
    DxRequiredRule,    
} from 'devextreme-vue/validator'
import notify from 'devextreme/ui/notify'
import fuenteDatos from '../../../remoto/fuenteDatos.js'

let usuario_gestion =  {
    name: 'usuario_gestion',

    components: {
        DxLoadPanel,
        DxTextArea,
        DxRequiredRule,
        DxValidator,
        DxButton,
        DxSelectBox,
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
            this.indicador_visible = false;
            let acciones_grid = ["ASIGNAR_RESPONSABLE"];
            let grid = window.$grid_gestion;   
            if (acciones_grid.indexOf(this.datos.accion) > -1) {
                //grid.refresh()  
                this.$router.push({path: "gestion_basica_grid"});
            }
            this.$parent.$parent.$_instance.hide();
        }
    },

    data() {
        return {
            // Indicador de tareas
            indicador_visible: false,

            //fuente: [], 
            fuente: fuenteDatos.creaFuenteDatosUniversal(
                "select", 
                "usuario", 
                this.datos.fuente, 
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
                    if ( 
                        (this.comentario == null) || 
                        (this.comentario == "") || 
                        (this.usuario == null) 
                    ) {
                        notify(
                            {
                                message: "Comentario y usuario son obligatorios",                             
                                position: {
                                    my: 'center top',
                                    at: 'center top'
                                }
                            },
                            "warning", 
                        )
                    }
                    else {
                        let parametros = {
                            comentario: this.comentario,
                            usuario   : this.usuario,
                            peticiones: this.datos.elementos,
                            accion    : this.datos.accion,
                            rapida    : this.datos.rapida
                        };
                        this.indicador_visible = true
                        let urlCompleta = (
                            window.$direcciones.servidorDatos + 
                            '/gestion_acciones'
                        );    
                        window.$f["http"].llamadoRestPost( 
                            urlCompleta, 
                            parametros, 
                            this.retorna, 
                            ""
                        );   
                        this.$parent.$_instance.option("disabled", true);
                    }
                }
            }
        }
    }
}

export default usuario_gestion;

</script>