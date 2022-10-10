<template src="./DataForm.html">
</template>

<script setup lang="ts">

import forma_general from "@/comunes_vue/forma/forma.js";

import { 
    methodForm, 
    eventsDxForm 
} from "@/comunes_vue/forma/component/methods.js";

import { 
    getCurrentInstance, 
    onMounted 
} 
from "vue";

// this -> that component
let that = getCurrentInstance().ctx;

// #################
// form definition #
// #################
// En la definicion no existe todavia referencia a window.$form
const methods = methodForm(that);
const events  = eventsDxForm(that)

// ## ATTRIBUTES ## 
const devExpressAttributes = function(items) {
    let itemsDe = [];
    for (const index in items) {
        itemsDe.push(forma_general.campo(items[index]));
    }

    return itemsDe
};


const nested_assign = function(items, forma) {
    for (let index in items) {
        items[index].forma = forma;
        // elementos, es definición en español
        if (items[index].elementos != undefined) {
            nested_assign(items[index].elementos, forma)
        }
   }

   return items
};


// #################################
// properties, events and contexts #
// #################################
that.name       = "DataForm";

// properties
const props        = defineProps(forma_general.forma_propiedades({}));
let attrsReceived  = forma_general.lee_propiedades(props);
that.attrsReceived = attrsReceived;

// events
const emit = defineEmits(['mounted'])
console.log("emit:", emit)

// Accion basica al montar
forma_general.forma_funciones.montado_general(that, props); 

that = $lib.assignAttributes(that, methods);
that = $lib.assignAttributes(that, events);

onMounted(() => {   
    that.instance = that.$refs.dxFormRef.instance;
    that.instance.basicas = {
        "forma_id": that.attrsReceived.id
    } 
    that.formRef  = that.$refs.dxFormRef;
    // items de la forma
    let items = (that.attrsReceived.items != undefined ? that.attrsReceived.items: []); 
    items = nested_assign(items, that.instance);
    items = devExpressAttributes(items);
    that.instance.option("items", items)    
    that.$emit('mounted', that);
})

defineExpose( Object.assign({}, that) )

</script>