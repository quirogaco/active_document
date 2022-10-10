import gestionProps from './parts/GestionProps';

import { is } from 'bpmn-js/lib/util/ModelUtil';

const LOW_PRIORITY = 500;

export default function GestionPropertiesProvider(propertiesPanel, translate) {

    let removeEntrie = function (element, entries, idRemove) {
        let newEntries = [];

        for (const index in entries) {
            let entrie = entries[index];
            if (entrie.id != idRemove) {
                if (is(element, "bpmn:Process")) {
                    newEntries.push(entrie)
                }
            }
        }

        return newEntries;
    }

    let filterGroups = function (groups, element) {
        let newGroups = [];
        let newGroup;

        for (const index in groups) {
            let group = groups[index];

            // grupo general es fijo para todos
            if (group.id == "general") {
                if (is(element, "bpmn:Process")) {
                    group.entries = removeEntrie(element, group.entries, "versionTag")
                }
                else {
                    newGroups.push(group);
                }
            }

            // flow
            if (group.id == "details") {
                if (is(element, "bpmn:SequenceFlow")) {
                    newGroups.push(group);
                }
            }
        }

        return newGroups;
    };

    let filterTabs = function (tabs, element) {
        let newTabs = []
        for (const index in tabs) {
            let tab = tabs[index];
            if (tab.id == "general") {
                tab.groups = filterGroups(tab.groups, element)
                newTabs.push(tab);
            }
        }

        return newTabs;
    };

    this.getTabs = function (element) {
        return function (tabs) {
            tabs = filterTabs(tabs, element);
            if (is(element, 'bpmn:UserTask')) {
                for (const index in tabs) {
                    let tab = tabs[index];
                    if (tab.id == "general") {
                        tab.groups.push(createGestionGroup(element, translate));
                    }
                }
            }

            return tabs;
        }

    };

    propertiesPanel.registerProvider(LOW_PRIORITY, this);
}

GestionPropertiesProvider.$inject = ['propertiesPanel', 'translate'];

function createGestionGroup(element, translate) {

    // create a group called "Magic properties".
    const gestionGroup = {
        id: 'gestion',
        label: translate('Propiedades de gestión'),
        entries: gestionProps(element, translate)
    };

    return gestionGroup
}