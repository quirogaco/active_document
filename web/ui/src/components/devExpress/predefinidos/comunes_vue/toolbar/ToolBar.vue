<template src="./ToolBar.html">
</template>

<script>
import { getCurrentInstance, ref, onMounted } from "vue";

// ##################################
// barra de herramientas definition #
// ##################################
import DxToolbar from 'devextreme-vue/toolbar';

// ## COMPONENT ## 
let Toolbar = {
    name: 'Toolbar',

    emits: ['mounted'],

    components: {
        DxToolbar
    },

    props: {
        attributes: {
            type: Object,
            default() {
                return {}
            }
        },

    },

    // setup(props, { attrs, slots, emit, expose })
    setup(props, ctx) {
        const dxToolbar = ref(null);
        let toolbar_attrs = {};

        onMounted(() => {  
            let that      = getCurrentInstance().ctx;           
            that.instance = that.$refs.dxToolbar.instance;   
        
            // items de la barra de herramientas
            let items = (props.attributes.items != undefined ? props.attributes.items: []);   
            that.instance.option("items", items)
                        
            that.$emit('mounted', that);                           
        })

        return {
            dxToolbar,
            toolbar_attrs      
        }
    },

    methods: {}
}

export default Toolbar

</script>