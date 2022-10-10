<template>
    <div class="container-fluid shadow p-1 mb-1 rounded">
        <p class="text-center fs-3">Flujos dinámicos</p>
        <DataGrid      
            ref             = "grid"  
            @dblClickCell   = "dblClickCell"
            @clickRow       = "clickRow"
            @mounted        = "mountedGrid"
            :attributes     = "attributes"
        />
    </div>
</template>

<script setup lang="ts">
import { getCurrentInstance, ref, onMounted } from "vue";

// this component
let that = getCurrentInstance().ctx;

//**************************//
// Atributos del componente //
//**************************//
import columnas from "./flujos_dinamicos_columnas";
import barra    from "./flujos_dinamicos_barra";
that.name        = 'flujos_dinamicos_grid';
that.DataGridCmp = null;

//************************//
// Atributos del datagrid //
//************************//
let gridRef    = ref(null);
let attributes = {
    dataSource: {                
        dataSource: "tramites",
        //fields    : ["id", "nombre", "codigo"],
    },
    heigth : "100%",
    width  : "100%",
    columns: columnas.columnas,
    toolbar: barra.barraDef(that)
};

//**********************//
// Eventos del datagrid //
//**********************//
that.llamar_forma = function(parametros) {    
    $lib.llamar_componente("flujos_dinamicos_forma", parametros)
}

async function dblClickCell(event, DataGrid) {  
    let datos = await $lib.leer_registro_id("tramites", event.data.id);
    let parametros = {
        "id"    : event.data.id,
        "datos" : datos,         
        "mode"  : "editar",
        "return": that.name        
    } 
    that.llamar_forma(parametros);
};

function clickRow(event, DataGrid) {};

function mountedGrid(DataGrid) {
    that.DataGridCmp = DataGrid;
};

//**********************//
// Ganchos del datagrid //
//**********************//
onMounted(() => {})

</script>