# DEFINICIÓN DE LA CLASE USUARIO
class Usuario:
    # MÉTODO CONSTRUCTOR PARA INICIALIZAR LOS ATRIBUTOS DE INSTANCIA
    def __init__(self, nombre, apellidos, edad, direccion, telefono):
        self.nombre = nombre        # NOMBRE DEL USUARIO
        self.apellidos = apellidos  # APELLIDOS DEL USUARIO
        self.edad = edad            # EDAD DEL USUARIO
        self.direccion = direccion  # DIRECCIÓN DEL USUARIO
        self.telefono = telefono    # TELÉFONO DEL USUARIO

    # MÉTODO PARA INICIAR SESIÓN
    def iniciar_sesion(self):
        print("El usuario ha iniciado sesión")  # MENSAJE DE INICIO DE SESIÓN

    # MÉTODO PARA CERRAR SESIÓN
    def cerrar_sesion(self):
        print("El usuario ha cerrado sesión")  # MENSAJE DE CIERRE DE SESIÓN

    # MÉTODO PARA CAMBIAR EL NOMBRE DEL PERFIL
    def cambiar_nombre_perfil(self):
        print("Se cambió el nombre")  # MENSAJE DE CAMBIO DE NOMBRE

# CREACIÓN DE UN OBJETO USUARIO
usuario_1 = Usuario(
    "Enrique",                      # NOMBRE
    "Barros Fernández",            # APELLIDOS
    32,                            # EDAD
    "C/Programación Fácil n.º 34", # DIRECCIÓN
    "123456789"                    # TELÉFONO
)

# IMPRESIÓN DE TODOS LOS ATRIBUTOS DEL USUARIO
print("NOMBRE:", usuario_1.nombre)
print("APELLIDOS:", usuario_1.apellidos)
print("EDAD:", usuario_1.edad)
print("DIRECCIÓN:", usuario_1.direccion)
print("TELÉFONO:", usuario_1.telefono)



