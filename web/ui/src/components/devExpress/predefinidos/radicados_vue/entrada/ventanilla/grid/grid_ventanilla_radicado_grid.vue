<template>
    <div class="container-fluid shadow-sm ">
        <p class="text-center fs-3">Radicación ventanilla única</p>
        <DataGrid
            :attributes = "attributes"
        >
        </DataGrid>
    </div>
</template>

<script setup lang="ts">
//**************************//
// Atributos del componente //
//**************************//
import { getCurrentInstance, ref, onMounted } from "vue";
import columnas from "./grid_ventanilla_radicado_columnas.js";
import barra from "./grid_ventanilla_radicado_barra.js";
// import { DxDataGrid } from 'devextreme-vue/data-grid';

// this component
let that = getCurrentInstance().ctx;
let grid = ref(null);
that.name = "grid_ventanilla_radicado";
that.DataGridCmp = null;

//************************//
// Atributos del datagrid //
//************************//
let attributes = {
    dataSource: {                
        dataSource: "radicados_entrada"
    },
    heigth : "100%",
    width  : "100%",
    columns: columnas.columnas,
    toolbar: barra.barraDef(that)
};
console.log("barra.barraDef(that)", barra.barraDef(that))

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

</script>