import PaletteProvider          from 'bpmn-js/lib/features/palette'

// Propíedades de palette
import {
    assign
} from 'min-dash';

const _getPaletteEntries = PaletteProvider.paletteProvider[1].prototype.getPaletteEntries
const _createAction      = _getPaletteEntries.createAction

PaletteProvider.paletteProvider[1].prototype.getPaletteEntries = function(element) {  
    var actions = {},
        create = this._create,
        elementFactory = this._elementFactory,
        spaceTool = this._spaceTool,
        lassoTool = this._lassoTool,
        handTool = this._handTool,
        globalConnect = this._globalConnect,
        translate = this._translate;

    function createAction(type, group, className, title, options) {

        function createListener(event) {
            var shape = elementFactory.createShape(assign({ type: type }, options));

            if (options) {
                shape.businessObject.di.isExpanded = options.isExpanded;
            }

            create.start(event, shape);
        }

        var shortType = type.replace(/^bpmn:/, '');

        return {
            group: group,
            className: className,
            title: title || translate('Create {type}', { type: shortType }),
            action: {
                dragstart: createListener,
                click: createListener
            }
        };
    }

    
    assign(actions, {
        'create.start-event': createAction(
            'bpmn:StartEvent', 'event', 'bpmn-icon-start-event-none',
            translate('Create StartEvent')
        ),

        'create.end-event': createAction(
            'bpmn:EndEvent', 'event', 'bpmn-icon-end-event-none',
            translate('Create EndEvent')
        ),

        'create.exclusive-gateway': createAction(
            'bpmn:ExclusiveGateway', 'gateway', 'bpmn-icon-gateway-none',
            translate('Create Gateway')
        ),

        'create.usertask': createAction(
            'bpmn:UserTask', 'activity', 'bpmn-icon-user',
            translate('Tarea de usuario')
        ),

        'global-connect-tool': {
            group: 'tools',
            className: 'bpmn-icon-connection-multi',
            title: translate('Activate the global connect tool'),
            action: {
              click: function(event) {
                globalConnect.start(event);
              }
            }
          },
    });
    
    
    return actions;
}

export default {}