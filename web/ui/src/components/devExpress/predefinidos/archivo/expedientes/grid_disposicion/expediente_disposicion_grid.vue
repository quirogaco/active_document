<template src="./expediente_disposicion_plantilla.html">
</template>

<script>
import { DxLoadPanel } from 'devextreme-vue/load-panel';
import { DxButton } from 'devextreme-vue/button';
import {
    DxDataGrid,
    DxColumn,
    DxPager,
    DxPaging,
    DxSearchPanel,
    DxSelection,
    DxFilterRow,
    DxEditing,
    DxExport,
    DxToolbar
} from 'devextreme-vue/data-grid';

import DxDropDownButton from 'devextreme-vue/drop-down-button';
import { DxResponsiveBox, DxItem, DxLocation, DxCol, DxRow } from 'devextreme-vue/responsive-box';
import notify from 'devextreme/ui/notify';

import fuenteDatos from '../../../../remoto/fuenteDatos.js';
// Columnas
import expediente_disposicion_columnas from './expediente_disposicion_columnas.js';
// Metodos
import expediente_disposicion_metodos from './expediente_disposicion_metodos.js';
// Acciones
import expediente_disposicion_acciones from './expediente_disposicion_acciones.js';

const filtros = ["tabla", "=", "TRD"];
let that;

// Grid de gestión
let grid =  {
    components: {
        DxDropDownButton,
        DxLoadPanel,
        DxButton,
        DxDataGrid,
        DxColumn,
        DxPager,
        DxPaging,
        DxSearchPanel,
        DxSelection,
        DxFilterRow,
        DxEditing,
        DxExport,
        DxToolbar,
        
        // Responsive box
        DxResponsiveBox,
        DxLocation,
        DxCol,
        DxRow,
        DxItem
    },

    methods: expediente_disposicion_metodos.metodos,
    
    mounted() {        
        this.notify = notify;
        this.grid = this.$refs.grid.instance;  
        that = this;                    
    },

    data() {
        return {
            columnas      : expediente_disposicion_columnas.columnas,

            fuente_datos  : fuenteDatos.creaFuenteDatosConsulta('grid', null, 'agn_expedientes_trd', 'agn_expedientes_trd', filtros, {}),
            
            pageSizes     : [10, 25, 50, 100],

            // Ventana formas TRD
            opciones_ventana: {
                visible: false
            },
            emergente_key: 0,

            // Indicador de tareas
            indicador_visible: false,

            // Barra
            acciones_toolbar: expediente_disposicion_acciones.acciones,
            atributos_toolbar: {},            
            elemento_click: function(e) {                   
                switch (e.itemData.id) {
                    case 1:
                        expediente_disposicion_metodos.metodos.permite_eliminar(that)
                        break;

                    case 2:
                        expediente_disposicion_metodos.metodos.no_permite_eliminar(that)
                        break;

                    case 3:
                        expediente_disposicion_metodos.metodos.disposicion_final(that)
                        break;

                    case 4:
                        expediente_disposicion_metodos.metodos.fuid(that)
                        break;
                }
            }
        }
    }
}

export default grid

</script>