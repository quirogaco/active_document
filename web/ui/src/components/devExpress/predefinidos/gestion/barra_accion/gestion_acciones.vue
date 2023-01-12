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
    let evento = componente.$props.opciones.evento_grid_gestion;
    componente.$emit(evento, parametros)     
};

let barra_elementos = function(that) {
    let elementos = [{
        widget  : "dxDropDownButton",
        location: "after",
        options : {
            items      : gestion_acciones_elementos.items_borradores(that, that.opciones.contexto),                
            displayExpr: 'titulo',
            keyExpr    : 'id',
            text       : "Borradores",    
            onItemClick: elemento_click,  
            width      : 350,
            stylingMode: 'filled',
            type       : 'default'                                 
        }
    }];

    // itesm de gestion
    let items_gestion = gestion_acciones_elementos.items_gestion(that, that.opciones.contexto);
    if (items_gestion.length > 0) {
        elementos.push({
            widget  : "dxDropDownButton",
            location: "after",
            options : {
                items      : items_gestion,                
                displayExpr: 'titulo',
                keyExpr    : 'id',
                text       : "Acciones de Gestión",    
                onItemClick: elemento_click_gestion,  
                width      : 350,
                stylingMode: 'filled',
                type       : 'default'                                 
            }
        })               
    };

    return elementos;
}

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
            barra_elementos: barra_elementos(this),            
            onContentReady: function(e) {}
        }
    }
}

export default barra;

</script>