#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
os.environ["NLS_LANG"] = "AMERICAN_AMERICA.AL32UTF8"

##########################################################
## FUNCIONES COMUNES                                    ##
##########################################################

import ldap

##################################################
## DIRECTORIO ACTIVO
##################################################
def validar_usuario(username, password, servidor_ip, servidor_puerto):
    #LDAP_SERVER = 'ldap://172.16.1.20:389'
    LDAP_SERVER = 'ldap://' + str(servidor_ip) + ":" + str(servidor_puerto)

    #username = "fabigonz" 
    #username = "nohora.correa" 
    #username = "astrid.amaya"
    # fully qualified AD user name
    LDAP_USERNAME = '%s@esap.edu.co' % username

    # your password
    LDAP_PASSWORD = password
    #LDAP_PASSWORD = "Npcb1580*"
    #LDAP_PASSWORD = "Contraesap2*"
    #LDAP_PASSWORD = "Esap.2023"
    
    print(
        "LDAP_PASSWORD:", 
        LDAP_USERNAME, 
        LDAP_PASSWORD
    )

    try:
        # build a client
        ldap_client = ldap.initialize(LDAP_SERVER)#, bytes_mode=False)

        # perform a synchronous bind
        ldap_client.set_option(ldap.OPT_REFERRALS, 0)
        con = ldap_client.simple_bind_s(
            LDAP_USERNAME, 
            LDAP_PASSWORD.encode('iso-8859-1')
        )
    except ldap.INVALID_CREDENTIALS:
        ldap_client.unbind()
        return "Error en usuario o password"
    except ldap.SERVER_DOWN:
        return "Servidor LDAP no disponible"
    
    #ldap_client.unbind()
    
    return ""

#print("RESULTADO:", directorio_activo_validar("ventanillaunicapruebas", "Fabian2021*", "172.16.1.20", "389"))
#print("RESULTADO:", directorio_activo_validar("ldap", "Esap.2020", "172.16.1.20", "389"))

