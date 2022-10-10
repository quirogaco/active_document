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
        this.tvd_data.push(datos)
        this.arbol.getDataSource().reload()
        this.arbol.expandRow(padre_id)
    },
    
    datos_posicion(key){
        let id_igual = function(elemento) {
            return elemento.id == key;
        }
        return this.tvd_data.findIndex( id_igual )
    },

    modificar_nodo(padre_id, datos) {
        let key = this.arbol.getSelectedRowKeys()[0]
        let idx = this.datos_posicion(key)
        datos["padre_id"] = padre_id
        this.tvd_data.splice(idx, 1)
        this.tvd_data.push(datos)
        this.arbol.getDataSource().reload()   
    },

    borrar_nodo(padre_id, datos) {
        let key = this.arbol.getSelectedRowKeys()[0]
        let idx = this.datos_posicion(key)
        this.tvd_data.splice(idx, 1)
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
        window.$ventana_emergente_tvd.opciones.visible = false   
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
                    ventana      : "dependencia_tvd",
                    titulo       : "Dependencias TVD",
                    boton_mensaje: "Salvar Dependencia", 
                    datos        : datos
                }
                this.mostrar_ventana(parametros)      
                break;

            case 'serie': 
                parametros = {
                    alto         : 600,
                    ancho        : 600,
                    ventana      : "serie_tvd",
                    titulo       : "Series TVD",
                    datos        : datos
                }
                this.mostrar_ventana(parametros)         
                break;

            case 'subserie':   
                parametros = {
                    alto         : 600,
                    ancho        : 600,
                    ventana      : "subserie_tvd",
                    titulo       : "SubSeries TVD",
                    datos        : datos
                }
                this.mostrar_ventana(parametros)        
                break;
            
            case 'acesso':   
                parametros = {
                    alto         : 500,
                    ancho        : 600,
                    ventana      : "acceso_tvd",
                    titulo       : "Accesos TVD",
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
            this.boton_visibilidad(this.boton_limpia, true)    
            this.seleccionado_padre_id = e.selectedRowsData[0].padre_id       
            this.seleccionado_tipo     = e.selectedRowsData[0].tipo     
            this.seleccionado_id       = e.selectedRowsData[0].id    
            this.seleccionado_nombre   = e.selectedRowsData[0].nombre 
            this.boton_visibilidad(this.boton_accesos, true)   
            switch (this.seleccionado_tipo) {
                case 'dependencia':                    
                    this.boton_visibilidad(this.boton_serie, true)
                    this.boton_visibilidad(this.boton_dependencia, true)
                    break;

                case 'serie':
                    this.boton_visibilidad(this.boton_subserie, true)
                    break;

                case 'subserie':
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
                estructura = "agn_dependencia_tvd"     
                break
            
            case 'serie':             
                estructura = "agn_serie_tvd"     
                break
            
            case 'subserie':             
                estructura = "agn_subserie_tvd"     
                break
            
        }        
        let datos = await traer_registro(estructura, e.data.id)        

        // Tipo de ventana
        this.llamar_ventana(e.data.tipo, datos, "modificar")
    }      
}

export default metodos;