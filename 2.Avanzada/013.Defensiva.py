#CALCULADORA BÁSICA CON MANEJO DE ERRORES

# FUNCIÓN PARA SUMAR
def sumar(a, b):
    return a + b

# FUNCIÓN PARA RESTAR
def restar(a, b):
    return a - b

# FUNCIÓN PARA MULTIPLICAR
def multiplicar(a, b):
    return a * b

# FUNCIÓN PARA DIVIDIR CON VALIDACIÓN
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("NO SE PUEDE DIVIDIR ENTRE CERO")
    return a / b

# PROGRAMA PRINCIPAL
try:
    # PIDO LOS DOS NÚMEROS
    num1 = float(input("PRIMER NÚMERO: "))
    num2 = float(input("SEGUNDO NÚMERO: "))

    # PIDO LA OPERACIÓN A REALIZAR
    operacion = input("OPERACIÓN (+, -, *, /): ")

    # VERIFICO Y EJECUTO LA OPERACIÓN
    if operacion == "+":
        resultado = sumar(num1, num2)
    elif operacion == "-":
        resultado = restar(num1, num2)
    elif operacion == "*":
        resultado = multiplicar(num1, num2)
    elif operacion == "/":
        resultado = dividir(num1, num2)
    else:
        print("OPERACIÓN NO VÁLIDA")
    
    # MUESTRO EL RESULTADO
    print("RESULTADO:", resultado)

# MANEJO DE ERRORES SI SE INGRESA TEXTO
except ValueError:
    print("DEBES INGRESAR NÚMEROS VÁLIDOS")

# MANEJO DE ERROR DE DIVISIÓN ENTRE CERO
except ZeroDivisionError as e:
    print("ERROR:", e)

# CUALQUIER OTRO ERROR
except Exception as e:
    print("ALGO SALIÓ MAL:", e)
