<template>
    <div class="container-fluid shadow p-1 mb-1 rounded">
        <p class="text-center fs-4">Copias de Radicados</p>
        <DataGrid      
            ref             = "grid_ref"  
            @dblClickCell   = "dblClickCell"
            @clickRow       = "clickRow"
            @mounted        = "mountedGrid"
            :attributes     = "attributes"
        />
    </div>
</template>

<script setup lang="ts">

import { getCurrentInstance, ref, onMounted } from "vue";
import estructuras from '../../../../../librerias/estructuras.js';


// this component
let that = getCurrentInstance().ctx;

//**************************//
// Atributos del componente //
//**************************//
import columnas from "./copias_grid_columnas";
import barra    from "./copias_grid_barra";
that.name = 'copias_grid';
that.grid_cmp = null;

//************************//
// Atributos del datagrid //
//************************//
let grid_ref = ref(null);
let attributes = {
    dataSource: {                
        dataSource: "copias",
        filters: [
            ["estado", "=", "ASIGNADO"]
        ],    
    },
    selection: {
        mode: "multiple"
    },
    heigth: "100%",
    width: "100%",
    columns: columnas.columnas,
    toolbar: barra.barraDef(that)
};

//**********************//
// Eventos del datagrid //
//**********************//
that.llamar_forma = function(parametros) {    
    $lib.llamar_componente("flujos_dinamicos_forma", parametros)
}

async function dblClickCell(event, dataGrid) { 
    let datos_radicado = await estructuras.leer_registro_id("radicados_entrada", event.data.radicado_id);
    let datos = {
        "id"         : event.data.id,
        "datos"      : datos_radicado,
        "modo"       : "consulta",
        "llamado_por": "copias_grid"
    };
    
    $router.push({
        name: "forma_radicado_consulta",                      
        params: {
            "attributes_str": JSON.stringify(datos)
        }                            
    })
};

function clickRow(event, dataGrid) {};

function mountedGrid(dataGrid) {
    that.grid_cmp = dataGrid;
};

//**********************//
// Ganchos del datagrid //
//**********************//
onMounted(() => {})

</script>