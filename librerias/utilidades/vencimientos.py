import datetime

################
# VENCIMIENTOS #
################
# Es festivo ?
def es_festivo( fecha, festivos=[] ):
    resultado  = False    
    cero       = datetime.timedelta(0) 
    diferencia = -1
    for dia in festivos:
        diferencia = fecha - dia
        if diferencia == cero: 
            resultado = True
            break
    
    return resultado

# Es dia habil
def es_dia_habil( fecha, festivos=[] ):
    festivo    = es_festivo( fecha, festivos )
    dia_semana = fecha.weekday()   

    return (dia_semana < 5) and (not festivo)

# Siguiente dia habil
def siguiente_habil( fecha, festivos=[] ):
    un_dia      = datetime.timedelta(1)
    fecha_sigue = fecha + un_dia
    sigue       = True
    while ( sigue ):
        if not es_dia_habil( fecha_sigue, festivos ):
            # Dia habil puede siguiente dia
            fecha_sigue = fecha_sigue + un_dia
        else:
            sigue = False
    
    return fecha_sigue

# Prepara festivos
def prepara_festivos( festivos=[] ):
    return [ datetime.datetime(dia.year, dia.month, dia.day, 0, 0, 0, 0) for dia in festivos ]   

# Siguiente fecha - DIAS
def siguiente_fecha_habil_dias( fecha_inicial, dias=0, festivos=[] ):
    if dias > 0:
        # Festivos dias sin horas
        festivos    = prepara_festivos( festivos )
        # Fecha dias sin horas
        fecha_base  = datetime.datetime( fecha_inicial.year, fecha_inicial.month, fecha_inicial.day, 0, 0, 0, 0 )
    # Siguiente dia habil comienzan los terminos
        # Fecha habil solo si festivo es dia siguiente ala actaul
        # no esta claro porque suma festivos si no esta en el rango final
        fecha_habil = siguiente_habil( fecha_base, festivos )
    
        dias      -= 1
        # Calcula cuando son mas de un dia
        while ( dias > 0 ):    
            fecha_habil = siguiente_habil( fecha_habil, festivos )
            dias -= 1
    else:
        fecha_habil = fecha_inicial
            
    return fecha_habil

# Calcula el numero de dias habiles entre dos fechas
def diferencia_en_dias_habiles( fecha_hoy, fecha_vence, festivos=[] ):
    # Festivos dias sin horas
    festivos = prepara_festivos( festivos )
    un_dia = datetime.timedelta(1)
    cero_dia = datetime.timedelta(0)
    # Fechas rango
    fecha_hoy = datetime.datetime( fecha_hoy.year, fecha_hoy.month, fecha_hoy.day,   0, 0, 0, 0 )
    fecha_vence = datetime.datetime( fecha_vence.year, fecha_vence.month, fecha_vence.day, 0, 0, 0, 0 )
    # Fechas rango habiles 
    fecha_base = siguiente_habil( fecha_hoy,   festivos )
    fecha_final = siguiente_habil( fecha_vence, festivos )
    dias = 0    
    if ( fecha_base - fecha_final ) < cero_dia:
        # Dentro de los terminos
        # Cuenta dias hasta fecha final
        while ( ((fecha_base + un_dia) - fecha_final) <= cero_dia ): 
            fecha_base = fecha_base + un_dia
            if es_dia_habil( fecha_base, festivos ):        
                dias += 1
    else:
        # Fuera de terminos
        # Cuenta dias desde fecha final (negativo)        
        while ( (fecha_base - fecha_final) > cero_dia ):            
            fecha_base = fecha_base - un_dia
            if es_dia_habil( fecha_base, festivos ):        
                dias -= 1      
        
    return dias

# Calcula el porcentaje de avance en porcentaje
def diferencia_en_porcentaje_dias( dias_total, dias_hoy ):
    diferencia = 0
    if dias_total > 0:
        diferencia = 100 - round((dias_hoy / dias_total)  * 100)
        
    return diferencia