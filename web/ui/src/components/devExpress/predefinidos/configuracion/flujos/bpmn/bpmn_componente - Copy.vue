<template src="./bpmn_componente.html">
</template>

<script>
import DxButton from 'devextreme-vue/button';
import notify   from 'devextreme/ui/notify';
import { DxPopup } from 'devextreme-vue/popup'
import { DxScrollView } from 'devextreme-vue/scroll-view';
import visor    from './visor.js'

export default {
    name: 'vue-bpmn',
    
    components: {
        DxButton,
        DxPopup
    },

    props: {        
        attributes: {
            type: Object,
            default() {
                return {
                    xml: ""
                }
            }
        },
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
        this.bpmnViewer = visor.crea_visor(this, "#canvas-bpmn");  
        console.log("this.attributes:", this.attributes);
        if ( (this.attributes.xml == undefined) || (this.attributes.xml == "") ) {
            this.diagramXML = this.diagrama;
        }
        else {
            this.diagramXML = this.attributes.xml;
        }
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
            //let alto = Math.trunc( window.innerHeight * 0.75 ).toString() + "px"
            //return alto

            //return "1800px"
        },

        
        async leer_flujo() {
            try {
                const result = await this.bpmnViewer.saveXML({ format: true });
                return result
            } catch (err) {
                console.log(err);
                return null
            }            
        },
    }
};

</script>

<style>
@import 'bpmn-js/dist/assets/diagram-js.css';
@import 'bpmn-js/dist/assets/bpmn-font/css/bpmn.css';
@import 'bpmn-js/dist/assets/bpmn-font/css/bpmn-codes.css';
@import 'bpmn-js/dist/assets/bpmn-font/css/bpmn-embedded.css';
@import 'bpmn-js-properties-panel/dist/assets/bpmn-js-properties-panel.css';

.djs-palette {
  visibility: hidden;
  width     : 0px;
}

.panel {
    background-color: #F9F9FB !important;
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