from datetime import datetime

def year_parser(año):
    """
    Este parser convierte valores int a valores str de los años leídos.

    ARGUMENTOS:
        año (int): año leído de los datos del .csv

    DEVUELVE:
        res (str): año leído convertido a str
    """
    res = None
    if año == 1:
        res = 2012
    elif año == 0:
        res = 2011
    return res

def season_parser(estacion):
    """
    Este parser convierte valores int a valores str de las estaciones leídas.

    ARGUMENTOS:
        estacion (int): estación leída de los datos del .csv

    DEVUELVE:
        res (str): estación leída convertida a str
    """
    res = None
    if estacion == 1:
        res = "Invierno"
    elif estacion == 2:
        res = "Primavera"
    elif estacion == 3:
        res = "Verano"
    elif estacion == 4:
        res = "Otoño"
    return res

def weekday_parser(dia):
    """
    Este parser convierte valores int a valores str de los días leídos.

    ARGUMENTOS:
        dia (int): día leído de los datos del .csv

    DEVUELVE:
        res (str): día leído convertido a str
    """
    res = None
    if dia == 0:
        res = "Domingo"
    elif dia == 1:
        res = "Lunes"
    elif dia == 2:
        res = "Martes"
    elif dia == 3:
        res = "Miércoles"
    elif dia == 4:
        res = "Jueves"
    elif dia == 5:
        res = "Viernes"
    elif dia == 6:
        res = "Sábado"
    return res

def month_parser(mes):
    """
    Este parser convierte valores int a valores str de los meses leídos.

    ARGUMENTOS:
        mes (int): mes leído de los datos del .csv

    DEVUELVE:
        res (str): mes leído convertido a str
    """
    res = None
    if mes == 1:
        res = "Enero"
    elif mes == 2:
        res = "Febrero"
    elif mes == 3:
        res = "Marzo"
    elif mes == 4:
        res = "Abril"
    elif mes == 5:
        res = "Mayo"
    elif mes == 6:
        res = "Junio"
    elif mes == 7:
        res = "Julio"
    elif mes == 8:
        res = "Agosto"
    elif mes == 9:
        res = "Septiembre"
    elif mes == 10:
        res = "Octubre"
    elif mes == 11:
        res = "Noviembre"
    elif mes == 12:
        res = "Diciembre"
    return res

def temp_parser(temp):
    """
    Este parser convierte los valores de temperatura
    a sus valores reales multiplicándolos por su máximo
    y redondeando a dos cifras decimales.

    ARGUMENTOS:
        temp (float): temperatura leída de los datos del .csv

    DEVUELVE:
        res (float): temperatura leída convertida a su valor real en celsius
    """
    res = round(temp * 41, 2)
    return res

def atemp_parser(atemp):
    """
    Este parser convierte los valores de sensación térmica
    a sus valores reales multiplicándolos por su máximo
    y redondeando a dos cifras decimales.

    ARGUMENTOS:
        temp (float): sensación térmica leída de los datos del .csv

    DEVUELVE:
        res (float): sensación térmica leída convertida a su valor real en celsius
    """
    res = round(atemp * 50, 2)
    return res

def hum_parser(hum):
    """
    Este parser convierte los valores de humedad
    a sus valores reales multiplicándolos por su máximo
    y redondeando a dos cifras decimales.

    ARGUMENTOS:
        temp (float): humedad leída de los datos del .csv

    DEVUELVE:
        res (float): humedad leída convertida a su valor real en porcentaje
    """
    res = round(hum * 100, 2)
    return res

def wind_parser(windspeed):
    """
    Este parser convierte los valores de velocidad del viento
    a sus valores reales multiplicándolos por su máximo
    y redondeando a dos cifras decimales.

    ARGUMENTOS:
        temp (float): velocidad del viento leída de los datos del .csv

    DEVUELVE:
        res (float): velocidad del viento leída convertida a su valor real en km/h
    """
    res = round(windspeed * 67, 2)
    return res

def num_to_word(num):
    """
    Este parser convierte valores int a valores str de los años.

    ARGUMENTOS:
        num (int): año en int leído de los datos del .csv

    DEVUELVE:
        res (str): año en int leído convertido a año en str
    """
    if num == 2011:
        res = "Dos_Mil_Once"
    elif num == 2012:
        res = "Dos_Mil_Doce"
    return res

def date_parser(fecha):
    """
    Este parser convierte valores str a valores datetime de las fechas leídas.

    ARGUMENTOS:
        fecha (str): fecha leída de los datos del .csv

    DEVUELVE:
        res (datetime): fecha leída convertida a datetime
    """
    res = datetime.strptime(fecha, "%Y-%m-%d").date()
    return res

def int_to_bool(int):
    """
    Este parser convierte valores int a valores bool.

    ARGUMENTOS:
        int (int): int leído de los datos del .csv

    DEVUELVE:
        res (bool): int leído convertido a bool
    """
    if int == 1:
        res = True
    else:
        res = False
    return res

class colores:
    """
    Class para poner colores en la consola al ejecutar bike_renting_info_test
    y así mejorar la legibilidad de las salidas de las funciones test.
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
