import entryFactory from "bpmn-js-properties-panel/lib/factory/EntryFactory";

export default function (element, translate) {

    return [
        //accion({ id: "accion", element: element }, translate),
        
        asigna_responsable({ element: element }, translate),
        traslada_usuario_dependencia({ element: element }, translate),
        traslada_usuario_otra_dependencia({ element: element }, translate),
        traslada_usuario_entidad({ element: element }, translate),
        gestion_traslada_dependencia({ element: element }, translate),
        gestion_traslada_dependencia_entidad({ element: element }, translate),        

        gestion_visto_bueno({ element: element }, translate),
        gestion_aprobar({ element: element }, translate),
        gestion_devolver({ element: element }, translate),        

        finaliza({ element: element }, translate),
        archivo_anexa({ element: element }, translate),
        archivo_elimina({ element: element }, translate),

        accion_expediente({ element: element }, translate),
        accion_borrador({ element: element }, translate)
    ]
}

//********************//
// TRASLADO Y GESTIÓN //
//********************//
function asigna_responsable(props, translate) {
    let field = entryFactory.checkbox(translate, {
        id           : "gestion_asigna_responsable",
        label        : "Asignar responsable ?",
        modelProperty: "gestion_asigna_responsable"
    })

    return field
}

function traslada_usuario_dependencia(props, translate) {
    let field = entryFactory.checkbox(translate, {
        id           : "gestion_traslada_usuario_dependencia",
        label        : "Trasladar usuario dependencia ?",
        modelProperty: "gestion_traslada_usuario_dependencia"
    })

    return field
}

function traslada_usuario_otra_dependencia(props, translate) {
    let field = entryFactory.checkbox(translate, {
        id           : "gestion_traslada_usuario_otra_dependencia",
        label        : "Trasladar usuario otra dependencia ?",
        modelProperty: "gestion_traslada_usuario_otra_dependencia"
    })

    return field
}

function traslada_usuario_entidad(props, translate) {
    let field = entryFactory.checkbox(translate, {
        id           : "gestion_traslada_usuario_entidad",
        label        : "Trasladar usuario entidad ?",
        modelProperty: "gestion_traslada_usuario_entidad"
    })

    return field
}

function gestion_visto_bueno(props, translate) {
    let field = entryFactory.checkbox(translate, {
        id           : "gestion_visto_bueno",
        label        : "Enviar a visto bueno ?",
        modelProperty: "gestion_visto_bueno"
    })

    return field
}

function gestion_aprobar(props, translate) {
    let field = entryFactory.checkbox(translate, {
        id           : "gestion_aprobar",
        label        : "Aprobar ?",
        modelProperty: "gestion_aprobar"
    })

    return field
}

function gestion_devolver(props, translate) {
    let field = entryFactory.checkbox(translate, {
        id           : "gestion_devolver",
        label        : "Devolver ?",
        modelProperty: "gestion_devolver"
    })

    return field
}

function gestion_traslada_dependencia(props, translate) {
    let field = entryFactory.checkbox(translate, {
        id           : "gestion_traslada_dependencia",
        label        : "Trasladar dependencia ?",
        modelProperty: "gestion_traslada_dependencia"
    })

    return field
}

function gestion_traslada_dependencia_entidad(props, translate) {
    let field = entryFactory.checkbox(translate, {
        id           : "gestion_traslada_dependencia_entidad",
        label        : "Trasladar dependencia entidad?",
        modelProperty: "gestion_traslada_dependencia_entidad"
    })

    return field
}

//**********//
// ACCIONES //
//**********//
function finaliza(props, translate) {
    let field = entryFactory.checkbox(translate, {
        id           : "accion_finaliza",
        label        : "Finalizar gestiòn ?",
        modelProperty: "accion_finaliza"
    })

    return field
}

function archivo_anexa(props, translate) {
    let field = entryFactory.checkbox(translate, {
        id           : "accion_archivo_anexa",
        label        : "Anexar archivos ?",
        modelProperty: "accion_archivo_anexa"
    })

    return field
}

function archivo_elimina(props, translate) {
    let field = entryFactory.checkbox(translate, {
        id           : "accion_archivo_elimina",
        label        : "Eliminar archivos ?",
        modelProperty: "accion_archivo_elimina"
    })

    return field
}

function accion_expediente(props, translate) {
    let field = entryFactory.checkbox(translate, {
        id           : "accion_expediente",
        label        : "Asigna TRD ?",
        modelProperty: "accion_expediente"
    })

    return field
}

function accion_borrador(props, translate) {
    let field = entryFactory.checkbox(translate, {
        id           : "accion_borrador",
        label        : "Crea borrador respuesta ?",
        modelProperty: "accion_borrador"
    })

    return field
}


/*
function accion(props, translate) {
    const { element, id } = props;

    let field = entryFactory.selectBox(translate, {
        id           : "accion_tipo",
        description  : "Acciòn especifica",
        label        : "Accion",
        modelProperty: "accion_tipo",
        selectOptions: [
            { value: 'gestion',               name: 'Gestión' },
            { value: 'revisar',               name: 'Revisar' },
            { value: 'radicar',               name: 'Radicar' },            
            { value: 'finalizar',             name: 'Finalizar' },
            { value: 'trasladar_usuario',     name: 'Trasladar usuario' },
            { value: 'trasladar_dependencia', name: 'Trasladar dependencia' }
        ]
    })

    return field
}
*/