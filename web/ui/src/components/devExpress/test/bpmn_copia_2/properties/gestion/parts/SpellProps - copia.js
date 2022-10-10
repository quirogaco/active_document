import { TextFieldEntry, isTextFieldEntryEdited } from '@bpmn-io/properties-panel';
//import { useService } from 'bpmn-js-properties-panel'

import { useService } from 'bpmn-js-properties-panel'

console.log("useService:", useService)

export default function(element) {

  return [
    {
      id       : 'spell',
      component: Spell({id: "spell", element: element}),
      isEdited : isTextFieldEntryEdited
    }
  ];

  /*
  return [
    {
      id: 'spell',
      component: <Spell id="spell" element={ element } />,
      isEdited: isTextFieldEntryEdited
    }
  ];
  */
}

function Spell(props) {
  const { element, id } = props;

  const modeling = useService('modeling');
  const translate = useService('translate');
  const debounce = useService('debounceInput');

  const getValue = () => {
    return element.businessObject.spell || '';
  }

  const setValue = value => {
    return modeling.updateProperties(element, {
      spell: value
    });
  }

  textField({
    id         : id,
    element    : element,
    description: translate('Apply a black magic spell'),
    label      : translate('Spell'),
    getValue   : getValue,
    setValue   : setValue,
    debounce   : debounce 
  })

  /*
  return <TextFieldEntry
    id={ id }
    element={ element }
    description={ translate('Apply a black magic spell') }
    label={ translate('Spell') }
    getValue={ getValue }
    setValue={ setValue }
    debounce={ debounce }
  />
  */
}
