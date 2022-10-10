import {
    is
} from 'bpmn-js/lib/util/ModelUtil';
import CommandInterceptor from "diagram-js/lib/command/CommandInterceptor";

/*
var condition = moddle.create('bpmn:FormalExpression', { body: 'some-expression' });

  var connection = elementRegistry.get('someSequenceFlow');

  modeling.updateProperties(connection, {
    condition: condition
  });
*/

let contador = 0;

class MyCommandInterceptor extends CommandInterceptor {
    constructor(eventBus, modeling) {
        super(eventBus);
        
        //this.preExecuted(["shape.create"], ({ context }) => {   
            /*    
        this.preExecute(["connection.create"], ({ context }) => {  
            //console.log("createElements.preExecute-> modeling:", modeling)  
            const { connection } = context;
            const { source }     = context ;
            const { target }     = context;
        });*/

        this.canExecute(["shape.create"], ({ context }) => {  
            //console.log("canExecute-> context:", context)

            return false;
        });

        this.execute(["connection.create"], ({ context }) => {  
            //console.log("execute-> context:", context)
        });

        this.executed(["connection.create"], ({ context }) => {  
            //console.log("executed-> context:", context)
        });

        
        //this.postExecuted(["shape.create"], ({ context }) => {          
        this.postExecute(["connection.create"], ({ context }) => {  
            const { shape }      = context;                 
            const { connection } = context;
            const { source }     = context;
            //console.log("postExecute-> context:", context)  

            if (is(source.businessObject, 'bpmn:ExclusiveGateway')) {
                contador += 1;
                let filtro = 'juan==' + '"genio_' + contador + '"'
                var condition = connection.businessObject.$model.create('bpmn:FormalExpression', { body: filtro });
                //console.log("createElements.postExecuted-> condition:", condition)
                //console.log("createElements.postExecuted-> connection:", connection)                
                modeling.updateProperties(connection, {
                    conditionExpression: condition
                });                                          
            }

            //console.log("postExecuted-shape:", modeling)

        });
        

        //console.log("this.canExecute:", this.canExecute)        
    }
}

MyCommandInterceptor.$inject = ["eventBus", "modeling"];

export default {
    __init__: ["myCommandInterceptor"],
    myCommandInterceptor: ["type", MyCommandInterceptor]
};