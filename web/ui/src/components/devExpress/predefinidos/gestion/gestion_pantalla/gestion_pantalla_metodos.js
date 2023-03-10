import visores_archivo from "../../../../../librerias/visores_archivo.js";
import gestion_acciones_elementos
from "../gestion_acciones_elementos/gestion_acciones_elementos.js";
import gestion_pantalla_definiciones from "./gestion_pantalla_definiciones.js";

let valida_termino_accion = function(accion_id) {   
    let aprueba = true;
    // if ([3,2,8].indexOf(accion_id) > -1) {        
    //     let gestion_registro = $get_params("gestion_registro"); 
    //     if (gestion_registro.dias_gestion > 1) {
    //         $alertar("Ya pasaron mas de 2 dias habiles, no se puede trasladar o devolver! ", "Alerta");
    //         aprueba = false;       
    //     };         
    // };

    return aprueba;
};

let metodos = {
    // ######################################## //
    // Valida sin radicado tiene pdf principal  //
    // ######################################## //
    
    // Retorna información de validación remota
    'retorna_pdf': function(parametros) {
        let pdf_informacion = parametros["datos"]["pdf_informacion"]
        this.indicador_visible = false  
        if ( (pdf_informacion != null) && (pdf_informacion != "") ) {
            this.pdf_mostrar(pdf_informacion)
        }

        if ( 
            (this.parametros.borrador_id != null) && 
            (this.parametros.borrador_id != "") 
        ) {
            this.carga_borrador(this.parametros.borrador_id)
        }
    },

    // Invoca validación remota
    'valida_mostrar_pdf': function(origen_id, tipo_documento) {
        console.log("valida_mostrar_pdf>>>", tipo_documento)
        let estructura = "radicados_entrada";
        if (tipo_documento == "INTERNO") {
            estructura = "radicados_interno";
        };

        let parametros = {
            datos : {
                origen_id: origen_id,
                estructura : estructura
            },
            accion: "gestion_pdf_principal"
        };
        
        console.log("parametros>>>", parametros)       
        let urlCompleta = (
            window.$direcciones.servidorDatos + '/especifico_acciones'
        );   
        this.indicador_visible = true;
        window.$f["http"].llamadoRestPost( 
            urlCompleta, 
            parametros, 
            this.retorna_pdf, 
            ""
        );               
    },

    "pdf_visible": function(pdf_informacion) {
        return (pdf_informacion != null) && (pdf_informacion != "")
    },

    // Prepara valores para visor pdf en la forma, NO es invocación Popup
    "pdf_mostrar": function(pdf_informacion) {
        this.pdf_existe = true
        this.verPdf     = true 
        let pdf_parametros = {
            titulo_general: "Pdf del Radicado",
            archivo_id    : pdf_informacion.id, 
            tipo_documento: pdf_informacion.tipo_archivo, 
            titulo        : pdf_informacion.detalle,
            modo          : "leer",
            descarga      : 'no'
        }        
        let parametros = window.$lib.prepara_parametros_archivo(pdf_parametros); 
        this.opciones_pdf.nombrePdf = parametros.datos.idArchivo;
        this.opciones_pdf.buscarTexto = parametros.datos.buscarTexto;
        this.opciones_pdf.operacion = parametros.datos.operacion;           
        this.opciones_pdf.clase = parametros.datos.clase;
        this.opciones_pdf.descarga = parametros.datos.descarga;
        this.opciones_pdf.titulo = parametros.datos.titulo_general; 
        if ( 
            (this.parametros.borrador_id != null) && 
            (this.parametros.borrador_id != "") 
        ) {
            this.clase_pdf = "col-6 shadow-sm p-3 mb-3 bg-body rounded";
            this.clase_borrador = "col-6 shadow-sm p-3 mb-3 bg-body rounded";
        }
        else {
            this.clase_pdf = "col-12 shadow-sm p-3 mb-3 bg-body rounded"
        }      
        this.repintar_pdf += 1;
        this.barra_elementos_visuales = gestion_pantalla_definiciones.barra_elementos(
            this,
            this.parametros
        )
    },

    // ************************ //
    // Muestra pdf del borrador //
    //************************* //
    "retorna_borrador_mostrar": function(parametros) {
        window.$ocultar_esperar();
        visores_archivo.ver_descarga_archivo({
            archivo_id: parametros.nombre_archivo, 
            operacion : 'pdf_disco', 
            titulo    : "BORRADOR",
        })
    },

    "pdf_borrador_mostrar": function() {
        window.$mostrar_esperar("Por favor espere..")
        let parametros = {
            peticion: this.parametros.id,
            accion  : "PDF_BORRADOR"
        };        
        let urlCompleta = (
            window.$direcciones.servidorDatos + '/gestion_acciones'
        );
        window.$f["http"].llamadoRestPost( 
            urlCompleta, 
            parametros, 
            this.retorna_borrador_mostrar, 
            ""
        )   
    },

    // ######### //
    // BORRADOR  //
    // ########## //
    // Manejo de BORRADOR
    'carga_borrador': function(borrador_id) {
        this.verBorrador = false;
        let etapa_estado = this.parametros.etapa_estado;
        let colaborativa = this.parametros.colaborativa;

        // Edición de borrador
        let modo = "editar";
        if (etapa_estado == "APROBADO_RESPUESTA") modo = "lectura";
        if (colaborativa != "") modo = "lectura";
        
        // Muestra editor
        let parametros_editor = window.$lib.unifica_datos_visor({
            titulo_general: "Consulta de Plantillas",
            archivo_id: borrador_id, 
            tipo_documento: "docx", 
            titulo: "Borrador en gestión",
            modo: modo,
            descarga: 'no'
        })        
        
        this.editor.mostrar_editor(parametros_editor);
        this.parametros.borrador_id = borrador_id;
        this.verBorrador = true;
        this.borrador_existe = true;
        if (this.pdf_existe == true) {
            this.clase_borrador = "col-6 shadow-sm p-3 mb-3 bg-body rounded";
            this.clase_pdf      = "col-6 shadow-sm p-3 mb-3 bg-body rounded";
        }
        else {
            this.clase_borrador = "col-12 shadow-sm p-3 mb-3 bg-body rounded";
        }  

        this.barra_elementos_visuales = 
            gestion_pantalla_definiciones.barra_elementos(
                this,
                this.parametros
            )
    },

    elemento_click(e) {
        let boton = e.itemData.code; 
        let parametros = {};          
        switch (boton) {
            case 'borrador':
                // Pdf
                this.verPdf = false;
                this.clase_pdf = "col-6 shadow-sm p-3 mb-3 bg-body rounded";
                
                // Borrador
                this.verBorrador = true;                        
                this.clase_borrador = "col-12 shadow-sm p-3 mb-3 bg-body rounded";
                break;

            case 'documento':
                // Borrador
                this.verBorrador = false;
                this.clase_borrador = "col-6 shadow-sm p-3 mb-3 bg-body rounded";

                // Pdf
                this.verPdf = true;
                this.clase_pdf = "col-12 shadow-sm p-3 mb-3 bg-body rounded";
                break;

            case 'radicado':
                parametros = gestion_acciones_elementos.elemento_parametros(20); 
                this.asigna_parametros(parametros);
                this.emergente_key += 1;
                
                break;

            case 'gestion':
                parametros = gestion_acciones_elementos.elemento_parametros(21); 
                this.asigna_parametros(parametros);
                this.emergente_key += 1;
                
                break;

            case 'ver_borrador':
                this.pdf_borrador_mostrar();
                break;

            case 'regresar':
                this.$router.push({path: "gestion_basica_grid"});
                break;

            default:
                // Borrador
                this.verBorrador = true;
                this.clase_borrador = "col-6 shadow-sm p-3 mb-3 bg-body rounded";
                
                // Pdf
                this.verPdf = true;
                this.clase_pdf = "col-6 shadow-sm p-3 mb-3 bg-body rounded";                                                
        }
    },

    asigna_parametros(parametros) {
        this.opciones_ventana.alto = parametros.alto;
        this.opciones_ventana.ancho = parametros.ancho;
        this.opciones_ventana.componente_visible = parametros.ventana;  
        this.opciones_ventana.titulo = parametros.titulo;   
        this.opciones_ventana.boton_mensaje = parametros.boton_mensaje;    
        this.opciones_ventana.accion = parametros.accion;  
        this.opciones_ventana.fuente = parametros.fuente; 
        this.opciones_ventana.visible = true;
        this.opciones_ventana.elementos = [this.parametros.id];
        //this.opciones_ventana.datos =  "{}";
        this.opciones_ventana.gestion = {
            'gestion_id': this.parametros.id,
            'gestion': this.parametros,
            'origen_tipo': this.tipo_documento,
            'entrada': this.radicado
        };

        let that = this;
        let cerrar = function(desde) {
            that.opciones_ventana.visible = false; 
            that.emergente_key += 1;                               
        };

        let datos = {
            "datos": this.opciones_ventana,
            "modo": "consulta",
            "llamado_por": "_call_",
            "call": this.cerrar
        };

        $save_params(
            "ventana_emergente_gestion", 
            {"datos": datos}
        )

        if ( 
            (this.opciones_ventana.accion == "RADICAR_DOCUMENTO") && 
            (this.tipo_documento == "INTERNO") 
        ) {
            this.opciones_ventana.componente_visible = "ventanilla_interno_forma";
        };

        if ( this.opciones_ventana.accion == "CONSULTA_RADICADO") {
            let datos = {
                "radicado": this.radicado,                
                "modo": "consulta",
                "llamado_por": "_call_",
                "call": cerrar
            };

            $save_params(
                "forma_radicado_consulta", 
                {"datos": datos}
            )
        };

        if ( this.opciones_ventana.accion == "CONSULTA_GESTION") {
            let datos = {
                "radicado": this.radicado,
                "gestion": this.opciones_ventana.gestion.gestion,
                "modo": "consulta",
                "llamado_por": "_call_",
                "call": cerrar
            };

            $save_params(
                "gestion_datos_consulta", 
                {"datos": datos}
            )
        };

        // Información del radicado
        this.opciones_ventana.consulta = {
            'datos': this.radicado            
        };        
    },

    accion_click(e) {             
        if ( valida_termino_accion(e.itemData.id) ) {
            let parametros = gestion_acciones_elementos.elemento_parametros(
                e.itemData.id
            )  
            this.asigna_parametros(parametros)
            this.emergente_key += 1;
        }
    }
};

export default {
    metodos        : metodos
};