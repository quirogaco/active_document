import componentes_llamados_crud_form from './componentes_llamados_crud_form.js';
import componentes_llamados_crud_grid from './componentes_llamados_crud_grid.js';

export default {
    // GRID
    tituloCrud     : componentes_llamados_crud_grid.tituloCrud,
    botonCrud      : componentes_llamados_crud_grid.botonCrud, 
    dobleClickGrid : componentes_llamados_crud_grid.dobleClickGrid,
    
    // FORMA
    enviaForma   : componentes_llamados_crud_form.enviaForma,  
    botonCrea    : componentes_llamados_crud_form.botonCrea,
    botonModifica: componentes_llamados_crud_form.botonModifica,
    botonElimina : componentes_llamados_crud_form.botonElimina,    
    botonRegresa : componentes_llamados_crud_form.botonRegresa,
    botonesForma : componentes_llamados_crud_form.botonesForma,
} 