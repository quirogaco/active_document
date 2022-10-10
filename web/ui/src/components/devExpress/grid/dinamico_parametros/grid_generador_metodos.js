// Metodos del GRID
const metodos = function(configuracion) {    
    let metodosParametros      = window.$librerias.cargaAtributo(configuracion, 'metodos', {});
    
    // ##################
    // Metodos del GRID #
    // ##################
    // Se pueden adicionar metos por configuración, no se si otro metodos como eventos ?
    let metodos = {
        asignaAtributoDinamico(atributo, valor) {
            this[atributo] = valor;
        },

        filaDobleClick(e) {               
            if (this.dobleClick !== undefined) {
                this.dobleClick(e);
            }
        },

        // Hace parte de desarrollos dinamicos guardar este codigo
        insertaComponente(componenteNombre, rutaComponente, atributo, libreria=false) {   
            let componente = window._APLICACION_.component(componente_id);
            if (libreria == true) {
                import( "/* @vite-ignore */ devextreme-vue/" + rutaComponente ).then((modulo) => {
                    componente.components[componenteNombre] = modulo[componenteNombre]; 
                })
            }   
            else {                      
                import( ("/* @vite-ignore */  ../../" + rutaComponente) ).then((modulo) => {
                    if (modulo.default != undefined) {
                        // modulo.default es para componentes propio de la aplicacion
                        componente.components[componenteNombre] = modulo.default;  
                    }
                    else {
                        componente.components[componenteNombre] = modulo;  
                    }                                         
                })   
            }
            this[atributo] = componenteNombre;            
        },

        onRowPrepared: function(e) { 
            let eventos        = $lib.cargaAtributo(configuracion, 'eventos', {})
            let fila_preparada = $lib.cargaAtributo(eventos, 'fila_preparada', null)
            if (fila_preparada != null) {
                fila_preparada(e)
            }            
        },

        onOptionChanged: function(e) { 
            /*
            if (e.fullName == "searchPanel.text") {  
                console.log("cambia_panel de BUSQUEDA texot... ")
                e.component.__searchChanged = true;  
            }  
            */
        },

        /*
        EJEMPLOS DE COMO DEFINIR PLANTILLAS DINAMICAS PARA CELDA
        plantilla_columna_data: function(data) { 
            // plantilla: '<i class="fas fa-traffic-light" style="color:yellow"></i> {{ plantilla_columna_data(data) }}'
            console.log("plantilla_columna_data:", data)
            
            return data.data.estado
        },

        plantilla_columna: function(data) { 
            atributo de la columna -> 'plantilla': '<div v-html="plantilla_columna_estado(data)"></div>',
            metodo del grid -> 'plantilla_columna_estado': function(data) {
                contador += 1
                console.log("plantilla_columna_estado:", contador, data)
                let resultado =  '<i class="fas fa-traffic-light" style="color:red"></i>'  + " : " + contador + " : " + data.value
                return resultado
            }
        },
        */
    };

    const metodosCompletos = Object.assign(metodos, metodosParametros);

    return metodosCompletos
};


export default {
    metodos: metodos
}