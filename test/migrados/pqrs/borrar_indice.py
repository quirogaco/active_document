#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import configuracion_base

from librerias.datos.elastic import elastic_operaciones


# MIGRACIÓN
resultado = elastic_operaciones.eliminaIndice("radicado_pqr", "base")
#db_migrado_radicado_pqrs