let plantilla_base = `
<div class="container-fluid shadow-sm p-3 mb-5 bg-forma rounded" style=" height:800px ">
    <div class="container align-bottom" style="">
        <DxLoadPanel
            v-model:visible = "loadIndicatorVisible"
            message         = "Por favor espere"               
            shading-color   = "rgba(0,0,0,0.4)"
        />

        <div class="long-title centered">{{titulo}}</div>
        
        <div class=" centered " style="">
            <DxForm
                ref                 = "referencia"            
                :form-data          = "formaDatos"
                :items              = "campos"  
                :disabled           = "deshabilitada"
                :customizeItem      = "personalizaElemento"
                :colCount           = "columnasForma"
                :width              = "800"        
                
                :onInitialized      = "inicializado"
                :onContentReady     = "contenido_listo"
            >
            <!-- !TEMPLATES! -->
            </DxForm>
        </div>


        <div class="separador" />

        <DxToolbar
            ref       = "referenciaToolbar"
            :disabled = "toolbar"
            :visible  = "barraVisible"
            :items    = "elementosBarra"
        />

        <DxPopup
            v-model:visible         = "popupVisible"
            :drag-enabled           = "false"
            :close-on-outside-click = "true"
            :show-title             = "true"
            :width                  = "800"
            :height                 = "450"
            :title                  = "popupTitulo"
        >           
            <span style="white-space: pre-wrap;" >
                <b>{{popupMensaje}}</b>                
            </span>            
        </DxPopup>   
    </div>
</div>
`;


let crea_plantilla = function(configuracion) {
    let plantillaAtributos     = window.$librerias.cargaAtributo(configuracion, 'plantillaAtributos', {});
    let plantillas             = window.$librerias.cargaAtributo(plantillaAtributos, 'texto_plantilla', []);
    let textoPlantilla         = plantillas.join(' ');
    let textoCompleto          = plantilla_base.replace('<!-- !TEMPLATES! -->', textoPlantilla);

    return textoCompleto    
};

export default {
    crea_plantilla: crea_plantilla
}