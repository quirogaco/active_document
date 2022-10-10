let accion_click = function(e) {
    let accion = "" 
    if (e.itemData != undefined) {
        // toolbar dropdown button
        accion = e.itemData.id
    }
    else {
        // toolbar button
        accion = e
    }
    console.log("accion_click:", accion)
    let tramiteGestion = $cmp["tramiteGestion"]
    tramiteGestion.opciones_emergente.tipo_campos = null;
    tramiteGestion.opciones_emergente.titulo      = "";
    // Información del tramite
    tramiteGestion.opciones_emergente.tramite_id  = "";
    tramiteGestion.opciones_emergente.task_id     = "";
    switch (accion) {
        // Acciones tramite
        case 10:
            tramiteGestion.opciones_emergente.tipo_campos   = "usuario_responsable";
            tramiteGestion.opciones_emergente.titulo_accion = "Asignar";
            tramiteGestion.opciones_emergente.titulo        = "Asigna responable de gestiónar ( " + window.$usuario.ubicacion_nombre + " - "+ window.$usuario.dependencia_nombre + " )";
            break;

        case 20:
            tramiteGestion.opciones_emergente.tipo_campos   = "usuario_dependencia";
            tramiteGestion.opciones_emergente.titulo_accion = "Trasladar";
            tramiteGestion.opciones_emergente.titulo        = "Traslada a usuario de la dependencia del funcionario ( " + window.$usuario.dependencia_nombre + " )";
            break;

        case 30:
            tramiteGestion.opciones_emergente.tipo_campos   = "usuario_sede";
            tramiteGestion.opciones_emergente.titulo_accion = "Trasladar";
            tramiteGestion.opciones_emergente.titulo        = "Traslada a usuario de la territorial del funcionario ( " + window.$usuario.ubicacion_nombre + " )";
            break;

        case 40:
            tramiteGestion.opciones_emergente.tipo_campos   = "usuario_entidad";
            tramiteGestion.opciones_emergente.titulo_accion = "Trasladar";
            tramiteGestion.opciones_emergente.titulo        = "Traslada a usuario de la entidad";
            break;

        case 50:
            tramiteGestion.opciones_emergente.tipo_campos   = "enviar_visto_bueno";
            tramiteGestion.opciones_emergente.titulo_accion = "Enviar";
            tramiteGestion.opciones_emergente.titulo        = "Envia a visto bueno";
            break;

        case 60:
            tramiteGestion.opciones_emergente.tipo_campos   = "aprobar";
            tramiteGestion.opciones_emergente.titulo_accion = "Aprobar";
            tramiteGestion.opciones_emergente.titulo        = "Aprueba para radicar";
            break; 

        case 70:
            tramiteGestion.opciones_emergente.tipo_campos   = "devolver";
            tramiteGestion.opciones_emergente.titulo_accion = "Devolver";
            tramiteGestion.opciones_emergente.titulo        = "Devuelve para revisión";
            break; 

        case 80:
            tramiteGestion.opciones_emergente.tipo_campos   = "dependencia_usuario";
            tramiteGestion.opciones_emergente.titulo_accion = "Trasladar";
            tramiteGestion.opciones_emergente.titulo        = "Traslada a dependencia de la territorial del funcionario ( " + window.$usuario.ubicacion_nombre + " )";
            break; 

        case 90:
            tramiteGestion.opciones_emergente.tipo_campos   = "dependencia_entidad";
            tramiteGestion.opciones_emergente.titulo_accion = "Trasladar";
            tramiteGestion.opciones_emergente.titulo        = "Traslada a dependencia de la entidad";
            break;     

        case 100:
            tramiteGestion.opciones_emergente.tipo_campos   = "finalizar";
            tramiteGestion.opciones_emergente.titulo_accion = "Finalizar";
            tramiteGestion.opciones_emergente.titulo        = "Finaliza tramite";
            break;     
            
        // Datos
        case 200:
            tramiteGestion.opciones_emergente.tipo_campos   = "comentario_anotacion";
            tramiteGestion.opciones_emergente.titulo_accion = "Crear";
            tramiteGestion.opciones_emergente.titulo        = "Crea Comentario/anotación";
            break; 

        case 210:
            tramiteGestion.opciones_emergente.tipo_campos   = "archivos_anexos";
            tramiteGestion.opciones_emergente.titulo_accion = "Anexar";
            tramiteGestion.opciones_emergente.titulo        = "Anexa archivos";
            break; 

        case 220:
            tramiteGestion.opciones_emergente.tipo_campos   = "expediente";
            tramiteGestion.opciones_emergente.titulo_accion = "Asignar";
            tramiteGestion.opciones_emergente.titulo        = "Asigna expediente y tipo documental (TRD)";
            break; 

        case 230:
            tramiteGestion.opciones_emergente.tipo_campos   = "plantilla";
            tramiteGestion.opciones_emergente.titulo_accion = "Crear borrador";
            tramiteGestion.opciones_emergente.titulo        = "Crea borrador de respuesta";
            break; 

    }
    // Mostrar ventana emergente
    tramiteGestion.opciones_emergente.emergente_key += 1;
    tramiteGestion.opciones_emergente.visible        = true;
}


export default {
    accion_click: accion_click 
}