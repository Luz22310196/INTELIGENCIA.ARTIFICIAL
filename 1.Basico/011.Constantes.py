class Constantes:
    _PI = 3.14159

    @property
    def PI(self):
        return self._PI

    @PI.setter
    def PI(self, value):
        raise ValueError("No se puede modificar PI.")

# Intentar cambiar el valor de PI lanzará un error
const = Constantes()
print(const.PI)
# const.PI = 3.14  # Esto lanzará un ValueError
