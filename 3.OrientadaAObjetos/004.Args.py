# DEFINO UNA CLASE CON CONSTRUCTOR QUE ACEPTA *args
class Usuario:
    tipo_usuario = "Free"  # ATRIBUTO DE CLASE

    def __init__(self, nid, alias, nombre, apellidos, *args):
        # ATRIBUTOS DE INSTANCIA
        self.nid = nid
        self.alias = alias
        self.nombre = nombre
        self.apellidos = apellidos
        self.args = args  # ALMACENA LOS ARGUMENTOS ADICIONALES

# CREO UN OBJETO DE LA CLASE Usuario
usuario1 = Usuario("001", "PdePython", "Paula", "Bravo Rojas", "Persona estudiosa", "Amante del lenguaje de programación Python", "27")

# IMPRIMO LOS VALORES DE LOS ATRIBUTOS
print(usuario1.nid)  # MUESTRA EL NID
print(usuario1.args)  # MUESTRA LOS ARGUMENTOS ADICIONALES
