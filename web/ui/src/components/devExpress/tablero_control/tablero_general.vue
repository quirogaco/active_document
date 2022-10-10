<template>
    <DxPivotGrid
        :allow-sorting            = "true"
        :allow-sorting-by-summary = "true"
        :allow-filtering          = "true"
        :height                   = "620"
        :show-borders             = "true"
        :data-source              = "dataSource"
        :texts                    = "textos"
        :field-chooser            = "selector_campos"
        :field-panel              = "panel_campos"
        :header-filter            = "encabezado_filtros"
        :load-panel               = "carga_panel"
        row-header-layout         = "tree"
    >

        <DxScrolling
            mode="virtual"
        />

        <DxExport
            :enabled="true"
        />

    </DxPivotGrid>
</template>

<script>
import {
    DxPivotGrid,
    DxScrolling,
    DxExport,
    DxFieldPanel
} from 'devextreme-vue/pivot-grid';

//import deMessages from 'npm:devextreme/localization/messages/de.json!json';
//import ruMessages from 'npm:devextreme/localization/messages/ru.json!json';

import { locale, loadMessages, formatMessage } from 'devextreme/localization';

import fuenteDatos from '../remoto/fuenteDatos.js'

let campos = [
    {
        caption: 'Territorial/Sede',
        dataField: 'sede_nombre',
        width: 350,
        expanded: true,
        sortBySummaryField: 'valor',
        sortBySummaryPath: [],
        sortOrder: 'desc',
        area: 'row',
        allowFiltering: true,
        allowSorting  : true,
        allowSortingBySummary: true
    }, 
    {
        caption: 'Dependencia',
        dataField: 'dependencia_nombre',
        width: 350,
        sortBySummaryField: 'valor',
        sortBySummaryPath: [],
        sortOrder: 'desc',
        area: 'row',
        allowFiltering: true,
        allowSorting  : true,
    }, 
    {
        caption: 'Petición',
        dataField: 'peticion_nombre',
        area: 'row',
        sortBySummaryField: 'valor',
        sortBySummaryPath: [],
        sortOrder: 'desc',
        width: 350,
        allowFiltering: true,
        allowSorting  : true,
        expanded: true
    }, 
    {
        caption: 'Año',
        dataField: 'gestion_inicio',
        dataType: 'date',
        area: 'column',
        allowFiltering: true,
        allowSorting  : true,
        groupInterval : 'year', 
        headerFilter: {
            allowSearch: true
        }
    }, 
    {
        caption: 'Trimestre',
        dataField: 'gestion_inicio',
        dataType: 'date',
        area: 'column',
        allowFiltering: true,
        allowSorting  : true,
        groupInterval : 'quarter', 
        headerFilter: {
            allowSearch: true
        }
    }, 
    {
        caption: 'Mes',
        dataField: 'gestion_inicio',
        dataType: 'date',
        area: 'column',
        allowFiltering: true,
        allowSorting  : true,
        groupInterval : 'month', 
        headerFilter: {
            allowSearch: true
        }
    },     
    {
        caption: 'Valor',
        dataField: 'valor',
        summaryType: 'sum',
        isMeasure: true,
        area: 'data'
    }, 
    {
        dataField: 'Id',
        visible: false
    }
]

export default {
    created() {
        //loadMessages(deMessages);
        //loadMessages(ruMessages);
        //locale(navigator.language);
        locale("es")
        console.log("navigator.language:", "es")
    },

    components: {
        DxPivotGrid,
        DxScrolling,
        DxExport,
        DxFieldPanel
    },
    data() {
        return {
            dataSource: {
                //remoteOperations: true,
                store : fuenteDatos.creaFuenteDatosConsulta('pivot', null, 'tablero_general', 'peticiones'),
                fields: campos
            },

            textos: {
                'collapseAll'        : 'Cerrar todos',
                'dataNotAvailable'   : 'n/d',
                'expandAll'          : 'Expandir todos',
                'exportToExcel'      : 'Exportar a excel',
                'grandTotal'         : 'Gran total',
                'noData'             : 'Sin datos',
                'removeAllSorting'   : 'Remover ordenamientos',
                'showFieldChooser'   : 'Mostrar selector de campos',
                'sortColumnBySummary': 'Ordenar {0} por esta columna',
                'sortRowBySummary'   : 'Ordenar {0} por esta fila',
                'total'              : '{0} - (Total)'
            },

            selector_campos: {
                'allowSearch'     : false,
                'applyChangesMode': 'instantly',
                'enabled'         : true,
                'layout'          : 0,
                'searchTimeout'   : 800,
                'texts'           : {
                    'allFields'   : 'Todos los campos',
                    'columnFields': 'Columnas campos',
                    'dataFields'  : 'Campos datos',
                    'filterFields': 'Campos filtros',
                    'rowFields'   : 'Campos filas'
                },
                'title'           : 'Selector de campos',
                'width'           : 800

            },

            panel_campos: {
                'allowFieldDragging': true,
                'showColumnFields'  : true,
                'showDataFields'    : false,
                'showFilterFields'  : true,
                'showRowFields'     : true,
                'texts'           : {
                    'columnFieldArea'   : 'Suelte campos de columna aqui',
                    'dataFieldArea'     : 'Suelte campos de datos aqui',
                    'filterFieldArea'   : 'Suelte campos de filtros aqui',
                    'rowFieldArea'      : 'Suelte campos de filas aqui',                    
                },
                'visible'           : true
            },

            encabezado_filtros: {
                'allowSearch'       : true,
                'searchTimeout'     : 1500,
                'showRelevantValues': true,
                'texts'             : {
                    'cancel'    : 'Cancelar',
                    'emptyValue': '(Blancos)',
                    'ok'        : 'Aplique',                    
                },

            },

            carga_panel: {
                "text": "Cargando....."
            }

        }
    }
};
</script>
