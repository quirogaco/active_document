import librerias  from '../../../../librerias/librerias.js'
import tab_objeto from './tab_objeto.js'

// Tab panel
const tab_panel_objeto = function(atributos={}) {
    // Manejo de titulos
    let nombre          = librerias.cargaAtributo(atributos, "nombre",  null)   
    let expandir        = librerias.cargaAtributo(atributos, "expandir", null)
    let cssClase        = librerias.cargaAtributo(atributos, "cssClase", "bg_tab_panel")
    let elementos       = librerias.cargaAtributo(atributos, "elementos", [])
    let visible         = librerias.cargaAtributo(atributos, "visible", true)
    let opciones        = librerias.cargaAtributo(atributos, "opciones", true)
    let deferRendering  = librerias.cargaAtributo(atributos, "retrasado", "no")
    deferRendering = deferRendering == "si" ? true : false;

    // Opciones dede ser validado aqui.

    // Tabs
    let tabs = [];
    let elemento;
    for (const indice in elementos) {
        elemento = elementos[indice];
        tabs.push(tab_objeto.tab_objeto(elemento))
    }
    
    let tabPanelOptions = {
        'deferRendering' : deferRendering,
    }

    // Definición de la columna
    let definicion = {
        "itemType"       : 'tabbed', 
        "name"           : nombre,
        "nombre"         : nombre,
        "tabPanelOptions": opciones,
        "visible"        : visible,
        "tabs"           : tabs,
        "colSpan"        : expandir,
        'cssClass'       : cssClase,     
        'tabPanelOptions': tabPanelOptions   
        
    }
    
    return definicion;
}


export default {
    tab_panel_objeto: tab_panel_objeto
}