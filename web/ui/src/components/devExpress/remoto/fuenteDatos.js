import fuenteDatosForma    from './fuenteDatosForma.js'
import fuenteDatosConsulta from './fuenteDatosConsulta.js'

export default {
    creaFuenteDatosForma    : fuenteDatosForma.creaFuenteDatosForma,
    creaFuenteDatosConsulta : fuenteDatosConsulta.creaFuenteDatosConsulta,
    creaFuenteDatosUniversal: fuenteDatosConsulta.creaFuenteDatosUniversal,
    cargaDatosConsulta      : fuenteDatosConsulta.cargaDatosConsulta
}