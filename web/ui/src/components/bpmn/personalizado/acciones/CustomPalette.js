
let contador = 0

export default class CustomPalette {
  constructor(bpmnFactory, create, elementFactory, palette, translate) {
    this.bpmnFactory    = bpmnFactory;
    this.create         = create;
    this.elementFactory = elementFactory;
    this.translate      = translate;

    palette.registerProvider(this);
  }

  getPaletteEntries(element) {
    const {
      bpmnFactory,
      create,
      elementFactory,
      translate
    } = this;

    function createTask(accion) {      
      return function(event) {        
        const businessObject = bpmnFactory.create('bpmn:ServiceTask');

        contador  += 1;
        let id     = accion + "_" + contador;
        let nombre = accion + "_" + contador;       
        businessObject.id     = id;
        businessObject.name   = nombre;
        businessObject.accion = accion;

        const shape = elementFactory.createShape({
          type: 'bpmn:ServiceTask',
          businessObject: businessObject
        });

        create.start(event, shape);
      };
    }

    return {
      'create.aprobar': {
        group: 'activity',
        className: 'aprobar text-success',
        title: translate('Aprobar'),
        action: {
          dragstart: createTask("aprobar"),
          click: createTask("aprobar")
        }
      },
      'create.devolver': {
        group: 'activity',
        className: 'devolver text-warning',
        title: translate('Devolver'),
        action: {
          dragstart: createTask("devolver"),
          click: createTask("devolver")
        }
      },
      'create.trasladar': {
        group: 'activity',
        className: 'enviar text-primary',
        title: translate('Trasladar'),
        action: {
          dragstart: createTask("trasladar"),
          click: createTask("trasladar")
        }
      }
    };
  }
}

CustomPalette.$inject = [
  'bpmnFactory',
  'create',
  'elementFactory',
  'palette',
  'translate'
];