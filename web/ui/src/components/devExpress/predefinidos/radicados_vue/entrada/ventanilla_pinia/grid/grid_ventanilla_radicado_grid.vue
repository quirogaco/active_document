<template>
    <div class="container-fluid shadow-sm ">
        <ventana_emergente_archivo                  
            :opciones = "opciones_ventana_emergente_archivo"
            :key = "emergente_key"
        />

        <p class="text-center fs-3">Radicación ventanilla única</p>
        <DataGrid
            :attributes = "attributes_datagrid"
            @dblClickCell = "dblClickCell"
            @mounted = "mountedGrid"
        />
    </div>
</template>

<script setup lang="ts">
//**************************//
// Atributos del componente //
//**************************//
import {getCurrentInstance, ref, onMounted} from "vue";
let that = getCurrentInstance().ctx;
let grid = ref(null);
that.name = "grid_ventanilla_radicado";

// Archivos
import ventana_emergente_archivo 
from '../../../../comunes/archivos/ventana_emergente_archivo.vue';

// Columnas
import ventanilla_radicado_columnas 
from '../../../comunes/grid/grid_ventanilla_radicado_columnas.js';
import barra from "./grid_ventanilla_radicado_barra.js";

import {methods} from "./grid_ventanilla_radicado_metodos.js";
that = $lib.assignAttributes(that, methods);

// Ventana emergente archivos
let opciones_ventana_emergente_archivo = ref({
    visible : false,
    datos: {},
    atributos: {
        titulo_pantalla: "Cargar archivo",                   
        titulo_boton   : "Salvar archivo",
        mensaje_retorno: "Envio de archivo correcto!" 
    }
});
that.opciones_ventana_emergente_archivo = opciones_ventana_emergente_archivo;
let emergente_key = ref(0);
that.emergente_key = emergente_key;

// Datagrid
let attributes_datagrid = {
    dataSource: {                
        dataSource: "radicados_entrada"
    },
    height : "100%",
    width  : "100%",
    columns: ventanilla_radicado_columnas.columnas,
    toolbar: barra.barraDef(that),
    selection: { 
        mode: 'multiple' 
    }
};
//console.log("barra.barraDef(that)", barra.barraDef(that))

//**********************//
// Eventos del datagrid //
//**********************//
that.llamar_forma = function(parametros) {    
    // $lib.llamar_componente("flujos_dinamicos_forma", parametros)
}

async function dblClickCell(event, DataGrid) {  
    that.columna_doble_click(event)
};

function clickRow(event, DataGrid) {};

function mountedGrid(DataGrid) {
    that.grid = DataGrid;
    console.log(" mountedGrid -> that.grid:", that.grid)
};

//**********************//
// Ganchos del datagrid //
//**********************//
onMounted(() => {})

//defineExpose( Object.assign({}, that) )

</script>