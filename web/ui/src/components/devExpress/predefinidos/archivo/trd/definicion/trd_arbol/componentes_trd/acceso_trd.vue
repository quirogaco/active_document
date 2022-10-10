<template >

    <div class="bg_tab_panel">
        <div class="full-width-content ">

            <DxLoadPanel
                v-model:visible = "indicador_visible" 
                message         = "Por favor espere"               
                shading-color   = "rgba(0,0,0,0.4)"
            />


            <DxForm
                ref        = "forma"
                id         = "acessos_trd"
                :form-data = "opciones.datos"
            >

                <DxSimpleItem
                    :visible        = false
                    data-field      = "id"
                >                                     
                </DxSimpleItem>

                <DxSimpleItem
                    data-field      = "padre_id"
                    :visible        = false
                >                                     
                </DxSimpleItem>

                <DxSimpleItem
                    data-field      = "padre_tipo"
                    :editor-options = "opciones_padre_tipo"
                >
                    <DxLabel text="Padre tipo"/>                                   
                </DxSimpleItem>

                <DxSimpleItem
                    data-field      = "padre_nombre"
                    :editor-options = "opciones_padre_nombre"
                >
                    <DxLabel text="Padre nombre"/>                                   
                </DxSimpleItem>
                
                <DxSimpleItem
                    data-field  = "autorizacion"
                    editor-type = "dxRadioGroup"
                    :editor-options = "opciones_autorizacion"
                >
                    <DxLabel text="Autorización"/>
                    <DxRequiredRule message="Autorización obligatoria"/>                                      
                </DxSimpleItem>

                <DxSimpleItem                
                    data-field      = "usuarios"
                    editor-type     = "dxTagBox"
                    :editor-options = "opciones_usuarios"
                >
                    <DxLabel text="Usuarios autorizados"/>
                </DxSimpleItem>

                <DxSimpleItem                
                    data-field      = "grupos"
                    editor-type     = "dxTagBox"
                    :editor-options = "opciones_grupos"
                >
                    <DxLabel text="Grupos autorizados"/>
                </DxSimpleItem>

                <DxEmptyItem/>
                <DxEmptyItem/>                
            </DxForm>

            <DxToolbar
                ref = "barra"
                :items = "barra_botones"
            />

        </div>  

    </div>  

</template>

<script>
import { DxLoadPanel } from 'devextreme-vue/load-panel';
import { 
    DxForm,
    DxSimpleItem,
    DxEmptyItem,
    DxButtonItem,
    DxLabel,
    DxRequiredRule,
    DxStringLengthRule
} from 'devextreme-vue/form';


import DxToolbar, { DxItem } from 'devextreme-vue/toolbar'
import fuenteDatos from '../../../../../../remoto/fuenteDatos.js'

import pantalla_comunes      from './pantalla_comunes.js'

let tipo_estructura = "acceso"

let subserie_trd =  {
    name: (tipo_estructura + '_trd'),

    components: {
        // Tarea en ejecución
        DxLoadPanel,

        // Barra       
        DxItem,
        DxToolbar,

        // Forma
        DxForm,
        DxSimpleItem,
        DxEmptyItem,
        DxButtonItem,
        DxLabel,

        // Validadores
        DxRequiredRule, 
        DxStringLengthRule,        
    },

    props: {
        opciones: {
            type: Object,
            default: () => {
                return {}
            }
        },  
    },

    mounted: pantalla_comunes.montar_componente(tipo_estructura),
    methods: pantalla_comunes.metodos, 

    data() {
        return {  
            // Opciones editores
            opciones_padre_nombre: {
                disabled: true
            },

            opciones_padre_tipo: {
                disabled: true
            },

            opciones_padre_id: {
                visible: false
            },

            opciones_id: {
                visible: false
            },

            opciones_autorizacion: {
                items : ["RESERVADA", "CLASIFICADA", "PUBLICA"],
                layout: "horizontal"
            },

            opciones_usuarios: {
                dataSource  : fuenteDatos.creaFuenteDatosConsulta('select', null, 'usuarios', 'usuarios', [], []),
                displayValue: "nombre",
                displayExpr : "nombre",
                searchExpr  : "nombre",
                valueExpr   : "id"
            },

            opciones_grupos: {
                dataSource  : fuenteDatos.creaFuenteDatosConsulta('select', null, 'grupo_usuarios', 'grupo_usuarios', [], []),
                displayValue: "nombre",
                displayExpr : "nombre",
                searchExpr  : "nombre",
                valueExpr   : "id"
            },
            
            // GENERALES
            // Datos trd
            trd_id : "",

            // Indicador de tareas
            indicador_visible: false,
            
            // Barra de acciones
            barra_botones: pantalla_comunes.barra_botones(this)
        }
    }
}

export default subserie_trd;

</script>