<template src="./DataForm.html">
</template>

<script setup lang="ts">
import general_form from "@/comunes_vue/forma/forma.js";

import { 
    methodForm, 
    eventsDxForm 
} from "@/comunes_vue/forma/component/methods.js";

import { 
    getCurrentInstance, 
    ref,
    onMounted 
} 
from "vue";

let dxFormRef = ref(null);
// this -> that component
let that = getCurrentInstance().ctx;

// #################
// form definition #
// #################

// methods and events of the form
const methods = methodForm(that);
const events = eventsDxForm(that);

// devexpress fields definition
const dev_express_definition = function(items) {
    let definition_dev = [];
    for (const index in items) {
        // global definition to devexpress definition
        // It's not the component, just the definition object
        definition_dev.push(general_form.campo(items[index]));
    }

    return definition_dev
};


// assigns each field reference to the form
const nested_assign = function(items, form) {
    for (let index in items) {
        items[index].forma = form;
        // elementos, it is definition in spanish
        if (items[index].elementos != undefined) {
            nested_assign(items[index].elementos, form)
        }
   }

   return items
};

// #################################
// properties, events and contexts #
// #################################
that.name = "DataForm";

// must be declared as variables of the setup function script 
// to be exposed by default
const props = defineProps(general_form.forma_propiedades({}));
let parameters_received = general_form.lee_propiedades(props);
that.parameters_received = parameters_received;

// events
const emit = defineEmits(['mounted'])

// generic mounting action
general_form.forma_funciones.montado_general(that, props); 

// assign to that (this), methods and attributes
that = $lib.assignAttributes(that, methods);
that = $lib.assignAttributes(that, events);

onMounted(() => { 
    console.log(" MOUNTED that.$refs.dxFormRef--88:", that.$refs.dxFormRef.instance);  
    // // devexpress instance
    // that.instance = that.$refs.dxFormRef.instance;

    // // required for events, methods and fields of the form
    // that.instance.basicas = {
    //     "forma_id": that.parameters_received.config.id
    // };
    // that.formRef  = that.$refs.dxFormRef;
    
    // // assignment of items of the form
    // let items = (
    //     that.parameters_received.config.items != undefined ? 
    //     that.parameters_received.config.items: []
    // ); 
    // items = nested_assign(items, that.instance);
    // items = dev_express_definition(items);
    // that.instance.option("items", items);

    // // emit event of parent component
    // that.$emit('mounted', that);
});


defineExpose( Object.assign({}, that) );
</script>