import c

class UsuariosPremiumPlus(c.UsuariosPremium):
    participacion_sorteos = 25

    def muestra_datos(self):
        super().muestra_datos()
        print("El tipo de usuario es: ", c.UsuariosPremium.tipo_usuario)