import forma_objeto            from '../../forma/utilidades/forma_objeto.js'

let identificacion = forma_objeto.mostrar_datos([
    {
        "campo" : "tercero_clase",        
        "titulo": "Clase remitente"
    },
    {
        "campo"      : "tercero_tipo_tercero_nombre",
        "titulo"     : "Tipo de remitente", 
    },
    {
        "campo"      : "tercero_tipo_identificacion_nombre",
        "titulo"     : "Tipo de identificación", 
    },
    {
        'campo'      : 'tercero_nro_identificacion',
        'titulo'     : 'Nit / Número de identificación',
    },
    {
        'campo'      : 'tercero_razon_social',
        'titulo'     : 'Razon social',
    },    
    {
        'campo'      : 'tercero_nombres',
        'titulo'     : 'Nombres remitente',
    },
    {
        'campo'      : 'tercero_apellidos',
        'titulo'     : 'Apellidos remitente',
    },
    {
        'campo'      : 'tercero_cargo',
        'titulo'     : 'Cargo',
    },
    {
        'campo'      : 'tercero_correo_electronico',
        'titulo'     : 'Correo electrónico',
    },
    {
        'campo'      : 'tercero_direccion',
        'titulo'     : 'Dirección',
    },
    {
        'campo'      : 'tercero_codigo_postal',
        'titulo'     : 'Codigo postal',
    },
    {
        'campo'      : 'tercero_telefono',
        'titulo'     : 'Telefono',
    },
    {
        'campo'      : 'tercero_telefono_movil',
        'titulo'     : 'Telefono movil',
    },
    {
        'campo'      : 'tercero_fax',
        'titulo'     : 'Fax',
    },
    {
        "campo"      : "tercero_ciudad_nombre",
        "titulo"     : "Ciudad", 
    }
])

let grupoIdentificacion = forma_objeto.grupo_objeto({
    'titulo'   : 'Remitente identificación',
    'elementos': identificacion
});



export default{
    grupoIdentificacion: grupoIdentificacion
}