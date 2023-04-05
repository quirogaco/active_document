const atributos = {    
    accessKey:{ 
        "tipo"       : "texto",
        "defecto"    : null,
        "descripcion": "Especifica la tecla de método abreviado que establece el foco en el componente de la interfaz de usuario."
    },

    activeStateEnabled:{ 
        "tipo"       : "logico",
        "defecto"    : false,
        "descripcion": "Especifica si el componente de la interfaz de usuario cambia de estado al interactuar con un usuario."
    },

    allowColumnReordering:{ 
        "tipo"       : "logico",
        "defecto"    : false,
        "descripcion": "Especifica si un usuario puede reordenar las columnas."
    },

    allowColumnResizing:{ 
        "tipo"       : "logico",
        "defecto"    : false,
        "descripcion": "Especifica si un usuario puede cambiar el tamaño de las columnas."
    },

    autoNavigateToFocusedRow:{ 
        "tipo"       : "logico",
        "defecto"    : true,
        "descripcion": "Se desplaza automáticamente a la fila enfocada cuando se cambia la tecla de fila enfocada."
    },

    cacheEnabled:{ 
        "tipo"       : "logico",
        "defecto"    : true,
        "descripcion": "Especifica si los datos deben almacenarse en caché."
    },

    cellHintEnabled:{ 
        "tipo"       : "logico",
        "defecto"    : true,
        "descripcion": "Habilita una pista que aparece cuando un usuario pasa el puntero del mouse sobre una celda con contenido truncado."
    },

    columnAutoWidth:{ 
        "tipo"       : "logico",
        "defecto"    : false,
        "descripcion": "Especifica si las columnas deben ajustar su ancho al contenido."
    },

    columnChooser:{ 
        "tipo"       : "objeto",
        "defecto"    : {},
        "descripcion": "Configura el selector de columnas."
    },

    columnFixing:{ 
        "tipo"       : "objeto",
        "defecto"    : {},
        "descripcion": "Configura la fijación de la columna."
    },

    columnHidingEnabled:{ 
        "tipo"       : "logico",
        "defecto"    : false,
        "descripcion": "Especifica si el componente de la interfaz de usuario debe ocultar las columnas para adaptarse a la pantalla o al tamaño del contenedor. Se ignora si allowColumnResizing es verdadero y columnResizingMode es 'widget'."
    },

    columnMinWidth:{ 
        "tipo"       : "numero",
        "defecto"    : undefined,
        "descripcion": "Especifica el ancho mínimo de las columnas."
    },

    columnResizingMode:{ 
        "tipo"       : "texto",
        "defecto"    : "nextColumn",
        "descripcion": "Especifica cómo el componente de la interfaz de usuario cambia el tamaño de las columnas. Se aplica solo si allowColumnResizing es verdadero."
    },

    columns:{ 
        "tipo"       : "lista",
        "defecto"    : [],
        "descripcion": "Matriz de columnas de cuadrícula."
    },

    columnWidth:{ 
        "tipo"       : "numero",
        "defecto"    : undefined,
        "descripcion": "Especifica el ancho de todas las columnas de datos . Tiene una prioridad más baja que la columna . propiedad de ancho."
    },

    customizeColumns:{ 
        "tipo"       : "funcion",
        "defecto"    : undefined,
        "descripcion": "Utilice esta función para realizar pequeños ajustes en las columnas generadas automáticamente. Puede acceder y modificar las configuraciones de columna utilizando el parámetro de la función."
    },

    dataSource:{       
        "tipo"       : "texto",
        "defecto"    : null,
        "descripcion": "Vincula el componente de la interfaz de usuario a los datos."
    },

    dateSerializationFormat:{       
        "tipo"       : "texto",
        "defecto"    : "yyyy-MM-dd",
        "descripcion": "Especifica el formato en el que se deben enviar los valores de fecha y hora al servidor. Úselo solo si no especifica el origen de datos en el momento del diseño."
    },

    disabled:{ 
        "tipo"       : "logico",
        "defecto"    : false,
        "descripcion": "Especifica si el componente de la interfaz de usuario responde a la interacción del usuario."
    },

    editing:{ 
        "tipo"       : "objeto",
        "defecto"    : {},
        "descripcion": "Configura la edición."
    },

    elementAttr:{ 
        "tipo"       : "objeto",
        "defecto"    : {},
        "descripcion": "Especifica los atributos globales que se adjuntarán al elemento contenedor del componente de la interfaz de usuario."
    },

    errorRowEnabled: { 
        "tipo"       : "logico",
        "defecto"    : true,
        "descripcion": "Indica si se muestra la fila de error."
    },

    export:{ 
        "tipo"       : "objeto",
        "defecto"    : {},
        "descripcion": "Configura la exportación del lado del cliente."
    },

    filterBuilder:{ 
        "tipo"       : "objeto",
        "defecto"    : {},
        "descripcion": "Configura el generador de filtros integrado."
    },

    filterBuilderPopup:{ 
        "tipo"       : "objeto",
        "defecto"    : {},
        "descripcion": "Configura la ventana emergente en la que se muestra el generador de filtros integrado."
    },

    filterPanel:{ 
        "tipo"       : "objeto",
        "defecto"    : {},
        "descripcion": "Configura el panel de filtro."
    },

    filterRow:{ 
        "tipo"       : "objeto",
        "defecto"    : {},
        "descripcion": "Configura la fila del filtro."
    },

    filterSyncEnabled:{ 
        "tipo"       : "texto",
        "defecto"    : "auto",
        "descripcion": "Especifica si para sincronizar la fila de filtro , filtro de cabecera , y constructor de filtro . La expresión de filtro sincronizada se almacena en la propiedad"
    },

    filterValue: {
        "tipo"       : "objeto",
        "defecto"    : {},
        "descripcion": "Especifica una expresión de filtro."
    },

    focusedColumnIndex: {
        "tipo"       : "number",
        "defecto"    : -1,
        "descripcion": "El índice de la columna que contiene la celda de datos enfocada. Este índice se toma de la matriz de columnas ."
    },

    focusedRowEnabled:{ 
        "tipo"       : "logico",
        "defecto"    : true,
        "descripcion": "Especifica si la función de fila enfocada está habilitada."
    },

    focusedRowIndex: {
        "tipo"       : "number",
        "defecto"    : -1,
        "descripcion": "Especifica o indica el índice de la fila de datos enfocada. Utilice esta propiedad cuando focusRowEnabled sea verdadero ."
    },

    focusedRowKey:{ 
        "tipo"       : "texto",
        "defecto"    : undefined,
        "descripcion": "Especifica la clave de la fila de la cuadrícula enfocada inicial o actualmente. Úselo cuando focusRowEnabled sea verdadero ."
    },

    focusStateEnabled:{ 
        "tipo"       : "logico",
        "defecto"    : false,
        "descripcion": "Especifica si el componente de la interfaz de usuario se puede enfocar mediante la navegación del teclado."
    },

    grouping: {
        "tipo"       : "objeto",
        "defecto"    : {},
        "descripcion": "Configura la agrupación."
    },

    groupPanel: {
        "tipo"       : "objeto",
        "defecto"    : {},
        "descripcion": "Configures the group panel."
    },

    headerFilter: {
        "tipo"       : "objeto",
        "defecto"    : {},
        "descripcion": "Configura la función de filtro de encabezado."
    },

    height:{ 
        "tipo"       : "texto",
        "defecto"    : undefined,
        "descripcion": "Especifica la altura del componente de la interfaz de usuario."
    },

    highlightChanges:{ 
        "tipo"       : "logico",
        "defecto"    : false,
        "descripcion": "Especifica si resaltar filas y celdas con datos editados. repaintChangesOnly debería ser verdadero ."
    },

    hint:{ 
        "tipo"       : "texto",
        "defecto"    : undefined,
        "descripcion": "Especifica el texto de una pista que aparece cuando un usuario hace una pausa en el componente de la interfaz de usuario."
    },

    hoverStateEnabled:{ 
        "tipo"       : "logico",
        "defecto"    : true,
        "descripcion": "Especifica si el componente de la interfaz de usuario cambia su estado cuando un usuario se detiene en él."
    },
    
    keyboardNavigation:{ 
        "tipo"       : "objeto",
        "defecto"    : {},
        "descripcion": "Configura la navegación por teclado."
    },

    keyExpr:{ 
        "tipo"       : "texto",
        "defecto"    : "",
        "descripcion": "Especifica la propiedad (o propiedades) de la clave que proporcionan valores clave para acceder a los elementos de datos. Cada valor de clave debe ser único. Esta propiedad se aplica solo si los datos son una matriz simple."
    },

    loadPanel:{ 
        "tipo"       : "objeto",
        "defecto"    : {},
        "descripcion": "Configura el panel de carga."
    },

    masterDetail:{ 
        "tipo"       : "objeto",
        "defecto"    : {},
        "descripcion": "Le permite crear una interfaz maestro-detalle en la cuadrícula."
    },

    noDataText:{ 
        "tipo"       : "texto",
        "defecto"    : "Sin datos",
        "descripcion": "Especifica el texto que se muestra cuando el componente de la interfaz de usuario no muestra ningún dato."
    },

    onAdaptiveDetailRowPreparing:{ 
        "tipo"       : "funcion",
        "defecto"    : {},
        "descripcion": "Una función que se ejecuta antes de que se represente una fila de detalles adaptables."
    },

    onCellClick:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta cuando se hace clic o se toca una celda. Ejecutado antes de onRowClick."
    },

    onCellDblClick:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta cuando se hace doble clic en una celda o se toca dos veces. Ejecutado antes de onRowDblClick."
    },

    onCellHoverChanged:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta después de que el puntero entra o sale de una celda."
    },

    onCellPrepared:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta después de que se crea una celda."
    },

    onContentReady:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta cuando el contenido del componente de la interfaz de usuario está listo y cada vez que se cambia el contenido."
    },

    onContextMenuPreparing:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta antes de que se represente el menú contextual."
    },

    onDataErrorOccurred:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta cuando ocurre un error en la fuente de datos."
    },

    onDisposing:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta antes de eliminar el componente de la interfaz de usuario."
    },

    onEditCanceled:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta después de descartar los cambios de fila."
    },

    onEditCanceling:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta cuando se cancela la operación de edición, pero los cambios de fila aún no se descartan."
    },

    onEditingStart:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta antes de que una celda o fila cambie al estado de edición."
    },

    onEditorPrepared:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta después de que se crea un editor. No se ejecuta para celdas con editCellTemplate ."
    },

    onEditorPreparing:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se usa para personalizar el editor de una celda . No se ejecuta para celdas con editCellTemplate ."
    },

    onExporting:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta antes de que se exporten los datos."
    },

    onFocusedCellChanged:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta después de que cambia la celda enfocada. Se aplica solo a celdas en filas de datos o grupos."
    },

    onFocusedCellChanging:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta antes de que cambie la celda enfocada. Se aplica solo a celdas en filas de datos o grupos."
    },

    onFocusedRowChanged:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta después de que cambia la fila enfocada. Se aplica solo a filas de datos o grupos. focusRowEnabled debería ser verdadero ."
    },

    onFocusedRowChanging:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta antes de que cambie la fila enfocada. Se aplica solo a filas de datos o grupos. focusRowEnabled debería ser verdadero ."
    },

    onInitialized:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se utiliza en los marcos de JavaScript para guardar la instancia del componente de la interfaz de usuario."
    },

    onInitNewRow:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta antes de que se agregue una nueva fila al componente de la interfaz de usuario."
    },

    onKeyDown:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta cuando el componente UI está enfocado y se ha presionado una tecla."
    },

    onOptionChanged:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta después de que se cambia la propiedad de un componente de la interfaz de usuario."
    },

    onRowClick:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta cuando se hace clic o se toca una fila."
    },

    onRowCollapsed:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta después de contraer una fila."
    },

    onRowDblClick:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta cuando se hace doble clic en una fila o se toca dos veces. Ejecutado después de onCellDblClick ."
    },

    onRowExpanded:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta después de expandir una fila."
    },

    onRowExpanding:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta antes de que se expanda una fila."
    },

    onRowInserted:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta después de insertar una nueva fila en la fuente de datos."
    },

    onRowInserting:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta antes de que se inserte una nueva fila en la fuente de datos."
    },

    onRowPrepared:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta después de que se crea una fila."
    },

    onRowRemoved:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta después de eliminar una fila del origen de datos."
    },

    onRowRemoving:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta antes de que se elimine una fila del origen de datos."
    },

    onRowUpdated:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta después de actualizar una fila en la fuente de datos."
    },

    onRowUpdating:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta antes de que se actualice una fila en la fuente de datos."
    },

    onRowValidating:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta después de que las celdas de una fila se validan con las reglas de validación ."
    },

    onSaved:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta después de guardar los cambios de fila."
    },

    onSaving:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta antes de que se guarden los cambios de fila pendientes."
    },

    onSelectionChanged:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta después de seleccionar una fila o borrar su selección."
    },

    onToolbarPreparing:{ 
        "tipo"       : "funcion",
        "clase"      : "evento",
        "defecto"    : null,
        "descripcion": "Una función que se ejecuta antes de que se cree la barra de herramientas."
    },

    pager:{ 
        "tipo"       : "objeto",
        "defecto"    : {},
        "descripcion": "Configura el manejador de paginas."
    },

    paging:{ 
        "tipo"       : "objeto",
        "defecto"    : {},
        "descripcion": "Configura la paginación."
    },

    remoteOperations:{ 
        "tipo"       : "objeto",
        "defecto"    : {},
        "descripcion": "Notifica al DataGrid de las operaciones de procesamiento de datos del servidor."
    },

    renderAsync:{ 
        "tipo"       : "logico",
        "defecto"    : false,
        "descripcion": "Especifica si se debe representar la fila de filtro , las columnas de comando y las columnas con showEditorAlways establecido en verdadero después de otros elementos."
    },

    repaintChangesOnly:{ 
        "tipo"       : "logico",
        "defecto"    : false,
        "descripcion": "Especifica si se deben volver a pintar solo aquellas celdas cuyos datos cambiaron."
    },

    rowAlternationEnabled:{ 
        "tipo"       : "logico",
        "defecto"    : false,
        "descripcion": "Especifica si las filas deben sombrearse de manera diferente."
    },

    rowDragging:{ 
        "tipo"       : "objeto",
        "defecto"    : {},
        "descripcion": "Configura el reordenamiento de filas mediante gestos de arrastrar y soltar."
    },

    rowTemplate:{ 
        "tipo"       : "string",
        "defecto"    : undefined,
        "descripcion": "Especifica una plantilla personalizada para filas."
    },

    rtlEnabled: {
        "tipo"       : "logico",
        "defecto"    : false,
        "descripcion": "Cambia el componente de la interfaz de usuario a una representación de derecha a izquierda."
    },

    scrolling: {
        "tipo"       : "objeto",
        "defecto"    : {mode: "standard"},
        "descripcion": "Scrolling allows browsing data outside the UI component's viewport. The following scrolling modes are available in the DataGrid:"
    },

    searchPanel: {
        "tipo"       : "objeto",
        "defecto"    : {mode: "standard"},
        "descripcion": "Configura el panel de búsqueda."
    },

    selectedRowKeys: {
        "tipo"       : "lista",
        "defecto"    : null,
        "descripcion": "Le permite seleccionar filas o determinar qué filas se seleccionan. Se aplica solo si se selecciona . diferido es falso ."
    },

    selection: {
        "tipo"       : "lista",
        "defecto"    : null,
        "descripcion": "Configura la selección del tiempo de ejecución."
    },

    selectionFilter: {
        "tipo"       : "lista",
        "defecto"    : null,
        "descripcion": "selectionFilter"
    },

    showBorders:  {
        "tipo"       : "logico",
        "defecto"    : false,
        "descripcion": "Especifica si los bordes exteriores del componente de la interfaz de usuario están visibles."
    },

    showColumnHeaders:  {
        "tipo"       : "logico",
        "defecto"    : true,
        "descripcion": "Especifica si los encabezados de columna están visibles."
    },

    showColumnLines:  {
        "tipo"       : "logico",
        "defecto"    : true,
        "descripcion": "Especifica si las líneas verticales que separan una columna de otra son visibles."
    },

    showRowLines: {
        "tipo"       : "logico",
        "defecto"    : true,
        "descripcion": "Especifica si las líneas horizontales que separan una fila de otra son visibles."
    },

    sortByGroupSummaryInfo: {
        "tipo"       : "lista",
        "defecto"    : [],
        "descripcion": "Le permite ordenar grupos de acuerdo con los valores de los elementos de resumen del grupo."
    },

    sorting: {
        "tipo"       : "objeto",
        "defecto"    : {},
        "descripcion": "Configura la clasificación en tiempo de ejecución."
    },

    stateStoring: {
        "tipo"       : "objeto",
        "defecto"    : {},
        "descripcion": "Configura el almacenamiento de estados."
    },

    summary: {
        "tipo"       : "objeto",
        "defecto"    : {},
        "descripcion": "Especifica las propiedades del resumen de la cuadrícula."
    },

    tabIndex:{ 
        "tipo"       : "entero",
        "defecto"    : 0,
        "descripcion": "Especifica el número del elemento cuando se usa la tecla Tab para navegar."
    },

    twoWayBindingEnabled: {
        "tipo"       : "logico",
        "defecto"    : true,
        "descripcion": "Especifica si habilitar el enlace de datos bidireccional."
    },

    visible:{ 
        "tipo"       : "logico",
        "defecto"    : true,
        "descripcion": "Especifica si el componente de la interfaz de usuario está visible."
    },
    
    width:{ 
        "tipo"       : "texto",
        "defecto"    : undefined,
        "descripcion": "Especifica el ancho del componente de la interfaz de usuario."
    },

    wordWrapEnabled:{ 
        "tipo"       : "logico",
        "defecto"    : true,
        "descripcion": "Especifica si se debe ajustar el texto que no cabe en una columna."
    },
}

export default {
    atributos: atributos
}