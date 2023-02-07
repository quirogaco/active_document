// Rutas de componentes predefinidos en archivos fisicos vue
let rutas_componentes = {
    // Contenido principal
    'contenido_pantalla' : () => import('../components/devExpress/cajon/contenido.vue'),

    // CONFIGURA CANALES DE RADICACIóN
    'configura_parametros_generales': () => import('../components/devExpress/predefinidos/configuracion/parametros_generales/configura_parametros_generales.vue'), 

    // Roles
    'roles_grid'      : () => import('../components/devExpress/predefinidos/configuracion/roles/grid.vue'),
    'roles_formulario': () => import('../components/devExpress/predefinidos/configuracion/roles/formulario.vue'),

    // PLANTILLAS
    'plantilla_grid'     : () => import('../components/devExpress/predefinidos/configuracion/plantilla/plantilla_grid.vue'),
    'pantalla_plantilla' : () => import('../components/devExpress/predefinidos/configuracion/plantilla/pantalla_plantilla.vue'),

    // CONSECUTIVOS
    'consecutivos_grid'  : () => import('../components/devExpress/predefinidos/configuracion/consecutivos/consecutivos_grid.js'),
    'consecutivos_forma' : () => import('../components/devExpress/predefinidos/configuracion/consecutivos/consecutivos_forma.js'), 

    // Permisos archivo
    'permisos_archivo_grid'      : () => import('../components/devExpress/predefinidos/configuracion/permisos_archivo/grid.vue'),
    'permisos_archivo_formulario': () => import('../components/devExpress/predefinidos/configuracion/permisos_archivo/formulario.vue'),

    // Motivos devolución
    'motivo_devolucion_grid' : () => import('../components/devExpress/predefinidos/configuracion/motivo_devolucion/motivo_devolucion_grid.js'),
    'motivo_devolucion_forma': () => import('../components/devExpress/predefinidos/configuracion/motivo_devolucion/motivo_devolucion_forma.js'),

    // ###########################
    // ARCHIVO HISTORICO MIGRADO #
    // ###########################
    'archivo_historico_migrado_grid': () => import('../components/devExpress/predefinidos/migrados/historico_archivo/archivo_historico_migrado_grid.js'),

    // ################
    // MIGRACIóN PQRS #
    // ################
    // RADICADOS PQRS
    'radicado_pqr_grid'   : () => import('../components/devExpress/predefinidos/migrados/radicado_pqr/radicado_pqr_grid.js'),
    'radicado_pqr_forma'  : () => import('../components/devExpress/predefinidos/migrados/radicado_pqr/radicado_pqr_forma.js'),

    // ############################
    // MIGRACIóN VENTANILLA UNICA #
    // ############################
    // ENTRADAS RADICADOS 
    'entradas_ventanilla_grid' : () => import('../components/devExpress/predefinidos/migrados/ventanilla/entradas_ventanilla_grid.js'),
    'entradas_ventanilla_forma': () => import('../components/devExpress/predefinidos/migrados/ventanilla/entradas_ventanilla_forma.js'),

     // INTERNOS RADICADOS 
    'internos_ventanilla_grid' : () => import('../components/devExpress/predefinidos/migrados/ventanilla/internos_ventanilla_grid.js'),
    'internos_ventanilla_forma': () => import('../components/devExpress/predefinidos/migrados/ventanilla/internos_ventanilla_forma.js'),

     // SALIDAS RADICADOS 
    'salidas_ventanilla_grid' : () => import('../components/devExpress/predefinidos/migrados/ventanilla/salidas_ventanilla_grid.js'),
    'salidas_ventanilla_forma': () => import('../components/devExpress/predefinidos/migrados/ventanilla/salidas_ventanilla_forma.js'),

     // ############################
     // RADICACIóN  FORMULARIO WEB #
     // ############################
     // RADICADOS 
    
     // Juridica
    'radicado_general_grid'  : () => import('../components/devExpress/predefinidos/radicados/radicados_grid.js'),
    'radicado_juridica_forma': () => import('../components/devExpress/predefinidos/radicados_vue/entrada/web_juridica_formulario/web_juridica_forma_radicado.vue'),

    //'radicado_juridica_forma': () => import('../components/devExpress/predefinidos/radicados/web_juridica_forma.js'),

    // Natural
    'natural_radicados_grid' : () => import('../components/devExpress/predefinidos/radicados/natural_radicados_grid.js'),
    'natural_web_forma'      : () => import('../components/devExpress/predefinidos/radicados_vue/entrada/web_natural_formulario/web_natural_forma_radicado.vue'),
    //'natural_web_forma'      : () => import('../components/devExpress/predefinidos/radicados/natural_web_forma.js'),

    // Anonimos
    'anonimo_radicados_grid' : () => import('../components/devExpress/predefinidos/radicados/anonimo_radicados_grid.js'),
    'anonimo_web_forma'      : () => import('../components/devExpress/predefinidos/radicados_vue/entrada/web_anonimo_formulario/web_anonimo_forma_radicado.vue'),
    //'anonimo_web_forma'      : () => import('../components/devExpress/predefinidos/radicados/anonimo_web_forma.js'),

    // Traslado y asignación
    'grid_pqrs_asigna_grid': () => import('../components/devExpress/predefinidos/radicados_vue/asignacion/pqrs/grid_pqrs_asigna_grid.vue'),
    'forma_pqrs_asigna'    : () => import('../components/devExpress/predefinidos/radicados_vue/asignacion/pqrs/forma_pqrs_asigna.vue'),

    // ############################
    // GESTION #
    // ############################
    //'gestion_basica_grid'  : () => import('../components/devExpress/predefinidos/gestion/gestion_basica_grid.js'),
    'gestion_basica_grid': () => import('../components/devExpress/predefinidos/gestion/grid_gestion/gestion_basica_grid.vue'),
    'gestion_pantalla': () => import('../components/devExpress/predefinidos/gestion/gestion_pantalla/gestion_pantalla.vue'),
    'tablero_general': () => import('../components/devExpress/tablero_control/tablero_general.vue'),
    'grid_gestion_consulta': () => import('../components/devExpress/predefinidos/gestion/gestion_oficina/grid_gestion_consulta.vue'),
    
    // ######
    // PQRS #
    // ######
    'grid_radica_asigna_grid'    : () => import('../components/devExpress/predefinidos/radicados_vue/entrada/pqrs/grid_radica_asigna_grid.vue'),
    'pqrs_radicado_forma'    : () => import('../components/devExpress/predefinidos/radicados_vue/pqrs/radicacion_formulario/pqrs_forma_radicado.vue'),
    
    // ########################
    // RADICACIóN VENTANILLA #
    // #######################
    // ENTRADAS
    // 'ventanilla_radicado_grid' : () => import('../components/devExpress/predefinidos/radicados_vue/entrada/ventanilla/grid/grid_ventanilla_radicado_grid.vue'),
    // 'ventanilla_radicado_forma': () => import('../components/devExpress/predefinidos/radicados_vue/entrada/ventanilla/form/ventanilla_forma_radicado.vue'),
    'ventanilla_radicado_grid' : () => import('../components/devExpress/predefinidos/radicados_vue/entrada/ventanilla_pinia/grid/grid_ventanilla_radicado_grid.vue'),
    'ventanilla_radicado_forma': () => import('../components/devExpress/predefinidos/radicados_vue/entrada/ventanilla_pinia/form/ventanilla_forma_radicado.vue'),    
    'forma_radicado_consulta'  : () => import('../components/devExpress/predefinidos/radicados_vue/comunes/consulta/forma_radicado_consulta.vue'),

    // SALIDAS
    'grid_ventanilla_salida' : () => import('../components/devExpress/predefinidos/radicados_vue/salida/consulta/grid_ventanilla_salida.vue'),
    'salida_forma_radicado'  : () => import('../components/devExpress/predefinidos/radicados_vue/salida/radicacion_formulario/salida_forma_radicado.vue'), 
    'forma_salida_consulta': () => import('../components/devExpress/predefinidos/radicados_vue/comunes/consulta_salida/forma_salida_consulta.vue'),   
    
    
    // INTERNOS
    //'grid_ventanilla_interno': () => import('../components/devExpress/predefinidos/radicados_vue/interno/consulta/grid_ventanilla_interno.vue'),
    'interno_forma_radicado' : () => import('../components/devExpress/predefinidos/radicados_vue/interno/radicacion_formulario/interno_forma_radicado.vue'),
    'forma_interno_consulta' : () => import('../components/devExpress/predefinidos/radicados_vue/comunes/consulta_interno/forma_interno_consulta.vue'),

    // CORREOS POR DESCARGAR
    'correos_grid': () => import('../components/devExpress/predefinidos/correos/correos_grid.vue'), 

    // #############
    // ENVIOS GRID #
    // ############
    // PLANILLA ENVIOS FISICOS GRID
    'planilla_grid'         : () => import('../components/devExpress/predefinidos/envios/grid_planilla/planilla_grid.vue'),
    'envios_grid'           : () => import('../components/devExpress/predefinidos/envios/grid_envios/envios_grid.vue'),
    'devoluciones_grid'     : () => import('../components/devExpress/predefinidos/envios/grid_devoluciones/devoluciones_grid.vue'),
    'envio_electronico_grid': () => import('../components/devExpress/predefinidos/envios/grid_envio_electronico/envio_electronico_grid.vue'),
    'ventana_planilla'      : () => import('../components/devExpress/predefinidos/envios/ventana_planilla/ventana_planilla.vue'),

    // #################
    // MASIVOS SALIDAS #
    // #################
    'destinatarios_listado_grid': () => import('../components/devExpress/predefinidos/masivos_salidas/grid_listado_destinatarios/destinatarios_listado_grid.vue'),
    'ventana_listado'           : () => import('../components/devExpress/predefinidos/masivos_salidas/ventana_listado/ventana_listado.vue'),
    'salida_masiva'             : () => import('../components/devExpress/predefinidos/masivos_salidas/forma_masivo/salida_masiva.js'),

    // #################
    // MASIVOS INTERNOS #
    // #################
    'destinatarios_listado_interno_grid': () => import('../components/devExpress/predefinidos/masivos_internos/grid_listado_destinatarios/destinatarios_listado_grid.vue'),
    'ventana_listado_interno'           : () => import('../components/devExpress/predefinidos/masivos_internos/ventana_listado/ventana_listado.vue'),
    'interno_masiva'                    : () => import('../components/devExpress/predefinidos/masivos_internos/forma_masivo/interno_masiva.js'),

    // #########
    // ARCHIVO #
    // #########

    // #####
    // TRD #
    // #####    
    'trd_basica_grid'  : () => import('../components/devExpress/predefinidos/archivo/trd/definicion/grid_trd/trd_basica_grid.vue'),
    'trd_pantalla'     : () => import('../components/devExpress/predefinidos/archivo/trd/definicion/pantalla_trd/pantalla_trd.vue'),

    // EXPEDIENTES
    'expediente_basica_grid'  : () => import('../components/devExpress/predefinidos/archivo/expedientes/grid_expediente/expediente_basica_grid.vue'),
    'pantalla_expediente'     : () => import('../components/devExpress/predefinidos/archivo/expedientes/pantalla_expediente/pantalla_expediente.vue'),

    // CONSULTA EXPEDIENTES
    'expediente_consulta_basica_grid': () => import('../components/devExpress/predefinidos/archivo/expedientes/grid_expediente_consulta/expediente_consulta_basica_grid.vue'),
    'pantalla_consulta_expediente'   : () => import('../components/devExpress/predefinidos/archivo/expedientes/pantalla_consulta_expediente/pantalla_consulta_expediente.vue'),

    // PRESTAMO EXPEDIENTES
    'prestamo_basica_grid': () => import('../components/devExpress/predefinidos/archivo/expedientes/grid_prestamo/prestamo_basica_grid.vue'),

    // TRANSFERENCIAS
    'transferencia_basica_grid': () => import('../components/devExpress/predefinidos/archivo/transferencias/grid_transferencia/transferencia_basica_grid.vue'),
    'pantalla_transferencia'   : () => import('../components/devExpress/predefinidos/archivo/transferencias/pantalla_transferencia/pantalla_transferencia.vue'),

    // TRANSFERENCIAS OFICINA
    'expediente_transfiere_grid': () => import('../components/devExpress/predefinidos/archivo/expedientes/grid_transferencia/expediente_basica_grid.vue'),

    // DISPOSICION FINAL
    'expediente_disposicion_grid': () => import('../components/devExpress/predefinidos/archivo/expedientes/grid_disposicion/expediente_disposicion_grid.vue'),
    
    // #####
    // TVD #
    // #####
    'tvd_basica_grid'  : () => import('../components/devExpress/predefinidos/archivo/tvd/definicion/grid_tvd/tvd_basica_grid.vue'),
    'tvd_pantalla'     : () => import('../components/devExpress/predefinidos/archivo/tvd/definicion/pantalla_tvd/pantalla_tvd.vue'),

    // TVD EXPEDIENTES
    'tvd_expediente_basica_grid'  : () => import('../components/devExpress/predefinidos/archivo/tvd_expedientes/tvd_grid_expediente/tvd_expediente_basica_grid.vue'),
    'tvd_pantalla_expediente'     : () => import('../components/devExpress/predefinidos/archivo/tvd_expedientes/tvd_pantalla_expediente/tvd_pantalla_expediente.vue'),

    // ####################
    // REPORTES DINAMICOS #
    // ####################
    'reportes_dinamicos_grid'      : () => import('../components/devExpress/predefinidos/configuracion/reportes_dinamicos/grid_reportes_dinamicos.vue'),
    'formulario_reportes_dinamicos': () => import('../components/devExpress/predefinidos/configuracion/reportes_dinamicos/formulario_reportes_dinamicos.vue'),

    // # IMPRESION REPORTES
    'grid_reportes_imprime'      : () => import('../components/devExpress/predefinidos/configuracion/reportes_dinamicos_imprimir/grid_reportes_imprime.vue'),
    'formulario_reportes_imprime': () => import('../components/devExpress/predefinidos/configuracion/reportes_dinamicos_imprimir/formulario_reportes_imprime.vue'),


    // ######################
    // FORMUALRIO DINAMICOS #
    // ######################
    'formularios_dinamicos_grid': () => import('../components/devExpress/predefinidos/configuracion/formularios_dinamicos/grid/grid.vue'),
    'formulario_constructor'    : () => import('../components/devExpress/predefinidos/configuracion/formularios_dinamicos/form/formulario_constructor.vue'),

    // ##################
    // FLUJOS DINAMICOS #
    // ##################
    'flujos_dinamicos_grid' : () => import('../components/devExpress/predefinidos/configuracion/flujos/grid/flujos_dinamicos_grid.vue'),
    'flujos_dinamicos_forma': () => import('../components/devExpress/predefinidos/configuracion/flujos/forma/flujos_dinamicos_forma.vue'),
    
    // CONSULTA DE RADICADOS
    'consulta_radicados_web': () => import('../components/devExpress/predefinidos/radicados_consulta/consulta_radicados_web.vue'), 

}  

export default {
    rutas_componentes: rutas_componentes
} 