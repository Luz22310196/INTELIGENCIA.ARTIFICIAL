class Usuario:
    """DEFINICIÓN DE LA CLASE USUARIO"""
    def __init__(self, user_id, nombre, apellidos):
        self.user_id = user_id                    # ATRIBUTO PÚBLICO
        self.nombre = nombre            # ATRIBUTO PÚBLICO
        self.__apellidos = apellidos    # ATRIBUTO PRIVADO

    # MÉTODO PÚBLICO PARA MOSTRAR EL APELLIDO
    def muestra_apellidos(self):
        print(f"LOS APELLIDOS SON: {self.__apellidos}.")

# CREACIÓN DEL OBJETO USUARIO
usuario_1 = Usuario(1, "Enrique", "Barros Fernández")

# LLAMADA AL MÉTODO
usuario_1.muestra_apellidos()

class Persona:
    def __init__(self, nombre, edad, altura_cm):
        self.nombre = nombre
        self.edad = edad
        self.altura_cm = altura_cm

    # Calcula y devuelve la altura en metros
    def __calcular_altura_metros(self):
        return self.altura_cm / 100

    # Método público para mostrar los resultados
    def obtener_altura_metros(self):
        altura_metros = self.__calcular_altura_metros()
        print(f"La altura de {self.nombre} es de {altura_metros} metros.")

# Ejemplo de uso
persona = Persona("Ana", 30, 170)
persona.obtener_altura_metros()
