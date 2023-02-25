<template src="./grid_gestion_consulta_plantilla.html">
</template>

<script>
import { DxButton } from 'devextreme-vue/button';
import {
    DxDataGrid,
    DxPager,
    DxPaging,
    DxSearchPanel,
    DxSelection,
    DxFilterRow,
    DxExport
} from 'devextreme-vue/data-grid';
import notify from 'devextreme/ui/notify'

import fuenteDatos from '../../../remoto/fuenteDatos.js'

// Columnas
import grid_gestion_consulta_columnas 
from './grid_gestion_consulta_columnas.js'
// Metodos
import grid_gestion_consulta_metodos
from './grid_gestion_consulta_metodos.js'


let valor_filtro = window.$usuario.dependencia_id;
let filtros_grid = [ 
    ["dependencias_id", "contain", valor_filtro]
];

let campo_filtro = "gestion_dependencia_id";
let eventos = {
    "cargar_datos_antes": function(opciones, idComponente) {
        console.log("ANTES DE CARGAR>>:", opciones, campo_filtro);
        let filtros = [];
        if ( (opciones.filter) && (opciones.filter.filter) ) {        
            filtros = opciones.filter.filter(function (el) {
                if (el.indexOf("estado_gestion") > -1) {
                    return true;
                }
            });
        };
         
        console.log("filtros:", filtros);
        if (filtros.length > 0) {
            opciones.filter.push(
                [campo_filtro, "=", valor_filtro]
            )
        };

        return opciones;
    }
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
        
        // Responsive box
       
        // // Ventana notifica
        // ventana_emergente_firma,

        // // Ventana anula
        // ventana_emergente_anula
    },

    methods: grid_gestion_consulta_metodos.metodos,
    
    mounted() {
        this.grid = this.$refs.grid.instance;
        this.notify = notify;                       
    },

    data() {
        return {
            columnas: grid_gestion_consulta_columnas.columnas,
            fuente_datos: fuenteDatos.creaFuenteDatosConsulta(
                'grid', 
                null, 
                'radicados_unico', 
                'radicados_unico', 
                filtros_grid, 
                eventos
            ),            
            pageSizes: [10, 25, 50, 100],
            displayMode: 'full',
            showPageSizeSelector: true,
            showInfo: true,
            showNavButtons: true,

            // Ventanas emergentes
            opciones_ventana: {
                visible: false
            },
            emergente_key: 0,

            opciones_ventana_anula: {
                visible: false
            },            
            emergente_key_anula:0,
            titulo_grid: "DOCUMENTOS GESTIONADOS EN LA DEPENDENCIA",
            retorna_grid: "grid_gestion_consulta"
        }
    }
}

export default grid

</script>