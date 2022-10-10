import Modeler from "bpmn-js/lib/Modeler";

import CamundaModdlePackage from "camunda-bpmn-moddle/resources/camunda";
import CamundaModdleExtension from "camunda-bpmn-moddle/lib";

import PropertiesPanelModule from "bpmn-js-properties-panel";
import CamundaPropertiesProviderModule from "bpmn-js-properties-panel/lib/provider/camunda";
import CustomPaletteModule from "./palette";

import "bpmn-js/dist/assets/diagram-js.css";
import "bpmn-js/dist/assets/bpmn-font/css/bpmn-embedded.css";

import "bpmn-js-properties-panel/dist/assets/bpmn-js-properties-panel.css";

import "./styles.css";

import diagram from "./diagram.bpmn";

const container = document.getElementById("container");

const modeler = new Modeler({
  container,
  keyboard: {
    bindTo: document
  },
  propertiesPanel: {
    parent: "#properties-panel-container"
  },
  additionalModules: [
    PropertiesPanelModule,
    CamundaPropertiesProviderModule,
    CamundaModdleExtension,
    CustomPaletteModule
  ],
  moddleExtensions: {
    camunda: CamundaModdlePackage
  }
});

modeler
  .importXML(diagram)
  .then(({ warnings }) => {
    if (warnings.length) {
      console.log(warnings);
    }

    const canvas = modeler.get("canvas");

    canvas.zoom("fit-viewport");
  })
  .catch((err) => {
    console.log(err);
  });
