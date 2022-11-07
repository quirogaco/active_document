<template>
    <div class="container-fluid page_holder_main">
        <div class="barra fixed-top shadow">
            <div class="container-fluid" style="height: 45px">
                <div class="row">
                    <div class="col-1 border-end">
                        <DxButton
                            :width="35"
                            :height="35"
                            text=""
                            hint="Mostrar/Esconder Menu"
                            type="normal"
                            icon="fas fa-bars"
                            styling-mode="text"
                            :element-attr="buttonAttributes"
                            @click="onClickNavegacion($event)"
                        />                                            
                    </div>                    

                    <div class="col-1 p-2 texto_grande">
                    </div>
                  
                    <div class="col-7 p-2 centered" style="height: 35px;">                    
                        <div class="centered">
                            {{ usuario_nombre }} / {{ ubicacion_nombre }}
                        </div>   
                    </div>

                    <div class="col-3 border-start">
                        <DxButton
                            :width="25"
                            :height="35"
                            text=""
                            hint="Ayuda"
                            type="normal"
                            icon="fas fa-question"
                            styling-mode="text"
                            :element-attr="buttonAttributes"
                            @click="onClickAyuda($event)"
                        />

                        <DxButton
                            :width="25"
                            :height="35"
                            text=""
                            hint="Salir"
                            type="normal"
                            icon="fas fa-times"
                            styling-mode="text"
                            :element-attr="buttonAttributes"
                            @click="onClickSalir($event)"
                        />
                    </div>

                </div> 
            </div>  
        </div> 

        <div class="container-fluid mt-5 " >

                <DxDrawer      
                    :opened-state-mode="selectedOpenMode"
                    :position="selectedPosition"
                    :reveal-mode="selectedRevealMode"
                    v-model:opened="openState"                
                    :close-on-outside-click="true"
                    template="listMenu"                              
                >

                    
                        <template #listMenu>
                            <NavigationList/>
                        </template>

                    
                        <div class="container-fluid blanco overflow-auto" >
                            <router-view>                        
                            </router-view>
                        </div>

                </DxDrawer>   

        </div>

    </div>

</template>

<script>
import { 
    onMounted,    
    getCurrentInstance,
    ref
} from 'vue'

import DxButton from 'devextreme-vue/button';
import DxDrawer        from 'devextreme-vue/drawer';
import DxToolbar       from 'devextreme-vue/toolbar';
import NavigationList  from './NavigationList.vue';
import contenido       from './contenido.vue';
import visores_archivo from "../../../librerias/visores_archivo.js"

export default {
    components: {
        DxDrawer,
        DxToolbar,
        DxButton,
        NavigationList,
        contenido
    },

    setup() {
        onMounted(() => {            
            //<contenido/>
            //window.$rutasNavegacion.ruta.push({path: "contenido_pantalla"})
            window.$router.push({path: "contenido_pantalla"})
        })
    },

    data() {
        return {
            showModes         : ['push', 'shrink', 'overlap'],
            positionModes     : ['left', 'right'],
            showSubmenuModes  : ['slide', 'expand'],
            selectedOpenMode  : 'shrink',
            selectedPosition  : 'left',
            selectedRevealMode: 'slide',
            openState         : true,

            buttonAttributes: {
                class: ' boton_barra m-1 '
            },            

            'titulo': "SGDEA",
            
            // Usuario
            usuario_nombre: window.$usuario.nombre,
            ubicacion_nombre: window.$usuario.ubicacion_nombre          
        }
    },

    methods: {
        screenSizeChanged() {},
        click_salir: function() {},
        click_ayuda: function() {},

        onClickNavegacion: function($event) {
            this.openState = !this.openState
        },

        onClickSalir: function() {
            window.$mostrar_esperar("Saliendo..")
            window.$router.go(0)
        },

        onClickAyuda: function() {
            visores_archivo.ver_descarga_archivo({
                archivo_id: "radicacion_ventanilla.pdf", 
                operacion : 'manuales_pdf', 
                titulo    : "Manuales",
            })
        },

        asignaAtributoDinamico(atributo, valor) {
            this[atributo] = valor;
        }
    }
};

</script>

<style>
.barra {
    background-color: white;
    color: rgb(29, 42, 69);
    font-weight: 600;
    font-size: 14px;
}

.boton_barra {
    background-color: Transparent;
    background-repeat:no-repeat;
    border: none;
    cursor:pointer;
    overflow: hidden;      
}

.texto_grande_azul {
    font-weight: 600;
    font-size: 15px;
    color: rgba(0, 102, 255, 0.842)
}

</style>