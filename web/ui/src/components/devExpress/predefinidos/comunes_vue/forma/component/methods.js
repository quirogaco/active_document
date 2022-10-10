// this is DxForm, that is Form (this component)

export const eventsDxForm = function(that) {   
    return {}
}

export const methodForm = function(that) {
    return {        
        formData(datos=null) {            
            return $forma.formData(that.instance, datos)
        },
        
        validateData() {
            return $forma.forma_validacion(that.instance, {})
        },

        repaint() {
            that.instance.repaint();
        }
    }
}

export default {
    eventsDxForm: eventsDxForm,
    methodForm: methodForm
}