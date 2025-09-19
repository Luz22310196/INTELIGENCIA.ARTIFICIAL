# DEFINO UNA CLASE CON CONSTRUCTOR
class Ninja:
    def __init__(self, hp, resistencia, xp, vidas=1, salto=None):  # CORREGIDO: None EN MAYÚSCULA
        # HP, RESISTENCIA, XP Y VIDAS SON ATRIBUTOS DEL OBJETO
        self.hp = hp
        self.resistencia = resistencia
        self.xp = xp
        self.vidas = vidas  # ESTE ATRIBUTO TIENE VALOR POR DEFECTO SI NO SE PASA
        self.salto = salto  # SE AÑADE EL ATRIBUTO SALTO, OPCIONAL

    # MÉTODO PARA MOSTRAR MENSAJE DE GAME OVER
    def game_over(self):
        print("GAME OVER")

# CREO OBJETO CON TODOS LOS PARÁMETROS (SALTO LO DEJO COMO None)
ninja_principal = Ninja(100, 50, 1, 3)
print("PRINCIPAL:", ninja_principal.hp, ninja_principal.resistencia, ninja_principal.xp, ninja_principal.vidas)

# CREO OTRO OBJETO USANDO EL VALOR POR DEFECTO PARA 'VIDAS'
ninja_enemigo = Ninja(25, 10, 2)  # NO DOY 'VIDAS', TOMA EL VALOR POR DEFECTO = 1
print("ENEMIGO:", ninja_enemigo.hp, ninja_enemigo.resistencia, ninja_enemigo.xp, ninja_enemigo.vidas)

# AGREGO O MODIFICO EL ATRIBUTO SALTO EN ninja_principal
ninja_principal.salto = True
print("NINJA PRINCIPAL SALTO:", ninja_principal.salto)

# EL ATRIBUTO SALTO TAMBIÉN EXISTE EN ninja_enemigo, PERO VALE None
print("NINJA ENEMIGO SALTO:", ninja_enemigo.salto)
