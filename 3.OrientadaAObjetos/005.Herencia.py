class Usuarios:
    tipo_usuario = "Free"
    publicidad = True

    def __init__(self, nid, alias, nombre, apellidos):
        self.nid = nid
        self.alias = alias
        self.nombre = nombre
        self.apellidos = apellidos

    def muestra_datos(self):
        print("El nombre y los apellidos del usuario son: " + self.nombre, self.apellidos)
        print("El ID de usuario es: " + self.nid + ".")
        print("El alias del usuario es: " + self.alias + ".")


class UsuariosPremium:
    tipo_usuario = "Premium"
    publicidad = False

    def __init__(self, nid, alias, nombre, apellidos):
        self.nid = nid
        self.alias = alias
        self.nombre = nombre
        self.apellidos = apellidos

    def muestra_datos(self):
        print("El nombre y los apellidos del usuario son: " + self.nombre, self.apellidos)
        print("El ID de usuario es: " + self.nid + ".")
        print("El alias del usuario es: " + self.alias + ".")

usuario1 = Usuarios("001", "raulito43", "Raúl", "Fernández Gomila")

usuario1.muestra_datos()

print(usuario1.tipo_usuario)

class UsuariosPremium1(Usuarios):
    tipo_usuario = "Premium"
    publicidad = False