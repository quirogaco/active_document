<template>
    <DataGrid      
       ref             = "grid"  
       @dblClickCell   = "dblClickCell"
       @clickRow       = "clickRow"
       @mounted        = "mountedGrid"
       :attributes     = "attributes"
    />
</template>

<script>
import { getCurrentInstance, ref } from "vue";
import columnas from "./columnas";

// 
const ejecutar = function(selected, component, that) {
    console.log("ejecutar:", selected, component, that)
}

// Se invoca como funciòn para para el componente como atributo
let toolbarElements = function(that) {
    let toolbar = [
        {
            location: 'before',
            widget  : 'dxButton',
            options : {
                text : 'JUAN TOOLBAR !$!',
                onClick(e) {
                    let opciones = {
                        "call": ejecutar,
                    }
                    that.grid.choose(1, that, opciones)
                },
            }
        }
    ]

    return toolbar
}

let test = {
    name : 'test',
    props: {},

    // setup(props, { attrs, slots, emit, expose })
    setup(props) {
        let that = getCurrentInstance().ctx 
        // template grid ref
        let grid = ref(null)

        // grid attributes
        let attributes = {
            dataSource: {                
                dataSource: "agn_expedientes_trd",
                //fields    : ["id", "nombre", "codigo"],
            },
            columns: columnas.columnas,
            toolbar: toolbarElements(that)
        }   

        return {
            grid,
            attributes
        }
    },

    // Metodos
    methods: {
        dblClickCell(event, grid) {
            //console.log("cellDblClick ->", event, grid)   
            console.log("this.$router->", this.$router.getRoutes())   
            
            this.$router.push({
                //name  : "test_DataForma",
                path  : "/test_DataForma",
            }) 
            
        },

        clickRow(event, grid) {
            //console.log("this.grid objeto>>>", this.grid.dxGrid) //, grid) 
            //console.log("this.grid", this.applicationComponents) 
        },

        mountedGrid(grid) {
            console.log("mountedGrid", grid)
        },

    }
}

export default test

</script>