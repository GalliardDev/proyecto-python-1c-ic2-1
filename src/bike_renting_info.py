from collections import namedtuple, Counter
import csv
import datetime
import string
from modules.parsers import *
import matplotlib.pyplot as plt

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# PRIMERA ENTREGA
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
tupla_datos = namedtuple("Registro", ["instant","dteday","season","yr","mnth","holiday","weekday","workingday","weathersit","temp","atemp","hum","windspeed","casual","registered","cnt"])

def lee_fichero(fichero):
    '''
    Función que lee un fichero csv codificado en utf-8 
    y convierte los datos en una lista de tuplas. Los 
    valores de esta lista de tuplas luego se asignan a
    la namedtuple definida al principio.
    
    ARGUMENTOS: 
        - fichero (string): ruta del fichero 
    DEVUELVE: 
        - tupla_datos (namedtuple): ["Registro", (instant, dteday, season, yr, mnth, holiday, weekday, workingday, weathersit, temp, atemp, hum, windspeed, casual, registered, cnt)] -> [str, (int, str, int, int, int, bool, int, bool, int, float, float, float, float, int, int, int)]
    
    Cada columna de data.csv se corresponde con un día del año con los datos:
        - Día
        - Fecha
        - Estación
        - Año
        - Mes
        - Vacaciones (S/N)
        - Día de la semana
        - Día laborable (S/N)
        - Clima
        - Temperatura (ºC)
        - Sensación térmica
        - Humedad (%)
        - Velocidad del viento (Km/h)
        - Usuario no registrado
        - Usuario registrado
        - Alquileres totales de bicis (usuarios registrados y no registrados)
    '''
    with open(fichero, encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        registros = []
        for registro in lector:
            instant = int(registro[0])
            dteday = date_parser(str(registro[1]))
            season = season_parser(int(registro[2]))
            yr = year_parser(int(registro[3]))
            mnth = month_parser(int(registro[4]))
            holiday = int_to_bool(int(registro[5])) 
            weekday = weekday_parser(int(registro[6]))
            workingday = int_to_bool(int(registro[7]))
            weathersit = int(registro[8])
            temp = temp_parser(float(registro[9]))
            atemp = atemp_parser(float(registro[10]))
            hum = hum_parser(float(registro[11]))
            windspeed = wind_parser(float(registro[12]))
            casual = int(registro[13])
            registered = int(registro[14])
            cnt = int(registro[15])
            tupla_registros = tupla_datos(instant,dteday, season, yr, mnth, holiday, weekday, workingday, weathersit, temp, atemp, hum, windspeed, casual, registered, cnt)
            registros.append(tupla_registros)
    return registros

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# SEGUNDA ENTREGA
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ================================ BLOQUE I ===============================
def filtra_por_estacion(datos, estacion):
    """
    Esta función recorre la namedtuple tipo Registro buscando
    la estación especificada para filtrar los datos respecto 
    a ella.

    ARGUMENTOS:
        datos (lista): lista de namedtuples tipo Registro
        estacion (string): Invierno, Primavera, Verano, Otoño

    DEVUELVE:
        filtro (lista): datos filtrados respecto a la estación especificada
    """
    return [d for d in datos if estacion == d.season]

def total_usuarios_registrados_por_estacion(datos, estacion):
    """
    Esta función calcula el total de usuarios registrados
    durante una estación concreta.

    ARGUMENTOS:
        datos (lista): lista de namedtuples tipo Registro
        estacion (string): Invierno, Primavera, Verano, Otoño

    DEVUELVE:
        registrados (int): número total de usuarios registrados 
        durante la estación
    """
    return sum(d.registered for d in datos if estacion==d.season)
# =========================================================================

# =============================== BLOQUE II ===============================
def maximo_usuarios_registrados_por_estacion_y_año(datos, estacion, año):
    """
    Esta función calcula el máximo de usuarios registrados durante
    una estación concreta de un año específico.

    ARGUMENTOS:
        datos (lista): lista de namedtuples tipo Registro
        estacion (string): Invierno, Primavera, Verano, Otoño
        año (int): 2011, 2012

    DEVUELVE:
        lista (list): [Registro(instant, dteday, season, yr, mnth, holiday, weekday, workingday, weathersit, temp, atemp, hum, windspeed, casual, registered, cnt)]
    """
    return max([d.registered for d in datos if estacion == d.season and año == d.yr])

def ordena_usuarios_registrados_por_estacion_y_año(datos, estacion, año):
    """
    Esta función devuelve una lista de namedtuples tipo Registro
    ordenadas de mayor a menor filtrando por los usuarios
    registrados en cada estación de un año específico.

    ARGUMENTOS:
        datos (lista): lista de namedtuples tipo Registro
        estacion (string): Invierno, Primavera, Verano, Otoño
        año (int): 2011, 2012

    DEVUELVE:
        lista (list): [Registro(instant, dteday, season, yr, mnth, holiday, weekday, workingday, weathersit, temp, atemp, hum, windspeed, casual, registered, cnt)]
    """   
    return sorted([d for d in datos if año == d.yr and estacion == d.season], key=lambda d: d.registered, reverse=True)

def vacaciones_por_mes_y_año(datos):
    '''
    Esta función devuelve un diccionario con los días (fecha completa)
    que son festivos de cada mes. En el diccionario la clave es el mes
    y el valor la lista de días.
    
    ARGUMENTOS:
        datos (lista): lista de namedtuples tipo Registro
    
    DEVUELVE:
        s (dict) -> {Mes:[Días festivos]}
    '''
    s = dict()
    # Creación del diccionario         
    for d in datos:
        key = d.mnth
        if key not in s:
            s[key] = []
        elif key in s:
            if d.mnth in s.keys() and d.holiday == True:
                s[d.mnth].append(datetime.strftime(d.dteday,"%d/%m/%Y"))
    return s
# =========================================================================

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# TERCERA ENTREGA
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# =============================== BLOQUE III ==============================
def total_laborables_por_mes_y_año(datos, año):
    '''
    Esta función devuelve un diccionario con los días (fecha completa)
    que son festivos de cada mes. En el diccionario la clave es el mes
    y el valor la lista de días.
    
    ARGUMENTOS:
        datos (lista): lista de namedtuples tipo Registro
    
    DEVUELVE:
        s (dict) -> {Mes:[Días festivos]}
    '''
    s = dict()
    # Creación del diccionario         
    for d in datos:
        key = d.mnth
        if key not in s:
            s[key] = 0
        elif key in s:
            if d.mnth in s.keys() and d.workingday == True and año == d.yr:
                s[d.mnth]+=1
    return s

def moda_temperatura(datos):
    '''
    Esta función devuelve un diccionario tipo Counter
    con las veces que se repite cada valor de temperatura
    (d.temp) para luego ver cuál se repite más.
    
    ARGUMENTOS:
        datos (lista): lista de namedtuples tipo Registro
    
    DEVUELVE:
        s (dict) -> Counter({d.temp:veces})
    '''
    return Counter([d.temp for d in datos])

def humedad_maxima_por_mes_y_año(datos, año):
    '''
    Esta función devuelve un diccionario en el que las
    claves son los meses y los valores el valor máximo
    de humedad en porcentajes (%).
    
    ARGUMENTOS:
        datos (lista): lista de namedtuples tipo Registro
    
    DEVUELVE:
        s (dict) -> {d.mnth:max(d.hum)}
    '''
    s = dict()
    # Creación del diccionario         
    for d in datos:
        key = d.mnth
        if key not in s:
            s[key] = 0
        elif key in s:
            if d.mnth in s.keys() and año == d.yr:
                s[d.mnth]=max([d.hum for d in datos if key == d.mnth])
    return s

def incremento_usuarios_registrados(datos):
    '''
    Esta función devuelve una lista de los incrementos 
    porcentuales de usuarios registrados del 2012 respecto
    al 2011.
    
    ARGUMENTOS:
        datos (lista): lista de namedtuples tipo Registro
    
    DEVUELVE:
        l (list) -> [porcentaje_Enero,...,porcentaje_Diciembre]
    '''
    meses = []
    for d in datos:
        if d.mnth not in meses:
            meses.append(d.mnth)

    s_2011 = dict()
    for d in datos:
        key = d.mnth
        if key not in s_2011:
            s_2011[key] = 0
        elif key in s_2011:
            for mes in meses:
                if mes == d.mnth:
                    s_2011[d.mnth]=sum(d.registered for d in datos if 2011 == d.yr and key == d.mnth)

    s_2012 = dict()
    for d in datos:
        key = d.mnth
        if key not in s_2012:
            s_2012[key] = 0
        elif key in s_2012:
            for mes in meses:
                if mes == d.mnth:
                    s_2012[d.mnth]=sum(d.registered for d in datos if 2012 == d.yr and key == d.mnth)
    
    l = []
    for d in datos:
        incremento_porcentual = round((s_2012[d.mnth]-s_2011[d.mnth])/s_2011[d.mnth]*100,2)
        if incremento_porcentual not in l:
            l.append(incremento_porcentual)

    return l
# =========================================================================

# =============================== BLOQUE IV ===============================
def dibuja_grafica_incremento_usuarios_registrados(datos):
    '''
    Esta función grafica una gráfica basada en los datos de la función
    anterior, la cuál calculaba los incrementos porcentuales de los usuarios
    registrados por mes.
    
    ARGUMENTOS:
        datos (lista): lista de namedtuples tipo Registro
    
    DEVUELVE:
        none (dibuja una gráfica)
    '''
    v = incremento_usuarios_registrados(datos)
    m = [i for i in range(1,13)]
    plt.plot(m,v)
    plt.title("Incremento porcentual respecto a meses")
    plt.xlabel("Meses en números")
    plt.ylabel("Incremento porcentual usuarios registrados")
    plt.show()
# =========================================================================

# =============================== DEFENSA =================================
def estacion_temperatura_humedad(datos):
    '''
    Esta función toma como parámetro el dataset y devuelve
    la estació, temperatura y humedad en tuplas en una lista.
    ARGUMENTOS:
        datos (lista): lista de namedtuples tipo Registro
    DEVUELVE:
        lista (list): lista de  tuplas tipo [(estacion,temperatura,humedad)]
    '''
    climatologia = namedtuple("Clima","Estacion,Temperatura,Humedad")
    lista = []
    for d in datos:
        tupla = climatologia(d.season,d.temp,d.hum)
        lista.append(tupla)
    return lista

def media_temperaturas_por_estacion(datos, humedad):
    s = dict()
    for d in datos:
        key = d.season
        if d.hum > humedad:
            if key not in s:
                    s[key] = [d.temp]
            elif key in s:
                    s[key].append(d.temp)

    t = dict()
    for i in s:
        key = d.season
        if key not in t:
            t[key] = 0
        elif key in t:
            t[key] = sum(s[i])/len(s)
    return t
# =========================================================================