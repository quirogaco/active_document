import BpmnJS from 'bpmn-js/lib/Modeler';
import propertiesPanelModule    from 'bpmn-js-properties-panel';
import propertiesProviderModule from 'bpmn-js-properties-panel/lib/provider/camunda';

// Paleta reducida
import palette from './custom_palette/palette/palette.js';

// Render de tareas de usuarios especificas
import customRenderer from './custom_render';

// context pad custom
import customPad from './custom_pad/pad.js';

// comandos interceptor
import MyCommandInterceptor from "./command/MyCommandInterceptor.js";

// reglas personalizdas
import customRules from "./customRule/customRules.js";

// atributos de panel de propiedades
import gestionPropertiesProviderModule from './properties/gestion';
import gestionModdleDescriptor         from './descriptors/gestion';

const crea_visor = function(componente, container) {
    // Opciones
    let _options = Object.assign({
        container: container,

        propertiesPanel: {
            parent: '#js-properties-panel'
        },             
        
        additionalModules: [
            propertiesPanelModule,
            propertiesProviderModule,
            gestionPropertiesProviderModule,
            customPad.overrideContextPadProvider,
            customRules,
            customRenderer,
            MyCommandInterceptor,
            {
                //moveCanvas: [ 'value', '' ],
                zoomScroll: [ 'value', '' ]
            } 
        ],
                    
        moddleExtensions: {
            gestion: gestionModdleDescriptor
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

    visor.on('element.click', function(event) {
        //console.log('visor->element.click:', event);
    })
    //*/

    return visor
}

const carga_diagrama = async function(visor, diagramXML) {
    await visor.importXML(diagramXML).then(() => {})
}

export default {
    crea_visor    : crea_visor,
    carga_diagrama: carga_diagrama
}