<template src="./envio_electronico_plantilla.html">
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
import { DxResponsiveBox, DxItem, DxLocation, DxCol, DxRow } from 'devextreme-vue/responsive-box'
import { locale, loadMessages, formatMessage } from 'devextreme/localization'
import notify from 'devextreme/ui/notify'

import fuenteDatos from '../../../remoto/fuenteDatos.js'

// Columnas
import envio_electronico_columnas from './envio_electronico_columnas.js'
// Metodos
import envio_electronico_metodos from './envio_electronico_metodos.js'

// Grid de envio electronico
let grid =  {
    created() {
        locale("es")
    },

    components: {
        DxDataGrid,
        DxColumn,
        DxSelection,
        DxEditing,
        DxButton
    },
    
    methods: envio_electronico_metodos.metodos,
    
    mounted() {
        setTimeout(() => {
            window.$grid_planilla = this
        }, 3000);
        this.notify = notify        
    },

    data() {
        return {
            screen(width) {
                return (width < 700) ? 'sm' : 'lg';
            }, 

            columnas      : envio_electronico_columnas.columnas, // Columnas grid

            fuente_datos  : fuenteDatos.creaFuenteDatosConsulta('grid', null, 'salida', 'radicados_salida', [], []),

            selectedItemKeys: [],
            selectionChanged: (data)=>{
                this.selectedItemKeys = data.selectedRowKeys                
            },   
            
            urlCompleta: window.$direcciones.servidorDatos + '/envio_acciones'   
        }
    }
}

export default grid

</script>