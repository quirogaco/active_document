
import { jsPDF } from 'jspdf'
import 'jspdf-autotable';
import { exportDataGrid as exportDataGridToPdf } from 'devextreme/pdf_exporter'

let metodos = {
    cambia_grid() {
        let columnas = this.crea_columnas()
        this.grid_reporte.option("columns", columnas) 
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
    },

    mostrar_botones() {
        this.mostrar_todos()
        this.barra.repaint()
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

    boton_click(e) {
        this.$router.push("grid_reportes_imprime")
    }
}

let barra_botones = function(forma) {
    return  [       
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