// ###################
// Llamado de forma //
// ###################

// Llama por router del GRID (componente), la forma (componente) 
const pushAsincronico = function(componente, llamado) {    
    let pushAsync = function(llamado) {
        return new Promise((resolve) => {
            resolve(window.$rutasNavegacion.ruta.push({path: llamado}));
        });
    };

    return pushAsync;
}

// Llamado asincronico a un componente
async function llamarFormaComponente(pushAsync, llamado, datos=null, modo= "", regresar="/") {
    // LLama componente asincronico
    await pushAsync(llamado, datos, regresar).then(() => {                           
        let componenteLLamado = window.$ns[llamado];
        if (componenteLLamado != undefined) {            
            // Asigna datos            
            if (datos != null) {
                componenteLLamado.asignaAtributoDinamico("formaDatos", datos)
            }
            else {
                //componenteLLamado.asignaAtributoDinamico("formaDatos", {})   
            }

            // Componente al cual regres
            if (regresar != null) {
                componenteLLamado.asignaAtributoDinamico("regresarComponente", regresar);  
            }

            componenteLLamado.asignaAtributoDinamico("forma_modo", modo)
        }    
        
        // Botones de la forma
        estadoBoton(llamado+"_boton_crea",     false);
        estadoBoton(llamado+"_boton_modifica", false);
        estadoBoton(llamado+"_boton_elimina",  false);
        estadoBoton(llamado+"_boton_regresa",  false);

        if (modo == "crear") {
            estadoBoton(llamado+"_boton_crea",    true);
            estadoBoton(llamado+"_boton_regresa", true);
        }  

        if (modo == "modificar") {
            estadoBoton(llamado+"_boton_modifica", true);
            estadoBoton(llamado+"_boton_elimina",  true);
            estadoBoton(llamado+"_boton_regresa",  true);
        } 

        if (modo == "consulta") {
            estadoBoton(llamado+"_boton_regresa", true);
        }  
    })
}

// Llamar componente crud, usando atributos y router 
async function llamarComponenteCrud(estructura, llamador, llamado, datos={}, modo="", regresar=null) {
    // Regresar a
    let regresarA = "/" + llamador;
    let llamarA = llamado;
    
    // Invoca componente llamado    
    let componente = window.$ns[llamador];  // Componente llamador    
    let pushAsync = pushAsincronico(componente, llamarA);
    await llamarFormaComponente(pushAsync, llamarA, datos, modo, regresarA)
}

// ######################
// Botones Utilitarios //
// #####################

// Asigna esto visible a un boton
const estadoBoton = function(idBoton, valor) {
    let componente = window.$ns[idBoton];
    if (componente != undefined) {
        componente.option("visible", valor);
    } 
} 

const creaBotonBarra = function(idBoton, atributos={}, click=null) {
    let boton = {
        stylingMode: 'contained',
        widget     : "dxButton",        
        options    : {
            text       : atributos.titulo,
            type       : atributos.tipo,
            stylingMode: 'contained',
            icon       : atributos.icono,
            elementAttr: {
                id: idBoton
            },
            onClick       : click,
            onContentReady: elementoListo(idBoton), 
        }              
    }     

    return boton;
}

// ##############
// Utilitarios //
// ##############

// Evento para cuando un componente este listo y registrarlo
const elementoListo = function(idElemento) {
    const listoBoton = function(e){            
        window.$ns[idElemento] = e.component;         
    }

    return listoBoton;
}

export default {
    estadoBoton         : estadoBoton,
    creaBotonBarra      : creaBotonBarra,
    elementoListo       : elementoListo,
    llamarComponenteCrud: llamarComponenteCrud
} 