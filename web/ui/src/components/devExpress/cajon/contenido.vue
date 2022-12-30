<template>
    
    <div class="container-sm p-2 m-2 w-80 hidden-mobile">
    </div>

</template>

<script>

import { 
    onMounted, 
    ref,
    getCurrentInstance
} from 'vue'

import { DxScheduler, DxResource } from 'devextreme-vue/scheduler';
import { DxList } from 'devextreme-vue/list';
import DxTreeView from "devextreme-vue/ui/tree-view";

export default {
    components: {
        DxList,
        DxTreeView,
        DxScheduler, 
        DxResource
    },

    data() {
        return {
            groups: ['gestion'],
            views: ['month'],
            currentDate: new Date(),
            employees : [],
            dataSource: []
        };
    },

    setup() {
        onMounted(() => {
            let unoMismo              = getCurrentInstance();
            window.$ns['_navegador_'] = unoMismo.ctx; 
            unoMismo.ctx.asignaAtributoDinamico("navegacion", window.$rutasNavegacion.navegaciones);   
        })

        return {
            navegacion: ref([]),
            treeViewAttributes: {
                id   : 'arbol_navegacion',
                class: ''
            }
        };
    },

    methods: {        
        navigate(parametro) {},

        asignaAtributoDinamico(atributo, valor) {
            this[atributo] = valor;
        },

        handleItemClick(e) {
            /*
            console.log("0.............***")
            if (!e.itemData.path || this.compactMode) {
                return;
            }
            //this.$router.push(e.itemData.path);   
            window.$router.push(e.itemData.path);   
            window.scroll(0,0);        
            const pointerEvent = e.event;
            pointerEvent.stopPropagation();  
            */          
        },
    }
};

</script>

<style>
</style>