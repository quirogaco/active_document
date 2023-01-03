<template>
    <DxDataGrid
        v-bind = "grid_attributes"
        v-on = "events"
    >
    </DxDataGrid>
</template>

<script setup lang="ts">
// #################################
// Import components and libraries #
// #################################
import { getCurrentInstance, ref, onMounted } from "vue";
import { DxDataGrid } from 'devextreme-vue/data-grid';

// this component
let that = getCurrentInstance().ctx;

// Imports component definition
import utilities from "./utilities.js";
import { methodDataGrid, eventsDxDataGrid } from './methods.js';
const methods = methodDataGrid(that);
const events  = eventsDxDataGrid(that)

import basicAttributes from './basicAttributes.js';

// #################################
// properties, events and contexts # 
// #################################

that.name = "DataGrid";
let dxGridRef = ref(null);

// properties
const props = defineProps({
    attributes: {
        type: Object,
        default() {
            return {}
        }
    }
})

// events
const emit = defineEmits(['mounted', 'clickRow', 'dblClickCell'])

// attributes
let attributes = Object.assign({}, props.attributes);

 // create columns
let columns = utilities.createColumns(attributes.columns);
attributes.columns = columns;

// create data source type
if (attributes.dataSource == undefined) {
    attributes.dataSource = []
}
let source = utilities.createDataSource(attributes.dataSource);
//attributes.dataSource.dataSource = source;
attributes.dataSource = source;

// create toolbar
if (attributes.toolbar !== undefined) {
    attributes.toolbar = utilities.createToolbar(
        basicAttributes.attributes, 
        attributes.toolbar
    )
}

// basic grid attributes
let grid_attributes = {
    ...basicAttributes.attributes,
    ...attributes
}

onMounted(() => {          
    that.name   = name;
    that.dxGrid = that.$refs.grid;
    that = $lib.assignAttributes(that, methods);
    that = $lib.assignAttributes(that, events);
    that.$emit('mounted', that);
})

</script>