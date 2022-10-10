import BaseRenderer from 'diagram-js/lib/draw/BaseRenderer';

import {
    append as svgAppend,
    attr as svgAttr,
    classes as svgClasses,
    create as svgCreate
} from 'tiny-svg';

import {
    getRoundRectPath
} from 'bpmn-js/lib/draw/BpmnRenderUtil';

import {
    is,
    getBusinessObject
} from 'bpmn-js/lib/util/ModelUtil';

import { isNil } from 'min-dash';

const HIGH_PRIORITY      = 1500,
      TASK_BORDER_RADIUS = 2

export default class CustomRenderer extends BaseRenderer {
    constructor(eventBus, bpmnRenderer) {
        super(eventBus, HIGH_PRIORITY);

        this.bpmnRenderer = bpmnRenderer;
    }

    canRender(element) {
        // ignore labels
        return !element.labelTarget;
    }

    drawShape(parentNode, element) {
        const shape       = this.bpmnRenderer.drawShape(parentNode, element);
        const accion_tipo = this.leer_accion(element);
        
        if (!isNil(accion_tipo)) {
            const color = this.leer_color(accion_tipo);
            
            // Cajon
            const rect  = drawRect(parentNode, 100, 20, TASK_BORDER_RADIUS, color);
            svgAttr(rect, {
                transform: 'translate(-2, -25)'
            });

            // Texto
            var text = svgCreate('text');
            svgAttr(text, {
                'fill'       : '#000',
                'font-weight': '800',
                'transform'  : 'translate(-2, -12)'
            });

            svgClasses(text).add('djs-label');

            svgAppend(text, document.createTextNode(accion_tipo));

            svgAppend(parentNode, text);
        }

        return shape;
    }

    getShapePath(shape) {
        if (is(shape, 'bpmn:ServiceTask')) {
            return getRoundRectPath(shape, TASK_BORDER_RADIUS);
        }

        return this.bpmnRenderer.getShapePath(shape);
    }

    leer_accion(element) {
        const businessObject = getBusinessObject(element);
        console.log("businessObject:", businessObject)

        const { accion_tipo } = businessObject;

        return accion_tipo;
    }

    leer_color(accion_tipo) {
        let color = '#f2800f'
        switch (accion_tipo) {
            case "Gestion":
                color = '#00FF80'
                break;
        
            case "Visto bueno":
                color = '#FFFF00'
                break;
            
            case "Asignacion":
                color = '#A9D0F5'
                break;
        }

        return color;
    }
}

CustomRenderer.$inject = [ 'eventBus', 'bpmnRenderer' ];

// helpers //////////

// copied from https://github.com/bpmn-io/bpmn-js/blob/master/lib/draw/BpmnRenderer.js
function drawRect(parentNode, width, height, borderRadius, color) {
    const rect = svgCreate('rect');

    svgAttr(rect, {
        width: width,
        height: height,
        rx: borderRadius,
        ry: borderRadius,
        stroke: color,
        strokeWidth: 2,
        fill: color
    });

    svgAppend(parentNode, rect);

    return rect;
}