import handlebars from 'handlebars';

// Atributos dos puntos, apuntan a opciones item de la forma
const plantillaDosPuntosDiccionario = function(atributos, nombre, margen="") {  
    /* 
    Genera texto interno.
    Ej:
    {{#each atributos}} 
        :dataField         = "opciones_items.nombres.dataField"        
        :name              = "opciones_items.nombres.name"
        :helpText          = "opciones_items.nombres.helpText"
        :label             = "opciones_items.nombres.label"                
        :editorType        = "opciones_items.nombres.editorType"
        :validationRules   = "opciones_items.nombres.validationRules"
        :editorOptions     = "opciones_items.nombres.editorOptions"  
    {{/each}}
    */
    let data = {
        "atributos": atributos,
        "nombre"   : nombre,
        "margen"   : margen
    };
    let textoPlantilla = '\n{{#each atributos}}        {{../margen}}:{{@key}} = "opciones_items.{{../nombre}}.{{@key}}" \n {{/each}}';
    let plantilla      = handlebars.compile(textoPlantilla);
    let resultado      = plantilla(data);
   
    return resultado;
};

// Plantilla completa cierra con componentes
const plantillaCompletaComponente = function(item="DxSimpleItem", textoInterno="", textoCuerpo="", margen="") {  
    /* 
    Genera texto completo.
    Ej:
        <{item}DxSimpleItem{item}
        {textoInterno}    
            :dataField         = "opciones_items.nombres.dataField"        
            :name              = "opciones_items.nombres.name"
            :helpText          = "opciones_items.nombres.helpText"
            :label             = "opciones_items.nombres.label"                
            :editorType        = "opciones_items.nombres.editorType"
            :validationRules   = "opciones_items.nombres.validationRules"
            :editorOptions     = "opciones_items.nombres.editorOptions"  
        {textoInterno}         
        />   
    */    
    let resultado = `\n   ${margen}<${item}\n ${textoInterno}\n   ${margen}>  ${textoCuerpo}\n   ${margen}</${item}>\n`

    return resultado;
};

// Plantilla contenido abierto ej. contenido HTML
const plantillaContenido = function(item="Contenido", textoInterno="", textoCuerpo="", margen="") {  
    /* 
    Genera texto completo.
    Ej:
        <{item}DxSimpleItem{item}
        {textoInterno}    
            :dataField         = "opciones_items.nombres.dataField"        
            :name              = "opciones_items.nombres.name"
            :helpText          = "opciones_items.nombres.helpText"
            :label             = "opciones_items.nombres.label"                
            :editorType        = "opciones_items.nombres.editorType"
            :validationRules   = "opciones_items.nombres.validationRules"
            :editorOptions     = "opciones_items.nombres.editorOptions"  
        {textoInterno}         
        />   
    */    
    let resultado = `\n   ${margen}\n ${textoInterno}\n   ${margen}  ${textoCuerpo}\n`

    return resultado;
};

// Genera template para componente
/*
<template #template_03="{ data }">
                <DxDataGrid
                    :onInitialized = "iniciaComponente"
                    :elementAttr   = "opciones_items.grilla_opciones.elementAttr"      
                >
                    <DxColumn data-field="FullName"></DxColumn>
                    <DxColumn data-field="Position"></DxColumn>                    
                    <DxColumn data-field="City" />
                    <DxColumn data-field="Country"></DxColumn>
                    <DxColumn data-field="Address" />
                    <DxColumn data-field="HomePhone" />
                    <DxColumn data-field="PostalCode" />
                </DxDataGrid>
</template>

<template #template_101="{ data }">  
   
 </template>

*/
const genera_template = function(template_consecutivo, textoCuerpo="") {
    let resultado = `\n <template #${template_consecutivo}="{ data }">  ${textoCuerpo}\n</template>\n`

    return resultado;
};

export default {
    plantillaDosPuntosDiccionario: plantillaDosPuntosDiccionario,
    plantillaCompletaComponente  : plantillaCompletaComponente,
    plantillaContenido           : plantillaContenido,
    genera_template              : genera_template
}