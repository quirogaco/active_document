import imagenes from '../imagenes';

export default function PaletteProvider_ad(palette, create, elementFactory) {

  this._create = create;
  this._elementFactory = elementFactory;

  palette.registerProvider(this);
}

PaletteProvider_ad.$inject = [
  'palette',
  'create',
  'elementFactory'
];

PaletteProvider_ad.prototype.getPaletteEntries = function() {

  var elementFactory = this._elementFactory,
      create = this._create;

  function startCreate(event) {
    var serviceTaskShape = elementFactory.create(
      'shape', { type: 'bpmn:ServiceTask' }
    );

    create.start(event, serviceTaskShape);
  }

  return {
    /*
    'create.exclusive-gateway': createAction(
      'bpmn:ExclusiveGateway', 'gateway', 'bpmn-icon-gateway-none',
      translate('Create Gateway')
    ),
    */

    'create-service-task': {
      group: 'activity',
      title: 'Aprobar documento',
      imageUrl: imagenes.aprobado.dataUrl,
      action: {
        dragstart: startCreate,
        click: startCreate
      }
    }
  };
};