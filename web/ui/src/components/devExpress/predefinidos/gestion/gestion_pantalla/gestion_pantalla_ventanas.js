let ventanas_globales = [
    // 0 - ambos
    {
        alignment: 'left',
        code     : 'ambos',
        type     : 'default',
        text     : 'Borrador-Documento', 
    },

    // 1 - borrador
    {
        icon     : 'fas fa-file-word',
        alignment: 'center',
        code     : 'borrador',
        type     : 'default',
        text     : 'Borrador',
    },

    // 2 - pdf documento
    {
        icon     : 'fas fa-file-pdf',
        alignment: 'right',
        code     : 'documento',
        type     : 'default',
        text     : 'Documento',
    },

    // 3 - radicado
    {
        icon     : 'fas fa-file-alt',
        alignment: 'right',
        code     : 'radicado',
        type     : 'default',
        text     : 'Datos Radicado',
    },

    // 4 - datos gestión
    { 
        icon     : 'fas fa-file-alt',
        alignment: 'right',
        code     : 'gestion',
        type     : 'default',
        text     : 'Datos Gestión',
    },

    // 5 - datos gestión
    { 
        icon     : 'fas fa-eye',
        alignment: 'right',
        code     : 'ver_borrador',
        type     : 'default',
        text     : 'Pdf borrador',
    },
    
    // 6 - regresar
    {
        icon     : 'fas fa-backward',
        alignment: 'right',
        code     : 'regresar',
        type     : 'default',
        text     : 'Regresar',
    }
]

const esconde_botones = function(ocultar) {
    let ventanas = []
    for (const iv in ventanas_globales) {
        let codigo  = ventanas_globales[iv]["code"]
        let mostrar = true 
        for (const io in ocultar) {
            if (codigo == ocultar[io]) mostrar = false;
        }

        if (mostrar == true) ventanas.push(ventanas_globales[iv])
    }

    return ventanas
}

// Botones de manejo de ventanas pdf y borrador
const ver_ventanas = function(forma) {
    let ocultar = []
    console.log("forma.parametros.borrador_id>>", forma.parametros);
    // Ocultar radicado
    if ( forma.parametros.origen_tipo == "SALIDA") {
        ocultar.push("radicado");
    }

    if ( forma.parametros.origen_tipo == "INTERNO") {
        ocultar.push("gestion");
    }

    // Ocultar borrador
    if ( 
            (forma.parametros.borrador_id == "") || 
            (forma.parametros.borrador_id == undefined) 
    ) {
        ocultar.push("borrador")
        ocultar.push("ambos")  
        ocultar.push("ver_borrador")      
    }

    // Ocultar pdf
    if ( (forma.pdf_existe == false) ) {
        ocultar.push("documento")
        ocultar.push("ambos")
    }
    
    let ventanas = esconde_botones(ocultar)
    let etapa_estado = forma.parametros.etapa_estado

    switch (etapa_estado) {
        case "APROBADO_RESPUESTA":
            //ventanas = []  
            break
        
        case "ASIGNADO_DEPENDENCIA":
            //ventanas = ventanas_globales
            break

        default:
            //ventanas = ventanas_globales
            break
            
    }

    return ventanas
}

export default {
    ventanas_globales: ventanas_globales,
    ver_ventanas: ver_ventanas
}