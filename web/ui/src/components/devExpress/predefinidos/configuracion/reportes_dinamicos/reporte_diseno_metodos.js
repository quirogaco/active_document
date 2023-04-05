
import { jsPDF } from 'jspdf'
import 'jspdf-autotable';
import { exportDataGrid as exportDataGridToPdf } from 'devextreme/pdf_exporter'

import fuenteDatos  from '../../../remoto/fuenteDatos.js'
let urlCompleta = window.$direcciones.servidorDatos + '/especifico_acciones'

let metodos = {
    retorna: function(retorna) {        
        let accion = retorna["accion"]
        this.columnas_prevista = []   
        this.lista_campos      = []
        let datos              = retorna["datos"]["datos"]
        if (accion=="leer_fuentes") {                 
            this.fuentes_select.option("dataSource", this.nueva_fuente_datos(datos)) 
        }

        if (accion=="leer_campos_fuente") {      
            this.lista_campos = datos
        }

        if (accion=="crear_reporte") {
            this.parametros.modo = "modificar"            
            this.mostrar_botones()            
        }

        if (accion=="borrar_reporte") {
            this.$router.push("expediente_basica_grid")         
        }
    },

    cambia_fuente: function(objeto) {
        this.grid_reporte.option("columns", []) 
        this.columnas_reporte  = []
        this.leer_fuentes("leer_campos_fuente", {"fuente": objeto.selectedItem.id})  
        this.fuente_datos_grid = fuenteDatos.creaFuenteDatosConsulta('grid', null, objeto.selectedItem.estructura, objeto.selectedItem.estructura, [], [])
    },

    leer_fuentes: function(accion, datos={}) {
        let parametros = {
            datos : datos,
            accion: accion
        }
        window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna, "")   
    },


    // Eventos DISEÑADOR
    comienza_arrastrar_disenador(e) {
        e.itemData = e.fromData[e.fromIndex];
        e.itemData["titulo"] = e.itemData["nombre"] 
    },

    suelta_disenador(e) {        
        let desde = e.fromComponent.option("elementAttr")["id"]
        // Elimina del origen
        if (desde == "reporte") {
            e.fromData.splice(e.fromIndex, 1);
        }
        this.cambia_grid()
    },

    // Eventos FORMA
    comienza_arrastrar_prevista(e) {
        e.itemData = e.fromData[e.fromIndex];
    },

    suelta_prevista(e) {        
        let desde = e.fromComponent.option("elementAttr")["id"]
        // Elimina del origen
        if (desde == "reporte") {
            e.fromData.splice(e.fromIndex, 1)
        }
        // Inserta destino
        this.contador_campos += 1
        e.itemData.titulo = e.itemData.titulo
        e.toData.splice(e.toIndex, 0, e.itemData)    
        this.cambia_grid()    
    },

    click_campo(campo) {
        this.opciones_atributo.datos    = campo
        this.opciones_atributo.visible  = true
        this.emergente_key             += 1
    },

    // Tipo de editor
    definir_editor(columna) {
        let tipo    = "string"  
        let formato = ""

        switch (columna.datos.tipo) {
            case "entero":
                tipo = "integer"
                break

            case "fecha":
                tipo    = "date"
                formato = "y-MM-dd" 
                break  
        }     
    
        return {"tipo": tipo, "formato": formato}
    },

    cambia_grid() {
        let columnas = this.crea_columnas()
        this.grid_reporte.option("columns", columnas) 
    },

    crea_columnas() {
        let columnas = [];
        for (let columna of this.columnas_reporte) {
            // EDITOR
            let datos = this.definir_editor(columna)
            
            // Definición columna
            let definicion = {
                dataType : datos.tipo,
                caption  : columna["titulo"],
                dataField: columna["id"],
                format   : datos.formato  
            }
            columnas.push(definicion)
        }
        return columnas;
    },

    exportar_pdf() {
        const doc = new jsPDF();
        exportDataGridToPdf({
            jsPDFDocument: doc,
            component: this.grid_reporte
        }).then(() => {
            doc.save('datos.pdf');
        })
    },

    mostrar_todos() {
        let botones = this.barra_botones
        botones[0].options.visible = true
        botones[1].options.visible = true
        botones[2].options.visible = true
        botones[3].options.visible = true
    },

    mostrar_botones() {
        this.mostrar_todos()
        let botones = this.barra_botones
        if (this.parametros.modo == "crear") {
            botones[1].options.visible = false
            botones[2].options.visible = false
        }

        if (this.parametros.modo == "modificar") {
            botones[0].options.visible = false    
            this.expediente_archivos_visible = true        
        }

        this.barra.repaint()
    },

    boton_click(e) {
        let boton      = e.component.option("hint")
        let enviar     = true
        let validacion = this.forma.validate()   
        let datos      = this.forma.option("formData")  
        datos["columnas_reporte"] = this.columnas_reporte
        let parametros = {
            datos: datos
        }
        console.log("datos:", datos)

        switch (boton) {
            case 'crear': 
                parametros["accion"] = "crear_reporte"
                break;

            case 'borrar':      
                parametros["accion"] = "borrar_reporte"              
                break;

            case 'regresar':       
                enviar = false         
                this.$router.push("reportes_dinamicos_grid")
                break;
        }

        if ( ( validacion.isValid == true) && (enviar == true) ) {
            this.indicador_visible = true
            window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna, "")   
        }
    
        if ( ( validacion.isValid == false) && (enviar == true ) ) {
            this.notify("Valores invalidos o incompletos", "error")     
        }        
    }
}

let barra_botones = function(forma) {
    return  [       
        { 
            widget  : "dxButton",           
            options :{ //0
                icon       : 'fas fa-plus-square',
                alignment  : 'center',
                hint       : 'crear',
                type       : 'success',
                text       : 'Salvar Reporte', 
                stylingMode: "contained", 
                onClick    : forma.boton_click,
            } 
        },

        {
            widget  : "dxButton",           
            options :{ //1
                icon       : 'fas fa-edit',
                alignment  : 'center',
                hint       : 'modificar',
                type       : 'default',
                text       : 'Modificar Reporte',
                stylingMode: "contained",    
                onClick    : forma.boton_click,             
            }
        },

        {
            widget  : "dxButton",           
            options :{ //2
                icon       : 'fas fa-times-circle',
                alignment  : 'center',
                hint       : 'borrar',
                type       : 'danger',
                text       : 'Borrar Reporte',
                stylingMode: "contained",   
                onClick    : forma.boton_click,            
            }
        },

        {
            widget  : "dxButton",           
            options :{ //3
                icon       : 'fas fa-angle-left',
                alignment  : 'center',
                hint       : 'regresar',
                type       : 'normal',
                text       : 'Regresar',   
                stylingMode: "contained",  
                onClick    :forma.boton_click,         
            }
        },
                    
    ]              
}

export default {
    metodos       : metodos,
    barra_botones: barra_botones
}