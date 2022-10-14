// this is Popup (this component)

export const eventsPopup = function(that) {   
    return {}
}

export const methodsPopup = function(that) {
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