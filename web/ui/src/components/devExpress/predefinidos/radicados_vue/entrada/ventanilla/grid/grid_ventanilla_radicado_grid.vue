<template>
    <div class="container-fluid shadow-sm ">
        <Popup
            :attributes="attributes_popup"
            :key= "render_popup_key"
        />

        <p class="text-center fs-3">Radicación ventanilla única</p>
        <DataGrid
            :attributes = "attributes_datagrid"
        />
    </div>
</template>

<script setup lang="ts">
//**************************//
// Atributos del componente //
//**************************//
import DxButton from 'devextreme-vue/button';
import {getCurrentInstance, ref, onMounted} from "vue";
let that = getCurrentInstance().ctx;
let grid = ref(null);
that.name = "grid_ventanilla_radicado";

import columnas from "./grid_ventanilla_radicado_columnas.js";
import barra from "./grid_ventanilla_radicado_barra.js";

import {methods} from "./grid_ventanilla_radicado_metodos.js";
that = $lib.assignAttributes(that, methods);

//let .DataGridCmp = null;

// POPUP
let attributes_popup = {  
    internalComponent: "DataForma",
    attributes_str: '{"sa": "aaaasss", "sb": "ssssbebebebe", "sc": "sscedefegehess"}',
    attributes: {
        a: "aaaa",
        b: "bebebebe",
        c: "cedefegehe"
    }
};
// Para llamarlo con that desde methods
that.attributes_popup = attributes_popup;
let render_popup_key = ref(0);
that.render_popup_key = render_popup_key;

// DATAGRID
let attributes_datagrid = {
    dataSource: {                
        dataSource: "radicados_entrada"
    },
    height : "100%",
    width  : "100%",
    columns: columnas.columnas,
    toolbar: barra.barraDef(that)
};
//console.log("barra.barraDef(that)", barra.barraDef(that))

//**********************//
// Eventos del datagrid //
//**********************//
that.llamar_forma = function(parametros) {    
    // $lib.llamar_componente("flujos_dinamicos_forma", parametros)
}

async function dblClickCell(event, DataGrid) {  
    // let datos = await $lib.leer_registro_id("tramites", event.data.id);
    // let parametros = {
    //     "id"    : event.data.id,
    //     "datos" : datos,         
    //     "mode"  : "editar",
    //     "return": that.name        
    // } 
    // that.llamar_forma(parametros);
};

function clickRow(event, DataGrid) {};

function mountedGrid(DataGrid) {
    //that.DataGridCmp = DataGrid;
};

//**********************//
// Ganchos del datagrid //
//**********************//
onMounted(() => {})

defineExpose( Object.assign({}, that) )

</script>