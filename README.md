# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  22/23)
Autor/a: José Manuel Amador Gallardo &nbsp;&nbsp;&nbsp;UVUS:XXXNNNN<br>

El dataset es una información sobre la empresa de alquiler de bicicletas, Capital Bikeshare en Washington D.C. durante los años 2011/2012. Consta de 16 columnas de las cuales una es de tipo fecha y el resto varía entre *int*, *float* y *bool*.


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **bike_renting_info.py**: Contiene las funciones principales del proyecto, como leer el fichero ```data.csv``` o varios filtros.
  * **bike_renting_info_test.py**: Contiene las funciones que testean las funciones definidas en ```bike_renting_info.py```.
* **/src/modules**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **parsers.py**: Contiene funciones auxiliares para hacer parse de algunos datos.
* **/data**: Contiene el dataset del proyecto.
    * **data.csv**: Datos recopilados sobre la empresa de alquiler de bicicletas, Capital Bikeshare en Washington D.C. durante los años 2011/2012.
    
## Estructura del *dataset*

En el dataset se encuentran los siguientes datos:

* **instant**: de tipo *int*, representa el índice del registro
* **dteday**: de tipo *datetime*, representa la fecha
* **season**: de tipo *int*, representa la estación
* **yr**: de tipo *bool*, representa el año
* **mnth**: de tipo *int*, representa el mes
* **holiday**: de tipo *bool*, representa si es vacaciones o no
* **weekday**: de tipo *int*, representa el día de la semana
* **workingday**: de tipo *bool*, representa si el día es laborable o no
* **weathersit**: de tipo *int*, representa el clima
* **temp**: de tipo *float*, representa la temperatura en Celsius
* **atemp**: de tipo *float*, representa la sensación térmica en Celsius
* **hum**: de tipo *float*, representa los valores de humedad
* **windspeed**: de tipo *float*, representa la velocidad del viento
* **casual**: de tipo *int*, representa los usuarios casuales (no registrados)
* **registered**: de tipo *int*, representa los usuarios registrados
* **cnt**: de tipo *int*, representa las bicicletas totales alquiladas entre casuales y registrados

## Tipos implementados

Se ha implementado una *namedtuple* llamada **tupla_datos** la cual almacena los datos del fichero .csv

## Funciones implementadas

### bike_renting_info.py

#### BLOQUE I
* **lee_fichero**: Lee un fichero csv y añade sus líneas a una lista de namedtuples del tipo definido: Registro.
* **filtra_por_estacion**: Filtra los datos respecto a una estación y devuelve una lista con las namedtuples de tipo Registro de dicha estación.
* **total_usuarios_registrados_por_estacion**: Calcula el total de usuarios registrados en una estación concreta.

#### BLOQUE II
* **maximo_usuarios_registrados_por_estacion_y_año**: Devuelve el número de usuarios registrados durante una estación de un año específico.
* **ordena_usuarios_registrados_por_estacion_y_año**: Devuelve una lista de namedtuples tipo Registro ordenadas de mayor a menor según el valor numérico de los usuarios registrados para una estación y año concretos.
* **vacaciones_por_mes_y_año**: Devuelve un diccionario con los días que son festivos de cada mes. En el diccionario las claves son los meses y los valores son listas con los días (dd/MM/YYYY).

#### BLOQUE III
* **total_laborables_por_mes_y_año**: Devuelve un diccionario en el cuál las claves son los meses y los valores el total de días laborables (int).
* **moda_temperatura**: Devuelve el valor de temperatura más repetido durante los dos años.
* **humedad_maxima_por_mes_y_año**: Devuelve un diccionario con el máximo porcentual de humedad filtrado por mes y año. En el diccionario las claves son los meses y el valor el máximo de temperatura (float).
* **incremento_usuarios_registrados**: Devuelve una lista con los incrementos porcentuales del 2012 respecto al 2011. Cada valor corresponde a un mes [ 0->Enero,1->Febrero,...,12->Diciembre ]

#### BLOQUE IV
* **dibuja_grafica_incremento_usuarios_registrados**: Grafica una gráfica respecto a los incrementos porcentuales mencionados.

### bike_renting_info_test.py

#### BLOQUE I
* **lee_fichero_test**: Testea la función *lee_fichero* printeando los registros leídos y dos intervalos de datos.
* **filtra_por_estacion_test**: Testea la función *filtra_por_estacion* printeando los registros leídos y dos intervalos de datos.
* **total_usuarios_registrados_por_estacion_test**: Testea la función *total_usuarios_registrados_por_estacion* printeando la cantidad total de usuarios registrados en una estación.

#### BLOQUE II
* **maximo_usuarios_registrados_por_estacion_y_año_test**: Testea la función *maximo_usuarios_registrados_por_estacion_y_año* printeando el máximo de usuarios registrados según los parámetros dados (estación y año).
* **ordena_usuarios_registrados_por_estacion_y_año_test**: Testea la función *ordena_usuarios_registrados_por_estacion_y_año* printeando la lista de namedtuples tipo Registro ordenadas según usuarios registrados.
* **vacaciones_por_mes_y_año_test**: Testea la función *vacaciones_por_mes_y_año* y devuelve los datos de los días que son festivos, en su formato de fecha completa, metidos en una lista. Dicha lista es el valor de las claves del diccionario, que son los meses.

#### BLOQUE III
* **total_laborables_por_mes_y_año_test**: Testea la función *total_laborables_por_mes_y_año* printeando el diccionario completo.
* **moda_temperatura_test**: Testea la función *moda_temperatura* printeando la moda de temperatura.
* **humedad_maxima_por_mes_y_año_test**: Testea la función *humedad_maxima_por_mes_y_año* printeando el diccionario completo.
* **incremento_usuarios_registrados_test**: Testea la función *incremento_usuarios_registrados* los incrementos porcentuales por mes.

#### BLOQUE IV
* **dibuja_grafica_incremento_usuarios_registrados_test**: Testea la función *dibuja_grafica_incremento_usuarios_registrados* graficando una gráfica respecto a los incrementos porcentuales mencionados.

### parsers.py
* **year_parser**: Convierte el *bool* de *yr* en un *int* año.
* **season_parser**: Convierte el *int* de *season* en un *string* con el nombre de la estación.
* **weekday_parser**: Convierte el *int* de weekday en un *string* con el nombre del día de la semana.
* **month_parser**: Convierte el *int* de *mnth* en un *string* con el nombre del mes.
* **temp_parser**: Multiplica la temperatura por su máximo.
* **atemp_parser**: Multiplica la sensación térmica por su máximo.
* **hum_parser**: Multiplica la humedad por su máximo.
* **wind_parser**: Multiplica la velocidad del viento por su máximo.
* **num_to_word**: Parsea los años *2011* y *2012* a *DosMilOnce* y *DosMilDoce* para usos posteriores en una namedtuple.
* **date_parser**: Convierte el *string* de *dteday* en *datetime*.
* **int_to_bool**: Convierte los *int* 1 y 0 a los *bool* True y False.
* **bcolors (class)**: Un class para aplicar colores a la consola y mejorar la legibilidad.
