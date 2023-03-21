<script lang="ts">
import handlebars from 'handlebars';

let templates_text = `        
    <template #contenido-template="{data, index}">                
        <p v-html="data.editorOptions.value"></p>
    </template>
`;

let data = {
    "templates_text": templates_text
};

// {{{}}}, triple para caracteres especiales
let template_base = handlebars.compile(`        
    <DxForm                    
        ref="dxFormRef"
        v-bind="config_form"        
    > 

      {{{templates_text}}} 

    </DxForm>
`);

let template_form = template_base(data);

export default {
    template: template_form,
    components: {
        DxForm
    },
    data: () => {
        return {
            config_form: ref({})
        }
    }
}
</script>

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


// validate configuration information of the form
const validate_configuration = function(parameters_received)  {
    let config_form = parameters_received;
    if (
        (parameters_received.config != undefined) && 
        (parameters_received.config != null)
    ) {
        config_form = parameters_received.config;
    };
    
    return config_form;
};

// determines if the field definitions are in devexpress 
// or acappella format
const form_field_configuration = function(config_form)  {
    let fields_form = config_form.items;
    if (config_form.fields_format != "devexpress") {
        fields_form = nested_assign(fields_form, that.instance);
        fields_form = dev_express_definition(fields_form);
    };
    
    return fields_form;
};


// #################################
// properties, events and contexts #
// #################################
that.name = "DataForm";

// must be declared as variables of the setup function script 
// to be exposed by default
const props = defineProps(general_form.forma_propiedades({}));
that.parameters_received = general_form.lee_propiedades(props);

// 1. como hacer compatible parameters_received sin formato de config y data ?
// 2. como identificar si  items  son definiciones devexpress o 
//    basicas para convertir
let config_form = validate_configuration(that.parameters_received);
config_form.items = form_field_configuration(config_form);
console.log("-- config_form --", config_form)
console.log("-- config_form.items --", config_form.items)

// events
const emit = defineEmits(['mounted']);

// generic mounting action
general_form.forma_funciones.montado_general(that, props); 

// assign to that (this), methods and attributes
that = $lib.assignAttributes(that, methods);
that = $lib.assignAttributes(that, events);

onMounted(() => {
    // console.log(" onMounted DATAFORM THAT-0:", that);
    // console.log(" onMounted DATAFORM that.$refs.dxFormRef:", that.$refs.dxFormRef);
    // //console.log(" onMounted DATAFORM that.$refs.dxFormRef.instance:", that.$refs.dxFormRef.instance);  
    // console.log(" onMounted DATAFORM that.parameters_received:", that.parameters_received);  
    // devexpress class, access to attributes
    that.dxForm = that.$refs.dxFormRef;
    // devexpress instance (object), acces to functions, ej: option
    that.instance = that.$refs.dxFormRef.instance;

    // required for events, methods and fields of the form
    // validar sin no viene con config... ver 1
    console.log("that.parameters_received:", that.parameters_received)
    that.instance.basicas = {
        "forma_id": that.parameters_received.config.id
    };
    that.config_form.value = config_form;
    emit('mounted', that);
});

//defineExpose( Object.assign({}, that) );
</script>