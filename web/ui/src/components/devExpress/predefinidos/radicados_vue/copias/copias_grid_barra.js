import { confirm } from 'devextreme/ui/dialog';
import dialogos    from '../../../../../librerias/dialogos.js';

const envio_datos = function(that, seleccion) {
    const retorna_envio = function(retorna_datos) {
        that.grid_cmp.refresh();
    };

    let parametros = {"ocultar" : seleccion.keys};
    $forma.envio_accion_notifica("oculta_informados", parametros, retorna_envio);
}

let barraDef = function(that) {
    return [
        $forma.botonBarra({
            text : 'Ocultar copia(s)',
            icon : 'fas fa-eye-slash',
            click: async function(e) {
                let seleccion = that.grid_cmp.selectedRecords(0);
                if (seleccion.status == true) {
                    if (await dialogos.confirmar("Ocultar", "Desea ocultar los radicados ?") == true) {
                        envio_datos(that, seleccion)
                    }
                }                  
            },
        })
    ]
}

export default {
    barraDef: barraDef
}