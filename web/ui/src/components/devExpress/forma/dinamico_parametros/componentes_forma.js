import { DxForm }          from 'devextreme-vue/form';
import DxToolbar           from 'devextreme-vue/toolbar';
import { DxLoadIndicator } from 'devextreme-vue/load-indicator';
import { DxPopup }         from 'devextreme-vue/popup';
import { DxFileUploader }  from 'devextreme-vue/file-uploader';
import DxRadioGroup        from 'devextreme-vue/radio-group';
import DxTextArea          from 'devextreme-vue/text-area';
import DxTagBox            from 'devextreme-vue/tag-box';
import { DxLoadPanel }     from 'devextreme-vue/load-panel';

// #########################
// Componentes de la forma #
// #########################
let componentes = {
    "DxForm"         : DxForm,
    "DxToolbar"      : DxToolbar,
    "DxLoadIndicator": DxLoadIndicator,
    "DxPopup"        : DxPopup,
    "DxFileUploader" : DxFileUploader,
    "DxRadioGroup"   : DxRadioGroup,
    "DxTextArea"     : DxTextArea,
    "DxTagBox"       : DxTagBox,
    
    "DxLoadPanel"    : DxLoadPanel,
}   

export default {
    componentes: componentes,
}