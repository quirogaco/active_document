<template>
    <div class="shadow p-1 mb-2 bg-light rounded">
        <DxToolbar
            :items = "barra_elementos"
        />
    </div>
</template>

<script>
import DxToolbar from 'devextreme-vue/toolbar'

import gestion_acciones_elementos from "../gestion_acciones_elementos/gestion_acciones_elementos.js"

let componente;

let elemento_click = function(e) {   
    let parametros = gestion_acciones_elementos.elemento_parametros(e.itemData.id)    
    let evento     = componente.$props.opciones.evento    
    componente.$emit(evento, parametros)     
};

let elemento_click_gestion = function(e) {      
    let parametros = gestion_acciones_elementos.elemento_parametros(e.itemData.id);   
    let evento     = componente.$props.opciones.evento_grid_gestion;
    console.log("componente:", componente, evento); 
    componente.$emit(evento, parametros)     
};

// Barra de gestión
let barra =  {
    name: 'gestion_acciones',

    created() {},

    props: {
        // Opciones del editor
        opciones: {
            type: Object,
            default: () => {
                return {}
            }
        },  
    },

    components: {
        DxToolbar,
    },

    mounted() {
        let contexto = this.opciones.contexto;  
        componente = this;                     
    },

    data() {
        return {
            barra_elementos: [
                {
                    widget  : "dxDropDownButton",
                    location: "after",
                    options : {
                        items      : gestion_acciones_elementos.items_borradores(this, this.opciones.contexto),                
                        displayExpr: 'titulo',
                        keyExpr    : 'id',
                        text       : "Borradores",    
                        onItemClick: elemento_click,  
                        width      : 350,
                        stylingMode: 'filled',
                        type       : 'default'                                 
                    }
                },

                {
                    widget  : "dxDropDownButton",
                    location: "after",
                    options : {
                        items      : gestion_acciones_elementos.items_gestion(this, this.opciones.contexto),                
                        displayExpr: 'titulo',
                        keyExpr    : 'id',
                        text       : "Acciones de Gestión",    
                        onItemClick: elemento_click_gestion,  
                        width      : 350,
                        stylingMode: 'filled',
                        type       : 'default'                                 
                    }
                }                
            ],
            
            onContentReady: function(e) {}
        }
    }
}

export default barra;

</script>