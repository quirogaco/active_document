import fuenteDatos  from '../../../../../../../components/devExpress/remoto/fuenteDatos.js';

async function traer_registro(estructura, id) {

    async function traer_datos(estructura, id) {            
        let opciones_carga = {
            searchExpr     : "id",
            searchOperation: "=",
            searchValue    : id
        }
        
        /// Trarea datos del registro del GRID
        async function traeDatos() { 
            let datos = await fuenteDatos.cargaDatosConsulta(opciones_carga, "tree", null, estructura);
            
            return datos;
        }
        let datos = await traeDatos();
    
        return datos[0];
    }

    return await traer_datos(estructura, id)
}

let metodos = {
    insertar_nodo(padre_id, datos) {
        datos["padre_id"] = padre_id
        this.trd_data.push(datos)
        this.arbol.getDataSource().reload()
        this.arbol.expandRow(padre_id)
    },
    
    datos_posicion(key){
        let id_igual = function(elemento) {
            return elemento.id == key;
        }
        return this.trd_data.findIndex( id_igual )
    },

    modificar_nodo(padre_id, datos) {
        let key = this.arbol.getSelectedRowKeys()[0]
        let idx = this.datos_posicion(key)
        datos["padre_id"] = padre_id
        this.trd_data.splice(idx, 1)
        this.trd_data.push(datos)
        this.arbol.getDataSource().reload()   
    },

    borrar_nodo(padre_id, datos) {
        let key = this.arbol.getSelectedRowKeys()[0]
        let idx = this.datos_posicion(key)
        this.trd_data.splice(idx, 1)
        this.arbol.getDataSource().reload()
    },

    ejecutar_operacion(operacion, padre_id, datos) {
        switch (operacion) {
            case 'salvar': 
                if (padre_id =="") {
                    this.insertar_nodo(-1, datos)
                }
                else {
                    this.insertar_nodo(padre_id, datos)
                } 
                break

            case 'modificar': 
                this.modificar_nodo(padre_id, datos)
                break  

            case 'borrar': 
                this.borrar_nodo(padre_id, datos)
                break 
        }
        this.indicador_visible = false
        window.$ventana_emergente_trd.opciones.visible = false   
        this.notify("Operación realizada correctamente", "success") 
    },

    boton_visibilidad(indice, visible=true) {
        this.botones_accion[indice]["visible"] = visible
        this.barra.repaint()
    },

    boton_ocultar_todos() {
        this.boton_visibilidad(this.boton_dependencia, false)
        this.boton_visibilidad(this.boton_serie, false)
        this.boton_visibilidad(this.boton_subserie, false)
        this.boton_visibilidad(this.boton_tipo, false)
        this.boton_visibilidad(this.boton_limpia, false)
        this.boton_visibilidad(this.boton_accesos, false)
    },

    mostrar_ventana(parametros) {
        this.emergente_key += 1;            
        this.opciones_ventana.alto               = parametros.alto 
        this.opciones_ventana.ancho              = parametros.ancho
        this.opciones_ventana.componente_visible = parametros.ventana  
        this.opciones_ventana.titulo             = parametros.titulo   
        this.opciones_ventana.visible            = true
        this.opciones_ventana.modo               = this.seleccionado_modo        
        // Información del registro
        this.opciones_ventana.datos              = parametros.datos
        // No puede ser padre de si mismo
        if (parametros.datos.id != this.seleccionado_id) {
            this.opciones_ventana.datos["padre_id"]     = this.seleccionado_id
            this.opciones_ventana.datos["padre_tipo"]   = this.seleccionado_tipo
            this.opciones_ventana.datos["padre_nombre"] = this.seleccionado_nombre     
        }          
    },

    llamar_ventana(tipo, datos={}, modo="crear") {
        let parametros         = {}
        this.seleccionado_modo = modo
        switch (tipo) {
            case 'dependencia': 
                parametros = {
                    alto         : 400,
                    ancho        : 600,
                    ventana      : "dependencia_trd",
                    titulo       : "Dependencias TRD",
                    boton_mensaje: "Salvar Dependencia", 
                    datos        : datos
                }
                this.mostrar_ventana(parametros)      
                break;

            case 'serie': 
                parametros = {
                    alto         : 650,
                    ancho        : 600,
                    ventana      : "serie_trd",
                    titulo       : "Series TRD",
                    datos        : datos
                }
                this.mostrar_ventana(parametros)         
                break;

            case 'subserie':   
                parametros = {
                    alto         : 650,
                    ancho        : 600,
                    ventana      : "subserie_trd",
                    titulo       : "SubSeries TRD",
                    datos        : datos
                }
                this.mostrar_ventana(parametros)        
                break;
            
            case 'tipo':   
                parametros = {
                    alto         : 500,
                    ancho        : 600,
                    ventana      : "tipo_trd",
                    titulo       : "Tipos TRD",
                    datos        : datos
                }
                this.mostrar_ventana(parametros)                
                break;

            case 'acesso':   
                parametros = {
                    alto         : 500,
                    ancho        : 600,
                    ventana      : "acceso_trd",
                    titulo       : "Accesos TRD",
                    datos        : datos
                }
                this.mostrar_ventana(parametros)                
                break;

            case 'limpia':
                this.arbol.clearSelection()
                this.limpiar_seleccion()
                break;                                                            
        }        
    },

    limpiar_seleccion() {
        this.seleccionado_padre_id = ""     
        this.seleccionado_tipo     = ""
        this.seleccionado_id       = ""
        this.seleccionado_nombre   = ""
    },

    boton_click(e) {        
        let boton = e.itemData.code      
        this.llamar_ventana(boton, {}, "crear")
    },

    seleccione_elemento(e) {   
        this.limpiar_seleccion()
        this.boton_ocultar_todos() 
        if  (e.selectedRowsData.length > 0) {  
            let selecionado            = e.selectedRowsData[0]     
            let hijos                  = this.arbol.getNodeByKey(selecionado.id).children;       
            this.seleccionado_padre_id = selecionado.padre_id       
            this.seleccionado_tipo     = selecionado.tipo     
            this.seleccionado_id       = selecionado.id    
            this.seleccionado_nombre   = selecionado.nombre 
            this.boton_visibilidad(this.boton_limpia, true)    
            this.boton_visibilidad(this.boton_accesos, true)   
            switch (this.seleccionado_tipo) {
                case 'dependencia':                    
                    this.boton_visibilidad(this.boton_serie, true)
                    this.boton_visibilidad(this.boton_dependencia, true)
                    break;

                case 'serie':
                    this.boton_visibilidad(this.boton_subserie, true)
                    if (hijos.length == 0) {
                        this.boton_visibilidad(this.boton_tipo, true)
                    }
                    break;

                case 'subserie':
                    this.boton_visibilidad(this.boton_tipo, true)
                    break;
                
                case 'tipo':
                    break;

                case 'limpia':
                    this.arbol.clearSelection()
                    this.boton_visibilidad(this.boton_dependencia, true)
                    break;                                                            
            }
        }
        else {
            this.boton_visibilidad(this.boton_dependencia, true)
        }
    },

    async onRowDblClick(e) {    
        let estructura = ""
        switch (e.data.tipo) {
            case 'dependencia':             
                estructura = "agn_dependencia_trd"     
                break
            
            case 'serie':             
                estructura = "agn_serie_trd"     
                break
            
            case 'subserie':             
                estructura = "agn_subserie_trd"     
                break
            
            case 'tipo':             
                estructura = "agn_tipo_documental_trd"     
                break

/* falta acessos */
            
        }        
        let datos = await traer_registro(estructura, e.data.id) 
       
        // Tipo de ventana
        this.llamar_ventana(e.data.tipo, datos, "modificar")
    }      
}

export default metodos;