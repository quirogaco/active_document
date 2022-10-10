import entryFactory from "bpmn-js-properties-panel/lib/factory/EntryFactory";

export default function(element, translate) {

  return [
    Spell({id: "accion", element: element}, translate)
  ]
}

function Spell(props, translate) {
  const { element, id } = props;
  
  let field = entryFactory.textField(translate, {
    id           : "tipo_accion",
    description  : "Atributos gestión",
    label        : "Accion",
    modelProperty: "tipo_accion"
  })

  //console.log("field: ", field)

  return field
}
