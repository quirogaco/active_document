// Require your custom property entries.
import acappellaPropiedad from "./acappellaPropiedad";

var LOW_PRIORITY = 500;

// Create the custom gestión tab.
// The properties are organized in groups.
function createGestionTabGroups(element, translate) {
  // Create a group called "Gestión".
  var blackGestionGroup = {
    id     : "gestion",
    label  : "Gestión atributos",
    entries: []
  };

  // Add the spell props to the gestión group.
  acappellaPropiedad(blackGestionGroup, element, translate);

  return [blackGestionGroup];
}

export default function GestionPropertiesProvider(propertiesPanel, translate) {
  this.getTabs = function (element) {
    return function (entries) {
      
      var gestionTab = {
        id    : "gestion",
        label : "Gestión",
        groups: createGestionTabGroups(element, translate)
      };

      entries.push(gestionTab);
      return entries;
    };
  };

  // Register our custom magic properties provider.
  // Use a lower priority to ensure it is loaded after the basic BPMN properties.
  propertiesPanel.registerProvider(LOW_PRIORITY, this);
}

GestionPropertiesProvider.$inject = ["propertiesPanel", "translate"];