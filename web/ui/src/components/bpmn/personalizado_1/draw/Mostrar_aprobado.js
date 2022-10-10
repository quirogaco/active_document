import inherits from 'inherits';

import BaseRenderer from 'diagram-js/lib/draw/BaseRenderer';

import {
  is
} from 'bpmn-js/lib/util/ModelUtil';

import imagenes from '../imagenes';

import {
  append as svgAppend,
  create as svgCreate,
  innerSVG
} from 'tiny-svg';


export default function Render(eventBus) {
  BaseRenderer.call(this, eventBus, 1500);

  this.canRender = function(element) {
    return is(element, 'bpmn:ServiceTask');
  };


  this.drawShape = function(parent, shape) {
    var url = imagenes.aprobado.dataUrl;

    var imagen = svgCreate('image', {
      x: 0,
      y: 0,
      width: shape.width,
      height: shape.height,
      href: url
    });

    svgAppend(parent, imagen);
    
    return imagen;
  };
}

//inherits(Render, BaseRenderer);

Render.$inject = [ 'eventBus' ];