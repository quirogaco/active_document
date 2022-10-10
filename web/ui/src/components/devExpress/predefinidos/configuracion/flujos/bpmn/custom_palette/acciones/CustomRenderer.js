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
    const shape  = this.bpmnRenderer.drawShape(parentNode, element);
    const accion = this.leer_accion(element);
    
    if (!isNil(accion)) {
      const color = this.leer_color(accion);
      
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

      svgAppend(text, document.createTextNode(accion));

      svgAppend(parentNode, text);
    }

    return shape;
  }

  getShapePath(shape) {
    if (is(shape, 'bpmn:UserTask')) {
      return getRoundRectPath(shape, TASK_BORDER_RADIUS);
    }

    return this.bpmnRenderer.getShapePath(shape);
  }

  leer_accion(element) {
    const businessObject = getBusinessObject(element);

    const { accion } = businessObject;

    return accion;
  }

  leer_color(accion) {
    let color = '#000000'
    switch (accion) {
        case "aprobar":
          color = '#00FF80'
          break;
      
        case "devolver":
          color = '#FFFF00'
          break;
      
        case "trasladar":
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