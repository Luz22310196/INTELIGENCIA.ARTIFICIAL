# DEFINO UNA FUNCIÓN DECORADORA QUE ENVUELVE CUALQUIER FUNCIÓN QUE LE PASE
def decoradora(funcion_parametro):
    def funcion_interna():
        # SE EJECUTA ANTES DE LA FUNCIÓN ORIGINAL
        print("El resultado de la operación es: ")
        funcion_parametro()  # LLAMO A LA FUNCIÓN ORIGINAL
        # SE EJECUTA DESPUÉS DE LA FUNCIÓN ORIGINAL
        print("Operación realizada con éxito.")
    return funcion_interna  # RETORNO LA NUEVA FUNCIÓN ENVUELTA

# APLICO LA DECORADORA A CADA FUNCIÓN MATEMÁTICA

@decoradora
def sumar():
    print(10 + 10)

@decoradora
def restar():
    print(10 - 20)

@decoradora
def multiplicar():
    print(45 * 2)

@decoradora
def dividir():
    print(4 / 87)

# AHORA LLAMO A LAS FUNCIONES PARA VER EL RESULTADO
sumar()
restar()
multiplicar()
dividir()
