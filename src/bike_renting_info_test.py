from bike_renting_info import *

# MÉTODO DE LECTURA DEL FICHERO
def lee_fichero_test(datos):
    print(f"\n\n{colores.FAIL}{colores.BOLD}PRUEBA DE LA FUNCIÓN lee_fichero{colores.ENDC}")
    print(datos[0:2])
    print(".\n.\n.")
    print(datos[729:731])

    print(f"{colores.OKCYAN}Se han leído", len(datos), f"registros de datos.{colores.ENDC}\n\n")

# ================================ BLOQUE I ===============================
def filtra_por_estacion_test(datos):
    s = "Primavera"
    d = filtra_por_estacion(datos, s)
    print(f"{colores.FAIL}{colores.BOLD}PRUEBA DE LA FUNCIÓN filtra_por_estacion{colores.ENDC}")       
    print(d[0:2])
    print(".\n.\n.")
    print(d[len(d)-2:len(d)])

    print(f"{colores.OKCYAN}Se han leido",len(d),f"datos sobre la estación {s}.{colores.ENDC}\n\n")

def total_usuarios_registrados_por_estacion_test(datos):
    s = "Invierno"
    d = total_usuarios_registrados_por_estacion(datos, s)    
    print(f"{colores.FAIL}{colores.BOLD}PRUEBA DE LA FUNCIÓN total_usuarios_registrados_por_estacion{colores.ENDC}")
    print(f"{colores.OKCYAN}Se registraron",d,f"usuarios en {s}.{colores.ENDC}\n\n")
# =========================================================================



# =============================== BLOQUE II ===============================
def maximo_usuarios_registrados_por_estacion_y_año_test(datos):
    s = "Otoño"
    y = 2011
    d = maximo_usuarios_registrados_por_estacion_y_año(datos,s,y)
    print(f"{colores.FAIL}{colores.BOLD}PRUEBA DE LA FUNCIÓN maximo_usuarios_registrados_por_estacion_y_año{colores.ENDC}")
    print(f"{colores.OKCYAN}El máximo de usuarios registrados en {s} en el año {y} es {d}.{colores.ENDC}\n\n")

def ordena_usuarios_registrados_por_estacion_y_año_test(datos):
    y = 2011
    s = "Verano"
    d = ordena_usuarios_registrados_por_estacion_y_año(datos,s,y)
    print(f"{colores.FAIL}{colores.BOLD}PRUEBA DE LA FUNCIÓN ordena_usuarios_registrados_por_estacion_y_año{colores.ENDC}")
    print(d[:3],"\n.\n.\n.\n",d[len(d)-3:len(d)])
    print(f"{colores.OKCYAN}Se han leído",len(d),f"datos de {s} del año {y} {colores.ENDC}\n\n")

def vacaciones_por_mes_y_año_test(datos):
    d = vacaciones_por_mes_y_año(datos)
    print(f"{colores.FAIL}{colores.BOLD}PRUEBA DE LA FUNCIÓN vacaciones_por_mes_y_año{colores.ENDC}")
    print(f"{d}")
    print(f"{colores.OKCYAN}Cada valor de las claves corresponde a la lista de días festivos.{colores.ENDC}\n\n")
# =========================================================================



# =============================== BLOQUE III ==============================
def total_laborables_por_mes_y_año_test(datos):
    y = 2011
    d = total_laborables_por_mes_y_año(datos, y)
    print(f"{colores.FAIL}{colores.BOLD}PRUEBA DE LA FUNCIÓN total_laborables_por_mes_y_año{colores.ENDC}")
    print(f"{colores.OKCYAN}Datos del año: {y}{colores.ENDC}")
    print(f"{d}")
    print(f"{colores.OKCYAN}Cada valor de las claves corresponde al total de días laborables de cada mes.{colores.ENDC}\n\n")

def moda_temperatura_test(datos):
    d = moda_temperatura(datos)
    print(f"{colores.FAIL}{colores.BOLD}PRUEBA DE LA FUNCIÓN moda_temperatura{colores.ENDC}")
    print(f"{colores.OKCYAN}La temperatura más repetida es {d.most_common(1)[0][0]}ºC.{colores.ENDC}\n\n")

