#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os
os.environ["NLS_LANG"] = "AMERICAN_AMERICA.AL32UTF8"

##########################################################
## FUNCIONES COMUNES                                    ##
##########################################################

import ldap
print("ldap:", ldap)

##################################################
## DIRECTORIO ACTIVO
##################################################

def check_credentials(username, password):
    LDAP_SERVER = 'ldap://172.16.1.20:389'
    # fully qualified AD user name
    print( "LDAP_SERVER:", LDAP_SERVER )
    LDAP_USERNAME = '%s@esap.edu.co' % username
    print( "LDAP_USERNAME:", LDAP_USERNAME )
    # your password
    LDAP_PASSWORD = password
    print( "LDAP_PASSWORD:", LDAP_PASSWORD )
    try:
        # build a client
        ldap_client = ldap.initialize(LDAP_SERVER)
        print("ldap_client:", ldap_client)
        # perform a synchronous bind
        ldap_client.set_option(ldap.OPT_REFERRALS,0)
        con = ldap_client.simple_bind_s(LDAP_USERNAME, LDAP_PASSWORD)
        print("con:", con)
    except ldap.INVALID_CREDENTIALS:
        ldap_client.unbind()
        return 'Wrong username ili password'
    except ldap.SERVER_DOWN:
        return 'AD server not awailable'
    
    #ldap_client.unbind()
    return ldap_client

print("")
#print("RESULTADO:", check_credentials("ldap", "Esap.2020"))

print("RESULTADO:", check_credentials("ventanillaunicapruebas", "Fabian2021*"))