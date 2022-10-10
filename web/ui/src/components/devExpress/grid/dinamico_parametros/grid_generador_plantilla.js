import { stringifyQuery } from "vue-router";

let plantilla_base = `
<div class="container-fluid" >

        <div class="shadow-lg p-1 m-1 bg_barra_grid rounded">

            <DxToolbar 
                :element-attr="toolbarAtributos"
                :items = "elementosBarra"
            />

        </div>

        <component :is="gridEncabezado"></component>
        
        <div class="position-absolute top-50 start-50 translate-middle fixed-top" >
            <DxLoadIndicator
                    :visible="loadIndicatorVisible"
                    class="button-indicator"
                    width= "150px"
                    height= "100px"
            />
        </div>

        <!-- la clase del contenedor grid tambie debe ser un parametro, container simple??? -->
        <div class="shadow-lg p-1 mb-1 bg-body rounded " >
            <DxDataGrid
                class="bg-light"

                @rowDblClick           = "filaDobleClick"               

                ref                    = "referencia"
                :elementAttr           = "atributosElemento"           
                :columns               = "columnas"
                :data-source           = "fuenteDatos"            
                :show-borders          = "true"
                :focusedRowEnabled     = "focoResaltado"
                :export                = "exportar"
                :loadPanel             = "panelDeCarga"
                :searchPanel           = "busquedaPanel"
                :filterRow             = "busquedaFila"
                :grouping              = "agrupa"
                :groupPanel            = "agrupaPanel"
                :noDataText            = "sinDatosTexto"
                :sorting               = "ordenamiento"      
                :remoteOperations      = "operacionesRemotas"
                :rowAlternationEnabled = "alternanciaDeFilas"
                :allowColumnReordering = "reordenaColumna"
                :allowColumnResizing   = "redimensionaColumna"
                :columnChooser         = "selectorColumnas"
                :columnFixing          = "fijadorDeColumna"    
                :wordWrapEnabled       = "ajustaPalabra"
                
                :onOptionChanged       = "onOptionChanged"
                :onRowPrepared         = "onRowPrepared"
            >

                <template #plantillaCelda={data}>
                    <div>
                        <i class="fas fa-traffic-light" style="color:red"></i> {{data.value}}
                    </div>
                </template>

                <!-- !TEMPLATES! -->

            </DxDataGrid>
        </div>

        <component :is="gridEncabezado"></component>
        
    </div>
`;

let contador_plantilla = 0
let crea_plantilla = function(configuracion) {
    // Creación de plantilla de columnas
    let columnas           = $lib.cargaAtributo(configuracion, "columnas", [])
    let plantilla_nombre   = ""
    let plantillla_columna = ""
    let plantillas         = []
    let plantilla_columna_base = `
        <template #$PLANTILLA_NOMBRE$= {data}>
            <div>
                $PLANTILLA_CUERPO$
            </div>
        </template>
    `
    let columna;
    for (const indice in columnas) {
        columna = columnas[indice]
        if (columna.plantilla != undefined) {
            // Texto plantilla de la columna 
            contador_plantilla += 1
            plantilla_nombre    = "columna_plantilla_" + contador_plantilla
            plantillla_columna  = plantilla_columna_base.replace("$PLANTILLA_NOMBRE$", plantilla_nombre)
            plantillla_columna  = plantillla_columna.replace("$PLANTILLA_CUERPO$", columna.plantilla)
            plantillas.push(plantillla_columna)

            // Definicion columna tenplate
            try {
                delete columna.plantilla
            } catch (error) {}
            columna["cellTemplate"] = plantilla_nombre 
        }
    }
    
    let textoPlantilla         = plantillas.join(' ');
    let textoCompleto          = plantilla_base.replace('<!-- !TEMPLATES! -->', textoPlantilla);

    return textoCompleto   
};

export default {
    crea_plantilla: crea_plantilla
}