def humedad_maxima_por_mes_y_año_test(datos):
    y = 2011
    d = humedad_maxima_por_mes_y_año(datos,y)
    print(f"{colores.FAIL}{colores.BOLD}PRUEBA DE LA FUNCIÓN humedad_maxima_por_mes_y_año{colores.ENDC}")
    print(f"{colores.OKCYAN}Datos del año: {y}{colores.ENDC}")
    print(f"{d}")
    print(f"{colores.OKCYAN}Cada valor de las claves corresponde al máximo de humedad de cada mes.{colores.ENDC}\n\n")

def incremento_usuarios_registrados_test(datos):
    d = incremento_usuarios_registrados(datos)
    print(f"{colores.FAIL}{colores.BOLD}PRUEBA DE LA FUNCIÓN incremento_usuarios_registrados{colores.ENDC}")
    print(f"Incremento de usuarios registrados en Enero: {d[0]} %")
    print(f"Incremento de usuarios registrados en Febrero: {d[1]} %")
    print(f"Incremento de usuarios registrados en Marzo: {d[2]} %")
    print(f"Incremento de usuarios registrados en Abril: {d[3]} %")
    print(f"Incremento de usuarios registrados en Mayo: {d[4]} %")
    print(f"Incremento de usuarios registrados en Junio: {d[5]} %")
    print(f"Incremento de usuarios registrados en Julio: {d[6]} %")
    print(f"Incremento de usuarios registrados en Agosto: {d[7]} %")
    print(f"Incremento de usuarios registrados en Septiembre: {d[8]} %")
    print(f"Incremento de usuarios registrados en Octubre: {d[9]} %")
    print(f"Incremento de usuarios registrados en Noviembre: {d[10]} %")
    print(f"Incremento de usuarios registrados en Diciembre: {d[11]} %")
    print(f"{colores.OKCYAN}Datos del año 2012 respecto a 2011.{colores.ENDC}\n\n")
# =========================================================================



# =============================== BLOQUE IV ===============================
def dibuja_grafica_incremento_usuarios_registrados_test(datos):
    print(f"{colores.FAIL}{colores.BOLD}PRUEBA DE LA FUNCIÓN dibuja_grafica_incremento_usuarios_registrados{colores.ENDC}")
    print(f"{colores.OKCYAN}Se ha dibujado la gráfica.{colores.ENDC}\n\n")
    dibuja_grafica_incremento_usuarios_registrados(datos)
# =========================================================================




# =============================== DEFENSA ===============================
def estacion_temperatura_humedad_test(datos):
    d = estacion_temperatura_humedad(datos)
    print(f"{colores.FAIL}{colores.BOLD}PRUEBA DE LA FUNCIÓN estacion_temperatura_humedad{colores.ENDC}")
    print(d[:3],"\n.\n.\n.\n",d[len(d)-3:len(d)],"\n\n")

def media_temperaturas_por_estacion_test(datos):
    t = 25.0
    d = media_temperaturas_por_estacion(datos,t)
    print(f"{colores.FAIL}{colores.BOLD}PRUEBA DE LA FUNCIÓN media_temperaturas_por_estacion{colores.ENDC}")
    print(d)
    print("\n\n")
# =========================================================================

# PROGRAMA PRINCIPAL (main)
def main():
    datalist = lee_fichero("./data/data.csv")

    lee_fichero_test(datalist) 
    filtra_por_estacion_test(datalist) 
    total_usuarios_registrados_por_estacion_test(datalist)
    maximo_usuarios_registrados_por_estacion_y_año_test(datalist) 
    ordena_usuarios_registrados_por_estacion_y_año_test(datalist)
    vacaciones_por_mes_y_año_test(datalist)
    total_laborables_por_mes_y_año_test(datalist)
    moda_temperatura_test(datalist)
    humedad_maxima_por_mes_y_año_test(datalist)
    incremento_usuarios_registrados_test(datalist)
    dibuja_grafica_incremento_usuarios_registrados_test(datalist)
    estacion_temperatura_humedad_test(datalist)
    media_temperaturas_por_estacion_test(datalist)


if __name__ == "__main__":
    main()