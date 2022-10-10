#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import configuracion_base

from librerias.datos.elastic import elastic_operaciones

#"""
# CONFIGURACIÓN
resultado = elastic_operaciones.eliminaIndice("accion", "base")
resultado = elastic_operaciones.eliminaIndice("ciudad", "base")
resultado = elastic_operaciones.eliminaIndice("consecutivo", "base")
resultado = elastic_operaciones.eliminaIndice("continente", "base")
resultado = elastic_operaciones.eliminaIndice("correo", "base")
resultado = elastic_operaciones.eliminaIndice("departamento", "base")
resultado = elastic_operaciones.eliminaIndice("dependencia", "base")
resultado = elastic_operaciones.eliminaIndice("festivo", "base")
resultado = elastic_operaciones.eliminaIndice("genero", "base")
resultado = elastic_operaciones.eliminaIndice("grupo", "base")
resultado = elastic_operaciones.eliminaIndice("medio_envio", "base")
resultado = elastic_operaciones.eliminaIndice("mensajeria", "base")
resultado = elastic_operaciones.eliminaIndice("motivo_devolucion", "base")
resultado = elastic_operaciones.eliminaIndice("pais", "base")
resultado = elastic_operaciones.eliminaIndice("peticion", "base")
resultado = elastic_operaciones.eliminaIndice("plantilla", "base")
resultado = elastic_operaciones.eliminaIndice("role", "base")
resultado = elastic_operaciones.eliminaIndice("tipo_entidad", "base")
resultado = elastic_operaciones.eliminaIndice("tipo_identificacion", "base")
resultado = elastic_operaciones.eliminaIndice("ubicacion", "base")
resultado = elastic_operaciones.eliminaIndice("usuario", "base")
#"""

# MIGRACIÓN
#resultado = elastic_operaciones.eliminaIndice("anexo_pqr", "base")
#resultado = elastic_operaciones.eliminaIndice("traza_anexo_pqr", "base")
#resultado = elastic_operaciones.eliminaIndice("funcionario_pqr", "base")
#resultado = elastic_operaciones.eliminaIndice("radicado_pqr", "base")
#resultado = elastic_operaciones.eliminaIndice("tercero_pqr", "base")
#resultado = elastic_operaciones.eliminaIndice("traza_pqr", "base")


# FORMULARIOS WEB
#resultado = elastic_operaciones.eliminaIndice("fweb_juridica", "base")

#resultado = elastic_operaciones.eliminaIndice("plantilla", "base")


####################### NUEVA DEFINICION #####################
#resultado = elastic_operaciones.eliminaIndice("opciones_sistema", "base")
#resultado = elastic_operaciones.eliminaIndice("acciones_sistema", "base")
#resultado = elastic_operaciones.eliminaIndice("roles", "base")
#resultado = elastic_operaciones.eliminaIndice("radicado_entrada", "base")

#resultado = elastic_operaciones.eliminaIndice("continentes", "base")
#resultado = elastic_operaciones.eliminaIndice("paises", "base")
#resultado = elastic_operaciones.eliminaIndice("departamentos", "base")
#resultado = elastic_operaciones.eliminaIndice("ciudades", "base")
#resultado = elastic_operaciones.eliminaIndice("ubicaciones", "base")
#resultado = elastic_operaciones.eliminaIndice("dependencias", "base")

#resultado = elastic_operaciones.eliminaIndice("usuarios", "base")
#resultado = elastic_operaciones.eliminaIndice("roles", "base")
#resultado = elastic_operaciones.eliminaIndice("tipo_identificacion", "base")

#resultado = elastic_operaciones.eliminaIndice("tipo_peticiones", "base")


