import gestion_acciones_elementos from "../gestion_acciones_elementos/gestion_acciones_elementos.js"
import gestion_pantalla_metodos from "./gestion_pantalla_metodos.js"
import gestion_pantalla_ventanas from "./gestion_pantalla_ventanas.js" 

const barra_elementos = function(forma, datos) {
    let barra_botones = [                   
        {
            widget  : "dxDropDownButton",
            location: "after",
            options : {
                items      : gestion_acciones_elementos.items_gestion(
                    forma, 
                    "ventana_gestion",
                    datos
                ),  
                displayExpr: 'titulo',
                keyExpr    : 'id',
                icon       : 'fas fa-mouse',  
                stylingMode: 'contained',
                keyExpr    : 'id',
                text       : "Acciones de Gestión",    
                onItemClick: forma.accion_click,  
                width      : 350,
                stylingMode: 'filled',
                type       : 'default'                                 
            }
            
        },
        
        {
            widget  : "dxButtonGroup",
            location: "before",                       
            options : {                            
                items      : gestion_pantalla_ventanas.ver_ventanas(forma),  
                onItemClick: forma.elemento_click
            }
        }     
    ]

    return barra_botones
}

export default {
    metodos : gestion_pantalla_metodos.metodos,
    barra_elementos: barra_elementos
}