<template>
    <div class="containers" ref="contenedor">
        <div class="canvas" ref="canvas"></div>
        <div id="js-properties-panel" class="panel"></div>        
    </div>
</template>

<script>
import BpmnJS                   from 'bpmn-js/lib/Modeler'
import ContextPadProvider       from 'bpmn-js/lib/features/context-pad'
import PaletteProvider          from 'bpmn-js/lib/features/palette'
import propertiesPanelModule    from 'bpmn-js-properties-panel'
import propertiesProviderModule from 'bpmn-js-properties-panel/lib/provider/camunda'
import camundaModdleDescriptor  from 'camunda-bpmn-moddle/resources/camunda'

// Propíedades de paleta
const _getContextPadEntries = ContextPadProvider.contextPadProvider[1].prototype.getContextPadEntries
ContextPadProvider.contextPadProvider[1].prototype.getContextPadEntries = function(element) {
    const entries = _getContextPadEntries.apply(this, [element]) 
    delete entries["append.end-event"]
    delete entries["append.intermediate-event"]
    delete entries["append.gateway"]
    delete entries["append.append-task"]
    delete entries["append.text-annotation"]
    delete entries["replace"]

    return entries;
}

// Propíedades de contexto
const _getPaletteEntries = PaletteProvider.paletteProvider[1].prototype.getPaletteEntries
PaletteProvider.paletteProvider[1].prototype.getPaletteEntries = function(element) {
    const actions = _getPaletteEntries.apply(this, [element])
    delete actions['hand-tool']
    
    return actions;
}

export default {
    data () {
        return {
            bpmnModeler: null,
            container  : null,
            canvas     : null,
            xmlStr     : null,
            processName: ''
        }
    },

    methods: {
        async createNewDiagram () {
            const diagrama =
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
                "</bpmn:definitions>";
            
            /*
            this.bpmnModeler.importXML(diagrama, function (err) {
                if (err) {
                    console.error(err)
                }
            })
            */
            
            console.log("diagrama-0:", this.bpmnModeler)
            await this.bpmnModeler.importXML(diagrama)
            console.log("diagrama-1:", diagrama)
            // access modeler components
            var canvas   = this.bpmnModeler.get('canvas');
            var overlays = this.bpmnModeler.get('overlays');


            // zoom to fit full viewport
            canvas.zoom('fit-viewport');
        },
    
        saveSVG (done) {
            this.bpmnModeler.saveSVG(done)
        },

        saveDiagram (done) {
            this.bpmnModeler.saveXML({ format: true }, function (err, xml) {
                done(err, xml)
            })
        },

        setEncoded (link, name, data) {
            const encodedData = encodeURIComponent(data)
            this.xmlStr = data
            if (data) {
                link.className = 'active'
                link.href = 'data:application/bpmn20-xml;charset=UTF-8,' + encodedData
                link.download = name
            }
        }
    },

    mounted () {
        this.container = this.$refs.contenedor
        const canvas   = this.$refs.canvas

        /*
        this.bpmnModeler = new BpmnJS({
            container: canvas,
            keyboard: {
                bindTo: window
            }
        });
        */
        
        
        this.bpmnModeler = new BpmnJS({
            container      : canvas,
            
            propertiesPanel: {
                parent: '#js-properties-panel'
            },

            additionalModules: [
                propertiesProviderModule,
                propertiesPanelModule
            ],
                        
            moddleExtensions: {
                camunda: camundaModdleDescriptor
            }     
        })
        

        let _this              = this
        const downloadLink     = this.$refs.saveDiagram
        const downloadSvgLink  = this.$refs.saveSvg
        this.bpmnModeler.on('commandStack.changed', function () {
            _this.saveSVG(function (err, svg) {
                _this.setEncoded(downloadSvgLink, 'diagram.svg', err ? null : svg)
            })
            _this.saveDiagram(function (err, xml) {
                _this.setEncoded(downloadLink, 'diagram.bpmn', err ? null : xml)
            })
        })
        
        this.createNewDiagram()
    }
}
</script>

<style lang="scss">
@import 'bpmn-js/dist/assets/diagram-js.css';
@import 'bpmn-js/dist/assets/bpmn-font/css/bpmn.css';
@import 'bpmn-js/dist/assets/bpmn-font/css/bpmn-codes.css';
@import 'bpmn-js/dist/assets/bpmn-font/css/bpmn-embedded.css';
@import 'bpmn-js-properties-panel/dist/assets/bpmn-js-properties-panel.css';
.containers{
    position: absolute;
    background-color: #ffffff;
    width: 100%;
    height: 90%;
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
.buttons{
    position: absolute;
    left: 20px;
    bottom: 20px;
    &>li{
    display:inline-block;margin: 5px;
    &>a{
        color: #999;
        background: #eee;
        cursor: not-allowed;
        padding: 8px;
        border: 1px solid #ccc;
        &.active{
        color: #333;
        background: #fff;
        cursor: pointer;
        }
    }
    }
}
</style>