#resultado = elastic_operaciones.eliminaIndice("tipo_terceros", "base")
#resultado = elastic_operaciones.eliminaIndice("terceros", "base")
#resultado = elastic_operaciones.eliminaIndice("peticiones", "base")
#resultado = elastic_operaciones.eliminaIndice("logs", "base")
#resultado = elastic_operaciones.eliminaIndice("radicados_entrada", "base")
#resultado = elastic_operaciones.eliminaIndice("radicados_salida", "base")
#resultado = elastic_operaciones.eliminaIndice("radicados_interno", "base")
#resultado = elastic_operaciones.eliminaIndice("destinatarios_listado", "base")

#resultado = elastic_operaciones.eliminaIndice("agn_trd", "base")
#resultado = elastic_operaciones.eliminaIndice("agn_dependencia_trd", "base")
#resultado = elastic_operaciones.eliminaIndice("agn_serie_trd", "base")
#resultado = elastic_operaciones.eliminaIndice("agn_subserie_trd", "base")
#resultado = elastic_operaciones.eliminaIndice("agn_tipo_documental_trd", "base")

#resultado = elastic_operaciones.eliminaIndice("agn_expedientes_trd", "base")
#resultado = elastic_operaciones.eliminaIndice("agn_documentos_trd", "base")
#resultado = elastic_operaciones.eliminaIndice("agn_prestamos_trd", "base")

#resultado = elastic_operaciones.eliminaIndice("plantillas", "base")
#resultado = elastic_operaciones.eliminaIndice("canales_comunicacion", "base")
#resultado = elastic_operaciones.eliminaIndice("radicados_entrada", "base")
#resultado = elastic_operaciones.eliminaIndice("correos_descargados", "base")

#resultado = elastic_operaciones.eliminaIndice("tipo_peticiones", "base")

#resultado = elastic_operaciones.eliminaIndice("peticiones", "base")

#resultado = elastic_operaciones.eliminaIndice("envios_fisicos", "base")
#resultado = elastic_operaciones.eliminaIndice("planilla_envios_fisicos", "base")

"""
resultado = elastic_operaciones.eliminaIndice("agn_trd", "base")
resultado = elastic_operaciones.eliminaIndice("agn_dependencia_trd", "base")
resultado = elastic_operaciones.eliminaIndice("agn_serie_trd", "base")
resultado = elastic_operaciones.eliminaIndice("agn_subserie_trd", "base")
resultado = elastic_operaciones.eliminaIndice("agn_tipo_documental_trd", "base")
resultado = elastic_operaciones.eliminaIndice("agn_expedientes_trd", "base")
resultado = elastic_operaciones.eliminaIndice("agn_documentos_trd", "base")
resultado = elastic_operaciones.eliminaIndice("agn_prestamos_trd", "base")
resultado = elastic_operaciones.eliminaIndice("agn_transferencias_trd", "base")
"""

#resultado = elastic_operaciones.eliminaIndice("agn_expedientes_trd", "base")

"""
resultado = elastic_operaciones.eliminaIndice("agn_tvd", "base")
resultado = elastic_operaciones.eliminaIndice("agn_dependencia_tvd", "base")
resultado = elastic_operaciones.eliminaIndice("agn_serie_tvd", "base")
resultado = elastic_operaciones.eliminaIndice("agn_subserie_tvd", "base")
resultado = elastic_operaciones.eliminaIndice("agn_expedientes_tvd", "base")
resultado = elastic_operaciones.eliminaIndice("agn_documentos_tvd", "base")
"""
#resultado = elastic_operaciones.eliminaIndice("dependencias", "base")
#resultado = elastic_operaciones.eliminaIndice("peticiones", "base")
#resultado = elastic_operaciones.eliminaIndice("archivos_anexos", "base")

#resultado = elastic_operaciones.eliminaIndice("logs", "base")
#resultado = elastic_operaciones.eliminaIndice("radicados_entrada", "base")
#resultado = elastic_operaciones.eliminaIndice("radicados_salida", "base")
#resultado = elastic_operaciones.eliminaIndice("radicados_interno", "base")
#resultado = elastic_operaciones.eliminaIndice("peticiones", "base")


# PARAMETRIZACION
#resultado = elastic_operaciones.eliminaIndice("logs_ingreso", "base")


