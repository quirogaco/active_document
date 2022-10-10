import { reactive, ref } from "vue";

// ******************** //
// VISORES HERRAMIENTAS //
// ******************** //

const mostrar_icono = function(boton, atributo) {    
    // esconde/Muestra
    $cmp["tramiteGestion"][atributo].show = !$cmp["tramiteGestion"][atributo].show;
    
    // cambia icono
    let icon = boton.option("icon").replace('far ', '').replace('fas ', '');
    if ($cmp["tramiteGestion"][atributo].show == true) icon = "far " + icon
    else icon = "fas " + icon;
    boton.option("icon", "");    
    boton.option("icon", icon);    
};

let herramientas = [
    {
        location: 'before',
        widget  : 'dxButton',            
        options : {
            icon: 'far fa-list-alt',
            hint: 'Mostrar/Ocultar Datos',
            // si  lleva text, genera error cambiar icono
            //text: 'Ver datos',
            type: 'default',
            onClick() {       
                mostrar_icono(this, "atributos_datos");
            },
        },
    }, 

    {
        location: 'before',
        widget  : 'dxButton',                                
        options : {
            icon: 'fas fa-file-pdf',
            hint: 'Mostrar/Ocultar Pdf',
           // text: 'Ver pdf',
            type: 'default',
            onClick() {    
                mostrar_icono(this, "atributos_pdf");
            },
        },
    }, 

    {
        location: 'before',
        widget  : 'dxButton',                                
        options : {
            icon: 'fas fa-file-word',
            hint: 'Mostrar/Ocultar borrador Word',
            type: 'default',
            //text: 'Ver borrador word',
            onClick() {                    
                mostrar_icono(this, "atributos_borrador");
            },
        },
    }, 

    {
        location: 'before',
        template: '<i class="fas fa-grip-horizontal"></i>'                
    } 
]

export default {
    herramientas: herramientas
}