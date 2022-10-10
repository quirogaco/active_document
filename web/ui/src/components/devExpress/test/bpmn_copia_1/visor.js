
import BpmnJS                   from 'bpmn-js/lib/Modeler';
import propertiesPanelModule    from 'bpmn-js-properties-panel';
import propertiesProviderModule from 'bpmn-js-properties-panel/lib/provider/camunda';
import camundaModdleDescriptor  from 'camunda-bpmn-moddle/resources/camunda';
import camundaModdlePackage     from "camunda-bpmn-moddle/resources/camunda";
import camundaModdleExtension   from "camunda-bpmn-moddle/lib";

//..
//import propertiesPanelModule    from './bpmn-js-properties-panel';
//import propertiesProviderModule from './bpmn-js-properties-panel/lib/provider/camunda';
//import camundaModdleDescriptor  from './camunda-bpmn-moddle/resources/camunda';
//import camundaModdleExtension   from './camunda-bpmn-moddle/lib';

import acappella from "./provider";

const crea_visor = function(componente, container) {
    // Opciones
    let _options = Object.assign({
        container: container,
        
        propertiesPanel: {
            parent: '#js-properties-panel'
        },     
        
        additionalModules: [
            //camundaModdleExtension,
            propertiesPanelModule,
            propertiesProviderModule,   
            acappella
            //camundaModdleExtension,
        ],
                    
        moddleExtensions: {
            //camunda: camundaModdleDescriptor,
            camunda: camundaModdlePackage
        }     
    }, componente.options)

    // Crea visor
    let visor = new BpmnJS(_options);

    // Eventos
    visor.on('import.done', function(event) {
        var error    = event.error;
        var warnings = event.warnings;
        if (error) {
            console.log('error', error);
        } else {
            console.log('shown', warnings);
        }
    })


    return visor
}

const carga_diagrama = async function(visor, diagramXML) {
    await visor.importXML(diagramXML).then(() => {})
}

export default {
    crea_visor    : crea_visor,
    carga_diagrama: carga_diagrama
}