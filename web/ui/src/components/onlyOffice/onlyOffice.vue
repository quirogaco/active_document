<template>
    <div
        :id="ideditor"
    >
    {{titulo}}
    </div>
</template>

<script>
    import { defineComponent } from 'vue'

    export default defineComponent({
        name: 'onlyOffice',
        components: {},
        props: {
            titulo   : String,
            urlLeer  : String,
            urlSalvar: String,
            ideditor : String
        },
        setup(props) {                   
            return {}
        }
    });
</script>