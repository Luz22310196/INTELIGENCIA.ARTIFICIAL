# DEFINICIÓN DE LA CLASE BASE
class Animal:
    """CLASES CON POLIMORFISMO"""
    def hablar(self):
        print("SOY UN ANIMAL")  # MÉTODO QUE IMPRIME UN MENSAJE GENÉRICO

# CLASE PERRO HEREDA DE ANIMAL
class Perro(Animal):
    def hablar(self):
        print("WOOF!")  # MÉTODO SOBRESCRITO QUE IMPRIME EL LADRIDO

# CLASE GATO HEREDA DE ANIMAL
class Gato(Animal):
    def hablar(self):
        print("MEOW!")  # MÉTODO SOBRESCRITO QUE IMPRIME EL MAULLIDO

# INSTANCIAS DE CADA CLASE
animal = Animal()  # OBJETO DE LA CLASE ANIMAL
perro = Perro()    # OBJETO DE LA CLASE PERRO
gato = Gato()      # OBJETO DE LA CLASE GATO

# LLAMADAS A LOS MÉTODOS HABLAR
animal.hablar()  # IMPRIME: "SOY UN ANIMAL"
perro.hablar()   # IMPRIME: "WOOF!"
gato.hablar()    # IMPRIME: "MEOW!"

# REDEFINICIÓN DE LAS CLASES PARA MOSTRAR POLIMORFISMO EN FUNCIONES
class Animal1:
    """FUNCIONES CON POLIMORFISMO"""
    def hablar(self):
        print("SOY UN ANIMAL")  # MÉTODO BASE

class Perro1(Animal1):
    def hablar(self):
        print("WOOF!")  # MÉTODO PERRO

class Gato1(Animal1):
    def hablar(self):
        print("MEOW!")  # MÉTODO GATO

# CREACIÓN DE OBJETOS
animal = Animal1()
perro = Perro1()
gato = Gato1()

# FUNCIÓN QUE DEMUESTRA POLIMORFISMO
def dar_voz(objeto):
    objeto.hablar()  # LLAMA AL MÉTODO hablar() DEL OBJETO PASADO

# LLAMADAS A LA FUNCIÓN CON DISTINTOS OBJETOS
dar_voz(animal)  # IMPRIME: "SOY UN ANIMAL"
dar_voz(perro)   # IMPRIME: "WOOF!"
dar_voz(gato)    # IMPRIME: "MEOW!"

# FUNCIÓN QUE MULTIPLICA 4 PARÁMETROS
def multiplicacion1(a, b, c, d):
    print(a * b * c * d)  # MULTIPLICA TODOS LOS PARÁMETROS Y MUESTRA EL RESULTADO

# LLAMADA A LA FUNCIÓN CON 4 VALORES
multiplicacion1(10, 2, 3, 6)  # IMPRIME: 360

# FUNCIÓN QUE MULTIPLICA 2 PARÁMETROS
def multiplicacion(a, b):
    print(a * b)  # MULTIPLICA 2 PARÁMETROS

# LLAMADA A LA FUNCIÓN CON 2 VALORES
multiplicacion(5, 7)  # IMPRIME: 35

# BUCLE QUE RECORRE UN RANGO DE 0 A 2
for i in range(3):
    print(i)  # IMPRIME: 0, 1, 2 EN LÍNEAS SEPARADAS+++++++++++++++++++++++++