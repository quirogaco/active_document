<template>
    <DataGrid        
       @dblClickCell   = "dblClickCell"
       @clickRow       = "clickRow"
       :attributes     = attributes
    />
</template>

<script>

let columnas = [
    // Nombre
    {
        caption    : "Asunto",
        dataField  : "nombre",
        dataType   : "string",        
        width      : 400,
        allowEditing  : false,       
    },

    // Subserie/Serie
    {
        caption       : "Serie/Subserie",
        dataField     : "serie_subserie",
        dataType      : "string",     
        width         : 250,
        allowEditing  : false,
    },

    // Dependencia
    {
        caption       : "Dependencia",
        dataField     : "dependencia_nombre",
        dataType      : "string",     
        width         : 250,
        allowEditing  : false,
    },
    
    // Etapa
    {
        caption       : "Etapa",
        dataField     : "etapa",
        dataType      : "string",         
        width         : 90,
        allowEditing  : false,
    },

    // Ubicacion
    {
        caption       : "Ubicación",
        dataField     : "ubicacion",
        dataType      : "string",         
        width         : 90,
        allowEditing  : false,
    },

    // Vence gestión
    {
        caption       : "Vence gestión",
        dataField     : "vence_gestion",
        dataType      : "date",
        format        : "yyyy-MM-dd",         
        width         : 120,
        allowEditing  : false,
    },


    // Vence central
    {
        caption       : "Vence central",
        dataField     : "vence_central",
        dataType      : "date",
        format        : "yyyy-MM-dd",         
        width         : 120,
        allowEditing  : false,
    },

    // Estado
    {
        caption       : "Estado",
        dataField     : "estado",
        dataType      : "string",         
        width         : 120,
        allowEditing  : false,
    },

    // Acceso
    {
        caption       : "Información",
        dataField     : "acceso_modo",
        dataType      : "string",         
        width         : 120,
        allowEditing  : false, 
    }
]

let toolbar = [
    {
        location: 'before',
        widget  : 'dxButton',
        options : {
            text : 'JUAN TOOLBAR !$!',
            onClick(e) {
                console.log("HOLA CLICK TOOL BAR")
            },
        }
    }

]

let test = {
    name : 'test',
    props: {},

    // setup(props, { attrs, slots, emit, expose })
    setup(props) {
        let attributes = {
            dataSource: {                
                dataSource: "agn_expedientes_trd",
                //fields    : ["id", "nombre", "codigo"],
            },

            columns: columnas,

            toolbar: toolbar
        }

        return {
            attributes
        }
    },

    // Metodos
    methods: {
        dblClickCell(event, grid) {
            console.log("cellDblClick ->", event, grid)            
        },

        clickRow(event, grid) {
            console.log("rowClick ->", event, grid)
        }
    }
}

export default test

</script>