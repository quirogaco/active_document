const campo_template = function(datos, nuevo_campo) {
    switch (datos.tipo) {
        case "texto":
            nuevo_campo.template           = "campo_texto";
            nuevo_campo._tipo              = "texto";
            nuevo_campo.editorOptions.modo = "text";
            break

        case "correo":
            nuevo_campo.template           = "campo_texto"; 
            nuevo_campo._tipo              = "correo";
            nuevo_campo.editorOptions.modo = "email";
            break

        case "area_texto":
            nuevo_campo.template = "campo_area";  
            nuevo_campo._tipo    = "texto_area";
            break

        case "entero":
            nuevo_campo.template = "campo_numerico";  
            nuevo_campo._tipo    = "entero";
            break

        case "fecha":
            nuevo_campo.template                              = "campo_fecha";
            nuevo_campo._tipo                                 = "fecha";
            nuevo_campo.editorOptions.type                    = "date"; //  tipo*            
            nuevo_campo.editorOptions.dateSerializationFormat = "yyyy-MM-dd";  // formato*
            nuevo_campo.editorOptions.displayFormat           = "yyyy-MM-dd";  // formato*
            nuevo_campo.editorOptions.openOnFieldClick        = true;
            nuevo_campo.editorOptions.opened                  = true; // editor
            break  

        case "fecha_hora":
            nuevo_campo.template                              = "campo_fecha_hora";
            nuevo_campo._tipo                                 = "fecha";
            nuevo_campo.editorOptions.type                    = "datetime"; //  tipo*            
            nuevo_campo.editorOptions.dateSerializationFormat = "yyyy-MM-dd hh:mm:ss";  // formato*
            nuevo_campo.editorOptions.displayFormat           = "yyyy-MM-dd hh:mm:ss";  // formato*
            nuevo_campo.editorOptions.openOnFieldClick        = true;
            nuevo_campo.editorOptions.opened                  = true; // editor
            break  

        case "chequeo":
            nuevo_campo.template           = "campo_check";
            nuevo_campo._tipo              = "chequeo";
            nuevo_campo.editorOptions.text = "SI"; // value*
            break

        case "opciones":
            nuevo_campo.template            = "campo_opciones";
            nuevo_campo._tipo               = "radio";
            nuevo_campo.editorOptions.items = [ // dataSource*
                "A",
                "B"
            ];
            break

        case "seleccion":
            nuevo_campo.template                         = "campo_seleccion";
            nuevo_campo._tipo                            = "seleccion";
            nuevo_campo.editorOptions.showClearButton    = true; // limpiar
            nuevo_campo.editorOptions.showDropDownButton = true; // desplegable                         
            nuevo_campo.editorOptions.items = [ // dataSource*
                "A",
                "B"
            ]
            break

        case "seleccion_multiple":
            nuevo_campo.template                         = "campo_seleccion_multiple";
            nuevo_campo._tipo                            = "etiqueta";
            nuevo_campo.editorOptions.showClearButton    = true; // limpiar
            nuevo_campo.editorOptions.showDropDownButton = true; // desplegable                             
            nuevo_campo.editorOptions.items = [ // dataSource*
                "A",
                "B"
            ];
            break

        case "archivo":
            nuevo_campo.template                   = "campo_archivo";
            nuevo_campo._tipo                      = "archivo";
            nuevo_campo.editorOptions.multiple     =  true; // multiple*
            nuevo_campo.editorOptions.uploadMethod = "POST"; // metodo_carga
            nuevo_campo.editorOptions.uploadMode   = "useButtons"; // modo_carga  
            break            
    }     
}

const crear_definicion = function(nombre, datos, uuid) {
    // Definicion  inicial del campo
    let nuevo_campo  = {
        uuid: uuid,
        editorOptions: {
            items      : [],
            uuid       : uuid,
            elementAttr: {}
        }
    }
    //nuevo_campo.editorOptions.elementAttr.id = nombre    
    nuevo_campo.editorOptions.elementAttr.id = uuid; 
    nuevo_campo.dataField = nombre; // id
    nuevo_campo.name      = nombre; // id
    nuevo_campo.label = {
        text: nombre // titulo
    }
    nuevo_campo.isRequired = false; // obligatorio
    campo_template(datos, nuevo_campo);

    return nuevo_campo
}

export default {
    crear_definicion: crear_definicion
}