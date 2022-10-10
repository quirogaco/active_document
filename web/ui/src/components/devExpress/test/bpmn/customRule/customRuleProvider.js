import inherits from "inherits";

import RuleProvider from "diagram-js/lib/features/rules/RuleProvider";

export default function CustomRules(eventBus, elementRegistry) {
  RuleProvider.call(this, eventBus);

  console.log("0-crea custom rule", elementRegistry);

  this._elementRegistry = elementRegistry;
}

inherits(CustomRules, RuleProvider);

CustomRules.$inject = ["eventBus", "elementRegistry"];

CustomRules.prototype.init = function () {
    let self = this;
    console.log("1-crea custom rule");

    
    this.addRule("connection.create", 2000, function (context) {
        // solo retorna false, o no retornar nada
        // si retorna true genera error
        console.log("connection.create", context.source.type, context.target.type);

        //return false;
    });

    this.addRule("elements.delete", 2000, function (context) {
        // permite ocultar icono de borrado en contextpad

        //console.log("elements.delete", context);
        
        //return false;        
    });

    this.addRule("elements.create", 2000, function (context) {
        //this rule is not working if element created from contextpad
        console.log("elements.create", context);
        
        return false;        
    });

    this.addRule("shape.append", 2000, function (context) {
        //this rule is not working if element created from contextpad
        console.log("shape APPEND --->");
        
        return false;
    });

    this.addRule("shape.create", 2000, function (context) {
        //this rule is not working if element created from contextpad
        console.log("shape CREATE --->");
        
        return false;
    });

};