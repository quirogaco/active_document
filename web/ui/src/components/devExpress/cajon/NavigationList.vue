<template>
    
    <div class="container-sm " >

        <DxTreeView
            key-expr="path"
            selection-mode="single"
            :focus-state-enabled="true"
            expand-event="click"
            @item-click="handleItemClick"            
            :items="navegacion"
            @selection-changed="navigate"  
            :element-attr="attributes"  
            :hover-state-enabled="true"        
        >                  

            <template #links="{ data }">
                <div>
                    <router-link :to="'/' + data.path">
                        <div>
                            <div class="">
                                <i :class="'dx-icon-' + data.icon"></i>
                            </div>
                            <span class="">{{ data.text }}</span>
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
            attributes: {
                id   : 'arbol_navegacion',
                class: 'arbol border-end'
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
            //this.$router.push(e.itemData.path);  
            $router.push(e.itemData.path);  
            window.scroll(0,0);        
            const pointerEvent = e.event;
            pointerEvent.stopPropagation();            
        },
    }
};

</script>

<style>


.dx-treeview-item {
    font-weight: bold;
    color: #355977;
}

.dx-treeview-item.dx-state-hover {
    background-color: silver;
    color: black;
}

</style>