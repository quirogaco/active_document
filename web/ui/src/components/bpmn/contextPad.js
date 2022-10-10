import BpmnJS                   from 'bpmn-js/lib/Modeler'
import propertiesPanelModule    from 'bpmn-js-properties-panel'
import propertiesProviderModule from 'bpmn-js-properties-panel/lib/provider/camunda'
//import camundaModdleDescriptor  from 'camunda-bpmn-moddle/resources/camunda'
//import camundaModdleExtension   from 'camunda-bpmn-moddle/lib'

//import Aprobado           from './personalizado/draw'
//import paletteProvider_ad from './personalizado/palette'

// CUSTOM
import customModule from './personalizado/acciones';
//import qaExtension from './custom/resources/qa';

// Paleta reducida
import paleta from './paleta.js'

const crea_visor = function(componente, container) {
    // Opciones
    let _options = Object.assign({
        container: container,
        
        propertiesPanel: {
            parent: '#js-properties-panel'
        },        
        
        
        additionalModules: [
            propertiesProviderModule,
            propertiesPanelModule,
            //camundaModdleExtension,

            //Aprobado,
            //paletteProvider_ad,

            customModule
        ],
                    
        moddleExtensions: {
            //camunda: camundaModdleDescriptor,
            //qa: qaExtension
        }     
    }, componente.options)

    // Crea visor
    let visor = new BpmnJS(_options);

    // Eventos
    visor.on('import.done', function(event) {
        var error    = event.error;
        var warnings = event.warnings;
        if (error) {
            //console.log('error', error);
        } else {
            //console.log('shown', warnings);
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

/*
const HIGH_PRIORITY = 1500;

const   qualityAssuranceEl = document.getElementById('quality-assurance'),
        suitabilityScoreEl = document.getElementById('suitability-score'),
        lastCheckedEl = document.getElementById('last-checked'),
        okayEl = document.getElementById('okay'),
        formEl = document.getElementById('form'),
        warningEl = document.getElementById('warning');

const carga_diagrama = async function(visor, diagramXML) {
    await visor.importXML(diagramXML).then(() => {
        const   moddle   = visor.get('moddle'),
                modeling = visor.get('modeling');                

        let analysisDetails,
            businessObject,
            element,
            suitabilityScore;

        // validate suitability score
        function validate() {
            const { value } = suitabilityScoreEl;

            if (isNaN(value)) {
            warningEl.classList.remove('hidden');
            okayEl.disabled = true;
            } else {
            warningEl.classList.add('hidden');
            okayEl.disabled = false;
            }
        }

        // open quality assurance if user right clicks on element
        visor.on('element.contextmenu', HIGH_PRIORITY, (event) => {
            event.originalEvent.preventDefault();
            event.originalEvent.stopPropagation();

            qualityAssuranceEl.classList.remove('hidden');

            ({ element } = event);

            // ignore root element
            if (!element.parent) {
            return;
            }

            businessObject = getBusinessObject(element);

            let { suitable } = businessObject;

            suitabilityScoreEl.value = suitable ? suitable : '';

            suitabilityScoreEl.focus();

            analysisDetails = getExtensionElement(businessObject, 'qa:AnalysisDetails');

            lastCheckedEl.textContent = analysisDetails ? analysisDetails.lastChecked : '-';

            validate();
            
        });
    })
}
*/