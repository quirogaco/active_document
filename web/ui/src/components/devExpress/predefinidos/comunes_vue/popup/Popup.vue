<template src="./Popup.html">
</template>

<script setup lang="ts">
//import DxForm from 'devextreme-vue/form';
import { 
    getCurrentInstance, 
    ref, 
    onMounted 
} from "vue";
import { DxPopup, DxPosition, DxToolbarItem } from 'devextreme-vue/popup';
import { DxScrollView } from 'devextreme-vue/scroll-view';
import DxButton from 'devextreme-vue/button';
import basicAttributes from './basicAttributes.js';
//import utilities from "./utilities.js";
import { methodsPopup } from './methods.js';
import { eventsPopup } from './methods.js';

// this -> that component
let that = getCurrentInstance().ctx;

// #################################
// properties, events and contexts #
// #################################
const methods = methodsPopup(that);
const events  = eventsPopup(that)

that.name = "Popup";
let reference = ref(null);

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
const emit = defineEmits(['mounted'])

// attributes
let attributes = Object.assign({}, props.attributes);

// basic grid attributes
let all_attributes = {
    ...basicAttributes.attributes,
    ...attributes
}

// console.log("popup_attributes:", all_attributes)

onMounted(() => {          
    //console.log("MOINTADO POPUP:", that)
    that.cmp = that.$refs.reference;
    that = $lib.assignAttributes(that, methods);
    that = $lib.assignAttributes(that, events);
    that.$emit('mounted', that);
})

</script>