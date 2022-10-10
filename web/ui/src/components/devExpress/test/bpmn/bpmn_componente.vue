<template src="./bpmn_componente.html">
</template>

<script>
import DxButton from 'devextreme-vue/button';
import notify   from 'devextreme/ui/notify';
import visor    from './visor.js'

export default {
    name: 'vue-bpmn',
    
    components: {
        DxButton
    },

    props: {
        url: {
            type: String,
            required: true
        },
        options: {
            type: Object
        }
    },

    data: function() {
        return {
            diagramXML: null,
            alto      : this.alto_visor(),
            diagrama  : 
                "<?xml version='1.0' encoding='UTF-8'?>" +
                "<bpmn:definitions xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xmlns:bpmn2='http://www.omg.org/spec/BPMN/20100524/MODEL' xmlns:bpmndi='http://www.omg.org/spec/BPMN/20100524/DI' xmlns:dc='http://www.omg.org/spec/DD/20100524/DC' xmlns:di='http://www.omg.org/spec/DD/20100524/DI' xsi:schemaLocation='http://www.omg.org/spec/BPMN/20100524/MODEL BPMN20.xsd' id='sample-diagram' targetNamespace='http://bpmn.io/schema/bpmn'>" +
                    
                    "<bpmn:process id='Gestion_proceso' isExecutable='true'>" +
                        "<bpmn:startEvent id='Evento_inicial_1'/>" +
                    "</bpmn:process>" +

                    "<bpmndi:BPMNDiagram id='BPMNDiagram_1'>" +
                        "<bpmndi:BPMNPlane id='BPMNPlane_1' bpmnElement='Gestion_proceso'>" +
                            "<bpmndi:BPMNShape id='_BPMNShape_StartEvent_2' bpmnElement='Evento_inicial_1'>" +
                                "<dc:Bounds height='36.0' width='36.0' x='200.0' y='50.0'/>" +
                            "</bpmndi:BPMNShape>" +
                        "</bpmndi:BPMNPlane>" +
                    "</bpmndi:BPMNDiagram>" +
                    
                "</bpmn:definitions>"
        };
    },

    mounted: function () {
        this.bpmnViewer = visor.crea_visor(this, this.$refs.container) 
        //if (this.url) {
            this.diagramXML = this.diagrama
        //}
    },

    beforeDestroy: function() {
        this.bpmnViewer.destroy();
    },

    watch: {
        url: function(val) {
            this.diagramXML = this.diagrama
        },

        diagramXML: async function(diagramXML) {
            visor.carga_diagrama(this.bpmnViewer, diagramXML) 
        }
    },

    methods: {
        alto_visor() {
            let alto = Math.trunc( window.innerHeight * 0.75 ).toString() + "px"
            return alto
        },

        async salvar_flujo(e) {
            const buttonText = e.component.option('text');
            try {
                const result = await this.bpmnViewer.saveXML({ format: true });
                const { xml } = result;
                console.log(xml);
            } catch (err) {
                console.log(err);
            }
            notify(`The ${buttonText} button was clicked`);
        },
    }
};
/*

.djs-palette {
  visibility: hidden;
  width: 0px;
}
*/
</script>

<style>
@import 'bpmn-js/dist/assets/diagram-js.css';
@import 'bpmn-js/dist/assets/bpmn-font/css/bpmn.css';
@import 'bpmn-js/dist/assets/bpmn-font/css/bpmn-codes.css';
@import 'bpmn-js/dist/assets/bpmn-font/css/bpmn-embedded.css';
@import 'bpmn-js-properties-panel/dist/assets/bpmn-js-properties-panel.css';

.djs-palette {
  visibility: hidden;
  width: 0px;
}

.containers{
    position: absolute;
    background-color: #ffffff;
    width: 100%;
    height: 100%;
}

.canvas{
    width: 100%;
    height: 100%;
}

.panel{
    position: absolute;
    right: 0;
    top: 0;
    width: 300px;
}

/* fontawesome codigo para iconos de paleta BPMN */
.aprobar::after {
    font-family: "Font Awesome 5 Free";
    font-weight: 900;
    content: "\f14a";
    background-color: yellow;
}

.asignar::before {
    font-family: "Font Awesome 5 Free";
    font-weight: 900;
    content: "\f138";
    background-color: #C1D3F8;
}

.radicar::before {
    font-family: "Font Awesome 5 Free";
    font-weight: 900;
    content: "\f5ac";
    background-color: #F8E6C1;
}

.gestionar::before {
    font-family: "Font Awesome 5 Free";
    font-weight: 900;
    content: "\f4fe";
    background-color: #81FE92;
}

</style>