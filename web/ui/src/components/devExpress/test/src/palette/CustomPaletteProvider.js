export default class CustomPaletteProvider {
  constructor(palette, elementFactory, create, translate) {
    this._elementFactory = elementFactory;
    this._create = create;
    this._translate = translate;

    palette.registerProvider(this);
  }

  getPaletteEntries(element) {
    const elementFactory = this._elementFactory;
    const create = this._create;
    const translate = this._translate;

    function createServiceTask(event) {
      const shape = elementFactory.createShape({
        type: "bpmn:ServiceTask"
      });

      shape.businessObject["type"] = "external";
      shape.businessObject["topic"] = "foo";

      console.log(shape.businessObject);

      create.start(event, shape);
    }

    return {
      "create.service-task": {
        group: "activity",

        className: "bpmn-icon-service-task",

        title: translate("Create ServiceTask"),

        action: {
          dragstart: createServiceTask,

          click: createServiceTask
        }
      }
    };
  }
}

CustomPaletteProvider.$inject = [
  "palette",
  "elementFactory",
  "create",
  "translate"
];
