<template src="./gestion_pantalla.html">
</template>

<script>
    import { 
        ref
    } from 'vue'
    import { DxResponsiveBox, DxItem, DxLocation, DxCol, DxRow } from 'devextreme-vue/responsive-box'
    import { DxScrollView }  from 'devextreme-vue/scroll-view'
    import { DxLoadPanel }   from 'devextreme-vue/load-panel'
    import notify            from 'devextreme/ui/notify'
    import { DxBox }         from 'devextreme-vue/box'
    import DxButtonGroup     from 'devextreme-vue/button-group'
    import DxDropDownButton  from 'devextreme-vue/drop-down-button'
    import onlyoffice_editor from "../../../../onlyOffice/onlyoffice_editor.vue"
    import pdf_componente    from "../../../../pdfjs/pdf_componente.vue"
    import DxToolbar         from 'devextreme-vue/toolbar'

    import utilidades_estructura from '../../../../../librerias/utilidades_estructura.js'

    import gestion_pantalla_definiciones from "./gestion_pantalla_definiciones.js"

    import ventana_emergente from '../ventana_emergente/ventana_emergente.vue'

    export default {
        components: { 
            DxScrollView,           
            DxResponsiveBox,
            DxItem,
            DxLocation,
            DxCol,
            DxRow,
            DxButtonGroup,
            DxDropDownButton,
            DxBox,
            DxToolbar,
            DxLoadPanel,

            ventana_emergente,

            // Componentes
            onlyoffice_editor,
            pdf_componente
        },

        props: {
            datos: {
                type: String,
                default: () => {
                    return "{}"
                }
            }
        },

        data() {            
            return {  
                parametros: {},
            
                // Esta pantalla
                pantalla_key: 0,

                // Indicador de tareas
                indicador_visible: false,

                // Ventana emergente
                opciones_ventana: {
                    visible: false
                },
                emergente_key: 0,

                // Titulo de gestión
                titulo_gestion: "",
                tipo_documento: "",

                // Borrador
                verBorrador        : false,
                repintar_onlyoffice: 0,
                borrador_existe    : false,
                borrador_ancho     : ref("90%"), 
                borrador_alto      : ref("90%"),  
                clase_borrador     : "col-6 shadow-sm p-3 mb-3 bg-body rounded",
                // Opciones editor onlyoffice
                opciones_editor: {},
                
                // Pdf
                verPdf      : false,  
                repintar_pdf: 0,
                pdf_existe  : false,   
                pdf_ancho   : ref("90%"), 
                pdf_alto    : ref("90%"),            
                clase_pdf   : "col-6 shadow-sm p-3 mb-3 bg-body rounded",
                // Opciones visor PDF
                opciones_pdf: {},

                // Radicado
                radicado : {},
                
                // Botones
                barra_elementos_visuales  : []
            }
        },

        async mounted() {
            // Pantalla para invocar en acciones
            window.$pantalla_gestion = this  
            let temporal    = JSON.parse(this.datos)
            this.parametros = await utilidades_estructura.leer_registro_id("peticiones", temporal["id"])
            
            // PDF
            this.visor_pdf = this.$refs.visor_pdf
            // Si tiene PDF PRINCIPAL
            this.valida_mostrar_pdf(this.parametros.origen_id)

            // EDITOR
            this.editor      = this.$refs.editor  
            this.verBorrador = true
            let borrador_id  = this.parametros.borrador_id  
            let etapa_estado = this.parametros.etapa_estado   

            // Radicado
            this.radicado = await utilidades_estructura.leer_registro_id("radicados_entrada", this.parametros.origen_id)
        
            // BARRA DE ACCIONES
            this.barra_elementos_visuales = gestion_pantalla_definiciones.barra_elementos(this)
            console.log("this.parametros:", this.parametros)
            
            // Mensaje tipo de documento en gestión
            this.tipo_documento = this.parametros.origen_tipo            
            if (this.tipo_documento == "ENTRADA") {
                console.log("this.parametros:", this.parametros)
                if (this.parametros.colaborativa == "") {
                    if (this.parametros.rapida == "SI") {
                        this.titulo_gestion = "Gestión de respuesta RAPIDA [ ENTRADA - "  + this.parametros.nro_radicado + " ] "
                    }
                    else {
                        this.titulo_gestion = "Gestión de respuesta radicado [ ENTRADA - "  + this.parametros.nro_radicado + " ] "
                    }
                }
                else {
                    this.titulo_gestion = "Gestión de respuesta COLABORATIVA [ ENTRADA - "  + this.parametros.nro_radicado + " ] "
                } 
            }

            if (this.tipo_documento == "SALIDA") {
                this.titulo_gestion = "Gestión de borrador de SALIDA"
            }

            if (this.tipo_documento == "INTERNO") {
                this.titulo_gestion = "Gestión de borrador INTERNO"
            }
        },

        methods: gestion_pantalla_definiciones.metodos
    }
</script>