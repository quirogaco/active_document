<!--

-->
<template>
    <div class="monitor-report">
        <Upload ref="upload" accept=".doc,.docx" :action="action" :headers="header" :format="['doc','docx']"
                :on-success="handleSuccess"
                :show-upload-list="false" :before-upload="handleBeforeUpload" :on-format-error="handleFormatError">
            <Button :loading="loading" class="up-class">上传</Button>
            <span> doc,docx</span>
        </Upload>
        <div class="office" v-if="pageLoading">
            <MonitorOffice :option="option"></MonitorOffice>
        </div>
    </div>
</template>

<script>
    import axios from "axios"
    import {GetMonitorReport} from "../../../../api/template"    
    import MonitorOffice from "../../../../components/monitor-office"

    export default {
        components: {
            MonitorOffice
        },
        data() {
            return {
                
                header: {
                    Authorization: `bearer ${sessionStorage.getItem("token")}`,
                },
                action: axios.defaults.baseURL + "/report/document/template",
                file: null,
                loading: false,
               
                option: {
                    url: "",
                    isEdit: false,
                    fileType: "",
                    title: ""
                },
                pageLoading: false
            }
        },
        mounted() {
            this.init();
        },
        methods: {
            init() {
                this.GetMonitorReport();
            },
            
            handleFormatError(file) {
                this.$Message.warning(file.name + 'ERROR');
                this.loading = false;
            },
            
            handleBeforeUpload(file) {
                this.file = file;
                this.onUpload();
                return false;
            },

            onUpload() {
                this.loading = true;
                let _baseURL = axios.defaults.baseURL;
                this.action = `${_baseURL}/report/document/template`;
                setTimeout(() => {
                    this.$refs.upload.post(this.file);
                }, 1000)
            },

            handleSuccess(res) {
                this.loading = false;
                if (res.status) {
                    this.$Message.success("OK");
                    this.GetMonitorReport();
                }
            },

            GetMonitorReport() {
                this.pageLoading = false
                GetMonitorReport().then(res => {
                    if (res.status) {
                        let data = res.data;
                        if (data) {
                            this.option = {
                                url: data.fileViewPath,
                                fileType: data.fileType,
                                title: "",
                                isEdit: false,
                            }
                        }
                        this.pageLoading = true
                    }
                })
            }
        }
    }
</script>
<style lang="less" scoped>
    .monitor-report {
        .up-class {
            margin-bottom: 10px;
        }

        .office {
            height: 100vh;
        }
    }
</style>