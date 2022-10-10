
import ArrayStore              from 'devextreme/data/array_store';

import forma_objeto            from '../../forma/utilidades/forma_objeto.js'
import consulta_basicos        from '../radicados_comunes/consulta_basicos.js'
import consulta_identificacion from '../radicados_comunes/consulta_identificacion.js'
import consulta_peticion       from '../radicados_comunes/consulta_peticion.js'
import consulta_anexos         from '../radicados_comunes/consulta_anexos.js'

let tab_panel  = forma_objeto.tab_panel_objeto({
    "opciones" : {
        //"visible": false
    },
    'elementos': [
        {
            "titulo"   : "Información del radicado",     
            "columnas" : 2,                          
            "elementos": [
                consulta_basicos.grupoBasico,
                consulta_identificacion.grupoIdentificacion,                
            ]
        },
        {
            "titulo"   : "Petición",
            "elementos": [
                consulta_peticion.grupoPeticion    
            ]
        },
        {
            "titulo"   : "Documento, anexos y copias",
            "elementos": [
                consulta_anexos.grupoArchivos
            ]
        },
        {
            "titulo"   : "Historico",     
            "elementos": [
                //grupoAnexos
            ]
        },
    ]
});

let campos = [
    tab_panel   
]

let forma_id = "ventanilla_radicado_consulta"  

let definicion = {
    'estructura'  : 'radicados_entrada',
    "titulo"      : "Consulta Radicados",
    'campos'      : campos,
    "nombre_forma": forma_id,    
    "metodos"     : {
        "retorno_envio": function(respuesta) {}
    },

    "eventos"     : {        
        "montado": function(objeto) {              
            window.scroll(0,0)     
            if (window.$datos_por_ahora != undefined) {   
                objeto.asignaAtributoDinamico("formaDatos", window.$datos_por_ahora.datos)  
            }
        },

        "inicializado": function(objeto) {
            //console.log("ventanilla_radicado_consulta -> INICIALIZADO")
        }
    },

    "metodos"     : {
        "cambiaDatosEvento": function(forma, datos) {
            // Grid de anexos
            console.log("CAMBIAR-->>>datos:", datos) // atributos_internos.archivos_anexos
            
            window.scroll(0,0)
            console.log("window.$ns", window.$ns)
            setTimeout( function() {
                let grid_anexo  = window.$ns["ventanilla_radicado_consulta_archivos"]        
                console.log("grid_anexo:", grid_anexo)             
                let fuenteAnexo = new ArrayStore({
                    data: datos["archivos"],
                    key : 'id'
                })
                console.log("fuenteAnexo:", fuenteAnexo)  
                grid_anexo.option('dataSource', fuenteAnexo)
            },
            10000)
        }
    }

}

let componente = forma_objeto.forma_objeto_crud(definicion)

export default componente;
