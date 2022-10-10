
// Rutas de componentes predefinidos en archivos fisicos vue
let rutas_componentes = {
    'radicado_juridica_forma': () => import('../components/devExpress/predefinidos/radicados/web_juridica_forma.js'),
    'natural_web_forma'      : () => import('../components/devExpress/predefinidos/radicados/natural_web_forma.js'),
    'anonimo_web_forma'      : () => import('../components/devExpress/predefinidos/radicados/anonimo_web_forma.js'),
}  

export default {
    rutas_componentes: rutas_componentes
} 