import inherits from "inherits";

import RuleProvider from "diagram-js/lib/features/rules/RuleProvider";

export default function CustomRules(eventBus, elementRegistry) {
  RuleProvider.call(this, eventBus);

  this._elementRegistry = elementRegistry;
}

inherits(CustomRules, RuleProvider);

CustomRules.$inject = ["eventBus", "elementRegistry"];

CustomRules.prototype.init = function () {
  let self = this;
  this.addRule("connection.create", 2000, function (context) {
    console.log(context);
    //get xml diagram representation???
    console.log(context);
    console.log(self._elementRegistry.getAll());
    return false;
  });

  this.addRule("elements.delete", 2000, function (context) {
    console.log(context);
    if (
      context.elements[0].id === "StartEvent_1" ||
      context.elements[0].id === "EndEvent_1"
    ) {
      return false;
    }
  });

  this.addRule("shape.create", 2000, function (context) {
    console.log(context);
    //this rule is not working if element created from contextpad
    //console.log("created");
  });
};
