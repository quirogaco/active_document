let contador = 0

export default class CustomContextPad {
  constructor(bpmnFactory, config, contextPad, create, elementFactory, injector, translate) {
    this.bpmnFactory    = bpmnFactory;
    this.create         = create;
    this.elementFactory = elementFactory;
    this.translate      = translate;

    if (config.autoPlace !== false) {
      this.autoPlace = injector.get('autoPlace', false);
    }

    contextPad.registerProvider(this);
  }

  getContextPadEntries(element) {
    const {
      autoPlace,
      bpmnFactory,
      create,
      elementFactory,
      translate
    } = this;

    function appendServiceTask(accion) {
      return function(event, element) {
        if (autoPlace) {
          const businessObject = bpmnFactory.create('bpmn:UserTask');

          contador  += 1 
          let id     = accion + "_" + contador
          let nombre = accion + "_" + contador
          businessObject.id     = id
          businessObject.name   = nombre          
          businessObject.accion = accion
          
          const shape = elementFactory.createShape({
            type: 'bpmn:UserTask',
            businessObject: businessObject
          });

          autoPlace.append(element, shape);
        } else {
          appendServiceTaskStart(event, element);
        }
      };
    }

    function appendServiceTaskStart(accion) {
      return function(event) {
        const businessObject = bpmnFactory.create('bpmn:UserTask');

        businessObject.accion = accion;

        const shape = elementFactory.createShape({
          type: 'bpmn:UserTask',
          businessObject: businessObject
        });

        create.start(event, shape, element);
      };
    }

    return {
      'append.aprobar': {
        group: 'model',
        className: 'aprobar text-success',
        title: translate('Aprobar'),
        action: {
          click: appendServiceTask("aprobar"),
          dragstart: appendServiceTaskStart("aprobar")
        }
      },

      'append.devolver': {
        group: 'model',
        className: 'devolver text-warning',
        title: translate('Devolver'),
        action: {
          click: appendServiceTask("devolver"),
          dragstart: appendServiceTaskStart("devolver")
        }
      },

      'append.trasladar': {
        group: 'model',
        className: 'enviar text-primary',
        title: translate('Trasladar'),
        action: {
          click: appendServiceTask("trasladar"),
          dragstart: appendServiceTaskStart("trasladar")
        }
      }
    };
  }
}

CustomContextPad.$inject = [
  'bpmnFactory',
  'config',
  'contextPad',
  'create',
  'elementFactory',
  'injector',
  'translate'
];