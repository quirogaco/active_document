<template>
    <DataForma     
       ref             = "form"  
       :attributes     = "atributos_forma"
    />

    <div class="d-flex justify-content-center">
        <ToolBar    
            ref             = "barra"  
            :attributes     = "atributos_barra"
        />
    </div>

</template>

<script>
import { getCurrentInstance, ref, onMounted } from "vue";
import items_forma from "./items_forma";
import items_barra from "./items_barra";

let test = {
    name : 'test',
    props: {},

    // setup(props, { attrs, slots, emit, expose })
    setup(props) {
        let that = getCurrentInstance().ctx 
        // template form ref
        let form = ref(null)

        // form attributes
        let atributos_forma = {
            id      : "forma_emergente_gestion",
            formData: {},
            items   : items_forma.items,
            colCount: 1,            
        }  

        // toolbar attributes
        let atributos_barra = {
            id      : "barra_emergente_gestion",
            items   : items_barra.items,
        }  

        onMounted(() => {  
            let that = getCurrentInstance().ctx 
        })

        return {
            form,
            atributos_forma,
            atributos_barra
        }
    },

    // Metodos
    methods: {        
    }
}

export default test

</script>