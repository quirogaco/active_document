
import { formatMessage, loadMessages } from 'devextreme/localization';
let messages = {
    "en": {
        "invalidData": "Invalid or incomplete data !!"
    },
    "es": {
        "invalidData": "Datos inválidos o incompletos !!"
    }
}
loadMessages(messages)

// Forma Props basicas
const forma_propiedades = function(propiedades={}) {
    let basicas = {
        // Cuando se invoca a traves de push por router recibe un json
        attributes_str: {
            type:  String,
            default() {
                return "{}"
            }
        },

        // Cuando se invoca como componente de otro se pasa un objeto directamente        
        attributes: {
            type: Object,
            default() {
                return {}
            }
        },

        // Se conserva por los primeros desarrollo
        datos: {
            type: String,
            default: () => {
                return "{}"
            }
        }
    }

    let propiedades_totales = Object.assign( {}, basicas, propiedades );
    
    return propiedades_totales
}

const lee_propiedades = function(props, name="") {
    console.log("FORM->PROPS:", props);
    2/0
    let attributes = {};
    if (props.attributes_str !== "{}") {
        attributes = $lib.texto_json(props.attributes_str);
    }
    else {
        if (Object.keys(props.attributes).length > 0) {
            // Clone borra las funciones y archivos..
            //attributes = $lib.clone(props.attributes);
            attributes = props.attributes;
        }
    }

    return attributes
}

const formData = function(form=null, data=null) {        
    if (data != null) {
        form.option("formData", data)
    }
    else {
        return form.option("formData")
    }
}

const forma_validacion  = function(forma) {
    let tamano           = 0
    let contador         = 0
    let datos_validos    = forma.validate() 
    let archivos_validos = true
    
    for (const indice in this._archivos) {
        let archivos = this._archivos[indice].component._files
        for (const indice_archivo in archivos) {
            if (archivos_validos == true) archivos_validos = archivos[indice_archivo].isValid();
            tamano          += archivos[indice_archivo].value.size
            contador        += 1
        }  
    }
    let forma_valida = (datos_validos.isValid && archivos_validos);
    if (forma_valida == false) {
        $notify(formatMessage("invalidData", null), "warning")         
    }

    return {
        "isValid" : forma_valida,
        "formData": formData(forma)
    }
}

const forma_funciones = {
    // Inicio funciones a personalizar
    // Montar componente
    montado_especifico: function(basicas) {},

    // Basica reemplazables por especifico de la forma
    regresar_visual: function() {
        //console.log("regresar_visual")
    },

    // Error en el servidor
    error_accion: function(error_datos) {
        //console.log("error_accion")
    },
    // Final funciones a personalizar

    // ERROR DE SISTEMA SERVIDOR NO MANEJADO
    error_remoto: function(error) {
        window.$ocultar_esperar()
        let mensaje_error = error.data.error
        $alertar(mensaje_error, "Error SERVIDOR!")
        if (this.error_accion != undefined) {
            this.error_accion(error.data)
        }
    },    

    montado_general(forma_componente, props={}) {        
        // Configuración inicial
        try {
            // Funciones para definiciones iniciales como RADICADO
            forma_componente.forma  = forma_componente.$refs.forma.instance;
            forma_componente._forma = forma_componente.$refs.forma;                     
            forma_componente.barra  = forma_componente.$refs.barra.instance;  
            forma_componente.parametros = JSON.parse(forma_componente.datos);
            window.$componentes["_formas"][forma_componente.basicas["forma_id"]] = forma_componente;        
            forma_componente.montado_especifico(forma_componente.basicas);
        } catch (error) {
            // Funciones nueva definicion de componentes 
            /*
            if (Object.keys(forma_componente.attributes).length === 0) {
                console.log("JSON:", JSON.parse(forma_componente.attributes_str))
                forma_componente.attributes = JSON.parse(forma_componente.attributes_str);
            }
            */
        }          
    },

    mostrar_botones() {
        this.mostrar_todos()
        this.barra.repaint()
    },

    define_accion(accion) {        
        switch (accion) {
            case 'regresar':     
                this.regresar_visual(accion)
                break;
        }

        return accion
    },

    forma_datos(datos=null) {        
        if (datos != null) {
            this.forma.option("formData", datos)
        }
        else {
            return this.forma.option("formData")
        }
    },

    limpia_datos(datos_basicos={}) {
        let datos_forma = Object.assign({}, datos_basicos)        
        this.forma.option("formData", datos_forma)

        return datos_forma
    },

    forma_repinta() {
        this.forma.repaint()
        this.limpia_archivos()
    },

    carga_datos(datos={}) {
        this.forma.option("formData", datos)

        return datos
    },

    limpia_archivos() {
        for (const indice in this._archivos) {
            this._archivos[indice].component._files = []       
            this._archivos[indice].component.option("value", [])              
        }
    },

    forma_validacion() {
        let tamano           = 0
        let contador         = 0
        let datos_validos    = this.forma.validate() 
        let archivos_validos = true
        for (const indice in this._archivos) {
            let archivos = this._archivos[indice].component._files
            for (const indice_archivo in archivos) {
                if (archivos_validos == true) archivos_validos = archivos[indice_archivo].isValid();
                tamano          += archivos[indice_archivo].value.size
                contador        += 1
            }  
        }
        let forma_valida = (datos_validos.isValid && archivos_validos)  

        return forma_valida
    }
}

export default {
    // Funciones de la forma
    forma_funciones  : forma_funciones,
    // Propiedadess de la forma        
    forma_propiedades: forma_propiedades,
    lee_propiedades  : lee_propiedades,

    // funciones independientes
    formData         : formData,
    forma_validacion : forma_validacion
}