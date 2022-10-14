import fuenteDatos from '../../../remoto/fuenteDatos.js';

// ###############
// grid messages #
// ###############
import { formatMessage, loadMessages } from 'devextreme/localization';
let messages = {
    "en": {
        "selectRecord"        : "Select a record, please !!",
        "selectedTheseRecords": "Select {0} record (s), please !!",
        "selectedRecords"     : "Please select at least one record !!",
        "youSure"             : "<i>Are you sure ?</i>",
        "confirm"             : "Confirm"
    },
    "es": {
        "selectRecord"        : "Seleccione un registro, por favor !!",
        "selectedTheseRecords": "Seleccione {0} registro(s), por favor !!",
        "selectedRecords"     : "Seleccione al menos un registro, por favor !!",
        "youSure"             : "<i>Esta seguro ?</i>",
        "confirm"             : "Confirme"
    }
}
loadMessages(messages)

// ## COLUMNS ## 
// basic definition column
let columnBasic = function(columnAttribute={}) {
    let basicDefinition = {
        caption       : ".",
        dataField     : ".",
        dataType      : "string",     
        width         : 50,
        allowEditing  : false
    }
    
    let column = {
        ...basicDefinition,
        ...columnAttribute
    }

    return column
}

// create definition-based column creation
let createColumns = function(columnsAttribute=[]) {
    let columns = [];
    
    if (Array.isArray(columnsAttribute) == true) {
        let column;
        for (const index in columnsAttribute) {
            column = columnBasic(columnsAttribute[index])
            columns.push(column) 
        }
    }

    return columns
}

// ## DATASOURCE ## 
// create data source
let createDataSource = function(dataSource) {
    let source = [];
    if (dataSource !== undefined) { 
        if ( (dataSource.dataSource != null) && (dataSource.dataSource != undefined) ) { 
            if (Array.isArray(dataSource.dataSource) == true) {
                source = fuenteDatos.creaFuenteDatosUniversal("grid", "", "", dataSource.dataSource)
            }
            else {
                let filters = (dataSource.filters != undefined? dataSource.filters : []);
                let events  = (dataSource.events  != undefined? dataSource.events  : {});
                let sorts   = (dataSource.sorts   != undefined? dataSource.sorts   : []);
                let fields  = (dataSource.fields  != undefined? dataSource.fields  : []);
                source      = fuenteDatos.creaFuenteDatosConsulta("grid", null, dataSource.dataSource, dataSource.dataSource, filters, events, sorts, fields);                        
            } 
        }       
    }

    return source
}

// ## TOOLBAR ## 
// create toolbar
let createToolbar = function(basicAttributes, propsToolbar) {
    let toolbar = $lib.clone(basicAttributes.toolbar);
    
    // search
    if (basicAttributes.searchPanel.visible == true) {
        toolbar.items.push("searchPanel")
    }

    // export
    if (basicAttributes.export.enabled == true) {
        toolbar.items.push("exportButton")
    }    

    // extend toolbar with attributes
    toolbar.items = toolbar.items.concat(propsToolbar);

    return toolbar
}

// ## METHODS ## 
import methods from './methods.js';

// mix local and imported methods
let getMethods = function(local, imported) {
    let methods = {
        ...local,
        ...imported
    }

    return methods
}

export default {
    columnBasic     : columnBasic,
    createColumns   : createColumns,
    createDataSource: createDataSource, 
    createToolbar   : createToolbar,
    getMethods      : getMethods
}