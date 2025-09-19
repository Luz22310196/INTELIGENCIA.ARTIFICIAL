# DECLARACIÓN DE LA CLASE
class Estudiante():
    """
    CLASE ESTUDIANTE:
    ESTA CLASE DEFINE UNA ESTRUCTURA BÁSICA DE UN ESTUDIANTE
    CON ATRIBUTOS DE CLASE Y MÉTODOS QUE IMPRIMEN MENSAJES.
    """

    # ATRIBUTOS DE CLASE
    universidad = "Universidad Nacional"  # NOMBRE DE LA UNIVERSIDAD
    pais = "México"                       # PAÍS DE PROCEDENCIA
    tipo_estudiante = "Regular"           # TIPO DE ESTUDIANTE

    # MÉTODO 1: IMPRIME INFORMACIÓN GENERAL DEL ESTUDIANTE
    def metodo_1(self):
        """IMPRIME LOS ATRIBUTOS DE CLASE DEL ESTUDIANTE"""
        print(f"Universidad: {Estudiante.universidad}")
        print(f"País: {Estudiante.pais}")
        print(f"Tipo de estudiante: {Estudiante.tipo_estudiante}")

    # MÉTODO 2: IMPRIME MENSAJE DE BIENVENIDA
    def metodo_2(self):
        """IMPRIME UN MENSAJE DE BIENVENIDA AL ESTUDIANTE"""
        print("Bienvenido al sistema de estudiantes")


# CÓDIGO PARA PROBAR LA CLASE

# CREAR OBJETO
est = Estudiante()

# LLAMAR A LOS MÉTODOS
est.metodo_1()
est.metodo_2()

