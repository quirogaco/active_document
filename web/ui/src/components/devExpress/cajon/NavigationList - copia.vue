<template>
    
    <div style="width:350px" class=" shadow-lg bg_navegacion page-holder sidebar">

        <DxTreeView
            key-expr="path"
            selection-mode="single"
            :focus-state-enabled="false"
            expand-event="click"
            @item-click="handleItemClick"
            width="350%"
            :items="navegacion"
            @selection-changed="navigate"  
            :element-attr="treeViewAttributes"          
        >                  

            <template #links="{ data }">
                <div>
                    <router-link :to="'/' + data.path">
                        <div>
                            <div class="dx-list-item-icon-container">
                                <i class="dx-icon dx-list-item-icon" :class="'dx-icon-' + data.icon"></i>
                            </div>
                            <span class="fs-5">{{ data.text }}</span>
                        </div>
                    </router-link>                    
                </div>
            </template>

        </DxTreeView>

    </div>

</template>

<script>

import { 
    onMounted, 
    ref,
    getCurrentInstance
} from 'vue'

import { DxList } from 'devextreme-vue/list';
import DxTreeView from "devextreme-vue/ui/tree-view";

export default {
    components: {
        DxList,
        DxTreeView
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
                class: 'bg_arbol'
            }
        };
    },

    methods: {        
        navigate(parametro) {},

        asignaAtributoDinamico(atributo, valor) {
            this[atributo] = valor;
        },

        handleItemClick(e) {
            if (!e.itemData.path || this.compactMode) {
                return;
            }
            this.$router.push(e.itemData.path);   
            window.scroll(0,0);        
            const pointerEvent = e.event;
            pointerEvent.stopPropagation();            
        },
    }
};

</script>

<style>
</style>