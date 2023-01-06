<template src="./gestion_basica_plantilla.html">
</template>

<script>
import {
    DxDataGrid,
    DxPager,
    DxPaging,
    DxSearchPanel,
    DxSelection,
    DxFilterRow,
    DxExport
} from 'devextreme-vue/data-grid';

import DxDropDownButton from 'devextreme-vue/drop-down-button'
import { DxResponsiveBox } from 'devextreme-vue/responsive-box'
import notify from 'devextreme/ui/notify'

import fuenteDatos from '../../../remoto/fuenteDatos.js'

// Columnas
import gestion_basica_columnas from './gestion_basica_columnas.js'

// Metodos
import gestion_basica_metodos from './gestion_basica_metodos.js'

// Ventana emergente
import ventana_emergente from '../ventana_emergente/ventana_emergente.vue'

// Barra de acciones
import gestion_acciones from '../barra_accion/gestion_acciones.vue'

// Eventos de la fuente de datos
let eventos = {
    'cargar_datos_antes': function (opciones, idComponente) {
        return opciones;
    },
}

let basica = {
    "estructura"  : "peticiones",
    "filtros_grid": [ 
        ["responsable_id", "=", window.$usuario.id], 
        ["estado_gestion", "=", "PENDIENTE"], 
        ["estado_", "=", "ACTIVO"] 
    ],
    "titulo_grid" : "Gestión de peticiones, documentos y tramites"
}

// Grid de gestión
let grid =  {
    components: {
        DxDataGrid,
        DxPager,
        DxPaging,
        DxSearchPanel,
        DxSelection,
        DxFilterRow,
        DxExport,
        
        // Acciones
        DxDropDownButton,

        // Responsive box
        DxResponsiveBox,
    
        // Ventana emergente
        ventana_emergente,

        // Barra de acciones
        gestion_acciones,        
    },

    methods: gestion_basica_metodos.metodos,
    
    mounted() {
        this.opciones_accion['grid'] = this.$refs;
        this.$refs.grid.instance.columnOption(
            "nro_radicado",
            {sortOrder: 'asc', sortIndex: 0} 
        );
        // this.dataGrid.instance.columnOption('FirstName', {  
        //     sortOrder: 'asc',  
        //     sortIndex: 0  
        // });  
        window.$peticion_datos = {}
        // setTimeout(() => {
        //     window.$grid_gestion = this.$refs.grid.instance
        // }, 3000);
        this.notify = notify                  
    },

    data() {
        return {
            basica        : basica,
            // Indicador de tareas
            indicador_visible: false,
            
            columnas      : gestion_basica_columnas.columnas, // Columnas grid
            fuente_datos  : fuenteDatos.creaFuenteDatosConsulta(
                'grid', 
                null, 
                basica.estructura, 
                basica.estructura, 
                basica.filtros_grid, 
                {}
            ),            
            pageSizes           : [10, 25, 50, 100],
            displayMode         : 'full',
            showPageSizeSelector: true,
            showInfo            : true,
            showNavButtons      : true,
            
            opciones_accion: {
                contexto: "grid_gestion",
                evento: "gridGestionMuestraVentanaEmergente",   
                evento_grid_gestion: "gridGestionMuestraVentanaEmergenteGrid"             
            },

            opciones_ventana: {
                visible: false
            },
            emergente_key: 0
        }
    }
}

export default grid
</script>