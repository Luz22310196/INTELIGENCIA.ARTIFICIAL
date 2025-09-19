# DEFINICIÓN DE UNA CLASE SIMPLE CON SU CONSTRUCTOR
class Usuario:
    def __init__(self, nombre, apellido, edad, correo=None, telefono=None):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.telefono = telefono

# CREAMOS DOS OBJETOS (INSTANCIAS) DE LA CLASE
usuario1 = Usuario("Enrique", "Barros", 32)
usuario2 = Usuario("Elvira", "Gómez", 27)

# AÑADIMOS ATRIBUTOS DINÁMICAMENTE A CADA OBJETO
usuario1.correo = "correo@gmail.com"
usuario2.telefono = "123456789"

# MUESTRA LOS ATRIBUTOS DE LA CLASE (vacío porque no tiene atributos de clase)
print(vars(Usuario), "\n")

# MUESTRA LOS ATRIBUTOS DEL OBJETO usuario1
print(vars(usuario1))

# MUESTRA LOS ATRIBUTOS DEL OBJETO usuario2
print(vars(usuario2))

# TAMBIÉN PODEMOS USAR __dict__ PARA VER LOS ATRIBUTOS DE UN OBJETO
print(usuario2.__dict__)


# FUNCIONES ANIDADAS Y ALCANCE DE VARIABLES

# EJEMPLO 1: FUNCION INTERNA ACCEDE A VARIABLE DE FUNCION EXTERNA
def funcion_externa2():
    a = 10
    def funcion_interna():
        b = 20
        print(a, b)  # 'a' viene de la externa, 'b' es local
    funcion_interna()

funcion_externa2()

# EJEMPLO 2: SOMBREADO DE VARIABLES (REDECLARACIÓN LOCAL)
def funcion_externa1():
    a = 10
    def funcion_interna1():
        a = 100  # esta 'a' es diferente
        print(a)  # imprime 100 (la local)
    funcion_interna1()
    print(a)  # imprime 10 (la de la externa, no fue modificada)

funcion_externa1()
