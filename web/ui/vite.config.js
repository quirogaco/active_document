const path = require('path');
const fs = require('fs');
import { defineConfig, loadEnv } from 'vite';
import vue from '@vitejs/plugin-vue';

let ubicacion = "../../";
let ambiente = loadEnv("development", ubicacion, prefix = 'CFG_')

export default defineConfig({
    plugins: [
        //basicSsl(),
        //HttpsCert(),
        vue({
            reactivityTransform: true
        })
    ],
    resolve: {
        alias: {
            'vue': 'vue/dist/vue.esm-bundler.js',
            '@': path.resolve('src/components/devExpress/predefinidos')
        }
    },

    define: {
        '_ambiente_': ambiente
    },

    build: {
        target: 'esnext'
    },

    server: {
        host: "0.0.0.0",
        port: 3000
    }
})