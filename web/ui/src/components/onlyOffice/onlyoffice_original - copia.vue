<template>
    <div id="monitorOffice"></div>
</template>

<script>
import {manejoTipoDocumento} from "./librerias"
    export default {
        props: {
            option: {
                type: Object,
                default: () => {
                    return {}
                }
            }
        },
        data() {
            return {
                doctype: ''
            }
        },
        mounted() {
            if (this.option.url)
                this.setEditor(this.option)
        },
        methods: {
            setEditor(option) {
               this.doctype = manejoTipoDocumento(option.fileType);
                // office
                let config = {
                    document: {
                        fileType: option.fileType,
                        key: "",
                        title: option.title,
                        permissions: {
                            comment: false,
                            download: false,
                            modifyContentControl: true,
                            modifyFilter: true,
                            print: false,
                            edit: option.isEdit,
                            // "fillForms": true,
                            // "review": true
                        },
                        url: option.url
                    },
                    documentType: this.doctype,
                    editorConfig: {
                        callbackUrl: option.editUrl,
                        lang: "es",
                        customization: {
                            autosave: false,
                            chat: false,
                            comments: false,
                            help: false,
                            // "hideRightMenu": false,
                            logo: {
                                image: "https://file.iviewui.com/icon/viewlogo.png",
                                imageEmbedded: "https://file.iviewui.com/icon/viewlogo.png",
                            },
                            spellcheck: true,
                        },
                    },
                    width: "100%",
                    height: "100%",
                };
                let docEditor = new DocsAPI.DocEditor("monitorOffice", config);
            },
        },
        watch: {
            option: {
                handler: function (n, o) {
                    this.setEditor(n);
                    this.doctype = manejoTipoDocumento(n.fileType);
                },
                deep: true,
            }
        }
    }
</script>