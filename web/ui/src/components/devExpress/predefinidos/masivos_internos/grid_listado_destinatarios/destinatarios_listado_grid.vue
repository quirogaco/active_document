<template src="./destinatarios_listado.html">
</template>

<script>
import {
    DxDataGrid,
    DxColumn,    
    DxSelection,
    DxEditing,
} from 'devextreme-vue/data-grid';
import { DxButton } from 'devextreme-vue/button';

import DxDropDownButton from 'devextreme-vue/drop-down-button'
import { locale, loadMessages, formatMessage } from 'devextreme/localization'
import notify from 'devextreme/ui/notify'

import fuenteDatos from '../../../remoto/fuenteDatos.js'

// Columnas
import destinatarios_listado_columnas from './destinatarios_listado_columnas.js'
// Metodos
import destinatarios_listado_metodos from './destinatarios_listado_metodos.js'

// Eventos de la fuente de datos
let eventos = {
    'cargar_datos_antes': function (opciones, idComponente) {
        return opciones;
    },
}
// Filtros de la fuente de datos
let filtros = ["origen", "=", "INTERNO"]

// Grid de destinatarios listados
let grid =  {
    created() {
        locale("es")
    },

    components: {
        DxDataGrid,
        DxColumn,
        DxSelection,
        DxButton
    },
    
    methods: destinatarios_listado_metodos.metodos,
    
    mounted() {
        setTimeout(() => {
            window.$grid_destinatarios_listado = this
        }, 3000);
        this.notify = notify        
    },

    data() {
        return {
            screen(width) {
                return (width < 700) ? 'sm' : 'lg';
            }, 

            columnas      : destinatarios_listado_columnas.columnas, // Columnas grid

            fuente_datos  : fuenteDatos.creaFuenteDatosConsulta('grid', null, 'destinatarios', 'destinatarios_listado', filtros, eventos),

            selectedItemKeys: [],
            selectionChanged: (data)=>{
                this.selectedItemKeys = data.selectedRowKeys                
            },      
        }
    }
}

export default grid

</script>