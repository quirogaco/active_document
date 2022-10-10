<template >

    <DxPopup
        ref                     = "popup"    
        v-model:visible         = "parametros.visible"        
        :drag-enabled           = "false"
        :close-on-outside-click = "true"
        :show-title             = "true"                   
        title                   = "Documento del expediente"
        width                   = 800
        height                  = 650            
    >        

        <div class="shadow-sm p-3 mb-3 bg-light rounded">

            <div class="container-fluid ">

                <DxLoadPanel
                    v-model:visible = "indicador_visible" 
                    message         = "Por favor espere"               
                    shading-color   = "rgba(0,0,0,0.4)"
                />


                <DxForm                       
                    ref        = "forma"
                    id         = "documento_expediente_base"
                    :form-data = "parametros.datos.datos_archivo"
                    :key       = "forma_key"
                    :col-count = "columnas"
                >

                    <DxGroupItem>
                        <DxSimpleItem     
                            ref             = "carpeta_nro"           
                            data-field      = "carpeta_nro"
                            editor-type     = "dxSelectBox"
                            :editor-options = "opciones_carpeta"
                        >
                            <DxLabel text="Carpeta"/>
                            <DxRequiredRule message="Carpeta es obligatorio"/>
                        </DxSimpleItem>  

                        <DxSimpleItem
                            data-field  = "soporte"
                            editor-type = "dxRadioGroup"
                            :editor-options = "opciones_soporte"
                        >
                            <DxLabel text="Soporte"/>
                            <DxRequiredRule message="Soporte obligatorio"/>                                      
                        </DxSimpleItem>  
                    </DxGroupItem>  

                    <DxGroupItem>
                        <DxSimpleItem
                            :visible        = false
                            data-field      = "id"
                        >                                     
                        </DxSimpleItem>                        

                        <DxSimpleItem                
                            data-field      = "tipo_id"
                            editor-type     = "dxSelectBox"
                            :editor-options = "opciones_tipo"
                        >
                            <DxLabel text="Tipo documental"/>
                            <DxRequiredRule message="Tipo es obligatorio"/>
                        </DxSimpleItem>

                        <DxSimpleItem
                            data-field  = "detalle"
                            editor-type = "dxTextBox"
                        >
                            <DxLabel text="Descripción"/>
                            <DxRequiredRule message="Descripción es obligatorio"/> 
                            <DxStringLengthRule
                                :max="200"
                                message="Maximo 200 caracteres"
                            />                      
                        </DxSimpleItem>

                        <DxSimpleItem
                            data-field  = "folios_fisicos"                    
                            editor-type = "dxNumberBox"
                            :isRequired = "opciones_folios.obligatorio"  
                            :visible    = "opciones_folios.visible" 
                            :editor-options = "opciones_folios.editor"  
                        >
                            <DxLabel text="Folios fisicos"/> 
                            <DxRangeRule
                                :min=1
                                message="Valor mayor o igual a 1"
                            />                                                
                        </DxSimpleItem>

                        <DxSimpleItem
                            data-field  = "fecha_creacion"
                            editor-type = "dxDateBox"
                            :editor-options = "opciones_fecha"                   
                        >
                            <DxLabel text="Fecha creación"/>
                            <DxRequiredRule message="Fecha es obligatoria"/>                                   
                        </DxSimpleItem>

                        <DxSimpleItem
                            data-field  = "observacion"
                            editor-type = "dxTextBox"
                        >
                            <DxLabel text="Observación"/>
                            <DxStringLengthRule
                                :max="200"
                                message="Maximo 200 caracteres"
                            />                      
                        </DxSimpleItem>

                        <DxSimpleItem
                            data-field  = "archivos" 
                            editor-type = "dxFileUploader"
                            :isRequired = "opciones_anexo.obligatorio"  
                            :visible    = "opciones_anexo.visible" 
                            :editor-options = "opciones_anexo.editor" 
                        >
                            <DxLabel text="Archivo electrónico"/>
                            <DxRequiredRule message="Archivo obligatorio"/>                                      
                        </DxSimpleItem>
                    </DxGroupItem>

                    <DxEmptyItem/>
                    <DxEmptyItem/>                
                </DxForm>

                <DxToolbar
                    ref = "barra"
                    :items = "barra_botones"
                />

            </div>  

        </div>
    
    </DxPopup>  

</template>

<script>
import { DxPopup } from 'devextreme-vue/popup'
import { DxLoadPanel } from 'devextreme-vue/load-panel'
import { DxFileUploader } from 'devextreme-vue/file-uploader'
import { 
    DxForm,
    DxSimpleItem,
    DxEmptyItem,
    DxButtonItem,
    DxGroupItem,
    DxLabel,
    DxRequiredRule,
    DxStringLengthRule,
    DxRangeRule
} from 'devextreme-vue/form'

import DxToolbar, { DxItem } from 'devextreme-vue/toolbar'

import fuenteDatos  from '../../../../../../../components/devExpress/remoto/fuenteDatos.js'
import forma_definiciones from "../../../../comunes_vue/forma/forma.js"

import pantalla_comunes      from './pantalla_comunes.js'

// CARPETA
let filtros = [];

let tipo_estructura = "archivo_base";

