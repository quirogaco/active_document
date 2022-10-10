<template src="./tramiteGestion.html">
</template>

<script>
import { getCurrentInstance, ref, reactive, onMounted } from "vue";
import DxToolbar        from 'devextreme-vue/toolbar';
import DxButtonGroup    from 'devextreme-vue/button-group';
import DxDropDownButton from 'devextreme-vue/drop-down-button';

import onlyoffice_editor from "../../../onlyOffice/onlyoffice_editor.vue";
import pdf_componente    from "../../../pdfjs/pdf_componente.vue";

// Atributos de gestion y especificos
import atributos from "./atributos.js";

// Metodos de gestión de tramite
import metodos from "./metodos.js"

// Ventana para ACCIONES
import ventana_emergente from './ventanas_tramite/ventana_emergente.vue';

// ## COMPONENT ## 
let Tramite = {
    name: 'tramiteGestion',

    emits: ['mounted'],

    components: {
        DxToolbar,
        DxButtonGroup,
        DxDropDownButton,
        
        // Visor, Editor
        onlyoffice_editor,
        pdf_componente,

        // Ventana emergente de acciones
        ventana_emergente
    },

    props: {},

    // setup(props, { attrs, slots, emit, expose })
    setup(props, ctx) {        
        let datos = atributos.atributos;

        onMounted(() => {              
            let that = getCurrentInstance().ctx;        
            window.$cmp["tramiteGestion"] = that;                      
            that.$emit('mounted', that);   
        })

        return {
            ...datos
        }
    },

    methods: {}   
}

export default Tramite
</script>

<style >
#tramite_botones_acciones .dx-buttongroup-item.dx-button.dx-button-mode-contained:not(.dx-item-selected) {
    background-color: #337AB7;
    color: #ffff;
    font-size: 16px;
}

#tramite_botones_acciones .dx-list .dx-empty-message, .dx-list-item-content {
    color: #000;
    font-weight: 500;
}

.borde {
    background-color: #337AB7;
}

.fondo_estado {
  background-color: #F9F9FA;
  color: blue;
}

.fondo_titulo_estado {
  background-color: #F2F4F8;
}

.negrilla {
  font-size: 14px;
}

</style>