<template>
    
    <div class="container-sm p-2 m-2 w-80 hidden-mobile">

            <div class="container-sm px-lg-4 px-xl-5">
                <section class="mb-3 mb-lg-1">
                    <div class="row">
                        <div class="col-xl-3 col-md-6 mb-4 ">
                            <div class="card-widget h-100">
                                <div class="card-widget-body bg-red-900">
                                    <div class="dot me-3 bg-blue"></div>
                                    <div class="text">
                                        <h6 class="mb-0">Documentos en gestión (Total)</h6>
                                        <span class="text-gray-500">145,14 GB</span>
                                    </div>
                                </div>
                                <hr/>
                                <div class="icon text-white bg-blue">
                                    <i class="fas fa-folder"></i>                                    
                                </div>
                            </div>
                        </div>
                        <div class="col-xl-3 col-md-6 mb-4 ">
                            <div class="card-widget h-100">
                                <div class="card-widget-body">
                                    <div class="dot me-3 bg-green"></div>
                                    <div class="text">
                                        <h6 class="mb-0">A tiempo</h6>
                                        <span class="text-gray-500">32</span>
                                    </div>
                                </div>
                                <div class="icon text-white bg-green">
                                    <i class="fas fa-hourglass"></i>
                                </div>
                            </div>
                        </div>
                        <div class="col-xl-3 col-md-6 mb-4 ">
                            <div class="card-widget h-100">
                                <div class="card-widget-body">
                                    <div class="dot me-3 bg-orange"></div>
                                    <div class="text">
                                        <h6 class="mb-0">Por vencer</h6>
                                        <span class="text-gray-500">400</span>
                                    </div>
                                </div>
                                <div class="icon text-white bg-orange">
                                    <i class="fas fa-hourglass-end"></i>
                                </div>
                            </div>
                        </div>
                        <div class="col-xl-3 col-md-6 mb-4 ">
                            <div class="card-widget h-100">
                                <div class="card-widget-body">
                                    <div class="dot me-3 bg-red"></div>
                                    <div class="text">
                                        <h6 class="mb-0">Vencidos</h6>
                                        <span class="text-gray-500">123</span>
                                    </div>
                                </div>
                                <div class="icon text-white bg-red">
                                    <i class="far fa-hourglass"></i>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>


            <section class="container-sm mb-4 mb-lg-5">
                    <div class="row">
                        <div class="col-lg-12 mb-2 mb-lg-0 ">
                            <div class="card h-100">
                                <div class="card-header azul_claro h-5">
                                    <h4 class=" ">Calendario vencimientos</h4>
                                </div>
                                <div class="card-body">                                                                        
                                    <DxScheduler
                                        time-zone="America/Los_Angeles"
                                        :data-source="dataSource"
                                        :current-date="currentDate"
                                        :views="views"
                                        :groups="groups"
                                        :show-all-day-panel="true"
                                        :first-day-of-week="1"
                                        :start-day-hour="8"
                                        :end-day-hour="18"
                                        current-view="month"
                                    >                                
                                    </DxScheduler>

                                </div>
                            </div>
                        </div>
                        
                    </div>
            </section>
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