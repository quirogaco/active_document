import { 
    ref
} from 'vue'

import fuenteDatos from '../../remoto/fuenteDatos.js'

// Definición atributos GRID
const atributos_grid = function(configuracion, eventos) {    
    // Información basica del GRID
    let tipoComponente = "grid";
    let componente_id  = configuracion.ruta + '_' + configuracion.id;

    // #############################
    // Variable generales del grid #
    // #############################
    // Atributos especificos JCR !!
    let idComponente           = componente_id;
    let fuenteDatosGrid        = window.$librerias.cargaAtributo(configuracion, 'fuente', null); // JCR !! Cuando es local como se hace ??
    let tipoFuente             = window.$librerias.cargaAtributo(configuracion, 'tipofuente', null); // JCR !! Cuando es local como se hace ??    
    let elementosBarra         = window.$librerias.cargaAtributo(configuracion, 'elementosBarra', []); 
    let filtros                = window.$librerias.cargaAtributo(configuracion, 'filtros', []); 
    let ajustaPalabra          = window.$librerias.cargaAtributo(configuracion, 'ajustaPalabra', 'si');
    ajustaPalabra = (ajustaPalabra == "si" ? true : false);
    
    // Definición de columnas
    let  columnas        = window.$librerias.cargaAtributo(configuracion, 'columnas', []);
    // Nombres de las columna
    let  nombresColumnas =  ['id'];
    for (let columna of columnas) {   
        nombresColumnas.push(columna.dataField)     
    }    
    
    // ########################
    // Configuración del GRID #
    // ########################

    // # Busquedas
    // Campo global de busqueda
    let mostrarBusqueda = window.$librerias.cargaAtributo(configuracion, 'busqueda', true);    
    let busquedaPanel_cfg = ref({
        highlightCaseSensitive  : false,
        highlightSearchText     : false,
        placeholder             : "Buscar...",
        searchVisibleColumnsOnly: false,
        text                    : "",
        visible                 : mostrarBusqueda,
        width                   : 350
    })

    // Agrupamiento    
    let agrupa_cfg = ref({
        allowCollapsing      : true,
        autoExpandAll        : false,
        contextMenuEnabled   : true,
        expandMode           : 'buttonClick',
        texts                : {
            groupByThisColumn    : 'Agrupar por esta columna',
            groupContinuedMessage: 'Continuación de la página anterior',
            groupContinuesMessage: 'Continúa en la página siguiente',
            ungroup              : 'Desagrupar',
            ungroupAll           : 'Desagrupar todo'
        }
    })

    // Panel de agrupamiento
    let agrupa = window.$librerias.cargaAtributo(configuracion, 'agrupa', true);  
    let agrupaPanel_cfg = ref({
        allowColumnDragging: true,
        emptyPanelText     : 'Arrastre una columna aquí para agruparla',
        visible            : agrupa, 
    })

    // Fila busqueda encabezado
    let busquedaFila_cfg = ref({
        applyFilter          : 'auto',
        applyFilterText      : 'Aplicar filtro',
        betweenEndText       : "Final",
        betweenStartText     : 'Inicio',        
        resetOperationText   : 'Limpia',
        showAllText          : '(Todos)',
        showOperationChooser : true,
        visible              : true,
        operationDescriptions: {
            between           : "Entre",
            contains          : "Contiene",
            endsWith          : "Termina con",
            equal             : "Igual",
            greaterThan       : "Mayor que",
            greaterThanOrEqual: "Mayor o igual que",
            lessThan          : "Menor que",
            lessThanOrEqual   : "Menor o igual que",
            notContains       : "No contiene",
            notEqual          : "Distinto a",
            startsWith        : "Comienza con",
        }
    })

    // Opciones de ordenamiento
    let ordenamiento_cfg = ref({
        ascendingText  : "Ascendente",
        descendingText : "Descendente",
        clearText      : "Limpia ordenamiento",
        mode           : "multiple",
        showSortIndexes: true
    })

    // Opciones de exportacion
    let exportar_cfg = ref({
        enabled: true,
            texts: {
                exportAll         : "Exportar todos los datos",
                exportSelectedRows: "Exportar filas seleccionadas",
                exportTo          : "Exportar a",
        }
    })

    // Operaciones remotas
    let operacionesRemotas_cfg = ref({
        groupPaging: true 
    })

    // Selector de columnas
    let selectorColumnas_cfg = ref({
        allowSearch   : true,
        emptyPanelText: "Arrastre una columna aquí para ocultarla.",
        enabled       : true,
        title         : "Selector de columnas"                
    })  

    // Fijador de Columnas
    let fijadorDeColumna_cfg = ref({
        enabled    : true,
        texts      : {
            fix          : "Fijar",
            leftPosition : "A la izquierda",
            rightPosition: "A la derecha",
            unfix        : "Deshacer"
        }
    })

    // #########################################
    // Diccionario atributos de setup del GRID #
    // #########################################
    let atributos = {
        referencia         : ref(null),    
        fuenteDatos        : fuenteDatos.creaFuenteDatosConsulta(tipoComponente, tipoFuente, idComponente, fuenteDatosGrid, filtros, eventos),
        
        // Columnas
        columnas           : ref(columnas),           
        nombresColumnas    : nombresColumnas,

        focoResaltado      : ref(true), 
        alternanciaDeFilas : ref(true),
        reordenaColumna    : ref(true),
        redimensionaColumna: ref(true),
        loadIndicatorVisible : ref(false),

        // Barra de acciones
        elementosBarra    : ref(elementosBarra),
        toolbarAtributos :  ref({  
            class : "p-0 mb-0 bg_barra_grid"  
        }), 

        // Encabezado y pie dinamicos
        gridEncabezado     : ref(null),

        // Aviso de cargando.
        panelDeCarga: {
            enabled: true,
            text   : "Cargando datos"
        },

        // Panel de busqueda
        busquedaPanel: busquedaPanel_cfg,

        // Fila de busqueda
        busquedaFila: busquedaFila_cfg,

        // Opciones de ordenamiento
        ordenamiento: ordenamiento_cfg,

        // Agrupamiento
        agrupa     : agrupa_cfg,
        agrupaPanel: agrupaPanel_cfg,

        // Opciones de exportacion
        exportar: exportar_cfg,          

        // Operaciones remotas  
        operacionesRemotas: operacionesRemotas_cfg,

        // Selector de columnas
        selectorColumnas: selectorColumnas_cfg, 

        // Fijador de columnas
        fijadorDeColumna: fijadorDeColumna_cfg,

        // Muestra plabras completas, expandieno la fila
        ajustaPalabra   : ref(ajustaPalabra),

        atributosElemento: ref({
            id   : idComponente,
            name : idComponente,
        }),

        // Mensajes
        sinDatosTexto    : ref("Sin Datos"),
    }

    return atributos
}

export default {
    atributos_grid: atributos_grid
}