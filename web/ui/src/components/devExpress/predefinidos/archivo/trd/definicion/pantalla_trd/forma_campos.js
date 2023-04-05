let items = [
    {
        "componente": "campo",
        "tipo": "seleccion",
        "id": "fondo_id",
        "titulo": "Fondo documental", 
        "fuente": "agn_fondo_documental", 
        "filtros_fuente": ["estado_", "=", "ACTIVO"],
        "muestra_expresion": "nombre",
        "muestra_valor": "nombre",
        "busqueda_expresion": "nombre",
        "obligatorio": true
    },

    {
        "componente" : "campo",
        "tipo": "texto",
        "id": "sigla",
        "titulo": "Sigla", 
        "obligatorio": true,
        "longitud": 30,
        "ancho": 320
    },
    
    {
        "componente": "campo",
        "tipo": "texto",
        "id": "nombre",
        "titulo": "Nombre", 
        "obligatorio": true,
        "longitud": 200,
        "ancho": 720
    },

    {
        "componente": "campo",
        "tipo": "texto",
        "id": "version",
        "titulo": "Versión", 
        "obligatorio": true,
        "longitud": 10,
        "ancho": 150
    },

    {
        "componente": "campo",
        "tipo": "fecha",
        "id": "fecha_version",
        "titulo": "Fecha aprobación", 
        "obligatorio": true,
        "ancho": 170
    },
    
    {
        "componente": "campo",
        "tipo": "radio",
        "id": "estado_",
        "titulo": "Estado TRD ?", 
        "obligatorio": true,
        "fuente"     : [
            {id:"SI", nombre:"SI"},
            {id:"NO", nombre:"NO"}
        ],
    },
    
    {
        "componente": "campo",
        "tipo": "texto",
        "id": "territorial_codigo",
        "titulo": "Sede codigo", 
        "obligatorio": true,
        "longitud": 20,
        "ancho": 150
    },

    {
        "componente": "campo",
        "tipo": "texto",
        "id": "territorial_nombre",
        "titulo": "Sede nombre", 
        "obligatorio": true,
        "longitud": 200,
        "ancho": 720
    },

    {
        "componente": "campo",
        "tipo": "seleccion",
        "id": "ubicaciones_gestion",
        "titulo": "Territorial de gestion", 
        "fuente": "ubicaciones", 
        "filtros_fuente": ["estado_", "=", "ACTIVO"],
        "muestra_expresion": "nombre",
        "muestra_valor": "nombre",
        "busqueda_expresion": "nombre",
        "obligatorio": true,
        "ancho": 720
    },

    {
        "tipo": 'archivo',
        "aceptar": ".xlsx",
        "extensiones": [".xlsx"],
        "titulo" : 'Excel a importar',    
        "obligatorio": true,
        "visible": false
    }
];

let get_items = function(importar) {
    items[9].visible = false;
    if  (importar == true) {
        items[9].visible = true;
    }

    return [{
        "tipo": 'grupo',
        'elementos': items
    }]
}

export default {
    items: get_items
}