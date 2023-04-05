import { on }      from "devextreme/events"
import { confirm } from 'devextreme/ui/dialog'


const campo_template = function(datos, nuevo_campo) {
    console.log("datos:", datos)
    nuevo_campo.editorOptions.modo = undefined
    switch (datos.tipo) {
        case "texto":
            nuevo_campo.template           = "campo_texto"  
            nuevo_campo.editorOptions.modo = "text"  
            break

        case "area_texto":
            nuevo_campo.template = "campo_area"  
            break

        case "entero":
            nuevo_campo.template = "campo_numerico"  
            break

        case "fecha":
            nuevo_campo.template                              = "campo_fecha" 
            nuevo_campo.editorOptions.type                    = "datetime"
            nuevo_campo.editorOptions.openOnFieldClick        = true
            nuevo_campo.editorOptions.dateSerializationFormat = "yyyy-MM-dd"  
            nuevo_campo.editorOptions.opened                  = true
            break  

        case "chequeo":
            tipo = "dxCheckBox"
            break

        case "radio":
            tipo = "dxRadioGroup"
            break

        case "selector":
            tipo = "dxSelectBox"
            break

        case "selector_multiple":
            tipo = "dxTagBox"
            break

        case "archivo":
            tipo = "dxFileUploader"
            break            
    }     
}

const crear_definicion = function(nombre, datos) {
    let nuevo_campo  = {
        editorOptions: {
            elementAttr: {}
        }
    }
    nuevo_campo.dataField = nombre 
    nuevo_campo.name      = nombre 
    campo_template(datos, nuevo_campo)
    nuevo_campo.editorOptions.elementAttr.id  = nombre 
    
    return nuevo_campo
}

export default {
    crear_definicion: crear_definicion
}