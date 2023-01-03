import { formatMessage } from 'devextreme/localization';
import { confirm as confirmDe } from 'devextreme/ui/dialog';

export const eventsDxDataGrid = function(that) {
    // this is DxDataGrid, that is DataGrid (this component)
    return {        
        rowClick(event) {
            console.log("rowClick");
            that.$emit('clickRow', event, that);
        },

        cellDblClick(event) {
            console.log("cellDblClick");
            that.$emit('dblClickCell', event, that);
        }
    }
}

export const methodDataGrid = function(that) {
    return {        
        // there are selected records
        getSelectedRecords() {
            return that.dxGrid.instance.getSelectedRowsData()
        },

        getSelectedKeys() {
            return that.dxGrid.instance.getSelectedRowKeys()
        },

        // validation and messages in record selection
        checkSelectedRecord(many=0, mode="exact") {
            let selected       = that.getSelectedRecords();
            let lengthSelected = selected.length;
        
            if (many == 0) { // ignore mode
                return selected
            }
            else {
                if (mode == "exact")   {
                    if (lengthSelected == many) {
                        return selected
                    }
                    else {
                        return []
                    }
                }
                else {
                    if (mode=="max")   {
                        if (lengthSelected <= many) {
                            return selected
                        }
                        else {
                            return []
                        }
                    }
                    else {
                        return []
                    }
                }
            }            
        },

        confirm(call=null, options={}) {
            let title    = options.title   || formatMessage("youSure", "");
            let message  = options.message || formatMessage("confirm", "");      
            let result = confirmDe(title, message);
            result.then((dialogResult) => {
                dialogResult ? call(selected, that, this): null;
            })            
        },
        
        // validates the selection of records
        selectedRecords(many=0, options={}) {                       
            let mode     = options.mode || "exact";
            let selected = that.checkSelectedRecord(many, mode);
            let response = {
                records: selected,
                keys   : that.getSelectedKeys(),
                status : false
            };
            
            // validates accuracy
            if (selected.length == 0) {          
                let message = many;
                if (many == 0) {
                    message = "al menos un";
                };      
                $notify(
                    formatMessage("selectedTheseRecords", message), 
                    "warning"
                )                
            }
            else {
                if (selected.length > 0) {
                    response.status = true
                }
                else {
                    if (many == 1) {
                        $notify(
                            formatMessage("selectRecord", ""), 
                            "warning"
                        )                
                    }
                    else {
                        if ( (many == 0) || (many > 1) ) {
                            $notify(
                                formatMessage("selectedRecords", ""), 
                                "warning"
                            )
                        }
                    } 
                    // que pasa cuando es un numero especifico 2, 4, 5 //jcr
                }  
            }
            
            return response;
        },

        //###############################
        // shortcuts to dxGridRef.instance #
        //###############################
        getSelectedRowKeys() {
            return that.dxGrid.instance.getSelectedRowKeys()
        },

        getSelectedRowsData() {
            return that.dxGrid.instance.getSelectedRowsData()
        },
        
        refresh() {
            return that.dxGrid.instance.refresh()
        },
    }
}

export default {}