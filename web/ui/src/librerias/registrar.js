import DataGrid  from "../components/devExpress/predefinidos/comunes_vue/grid/DataGrid.vue";
import DataForma from "../components/devExpress/predefinidos/comunes_vue/forma/component/DataForm.vue";
import ToolBar   from "../components/devExpress/predefinidos/comunes_vue/toolbar/ToolBar.vue";
import Popup     from "../components/devExpress/predefinidos/comunes_vue/popup/Popup.vue";

// Registrar componentes generales
let registrar_componentes = function(app) {
    app.component("DataGrid",  DataGrid);    
    app.component("DataForma", DataForma);   
    app.component("ToolBar", ToolBar);  
    app.component("Popup", Popup)     
}

export default {
    registrar_componentes: registrar_componentes   
}