let archivo_base_trd =  {
    name: (tipo_estructura + '_trd'),

    components: {
        DxPopup,
        DxFileUploader,     
        // Tarea en ejecución
        DxLoadPanel,

        // Barra       
        DxItem,
        DxToolbar,

        // Forma
        DxForm,
        DxSimpleItem,
        DxEmptyItem,
        DxGroupItem,
        DxButtonItem,
        DxLabel,

        // Validadores
        DxRequiredRule, 
        DxStringLengthRule,  
        DxRangeRule      
    },

    props: {
        parametros: {
            type: Object,
            default: () => {
                return {}
            }
        },  
    },

    methods: pantalla_comunes.metodos, 

    data() {
        return {  
            forma_key: 0,
            columnas : 1,

            // Opciones editores
            opciones_id: {
                visible: false
            },

            opciones_carpeta: {
                dataSource  : [],
                displayValue: "nombre",
                displayExpr : "nombre",
                searchExpr  : "nombre",
                valueExpr   : "id",
                showClearButton: true,
                elementAttr : {
                    id: "documento_carpeta",
                },
                onOpened: function (e) {
                    let componente = e.component;
                    let items      = componente.option("items");
                    if (items.length == 1){
                        componente.option("value", items[0].id)
                    }                    
                }
            },

            opciones_tipo: {
                dataSource  : fuenteDatos.creaFuenteDatosConsulta(
                    'select', 
                    null, 
                    'agn_tipo_documental_trd', 
                    'agn_tipo_documental_trd', 
                    filtros, 
                    []
                ),
                displayValue: "nombre",
                displayExpr : "nombre",
                searchExpr  : "nombre",
                valueExpr   : "id",
                ShowClearButton: true,
            },

            opciones_folios: {
                visible        : true,
                value          : 1,
                showSpinButtons: true,
                ShowClearButton: true,
                obligatorio    : true
            },

            opciones_fecha: {
                dateSerializationFormat: "yyyy-MM-dd",
                displayFormat          : "yyyy-MM-dd",
                onFocusIn              : function(e) {
                    e.component.open()
                },
                ShowClearButton: true,
            },

            opciones_anexo: {
                visible    : true,
                obligatorio: true,
                editor: {
                    selectButtonText: "Seleccione archivo",
                    uploadMode      : "useForm"
                }
            },

            opciones_soporte: {
                items : ["DIGITALIZADO", "ELECTRONICO", "FISICO"],
                value : "DIGITALIZADO",
                layout: "horizontal",
                required: true,
                onValueChanged: function(obj) {
                    // Este mismo componente
                    let componente = _APLICACION_.component("archivo_base_trd");                      
                    switch (obj.value) {
                        case "FISICO":
                            componente.opciones_folios.visible = true;
                            componente.opciones_anexo.visible  = false;
                            break  

                        case "ELECTRONICO":
                            componente.opciones_folios.visible = false;
                            componente.opciones_anexo.visible  = true;
                            break 

                        default:
                            componente.opciones_folios.visible = true;
                            componente.opciones_anexo.visible  = true;
                            break  
                    }; 
                    filtros = ["subserie_id", "=", window.$pantalla_expediente.subserie_id];                    
                    if ([null, ""].includes(window.$pantalla_expediente.subserie_id)) {
                        filtros = ["serie_id", "=", window.$pantalla_expediente.serie_id]
                    };
                    console.log("FILTRO CAMBIA-0", componente, filtros);
                    let fuente_tipo = fuenteDatos.creaFuenteDatosConsulta(
                        'select', 
                        null, 
                        'agn_tipo_documental_trd', 
                        'agn_tipo_documental_trd', 
                        filtros,
                        []
                    );
                    componente.opciones_tipo.dataSource = fuente_tipo;
                    
                },                  
            },            
            
            // GENERALES
            // Indicador de tareas
            indicador_visible: false,
            
            // Barra de acciones
            barra_botones: pantalla_comunes.barra_botones(this)
        }
    },

    mounted() {
        // Forma especifica
        this.forma = this.$refs.forma.instance;
        this.barra = this.$refs.barra.instance;
        // Registra componentes
        window._APLICACION_.component("archivo_base_trd", this);
        window.$ventana_emergente = this;
                
        // Se maneja desde EXPEDIENTE
        console.log("dddddddddarchivo_expediente MONTADO -->>>this.parametros->", this.parametros)
        
        // CARPETA Crea fuente de datos
        if (this.parametros.datos.padre == "EXPEDIENTE") {
            filtros = ["expediente_id", "=", this.parametros.datos.padre_id]            
        } 
        let fuente_carpeta = fuenteDatos.creaFuenteDatosConsulta('select', null, 'agn_carpetas_trd', 'agn_carpetas_trd', filtros, []);
        let carpeta_nro    = this.forma.instance().getEditor("carpeta_nro");
        carpeta_nro.option("dataSource", fuente_carpeta);

        // TIPO DOCUMENTAL
        filtros = ["subserie_id", "=", window.$pantalla_expediente.subserie_id]
        if ([null, ""].includes(window.$pantalla_expediente.subserie_id)) {
            filtros = ["serie_id", "=", window.$pantalla_expediente.serie_id]
        }     
        console.log("FILTROS TIPO:", filtros);
        let fuente_tipo = fuenteDatos.creaFuenteDatosConsulta(
            'select', 
            null, 
            'agn_tipo_documental_trd', 
            'agn_tipo_documental_trd', 
            filtros,
            []
        );
        let tipo_id = this.forma.instance().getEditor("tipo_id");
        tipo_id.option("dataSource", fuente_tipo);

        this.mostrar_botones()
    },
}

export default archivo_base_trd;

</script>