"""
resultado = elastic_operaciones.eliminaIndice("tipo_peticiones", "base")
resultado = elastic_operaciones.eliminaIndice("temas", "base")
resultado = elastic_operaciones.eliminaIndice("subtemas", "base")
resultado = elastic_operaciones.eliminaIndice("tipo_poblacion", "base")
resultado = elastic_operaciones.eliminaIndice("tipo_identificaciones", "base")
resultado = elastic_operaciones.eliminaIndice("rango_edad", "base")
resultado = elastic_operaciones.eliminaIndice("genero", "base")
resultado = elastic_operaciones.eliminaIndice("discapacidad", "base")
resultado = elastic_operaciones.eliminaIndice("tipo_terceros", "base")
resultado = elastic_operaciones.eliminaIndice("consecutivos", "base")
resultado = elastic_operaciones.eliminaIndice("plantillas", "base")
resultado = elastic_operaciones.eliminaIndice("ubicaciones", "base")
resultado = elastic_operaciones.eliminaIndice("continentes", "base")
resultado = elastic_operaciones.eliminaIndice("paises", "base")
resultado = elastic_operaciones.eliminaIndice("departamentos", "base")
resultado = elastic_operaciones.eliminaIndice("ciudades", "base")

resultado = elastic_operaciones.eliminaIndice("canales_comunicacion", "base")
resultado = elastic_operaciones.eliminaIndice("festivos", "base")
resultado = elastic_operaciones.eliminaIndice("dependencias", "base")

resultado = elastic_operaciones.eliminaIndice("usuarios", "base")
resultado = elastic_operaciones.eliminaIndice("roles", "base")
resultado = elastic_operaciones.eliminaIndice("grupo_usuarios", "base")
"""

#resultado = elastic_operaciones.eliminaIndice("peticiones", "base")

#resultado = elastic_operaciones.eliminaIndice("agn_expedientes_trd", "base")
#resultado = elastic_operaciones.eliminaIndice("agn_transferencias_trd", "base")

#resultado = elastic_operaciones.eliminaIndice("agn_tvd", "base")
#resultado = elastic_operaciones.eliminaIndice("agn_dependencia_tvd", "base")
#resultado = elastic_operaciones.eliminaIndice("agn_serie_tvd", "base")
#resultado = elastic_operaciones.eliminaIndice("agn_subserie_tvd", "base")
#resultado = elastic_operaciones.eliminaIndice("agn_expedientes_tvd", "base")
#resultado = elastic_operaciones.eliminaIndice("agn_documentos_tvd", "base")

#resultado = elastic_operaciones.eliminaIndice("peticiones", "base")
#resultado = elastic_operaciones.eliminaIndice("archivos_anexos", "base")

#resultado = elastic_operaciones.eliminaIndice("peticiones", "base")
#resultado = elastic_operaciones.eliminaIndice("radicados_salida", "base")
#resultado = elastic_operaciones.eliminaIndice("radicados_entrada", "base")   
#resultado = elastic_operaciones.eliminaIndice("radicados_interno", "base")  
#resultado = elastic_operaciones.eliminaIndice("agn_expedientes_tvd", "base")

#resultado = elastic_operaciones.eliminaIndice("logs", "base")

"""
resultado = elastic_operaciones.eliminaIndice("agn_dependencia_trd", "base")
resultado = elastic_operaciones.eliminaIndice("agn_serie_trd", "base")
resultado = elastic_operaciones.eliminaIndice("agn_subserie_trd", "base")
resultado = elastic_operaciones.eliminaIndice("agn_expedientes_trd", "base")
resultado = elastic_operaciones.eliminaIndice("agn_carpetas_trd", "base")
resultado = elastic_operaciones.eliminaIndice("agn_documentos_trd", "base")
resultado = elastic_operaciones.eliminaIndice("agn_tipo_documental_trd", "base")
"""

elastic_operaciones.eliminaIndice("grupo", "base")