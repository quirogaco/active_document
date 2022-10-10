import click_herramientas from "./click_herramientas.js"; 

let acciones_items = function() {
    let items = [
        // Acciones dropwdon
        { id:  10, titulo: 'Asignar responsable',                         icon: "fas fa-user-check" },
        { id:  20, titulo: 'Trasladar a usuario de la dependencia',       icon: "fas fa-people-arrows" },    
        { id:  30, titulo: 'Trasladar a usuario de la territorial/sede',  icon: "fas fa-user-cog" },        
        { id:  40, titulo: 'Trasladar a usuario de la entidad',           icon: "fas fa-users-cog" },     
        { id:  50, titulo: 'Enviar a visto bueno',                        icon: "fas fa-user-tag" },      
        { id:  60, titulo: 'Aprobar',                                     icon: "fas fa-check-double" },   
        { id:  70, titulo: 'Devolver',                                    icon: "fas fa-hand-point-left" },     
        { id:  80, titulo: 'Trasladar a dependencia de territorial/sede', icon: "fas fa-building" },    
        { id:  90, titulo: 'Trasladar a dependencia de entidad',          icon: "fas fa-city" }, 
        { id: 100, titulo: 'Finalizar',                                   icon: "fas fa-window-close" }
    ]

    return items;
}

let acciones = [
    {
        widget  : "dxDropDownButton",
        location: "after",
        options : {
            items      : acciones_items(),  
            displayExpr: 'titulo',
            keyExpr    : 'id',
            icon       : 'fas fa-cog',  
            stylingMode: 'contained',
            keyExpr    : 'id',
            text       : "Acciones Tramite",    
            onItemClick: click_herramientas.accion_click,  
            width      : 350,
            elementAttr: {
                id: 'tramite_botones_acciones',
                css: 'bg-danger'
            }                     
        }
        
    }
]

export default {
    acciones: acciones 
}