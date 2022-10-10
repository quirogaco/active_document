// #####################
// Metodos de la FORMA #
// #####################
// Se pueden adicionar metodos por configuración, no se si otro metodos como eventos ?
let metodos = {
    asignaAtributoDinamico(atributo, valor) {        
        this[atributo] = valor;      
        if (atributo == "formaDatos") {
            this.alCambiarDatos(this.formaComponente, valor)
        }
    },

    leeeAtributoDinamico(atributo) {            
        return this[atributo];
    },

    mensajePopup(titulo, mensaje) {   
        let tituloCompleto = this.titulo + " - " + titulo;         
        this.asignaAtributoDinamico('popupTitulo',  tituloCompleto);
        this.asignaAtributoDinamico('popupMensaje', mensaje);
        this.asignaAtributoDinamico('popupVisible', true);       
    },
    
    // Mensaje validación de datos
    mensajeValidacion(mensajes) {
        let mensaje = "";
        for (const indice in mensajes) {                            
            mensaje += "" + mensajes[indice].message + '\n';
        }
        this.mensajePopup("Error en datos", mensaje)
    },

    // Mensaje error envio
    errorEnvio(accion, errores) {
        let mensaje = "";
        if (Array.isArray(errores) ) {
            for(const error in errores) {
                mensaje += " - " + errores[error];
            }
        }
        else {
            mensaje += " - " + errores;
        }
        mensaje = mensaje.slice(2, mensaje.length);
        this.mensajePopup(("Error en " + accion + " - " + this.titulo), mensaje)     
    },

    limpiaNDET() {
        let ndet = window.$componentesNDET[this.componente_id];
        let componente;
        for ( const indice in ndet )  {
            componente = ndet[indice];
            if (typeof componente.option === 'function') {
                if (componente.NAME == "dxFileUploader") {
                    componente.option("value", []);
                }
            }            
        }
    },

    retornaEnvio(datos) {
        // Apaga icono de envio
        this.loadIndicatorVisible = false;

        // Habilita barra de botones
        this.asignaAtributoDinamico('toolbar', false);
        
        // Datos de respuesta
        let peticion = datos["peticion"]["parametros"]["__accion__"]   
        let accion   = "CREACIÓN";
        if   (peticion == "modificar") {
            accion = "MODIFICACIÓN"
        }   
        else if (peticion == "eliminar") {
            accion = "ELIMINACIÓN"
        }

        // Valida retorno            
        if (datos.error == "si") {                
            this.errorEnvio(accion, datos["datos"])
        }
        else {                   
            if ( (this.notifica == true) && (this.retorno_envio == undefined) ) {     
                this.notify("Operación realizada correctamente", "success")       
            }

            if (accion=="CREACIÓN") {
                // Valores por default JCR!!                   
                //this.asignaAtributoDinamico('formaDatos', {})
                //this.formaInstancia.option("formData", {})
                //this.limpiaNDET()
            }

            if (peticion=="eliminar") {
                window.$router.push({ path: this.regresarComponente });
            }

            // Invoca función de retorno si tenemos una
            if (this.retorno_envio != undefined) {
                this.retorno_envio(datos["datos"])
            }          
        }
    },

    enviaDatos(peticion, datosForma) {
        // Prende icono de envio
        this.loadIndicatorVisible = true;

        // Deshabilita barra de botones
        this.asignaAtributoDinamico('toolbar', true); 

        // Envia datos        
        let datos = datosForma;   
        switch (peticion) {
            case "insertar":
                datos = this.fuenteDatos.insert(datosForma)
                break

            case "modificar":
                datos = this.fuenteDatos.update(datosForma["id"], datosForma)
                break

            case "eliminar":
                datos = this.fuenteDatos.remove(datosForma["id"], datosForma) 
                this.este.formaInstancia.resetValues()
                break

            default:
                datosForma["__peticion__"] = peticion
                datos = this.fuenteDatos.insert(datosForma)        
        }     
        
        return datos;
    },

    alCambiarDatos(forma, valor) {
        if (this.cambiaDatosEvento != undefined) {
            this.cambiaDatosEvento( forma, JSON.parse(JSON.stringify(valor)) )
        }
    },

    // Elemento de la forma
    personalizaElemento(e) {},

    // Elemento de la forma
    inicializado(e) {
        let evento = this.eventos["inicializado"];
        if (evento != undefined) {
            //evento(e, this.formaComponente, this.formaDatos )
            evento(e, this.formaDatos )
        }        
    },

    contenido_listo(e) {
        let evento = this.eventos["contenido_listo"];
        if (evento != undefined) {
            evento(e, this.formaComponente, this.formaDatos )
        }        
    }
}

export default {
    metodos : metodos    
}