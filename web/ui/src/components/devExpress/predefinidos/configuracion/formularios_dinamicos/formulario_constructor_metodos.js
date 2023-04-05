let metodos = {
    // Eventos CONSTRUCTOR
    comienza_arrastrar_constructor(e) {
        e.itemData = e.fromData[e.fromIndex];
        e.itemData["label"] = e.itemData["titulo"] 
    },

    suelta_constructor(e) {
        let desde = e.fromComponent.option("elementAttr")["id"]
        // Elimina del origen
        if (desde == "prevista") {
            e.fromData.splice(e.fromIndex, 1);
        }
    },

    // Eventos FORMA
    comienza_arrastrar_prevista(e) {
        e.itemData = e.fromData[e.fromIndex];
    },

    suelta_prevista(e) {        
        let desde = e.fromComponent.option("elementAttr")["id"]
        // Elimina del origen
        if (desde == "prevista") {
            e.fromData.splice(e.fromIndex, 1)
        }
        // Inserta destino
        this.contador_campos += 1
        e.itemData.codigo = ("campo_" + this.contador_campos)
        e.itemData.label  = e.itemData.titulo
        e.toData.splice(e.toIndex, 0, e.itemData)        
    },

    posicion_campo(codigo) {        
        const es_codigo = (elemento) => elemento.codigo == codigo;
        let pocision = this.campos_constructor.findIndex(es_codigo)

        return pocision
    },

    click_campo(campo) {
        let posicion = this.posicion_campo(campo.codigo)
        this.opciones_atributo.datos    = campo
        this.opciones_atributo.posicion = posicion
        this.opciones_atributo.visible  = true
        this.emergente_key             += 1
    },

    // Reglas de validación
    reglas_validacion(campo) {
        let reglas = []
        if (campo.obligatorio  == "SI") {
            reglas.push({
                type   : "required",
                message: (campo.label + " es obligatorio")
            })
        }

        return reglas
    },

    // Tipo de editor
    definir_editor(campo) {
        let tipo = "dxTextBox"   
        switch (campo.tipo) {
            case "area_texto":
                tipo = "dxTextArea"
                break

            case "entero":
                tipo = "dxNumberBox"
                break

            case "fecha":
                tipo = "dxDateBox"
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

        return tipo
    },

    // editor atributos
    editor_opciones(campo) {
        let opciones =  {
            disabled: false            
        }
        switch (campo.tipo) {
            case "area_texto":
                break

            case "entero":
                break

            case "fecha":
                break  

            case "chequeo":
                console.log("campo.elementos:", campo.elementos)
                opciones["items"] = campo.elementos                      
                break

            case "radio":
                opciones["items"]  = campo.elementos
                opciones["layout"] = "horizontal"   
                break

            case "selector":
                opciones["items"] = campo.elementos
                break

            case "selector_multiple":
                opciones["items"] = campo.elementos
                break
    
            case "archivo":
                opciones["multiple"]   = true
                opciones["uploadMode"] = "useForm"
                break            
        }     

        return opciones
    },

    // Nombre del campo de datos
    definir_campo_datos(campo) {        
        if (campo.codigo == undefined) {
            this.contador_campos += 1
            campo.codigo = ("campo_" + this.contador_campos)
        }  

        return campo
    },

    boton_forma() {
        return {
            itemType: "button",
            horizontalAlignment: "center",
            buttonOptions: {
                text    : "Salvar",
                type    : "success",
                onClick : () => {
                    let validacion = this.forma_prevista.validate()
                    let datos      = this.forma_prevista.option("formData")
                    if ( validacion.isValid != true) {
                        this.notify("Valores invalidos o incompletos", "error")   
                    }
                }
            }
        }
    },

    crea_campos() {
        let campos   = [];
        let contador = 0;
        for (let campo of this.campos_constructor) {
            console.log("CAMPO:", campo)
            contador += 1;
            // EDITOR
            let tipo_editor = this.definir_editor(campo)
            // EDITOR
            campo = this.definir_campo_datos(campo)
            
            let definicion = {
                dataField : campo.codigo,
                editorType: tipo_editor,
                label: {
                    text: campo.label
                },
                // Opciones del campo
                editorOptions: this.editor_opciones(campo),
                // Reglas de validación
                validationRules: this.reglas_validacion(campo),
            };
            campos.push(definicion)
        }

        campos.push(this.boton_forma())

        return campos;
    }
}

export default {
    metodos: metodos
}


