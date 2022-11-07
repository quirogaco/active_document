<script setup lang="ts">
import DxForm from 'devextreme-vue/form';
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

// 1. como hacer compatible parameters_received sin formato de config y data ?
// 2. como identificar si  items  son definiciones devexpress o 
//    basicas para convertir
let fields_form = (
    that.parameters_received.config.items != undefined ? 
    that.parameters_received.config.items: []
); 
that.parameters_received.config.items = [];
//that.name = that.parameters_received.config.name;

// events
const emit = defineEmits(['mounted']);

// generic mounting action
general_form.forma_funciones.montado_general(that, props); 

// assign to that (this), methods and attributes
that = $lib.assignAttributes(that, methods);
that = $lib.assignAttributes(that, events);

onMounted(() => {
    console.log(" onMounted DATAFORM that.$refs.dxFormRef:", that.$refs.dxFormRef);
    console.log(" onMounted DATAFORM that.$refs.dxFormRef.instance:", that.$refs.dxFormRef.instance);  
    console.log(" onMounted DATAFORM that.parameters_received:", that.parameters_received);  
    // devexpress class, access to attributes
    that.dxForm = that.$refs.dxFormRef;
    // devexpress instance (object), acces to functions, ej: option
    that.instance = that.$refs.dxFormRef.instance;

    // required for events, methods and fields of the form
    // validar sin no viene copn config... ver 1
    that.instance.basicas = {
        "forma_id": that.parameters_received.config.id
    };
    
    // crea items en formato devexpress por sin no vienen asi ? ver 1.
    //fields_form = nested_assign(fields_form, that.instance);
    //fields_form = dev_express_definition(fields_form);
    that.instance.option("items", fields_form);
    //that.instance.option("items", null);

    // emit events of parent component
    //that.$emit('mounted', that);
    emit('mounted', that);
});


defineExpose( Object.assign({}, that) );
</script>

<script lang="ts">
import { defineComponent, ref, h } from "vue";

export default defineComponent({
  render() {
    let div = h("div", {}, `

        <DxForm        
            ref= "dxFormRef"
            v-bind= "parameters_received.config"        
        > 

            <template #contenido-template="{data, index}">                
                <p v-html="data.editorOptions.value"></p>
            </template>
                
        </DxForm>
    `);
    console.log("DIV->", div)
    
    return div
  }
})
</script>