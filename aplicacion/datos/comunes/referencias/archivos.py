#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

referencia_archivo = {
    "campoReferencia": "id",      
    "modo"           : "multiple",
    "atributosReferencia": [{
        "archivos": "_completo_"            
    }],            
    "estructuraDestino": "archivos_anexos",
    "campoDestino"     : "id",  
    "externa"          : {
        "tipo_relacion": "ANEXOS_RADICADO",
        'tipo'         : 'archivos'      
    }          
}

referencia_borrador = {
    "campoReferencia": "id",      
    "modo"           : "multiple",
    "atributosReferencia": [{
        "archivos": "_completo_"            
    }],            
    "estructuraDestino": "archivos_anexos",
    "campoDestino"     : "id",  
    "externa"          : {
        "tipo_relacion": "ANEXOS_RADICADO",
        'tipo'         : 'archivos'      
    }          
}