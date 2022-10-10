import entryFactory from "bpmn-js-properties-panel/lib/factory/EntryFactory";

var LOW_PRIORITY = 500;

function CustomPropertiesProvider(propertiesPanel, translate) {
  propertiesPanel.registerProvider(LOW_PRIORITY, this);

  this.getTabs = function (element) {
    const self = this;

    return function (tabs) {
      const formTab = tabs.find(({ id }) => id === "forms");

      if (!formTab) {
        return tabs;
      }

      const { groups } = formTab;

      const formsGroup = groups.find(({ id }) => id === "forms");

      if (!formsGroup) {
        return tabs;
      }

      const { entries } = formsGroup;

      self.replaceFormKeyEntry(entries);

      return tabs;
    };
  };

  this.replaceFormKeyEntry = function (entries) {
    const formKeyEntry = entries.find(({ id }) => id === "form-key");

    if (!formKeyEntry) {
      return;
    }

    const index = entries.indexOf(formKeyEntry);

    entries.splice(
      index,
      1,
      entryFactory.selectBox(translate, {
        id: "form-key",
        label: translate("Select a form"),
        modelProperty: "form"

        // todo: your stuff
        // https://github.com/bpmn-io/bpmn-js-properties-panel/blob/master/lib/factory/SelectEntryFactory.js
      })
    );
  };
}

CustomPropertiesProvider.$inject = ["propertiesPanel", "translate"];

export default {
  __init__: ["customPropertiesProvider"],
  customPropertiesProvider: ["type", CustomPropertiesProvider]
};
