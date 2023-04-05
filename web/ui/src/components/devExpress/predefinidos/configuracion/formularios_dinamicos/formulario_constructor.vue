<template src="./formulario_constructor.html">
</template>

<script>
import DxToolbar, { DxItem } from 'devextreme-vue/toolbar'
import DxButton              from 'devextreme-vue/button'
import { DxScrollView }      from 'devextreme-vue/scroll-view'
import { DxSortable }        from 'devextreme-vue/sortable'

import DxForm, {
    DxGroupItem,
    DxSimpleItem,
    DxButtonItem,
    DxLabel,
    DxRequiredRule,
    DxCompareRule,
    DxRangeRule,
    DxStringLengthRule,
    DxPatternRule,
    DxEmailRule,
    DxAsyncRule
} from 'devextreme-vue/form'

import { DxFileUploader } from 'devextreme-vue/file-uploader'
import DxSelectBox        from 'devextreme-vue/select-box'
import DxTagBox           from 'devextreme-vue/tag-box'
import DxTextArea         from 'devextreme-vue/text-area'

import notify from 'devextreme/ui/notify'

import atributos_campos from './atributos_campos.vue';

// Componentes disponibles
import { lista_componentes } from './definicion_componentes.js'

// Metodos
import formulario_constructor_metodos from "./formulario_constructor_metodos.js" 

// Constructor
let campos_formulario  = [];

// Forma
let campos_constructor = [];

export default {
    components: {
        DxToolbar,
        DxItem,
        DxButton,
        DxScrollView,
        DxSortable,

        // Forma
        DxForm,
        DxGroupItem,
        DxSimpleItem,
        DxButtonItem,
        DxLabel,
        DxRequiredRule,
        DxCompareRule,
        DxRangeRule,
        DxStringLengthRule,
        DxPatternRule,
        DxEmailRule,
        DxAsyncRule,

        DxFileUploader,
        DxSelectBox,
        DxTagBox,
        DxTextArea,

        // Atributos de los campos
        atributos_campos
    },

    mounted() {
        window.$_constructor = this      
        this.forma_prevista  = this.$refs.forma_prevista.instance
        this.notify          = notify 
    },

    data() {
        return {
            // Manejo de constructor
            prevista_constructor: true,
            constructor_opciones: {
                icon       : 'fab fa-wpforms',
                text       : 'Diseñador del formulario',
                type       : 'default',
                stylingMode: 'contained',
                onClick: () => {
                    this.prevista_forma       = false;
                    this.prevista_constructor = true;                       
                }
            },     

            constructor_atributos: {
                id: 'constructor'
            },

            // Manejo de prevista
            prevista_forma: true,
            formulario_opciones: {
                icon       : 'far fa-eye',
                text       : 'Prevista del formulario',
                type       : 'default',
                stylingMode: 'contained',
                onClick: () => {
                    this.prevista_forma       = true;
                    this.prevista_constructor = false;
                    this.campos_formulario    = this.crea_campos();      
                }
            },

            prevista_atributos: {
                id: 'prevista'
            },
            
            
            // Definiciond de componentes a usar
            lista_componentes,

            // Campos del CONSTRUCTOR
            campos_constructor,

            // Campos del formulario PREVISTA
            campos_formulario,

            // Parametros para editor de atributos
            contador_campos  : 0,
            emergente_key    : 0,
            opciones_atributo: {
                visible: false,
                datos  : {}
            }
        };
    },

    methods: formulario_constructor_metodos.metodos,
};
</script>

<style>

.lista {
    border-radius: 8px;
    margin: 15px;
    background-color: rgba(192, 192, 192, 0.4);
    display: inline-block;
    vertical-align: top;
    white-space: normal;
}

.lista-titulo {
    font-size: 16px;
    padding: 10px;
    padding-left: 30px;
    margin-bottom: -10px;
    font-weight: bold;
    cursor: pointer;
}

.scrollable-componente {
    height: 650px;
    width : 320px;
}

.card-componente {
    position: relative;
    background-color: white;
    box-sizing: border-box;
    width: 300px;
    padding: 5px 5px;
    margin: 5px;
    cursor: pointer;
}

.boton-componente {
    width: 250px;
}


.scrollable-forma {
    height: 650px;
    width : 450px;
}

.card-forma {
    position: relative;
    background-color: white;
    box-sizing: border-box;
    width: 400px;
    padding: 10px 10px;
    margin: 10px;
    cursor: pointer;
}

.ordenable-forma {
    min-height: 380px;
    height: 650px
}

.lista_atributos {
    border-radius: 8px;
    margin: 15px;
    background-color: rgba(192, 192, 192, 0.4);
    display: inline-block;
    vertical-align: top;
    white-space: normal;
    padding: 10px 10px;

    height: 650px;
    width : 450px;
}

</style>