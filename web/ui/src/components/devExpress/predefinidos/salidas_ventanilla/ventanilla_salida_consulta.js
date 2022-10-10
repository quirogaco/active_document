
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
                consulta_anexos.grupoAnexos
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

let forma_id = "ventanilla_salida_consulta"  

let definicion = {
    'estructura'  : 'radicados_salida',
    "titulo"      : "Consulta Radicados Salida",
    'campos'      : campos,
    "nombre_forma": forma_id,    
    "metodos"     : {
        "retorno_envio": function(respuesta) {}
    },
    "eventos"     : {        
        "montado": function(objeto) {                                      
            //console.log("ventanilla_radicado_consulta -> MONTADO")
            window.scroll(0,0)     
        },

        "inicializado": function(objeto) {
            //console.log("ventanilla_radicado_consulta -> INICIALIZADO")
        }
    },

    "metodos"     : {
        "cambiaDatosEvento": function(forma, datos) {
            // Grid de anexos
            console.log("datos:", datos) // atributos_internos.archivos_anexos
            
            window.scroll(0,0);
            let grid_anexo  = window.$ns["ventanilla_salida_consulta_archivos"]                     
            let fuenteAnexo = new ArrayStore({
                data: datos["archivos"],
                key : 'id'
            })
            grid_anexo.option('dataSource', fuenteAnexo);            
            
            /*
            // Grid de logs
            let gridLog   = window.$ns["radicado_pqr_logs"]
            let datosLog  = datos["logs"];            
            let fuenteLog = new ArrayStore({
                data: datosLog,
                key : 'id'
            })
            gridLog.option('dataSource', fuenteLog);
            
            // Grid de anexos
            let gridAnexo   = window.$ns["radicado_pqr_anexos"]
            let datosAnexo  = datos["anexos"];            
            let fuenteAnexo = new ArrayStore({
                data: datosAnexo,
                key : 'id'
            })
            gridAnexo.option('dataSource', fuenteAnexo);
            */
        }
    }

}

let componente = forma_objeto.forma_objeto_crud(definicion)

export default componente;