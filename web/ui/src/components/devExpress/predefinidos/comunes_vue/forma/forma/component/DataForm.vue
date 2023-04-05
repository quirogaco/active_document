<template src="./DataForm.html">
</template>

<script setup lang="ts">
import { getCurrentInstance, ref, onMounted } from "vue";

// this component
let that = getCurrentInstance().ctx;

// #################
// form definition #
// #################
import { 
    DxForm
} from 'devextreme-vue/form';
import DxSelectBox        from 'devextreme-vue/select-box';
import { DxFileUploader } from 'devextreme-vue/file-uploader';
import DxTextArea         from 'devextreme-vue/text-area';
// En la definicion no existe todavia referencia a window.$form
import forma_general      from "../../../comunes_vue/forma/forma.js"

// Imports component definition
import utilities from './utilities.js';
import { methodForm, eventsDxForm } from './methods.js';
const methods = methodForm(that);
const events  = eventsDxForm(that)

// ## ATTRIBUTES ## 
// dxForm basic attributesPass
import basicAttributes from './basicAttributes.js';

const devExpressAttributes = function(items) {
    let itemsDe = [];
    for (const index in items) {
        itemsDe.push(forma_general.campo(items[index]));
    }

    return itemsDe
}

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
const dxFormRef = ref(null);
let form        = that;

// properties
const props        = defineProps(forma_general.forma_propiedades({}));
let attrsReceived  = forma_general.lee_propiedades(props);
that.attrsReceived = attrsReceived;

// events
const emit = defineEmits(['mounted'])

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