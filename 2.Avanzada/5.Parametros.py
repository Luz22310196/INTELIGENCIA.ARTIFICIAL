# DEFINICIÓN DE LA CLASE USUARIO
class Usuario:
    # MÉTODO CONSTRUCTOR PARA DEFINIR LOS ATRIBUTOS DE INSTANCIA
    def __init__(self, nombre, apellidos, edad, direccion, telefono):
        self.nombre = nombre        # NOMBRE DEL USUARIO
        self.apellidos = apellidos  # APELLIDOS DEL USUARIO
        self.edad = edad            # EDAD DEL USUARIO
        self.direccion = direccion  # DIRECCIÓN DEL USUARIO
        self.telefono = telefono    # TELÉFONO DEL USUARIO

    # MÉTODO PARA INICIAR SESIÓN
    def iniciar_sesion1(self):
        print(f"El usuario {self.nombre} ha iniciado sesión")  # MENSAJE CON EL NOMBRE

# INSTANCIAS DE LA CLASE USUARIO
usuario_1 = Usuario("Enrique", "Barros Fernández",
                    32, "C/Programación Fácil n.º 34",
                    "123456789")  # PRIMER USUARIO

usuario_2 = Usuario("Adriana", "Barca López",
                    28, "Sin dirección",
                    "987654321")  # SEGUNDO USUARIO

# LLAMADAS A LOS MÉTODOS
usuario_1.iniciar_sesion1()  # EL USUARIO 1 INICIA SESIÓN
usuario_2.iniciar_sesion1()  # EL USUARIO 2 INICIA SESIÓN
