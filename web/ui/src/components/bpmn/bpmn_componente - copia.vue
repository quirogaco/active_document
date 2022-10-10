<template>
    <div class="container-fluid shadow vh-100 p-1 mb-2 rounded">
        
        <div 
            ref     = "container"     
            width   = "100%"    
            :height = "alto"
            class   = "vh-100"
        ></div>
        
        <div 
            id   = "js-properties-panel" 
            class= "panel">
        </div>   
    
    </div>    
</template>

<script>
import BpmnJS                   from 'bpmn-js/lib/Modeler'
import propertiesPanelModule    from 'bpmn-js-properties-panel'
import propertiesProviderModule from 'bpmn-js-properties-panel/lib/provider/camunda'
import camundaModdleDescriptor  from 'camunda-bpmn-moddle/resources/camunda'
import camundaModdleExtension   from 'camunda-bpmn-moddle/lib'

import Aprobado           from './personalizado/draw'
import paletteProvider_ad from './personalizado/palette'
console.log("paletteProvider_ad:", paletteProvider_ad)

import paleta   from './paleta.js'

export default {
    name: 'vue-bpmn',

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
                "<bpmn:process id='Process_1' isExecutable='false'>" +
                "<bpmn:startEvent id='StartEvent_1'/>" +
                "</bpmn:process>" +
                "<bpmndi:BPMNDiagram id='BPMNDiagram_1'>" +
                "<bpmndi:BPMNPlane id='BPMNPlane_1' bpmnElement='Process_1'>" +
                "<bpmndi:BPMNShape id='_BPMNShape_StartEvent_2' bpmnElement='StartEvent_1'>" +
                "<dc:Bounds height='36.0' width='36.0' x='200.0' y='50.0'/>" +
                "</bpmndi:BPMNShape>" +
                "</bpmndi:BPMNPlane>" +
                "</bpmndi:BPMNDiagram>" +
                "</bpmn:definitions>"
        };
    },

    mounted: function () {
        var container = this.$refs.container;
        var self = this;
        var _options = Object.assign({
            container: container,
            
            propertiesPanel: {
                parent: '#js-properties-panel'
            },
            
            additionalModules: [
                propertiesProviderModule,
                propertiesPanelModule,
                camundaModdleExtension,

                Aprobado,
                paletteProvider_ad
            ],
                        
            moddleExtensions: {
                //camunda: camundaModdleDescriptor
            }     
        }, this.options)
        this.bpmnViewer = new BpmnJS(_options);
        this.bpmnViewer.on('import.done', function(event) {
            var error    = event.error;
            var warnings = event.warnings;
            if (error) {
                self.$emit('error', error);
            } else {
                self.$emit('shown', warnings);
            }
            self.bpmnViewer.get('canvas').zoom('fit-viewport');
        });
        
        if (this.url) {
            //this.fetchDiagram(this.url);
            this.diagramXML = this.diagrama
        }

    },

    beforeDestroy: function() {
        this.bpmnViewer.destroy();
    },

    watch: {
        url: function(val) {
            //this.$emit('loading');
            //this.fetchDiagram(val);
            this.diagramXML = this.diagrama
        },

        diagramXML: async function(val) {
            //console.log("diagramXML:", val)
            console.log("diagramXML:")
            await this.bpmnViewer.importXML(val)
        }
    },

    methods: {
        alto_visor() {
            let alto = Math.trunc( window.innerHeight * 0.75 ).toString() + "px"
            console.log("ALTO:", alto)
            return alto
        },

        fetchDiagram: function(url) {
            var self = this;
            fetch(url)
            .then(function(response) {
                return response.text();
            })
            .then(function(text) {
                self.diagramXML = text;
            })
            .catch(function(err) {
                self.$emit('error', err);
            });
        }
    }
};
</script>

<style>
@import 'bpmn-js/dist/assets/diagram-js.css';
@import 'bpmn-js/dist/assets/bpmn-font/css/bpmn.css';
@import 'bpmn-js/dist/assets/bpmn-font/css/bpmn-codes.css';
@import 'bpmn-js/dist/assets/bpmn-font/css/bpmn-embedded.css';
@import 'bpmn-js-properties-panel/dist/assets/bpmn-js-properties-panel.css';

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
</style>