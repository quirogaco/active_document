<template src="./expediente_basica_plantilla.html">
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
import expediente_basica_columnas from './expediente_basica_columnas.js';
// Metodos
import expediente_basica_metodos from './expediente_basica_metodos.js';
// Acciones
import expediente_basica_acciones from './expediente_basica_acciones.js';
// Accesos permisos
import ventana_emergente_accesos from './ventana_emergente_accesos/ventana_emergente_accesos.vue';

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
        DxItem,

        ventana_emergente_accesos
    },

    methods: expediente_basica_metodos.metodos,
    
    mounted() {        
        this.notify = notify;
        this.grid = this.$refs.grid.instance;  
        that = this;                    
    },

    data() {
        return {
            columnas      : expediente_basica_columnas.columnas,

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
            acciones_toolbar: expediente_basica_acciones.acciones,
            atributos_toolbar: {},            
            elemento_click: function(e) {                   
                switch (e.itemData.id) {
                    case 1:
                        expediente_basica_metodos.metodos.crear(that)
                        break;

                    case 2:
                        expediente_basica_metodos.metodos.accesos(that)
                        break;

                    case 3:
                        expediente_basica_metodos.metodos.cerrar(that)
                        break;

                    case 4:
                        expediente_basica_metodos.metodos.abrir(that)
                        break;

                    case 5:
                        expediente_basica_metodos.metodos.indice_electronico(that)
                        break;

                    case 6:
                        expediente_basica_metodos.metodos.control(that)
                        break;

                    case 7:
                        expediente_basica_metodos.metodos.exportar_log(that)
                        break;

                    case 8:
                        expediente_basica_metodos.metodos.fuid(that)
                        break;

                    case 9:
                        expediente_basica_metodos.metodos.indice_electronico_excel(that)
                        break;
                }
            }
        }
    }
}

export default grid

</script>