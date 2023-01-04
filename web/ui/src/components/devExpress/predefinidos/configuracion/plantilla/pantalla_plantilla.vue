<template src="./pantalla_plantilla.html">
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
    DxStringLengthRule,
    DxItem 
} from 'devextreme-vue/form'
import { DxScrollView } from 'devextreme-vue/scroll-view';
import DxToolbar from 'devextreme-vue/toolbar';
import DxButton from 'devextreme-vue/button';
import notify from 'devextreme/ui/notify';
import DxValidationGroup from 'devextreme-vue/validation-group';

import general_form from "@/comunes_vue/forma/forma.js";
import fuenteDatos from '../../../remoto/fuenteDatos.js';
import onlyoffice_editor from '../../../../onlyOffice/onlyoffice_editor.vue';

import pantalla_plantilla_definiciones from "./pantalla_plantilla_definiciones.js";

let plantilla =  {
    name: 'plantilla',

    components: {
        // Tarea en ejecución
        DxLoadPanel,

        // Barra       
        DxItem,
        DxButton,        
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
        DxValidationGroup,

        DxScrollView,
        onlyoffice_editor
    },

    props: {
        datos: ""   
    },

    mounted() {
        this.archivo_visible = false;
        this.indicador_visible     = false;
        this.forma                 = this.$refs.forma.instance;            
        this.barra                 = this.$refs.barra.instance;
        this.editor                = this.$refs.editor;  
        this.notify                = notify; 
        window.$pantalla_plantilla = this;  
        //this.parametros            = JSON.parse(this.datos);
        this.parametros = general_form.lee_propiedades({}, "pantalla_plantilla");
        console.log(" PLANTILLA->this.parametros:", this.parametros);
        if (this.parametros.modo == "modificar") {
            // No cargar archivo de disco            
            //this.archivo_visible = true;
            // Mostrar visor            
            let archivo = this.parametros.plantilla_datos.mostrar_archivos;
            console.log(" PLANTILLA-> archivo:", archivo)
            if (archivo != undefined) {
                let parametros = window.$lib.unifica_datos_visor({
                    titulo_general: "Consulta de Plantillas",
                    archivo_id    : archivo.id, 
                    tipo_documento: archivo.tipo_archivo, 
                    titulo        : this.parametros.plantilla_datos.descripcion,
                    modo          : "editar",
                    descarga      : 'no'
                });
                this.editor_visible = true;
                this.repintar_onlyoffice += 1;
                this.editor.mostrar_editor(parametros);
            }
            else  {
                this.archivo_visible = true
            }             
        }
        else {
            this.archivo_visible = true
        }
        this.mostrar_botones()
    },

    methods: pantalla_plantilla_definiciones.metodos,

    data() {
        return {    
            // Opciones ONLY OFFICE        
            opciones_onlyoffice: {
                visible: false,
                editor : {}
            },            
            // Repintar only office 
            repintar_onlyoffice: 0,
            editor_visible     : false,

             // Indicador de tareas
            indicador_visible: false,

            // Datos de la forma
            parametros: {},

            opciones_id: {
                visible: false
            },
                
            // Opciones CAMPOS
            opciones_dependencia: {
                dataSource  : fuenteDatos.creaFuenteDatosConsulta('select', null, 'dependencias', 'dependencias', [], []),
                displayValue: "nombre_completo",
                displayExpr : "nombre_completo",
                searchExpr  : "nombre_completo",
                valueExpr   : "id"
            },

            // Carga de archivos
            archivo_visible: true,
            opciones_anexo: {
                uploadMode           : "useForm",
                allowedFileExtensions: ['.docx']
            },            
            
            // Barra de acciones
            barra_botones: pantalla_plantilla_definiciones.barra_botones(this)        
        }
    }
}

export default plantilla;

</script>