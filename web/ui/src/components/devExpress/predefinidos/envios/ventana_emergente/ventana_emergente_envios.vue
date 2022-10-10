<template>
    <DxPopup
        ref                     = "popup"
        v-model:visible         = "opciones.visible"
        :drag-enabled           = "false"
        :close-on-outside-click = "true"
        :show-close-button      = "true"
        :show-title             = "true"
        :title                  = "titulo"
        container               = ".dx-viewport" 
        :element-attr           = "popupAttributes"
    >
        <DxScrollView
            width = "100%"
            height= "100%"
        >
        
            <DxDataGrid
                ref="grid"
                :data-source             = "fuente_datos"
                :selection               = "{ mode: 'multiple' }"
                :show-borders            = "true"
                :columns                 = "columnas"
                @selection-changed       = "selectionChanged" 
                @toolbar-preparing       = "onToolbarPreparing"
            >
                <template #addButton>
                    <DxButton
                        @click = "addRecords()"
                        icon   = "fas fa-plus-square"
                        text   = "Adicionar salida(s)"
                    />
                </template>

            </DxDataGrid>
            
        </DxScrollView>
    </DxPopup>
</template>

<script>
import { DxPopup } from 'devextreme-vue/popup'
import { DxScrollView } from 'devextreme-vue/scroll-view'

import {
    DxDataGrid,
    DxColumn,    
    DxSelection,
} from 'devextreme-vue/data-grid';
import { DxButton } from 'devextreme-vue/button'

import fuenteDatos from '../../../remoto/fuenteDatos.js'

// Columnas
import grid_columnas from './grid_columnas.js'

// Ventana emergente
let ventana =  {
    name: 'ventana_emergente_envios',

    components: {
        DxPopup,
        DxScrollView,
        DxDataGrid,
        DxColumn,    
        DxSelection,
        DxButton
    },

    props: {
        opciones: {
            type: Object,
            default: () => {
                return {}
            }
        }        
    },
    
    mounted() {},

    data() {
        return {

            titulo : "Seleccionar salidas",

            columnas      : grid_columnas.columnas, // Columnas grid

            fuente_datos  : fuenteDatos.creaFuenteDatosConsulta('grid', null, 'salidas', 'radicados_salida', []),

            popupAttributes: {
                id: 'ventana_emergente_envios',
                class: 'bg_tab_panel'
            },

            seleccionados   : [],
            selectionChanged: (data)=>{
                this.seleccionados = data.selectedRowsData
            },

            onToolbarPreparing(e) {
                e.toolbarOptions.items.push({
                    location: 'after',
                    template: 'addButton'
                });
            },

            addRecords:()=> {
                let regitros = []
                for (let seleccionado of this.seleccionados) {
                    this.contador = this.contador + 1 
                    let datos = {                        
                        "id"            : this.contador,
                        "id_temporal"   : this.contador,
                        "radicado_id"   : seleccionado.id,
                        "nro_radicado"  : seleccionado.nro_radicado,                        
                        "fecha_radicado": seleccionado.fecha_radicado,                        
                        "destinatario"  : seleccionado.tercero_nombre_completo,                        
                        "direccion"     : seleccionado.tercero_direccion,
                        "ubicacion"     : seleccionado.tercero_ciudad_nombre,
                        "guia_envio"    : "",
                    }
                    regitros.push(datos)
                }
                window.$grid_envios.nuevos_registros(regitros)
            },

            contador: 0
        }
    }
}

export default ventana;

</script>