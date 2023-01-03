// ## ATTRIBUTES ## 
// dxDataGrid basic attributes
let attributes = {    
    dataSource: {
        dataSource: []
    },

    selection: {
        allowSelectAll    : true,
        deferred          : false,
        // 'multiple' | 'none' | 'single'  
        mode              : "single",           
        // 'allPages' | 'page' 
        selectAllMode     : "allPages", 
        // 'always' | 'none' | 'onClick' | 'onLongTap'    
        showCheckBoxesMode: "onClick" , 
    },

    ref                   : "grid",
    height                : "500px",
    width                 : "600px",
    allowColumnReordering : true,
    allowColumnResizing   : true,
    rowAlternationEnabled : true,
    showBorders           : false,
    showColumnLines       : false,
    wordWrapEnabled       : true,
    remoteOperations      : {
        groupPaging: true,
        paging: true,
        filtering: true,
        sorting: true,
        grouping: true,
        summary: true
    },

    // datagrid columns
    columns               : [],

    searchPanel: {
        visible             : true,                
        width               : "80%",
        placeholder         : "Buscar",
        highlightSearchText : false
    },

    filterRow: {
        applyFilter: "auto", //"onClick",
        visible    : true
    },

    pager: {
        allowedPageSizes     : [5, 10, 25, 50],
        displayMode          : "full",
        showInfo             : true,
        showNavigationButtons: true,
        showPageSizeSelector : true,
        visible              : true
    },

    paging: {
        enabled : true,
        pageSize: 10
    },

    export: {
        enabled: true
    },

    toolbar: {
        disabled: false,
        items   : [],
        visible : true
    },

    accessKey: null,
    cacheEnabled: false,
}

export default {
    attributes: attributes
}