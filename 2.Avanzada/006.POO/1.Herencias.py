# DEFINICIÓN DE LA CLASE BASE "CIUDADANO"
class Ciudadano:
    # MÉTODO CONSTRUCTOR QUE INICIALIZA LOS ATRIBUTOS "NOMBRE" Y "PROFESIÓN"
    def __init__(self, nombre, profesion):
        self.nombre = nombre            # GUARDA EL NOMBRE DEL CIUDADANO
        self.profesion = profesion      # GUARDA LA PROFESIÓN DEL CIUDADANO

    # MÉTODO QUE IMPRIME UN SALUDO PERSONALIZADO
    def saludar(self):
        print(f"Hola, soy {self.nombre}. Mi profesión es {self.profesion}.")
        # MUESTRA EL NOMBRE Y LA PROFESIÓN DEL OBJETO ACTUAL

# CLASE "MEDICO" QUE HEREDA DE "CIUDADANO"
class Medico(Ciudadano):
    # CONSTRUCTOR QUE RECIBE SOLO EL NOMBRE
    def __init__(self, nombre):
        super().__init__(nombre, "médico")  # LLAMA AL CONSTRUCTOR DE LA CLASE BASE Y ASIGNA "médico" COMO PROFESIÓN

# CLASE "POLICIA" QUE TAMBIÉN HEREDA DE "CIUDADANO"
class Policia(Ciudadano):
    # CONSTRUCTOR QUE RECIBE SOLO EL NOMBRE
    def __init__(self, nombre):
        super().__init__(nombre, "policía")  # LLAMA AL CONSTRUCTOR DE LA CLASE BASE Y ASIGNA "policía" COMO PROFESIÓN

# CREACIÓN DE UNA INSTANCIA DE LA CLASE "CIUDADANO"
persona1 = Ciudadano("Julia", "informática")  # CREA UN CIUDADANO CON NOMBRE Y PROFESIÓN PERSONALIZADOS

# CREACIÓN DE UNA INSTANCIA DE LA CLASE "MEDICO"
persona2 = Medico("Raúl")  # CREA UN MÉDICO LLAMADO RAÚL (PROFESIÓN AUTOMÁTICAMENTE DEFINIDA)

# CREACIÓN DE UNA INSTANCIA DE LA CLASE "POLICIA"
persona3 = Policia("Raquel")  # CREA UNA POLICÍA LLAMADA RAQUEL (PROFESIÓN AUTOMÁTICAMENTE DEFINIDA)

# LLAMADAS AL MÉTODO "saludar" DE CADA OBJETO
persona1.saludar()  # SALUDO DE JULIA (CIUDADANO)
persona2.saludar()  # SALUDO DE RAÚL (MÉDICO)
persona3.saludar()  # SALUDO DE RAQUEL (POLICÍA)
