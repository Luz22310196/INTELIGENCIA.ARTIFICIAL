# IMPORTO EL MÓDULO 'MATH' PARA REALIZAR OPERACIONES MATEMÁTICAS
import math 

# PIDO UN NÚMERO AL USUARIO PARA CALCULAR SU RAÍZ CUADRADA
numero = int(input("Introduce un número: "))

# CALCULO LA RAÍZ CUADRADA CON LA FUNCIÓN sqrt()
raiz = math.sqrt(numero)

# MUESTRO EL RESULTADO DE LA RAÍZ CUADRADA
print(f"La raíz cuadrada de {numero} es {raiz}")


# IMPORTO EL MÓDULO 'DATETIME' PARA MANEJAR FECHAS Y HORAS
import datetime

# CREO UN OBJETO DE TIPO 'time' CON HORA, MINUTOS, SEGUNDOS Y MICROSEGUNDOS
hora = datetime.time(14, 30, 20, 656)

# IMPRIMO CADA PARTE DE LA HORA POR SEPARADO
print(f"Hora: {hora.hour}")
print(f"Minutos: {hora.minute}")
print(f"Segundos: {hora.second}")
print(f"Microsegundos: {hora.microsecond}")

# CREO UN OBJETO CON LA FECHA ACTUAL USANDO date.today()
fecha_hoy = datetime.date.today()

# IMPRIMO LA FECHA ACTUAL
print(fecha_hoy)

# OBTENGO LA FECHA Y HORA EXACTA DEL MOMENTO DE LA EJECUCIÓN
hora_actual = datetime.datetime.now()

# IMPRIMO LA HORA Y FECHA ACTUAL
print(hora_actual)


# IMPORTO SOLO LA CLASE datetime DEL MÓDULO datetime
from datetime import datetime

# OBTENGO LA FECHA Y HORA ACTUAL
fecha_actual = datetime.now()

# FORMATEO LA FECHA EN UN FORMATO MÁS LEGIBLE (EJEMPLO: MONDAY, 19TH SEPTEMBER 2025)
fecha_formateada = fecha_actual.strftime("%A, %dth %B %Y")

# IMPRIMO LA FECHA FORMATEADA
print(fecha_formateada)
