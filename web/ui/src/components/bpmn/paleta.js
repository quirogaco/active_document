import ContextPadProvider       from 'bpmn-js/lib/features/context-pad'
import PaletteProvider          from 'bpmn-js/lib/features/palette'

// Propíedades de paleta
const _getContextPadEntries = ContextPadProvider.contextPadProvider[1].prototype.getContextPadEntries
ContextPadProvider.contextPadProvider[1].prototype.getContextPadEntries = function(element) {
    const entries = _getContextPadEntries.apply(this, [element]) 
    /*
    delete entries["append.intermediate-event"]
    delete entries["replace"]
    delete entries["connect"]
    */
    
    return entries;
}

// Propíedades de contexto
import {
    assign
} from 'min-dash';

const _getPaletteEntries = PaletteProvider.paletteProvider[1].prototype.getPaletteEntries
const _createAction      = _getPaletteEntries.createAction
console.log("_createAction:", _createAction)
/*
PaletteProvider.paletteProvider[1].prototype.getPaletteEntries = function(element) {
    const actions = _getPaletteEntries.apply(this, [element])
    
    delete actions['hand-tool']
    delete actions['lasso-tool']
    delete actions['space-tool']
    delete actions['global-connect-tool']
    delete actions['tool-separator']
    delete actions['create.intermediate-event']
    delete actions['create.data-object']
    delete actions['create.data-store']
    delete actions['create.subprocess-expanded']
    delete actions['create.participant-expanded']
    delete actions['create.group']
    
    
    actions['create.usertask'] = _createAction.apply(this,
        [
            'bpmn:UserTask', 'activity', 'bpmn-icon-task',
            translate('Tarea de usuario')
        ]
    )

    return actions;
}
*/

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

        'create.task': createAction(
            'bpmn:Task', 'activity', 'bpmn-icon-task',
            translate('Create Task')
        ),

        'create.usertask': createAction(
            'bpmn:UserTask', 'activity', 'bpmn-icon-user',
            translate('Tarea de usuario')
        )
    });
    
    return actions;
}

export default {}