import componentes_llamados_crud_comunes from './componentes_llamados_crud_comunes.js';
import dialogos                          from './dialogos.js';

// #####################
//         FORMA       #
// #####################

// Envia datos de la forma a la acción especifica
// Valida si es necesario, "eliminar" no valida
const enviaForma = function(idComponente, accion, validar=true) {
    let componente     = window.$ns[idComponente]
    let definicion     = window.$definiciones[idComponente]
    let formaInstancia = componente.referencia.$_instance        
    let validacion     = formaInstancia.validate()
    let datosForma     = JSON.parse( JSON.stringify( formaInstancia.option("formData") ) ) 
    let validado       = validacion.isValid
    let mensajes       = validacion.brokenRules

    // Validación y captura de archivos
    let archivos         = $lib.valoresForma("dxFileUploader", "archivos", definicion).archivos
    if ( (archivos != undefined) && (archivos.length > 0) ) {
        datosForma['archivos'] = archivos
    }
    let archivosMensajes = $lib.validaValoresForma("dxFileUploader", definicion);
    if (archivosMensajes.length > 0) {
        validado = false
        mensajes = mensajes.concat(archivosMensajes)
    }
    
    let metodo_envia = (componente.envia_datos != undefined) ? componente.envia_datos: componente.enviaDatos;
    if (validar == true) {
        if (validado == true) {
            metodo_envia(accion, datosForma)
        }
        else {
            componente.mensajeValidacion(mensajes)   
        }      
    }
    else {
        metodo_envia(accion, datosForma)
    }

    return formaInstancia
};

// Forma boton CREA
const botonCrea = function(idComponente, titulo="Crear") {
    let idBoton = idComponente + "_boton_crea";
    let atributos = {
        titulo: titulo, 
        tipo  : 'success',
        icono : 'add'
    };
    let click = () => {  
        enviaForma(idComponente, "insertar")                     
    };
    let boton = componentes_llamados_crud_comunes.creaBotonBarra(idBoton, atributos, click)

    return boton
};

// Forma boton MODIFICA
const botonModifica = function(idComponente, titulo="Modificar") {
    let idBoton = idComponente + "_boton_modifica";
    let atributos = {
        titulo: titulo, 
        tipo  : 'default',
        icono : 'edit'
    };
    let click = () => {  
        enviaForma(idComponente, "modificar")                           
    };
    let boton = componentes_llamados_crud_comunes.creaBotonBarra(idBoton, atributos, click)

    return boton
};

// Forma boton ELIMINA
const botonElimina = function(idComponente, titulo="Eliminar") {
    let idBoton   = idComponente + "_boton_elimina";
    let atributos = {
        titulo: titulo, 
        tipo  : 'danger',
        icono : 'clear'
    };
    let click = () => {   
        dialogos.miDialogo().show().then((resultado) => {
            if (resultado.respuesta == "SI") {
                enviaForma(idComponente, "eliminar", false);                    
            }
        });                                         
    };
    let boton = componentes_llamados_crud_comunes.creaBotonBarra(idBoton, atributos, click)

    return boton
};

// Forma boton REGRESA
const botonRegresa = function(idComponente, titulo="Regresar") {
    let idBoton = idComponente + "_boton_regresa";
    let atributos = {
        titulo: titulo, 
        tipo  : 'normal',
        icono : 'chevronprev'
    };
    let click = () => {  
        let componente = window.$ns[idComponente];
        window.$rutasNavegacion.ruta.push({ path: componente.regresarComponente })  
        //window.$router.push({ path: componente.regresarComponente })  
        //componente.$router.push({ path: componente.regresarComponente })    
        window.scroll(0,0);                          
    };
    let boton = componentes_llamados_crud_comunes.creaBotonBarra(idBoton, atributos, click)

    return boton
};

const botonesForma = function(idComponente, botones={crea:true, modifica:true, elimina:true, regresa:true}) {
    let lista = [];

    // Botones opción
    let crea     = (botones.crea     != undefined) ? botones.crea     : true;
    let modifica = (botones.modifica != undefined) ? botones.modifica : true;
    let elimina  = (botones.elimina  != undefined) ? botones.elimina  : true;
    let regresa  = (botones.regresa  != undefined) ? botones.regresa  : true;

    let titulo_crea     = (botones.titulo_crea     != undefined) ? botones.titulo_crea     : "Crear";
    let titulo_modifica = (botones.titulo_modifica != undefined) ? botones.titulo_modifica : "Modificar";
    let titulo_elimina  = (botones.titulo_elimina  != undefined) ? botones.titulo_elimina  : "Eliminar";
    let titulo_regresa  = (botones.titulo_regresa  != undefined) ? botones.titulo_regresa  : "Regresar";
    
    if (crea==true)     lista.push(botonCrea(idComponente,     titulo_crea));
    if (modifica==true) lista.push(botonModifica(idComponente, titulo_modifica));
    if (elimina==true)  lista.push(botonElimina(idComponente,  titulo_elimina));
    if (regresa==true)  lista.push(botonRegresa(idComponente,  titulo_regresa));

    return lista
}

export default {    
    // Acciones FORMA
    enviaForma   : enviaForma,     
    botonCrea    : botonCrea,
    botonModifica: botonModifica,
    botonElimina : botonElimina,    
    botonRegresa : botonRegresa,
    botonesForma : botonesForma,
} 