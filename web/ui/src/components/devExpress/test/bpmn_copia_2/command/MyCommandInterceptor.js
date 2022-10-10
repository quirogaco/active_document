import CommandInterceptor from "diagram-js/lib/command/CommandInterceptor";

class MyCommandInterceptor extends CommandInterceptor {
    constructor(eventBus, modeling) {
        super(eventBus);

        this.preExecuted(["shape.create"], ({ context }) => {
            /*
            console.log("createElements.preExecute->modeling:", context)
            const { shape } = context;
            console.log(".preExecute->shape:", modeling)
            shape.id = "mmmmm"  
            */          
        });

        this.postExecuted(["shape.create"], ({ context }) => {
            /*
            console.log("postExecuted-modeling:", modeling)
            const { shape } = context;
            console.log("shape:", shape)
            
            //shape.id = "nuevo_90"

            const { id } = shape;

            console.log("context:", context)
            //modeling.updateId(shape, "mmmmnnn");
            modeling.updateLabel(shape, id);
            */
        });
    }
}

MyCommandInterceptor.$inject = ["eventBus", "modeling"];

export default {
    __init__: ["myCommandInterceptor"],
    myCommandInterceptor: ["type", MyCommandInterceptor]
};