import ContextPadProvider       from 'bpmn-js/lib/features/context-pad'
import PaletteProvider          from 'bpmn-js/lib/features/palette'

/*
// Propíedades de paleta
const _getContextPadEntries = ContextPadProvider.contextPadProvider[1].prototype.getContextPadEntries;
//console.log("_getContextPadEntries:", _getContextPadEntries)
//console.log("ContextPadProvider.contextPadProvider[1]:", ContextPadProvider.contextPadProvider[1])

function appendAction(type, className, title, options) {
    console.log(">>>>:", _getContextPadEntries._translate)

    if (typeof title !== 'string') {
      options = title;
      title =  _getContextPadEntries._translate('Append {type}', { type: type.replace(/^bpmn:/, '') });
    }

    function appendStart(event, element) {

      var shape = elementFactory.createShape(assign({ type: type }, options));
      create.start(event, shape, {
        source: element
      });
    }


    var append = autoPlace ? function(event, element) {
      var shape = elementFactory.createShape(assign({ type: type }, options));

      autoPlace.append(element, shape);
    } : appendStart;


    return {
      group: 'model',
      className: className,
      title: title,
      action: {
        dragstart: appendStart,
        click: append
      }
    };
}


// Manejo de opciones menu de contexto cuando se selecciona un objeto visual en el flujo
ContextPadProvider.contextPadProvider[1].prototype.getContextPadEntries = function(element) {
    console.log("THIS:", this)

    const entries = _getContextPadEntries.apply(this, [element]) 

    
    let newEntrie = appendAction(
        this, 
        'bpmn:UserTask',
        'bpmn-icon-usertask',
        'Adiciona tarea de usuario'       
    )
    
    console.log("_getContextPadEntries.appendAction:", newEntrie)
    console.log("entries:", entries)
    
    delete entries["append.intermediate-event"]
    delete entries["append.text-annotation"]
    delete entries["replace"]
    delete entries["connect"]


    // user taks
    
    let options = Object.assign(entries["append.append-task"], {})
    options["className"] = "bpmn-icon-user-task";
    options["group"]     = "model";
    options["title"]     = "Adiciona tarea de usuario";
    entries["append.append-usertask"] = options
    delete entries["append.append-task"]
    
    
    return entries;
}
*/

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

    /*
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
        )
    });
    */
    
    return actions;
}

export default {}