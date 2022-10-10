<template src="./formulario_constructor.html">
</template>

<script>
import { getCurrentInstance, ref, onMounted } from "vue";

import DxForm, {
    DxGroupItem,
    DxSimpleItem,
    DxButtonItem,
    DxLabel
} from 'devextreme-vue/form';

import DxTextBox          from 'devextreme-vue/text-box';
import { DxNumberBox }    from 'devextreme-vue/number-box';
import DxDateBox          from 'devextreme-vue/date-box';
import DxButton           from 'devextreme-vue/button';
import { DxCheckBox }     from 'devextreme-vue/check-box';
import DxRadioGroup       from 'devextreme-vue/radio-group';
import { DxFileUploader } from 'devextreme-vue/file-uploader';
import DxSelectBox        from 'devextreme-vue/select-box';
import DxTagBox           from 'devextreme-vue/tag-box';
import DxTextArea         from 'devextreme-vue/text-area';
import DxButtonGroup      from 'devextreme-vue/button-group';

import forma_datos_campos from './forma_datos_campos.js';
import atributos_campos from './atributos_campos.vue';

// Botones barra
import botones_barra from './botones_barra.js';

// Componentes disponibles
import { campos_tipo } from './lista_componentes.js';

// Metodos
import formulario_constructor_metodos from "./formulario_constructor_metodos.js";

// borra JCR!!
import viewer_forma from './viewer/viewer_forma.vue'

export default {
    components: {
        DxForm,
        DxGroupItem,        
        DxSimpleItem,
        DxButtonItem,        
        DxTextBox,    
        DxNumberBox,    
        DxDateBox,
        DxCheckBox,
        DxRadioGroup,
        DxFileUploader,
        DxSelectBox,
        DxTagBox,
        DxTextArea,
        DxButton,
        DxButtonGroup,

        // Atributos de los campos
        atributos_campos,

        // BORRAR JCR!!
        viewer_forma
    },

    props: $forma.forma_propiedades({}),

    mounted() {
        let atributos = $forma.lee_propiedades(this.$props)
        // Forma de datos basicos
        this.forma_datos = this.$refs.forma_datos;   
        if (atributos.modo == 'modificar') {
            this.forma_datos.formData(atributos.datos);
            this.campos = atributos.datos.diseno;            
        };
        console.log("this.$props.attributes.modo:", this.$props.attributes)
        /*
        this.elementos_barra.items = botones_barra.getItems({
            'callBack': this.click_botones,
            'mode'    : atributos.modo
        })
        */

        // Forma diseño
        this.forma_diseno    = this.$refs.forma_diseno.instance;
        window.$forma_diseno = this;

        // Forma prevista
        this.forma_prevista     = this.$refs.formRef;               
        // Evento cuando se suelta un elemennto sobre la forma    
        formulario_constructor_metodos.drop_forma(this)    
        // Se recalcula las columnas de la forma, si se muestra o no atributos del campo
        this.calcula_forma_tamano()    
    },

    data() {
        return {
            // *********** //
            // Forma Datos //
            // *********** //
            forma_datos: ref(null),
            forma_datos_attributos: {
                id   : 'datos_forma_id',
                formData: {},
                items   : forma_datos_campos.items,
                colCount: 1        
            },
            
            // ***************** //
            // Forma Definicion  //
            // ***************** //
            // Atributos contenedor elementos
            muestra_elementos: true,
            clase_elementos  : "container-fluid shadow border border-2 p-1 col-sm-2",
            campos_tipo      : campos_tipo,
            
            // Atributos contenedor forma
            clase_forma    : "container-fluid border border-2 p-1 col-sm-7",
            forma_attributos: {
                id   : 'constructor_forma_id',
                class: 'bg-body shadow rounded'
            },
            definicion: true,

            // Atributos contenedor atributos
            muestra_atributos: ref(false),
            muestra_key      : 0,
            opciones_atributo: {
                datos: {
                    titulo: ""
                }
            },
            clase_atributos  : "container-fluid shadow border border-2 p-1 col-sm-3",

            // Id del contenedor de campos
            lista_ids: function(datos) {
                let contiene_id = "_contiene_" + datos.name

                return contiene_id
            },

            // Datos del campo drag
            datos_drag: null,

            // Campos de la forma
            campos: [],
            
            // *************** //
            // Forma prevista  //
            // *************** //
            formRef: ref(null),
            prevista_key: 0,
            atributos_forma: {
                id      : "forma_prevista",
                formData: {},
                items   : [],
                colCount: 1                     
            },

            // Barra de accion
            barraRef: ref(null),
            elementos_barra: {
                id   : "barra_formulario_constructor",
                items: botones_barra.getItems({
                    'callBack': this.click_botones,
                    'mode'    : $forma.lee_propiedades(this.$props).modo
                })
            },

            // Si es diseño o prevista de fomulario
            prevista: false,  
            
            // *********************//
            // VISOR SE BORRA ESTO  //
            // *********************//
            viewer_ref: ref(null),            
            viewer_key: 0,
            viewer_attributes: {
                id      : "viewer_consulta",
                formData: {},
                items   : [],
                colCount: 1   // ?                  
            },
            // Si es diseño o prevista de fomulario
            viewer: false 
            
        }
    },

    methods: formulario_constructor_metodos.metodos, 
        
}
</script>

<style>
.dx-buttongroup-wrapper{
    flex-flow: column nowrap;
}
</style>