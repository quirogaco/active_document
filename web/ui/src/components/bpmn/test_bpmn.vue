<template>

    <div class="container-fluid">

        <bpmn_componente     
            url="/public/diagram.bpmn"
            v-on:error="handleError"
            v-on:shown="handleShown"
        />
            
    </div> 

</template>

<script>    
    import bpmn_componente  from './bpmn_componente.vue'
    import DxButton         from 'devextreme-vue/button'
    import { DxPopup }      from 'devextreme-vue/popup'
    import { DxScrollView } from 'devextreme-vue/scroll-view'

    import librerias from '../../librerias/librerias.js'

    import { 
        onMounted,    
        getCurrentInstance,
        ref
    } from 'vue'

    export default {
        components: {        
            DxPopup,
            DxButton,
            DxScrollView,
            bpmn_componente
        },

        methods: {
            handleError: function(err) {
                console.error('failed to show diagram', err);
            },

            handleShown: function() {
                console.log('diagram shown');
            }
        },

        setup(props, context) {    

            onMounted(() => {

            }) 

            return { 
                visible     : ref(true),
            }
        }
    }
</script>