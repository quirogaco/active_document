import forma_definiciones from "../../../comunes_vue/forma/forma.js"

let fuente_orden = [
    {
        selector: "codigo",
        desc    : false
    }
] 

const discapacidad_id = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'      : '¿ Presenta algún tipo de discapacidad ?', 
        "fuente"      : "discapacidad",  
        "fuente_orden": fuente_orden
    }
    
    return forma_definiciones.genera_campo("seleccion", "discapacidad_id", id, atributos_base, atributos)
}

const poblacion_id = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'        : '¿ Perteneces a algún tipo de población especial ?', 
        "fuente"        : "tipo_poblacion",   
    }
    
    return forma_definiciones.genera_campo("seleccion", "poblacion_id", id, atributos_base, atributos)
}

const rango_id = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'        : 'Selecione su rango de edad', 
        "fuente"        : "rango_edad",   
        "obligatorio"   : true  
    }
    
    return forma_definiciones.genera_campo("seleccion", "rango_id", id, atributos_base, atributos)
}

const genero_id = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'        : '¿ Con cuál genero se identifica ?', 
        "fuente"        : "genero",   
        "obligatorio"   : true  
    }
    
    return forma_definiciones.genera_campo("seleccion", "genero_id", id, atributos_base, atributos)
}

const mensaje_informacion = function(id=null, atributos={}) {
    let atributos_base = {
        "valor":  `
        <div class="shadow-sm p-3 m-3 rounded ">
            <div class="fs-6">
                "La Escuela Superior de Administración conforme los lineamientos establecidos en la Ley 1581 de 2012
                y su decreto reglamentario, como responsable de la recolección de los datos personales suministrados en el presente 
                documento, garantiza la seguridad y confidencialidad respecto del tratamiento de los datos sensibles o personales suministrados 
                para los fines de la presente solicitud, igualmente propenderá por su debida custodia, uso, circulación y supresión."
                Manifiesto y acepto que conozco los términos y condiciones de política para el uso y tratamiento de datos personales.
                Y autorizo el uso de mis datos personales para recibir notificaciones sobre los trámites relacionados con las actividades 
                misionales adelantadas por la entidad.
            </div>
        </div>
    `
    }
    
    return forma_definiciones.genera_campo("contenido", "mensaje_informacion", id, atributos_base, atributos)
}

const manejo_informacion = function(id=null, atributos={}) {
    let atributos_base = {
        "titulo"     : 'Acepta tratamiento de datos?', 
        "fuente"     : [
            {"id": "SI", "nombre": "SI"},
            {"id": "NO", "nombre": "NO"}
        ],          
        "obligatorio": true
    }
    
    return forma_definiciones.genera_campo("radio", "manejo_informacion", id, atributos_base, atributos)
}

export default {
    discapacidad_id    : discapacidad_id,
    poblacion_id       : poblacion_id,
    rango_id           : rango_id,
    genero_id          : genero_id,
    mensaje_informacion: mensaje_informacion,
    manejo_informacion : manejo_informacion
}