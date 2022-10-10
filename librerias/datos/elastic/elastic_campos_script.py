#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

#########
# TEXTO #
#########


def fecha(campo):
    fuente = """
        int ano = doc['fecha_documento'].value.getYear();
        int mes = doc['fecha_documento'].value.getMonthValue();
        int dia = doc['fecha_documento'].value.getDayOfMonth();
        ZonedDateTime     formato = ZonedDateTime.of(ano, mes, dia, 0, 0, 0, 0, ZoneId.of("UTC"));
        DateTimeFormatter corta   = DateTimeFormatter.ofPattern("yyyy-MM-dd");
        String            fecha   = formato.format(corta);
        
        return fecha
    """

    guion = {
        'script': {
            'lang': 'painless',
            'source': fuente,
        }
    } 

    return guion

def fecha_hora(campo):
    fuente = """
        int ano      = doc['fecha_documento'].value.getYear();
        int mes      = doc['fecha_documento'].value.getMonthValue();
        int dia      = doc['fecha_documento'].value.getDayOfMonth();
        int hora     = doc['fecha_documento'].value.getHour();
        int minutos  = doc['fecha_documento'].value.getMinute();
        int segundos = doc['fecha_documento'].value.getSecond();
        ZonedDateTime     formato = ZonedDateTime.of(ano, mes, dia, hora, minutos, segundos, 0, ZoneId.of("UTC"));
        DateTimeFormatter corta   = DateTimeFormatter.ofPattern("yyyy-MM-dd hh:mm:ss");
        String            fecha   = formato.format(corta);
        
        return fecha
    """

    guion = {
        'script': {
            'lang': 'painless',
            'source': fuente,
        }
    }

    return guion

tipos_guiones = {
    "fecha"     : fecha,
    "fecha_hora": fecha_hora,
}

def campo_guion(campo, tipo):
    guion   = None
    funcion = tipos_guiones.get(tipo, None)
    if funcion is not None:
        guion = funcion(campo)

    return guion