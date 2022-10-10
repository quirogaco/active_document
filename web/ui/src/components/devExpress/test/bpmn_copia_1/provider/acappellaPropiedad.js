import entryFactory from "bpmn-js-properties-panel/lib/factory/EntryFactory";

import { is } from "bpmn-js/lib/util/ModelUtil";

export default function (group, element, translate) {
  console.log("group-0:", group)
  console.log("element-0:", element)
  // Only return an entry, if the currently selected
  // element is a start event.
  if (is(element, "bpmn:StartEvent")) {    
    
    group.entries.push(
      entryFactory.textField(translate, {
        id: "spell",
        description: "Atributos gestión",
        label: "Spell",
        modelProperty: "spell"
      })
    );
    
  }
}