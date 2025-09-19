"""
MÓDULO DOCUMENTACIÓN_EJEMPLO.PY

ESTE MÓDULO DEMUESTRA CÓMO USAR DOCSTRINGS, COMENTARIOS Y LA FUNCIÓN HELP()
PARA DOCUMENTAR CÓDIGO EN PYTHON COMO SE VE EN LA LECCIÓN.
"""

# FUNCIÓN CON DOCSTRING PARA DOCUMENTAR QUÉ HACE, SUS PARÁMETROS Y LO QUE RETORNA
def saludar(nombre):
    """
    SALUDAR: IMPRIME UN MENSAJE DE SALUDO PERSONALIZADO.

    :param nombre: UN STRING CON EL NOMBRE DE LA PERSONA A SALUDAR
    :return: NINGUNO, SOLO IMPRIME POR PANTALLA
    """
    print(f"Hola, {nombre}! Bienvenido/a.")

# OTRA FUNCIÓN CON DOCSTRING Y VALIDACIÓN DE TIPO
def calcular_promedio(numeros):
    """
    CALCULAR_PROMEDIO: RECIBE UNA LISTA DE NÚMEROS Y DEVUELVE SU PROMEDIO.

    :param numeros: LISTA DE INT O FLOATS
    :return: FLOAT QUE ES EL PROMEDIO DE LOS NÚMEROS
    :raises ValueError: SI 'numeros' NO ES LISTA O ESTÁ VACÍA
    """
    if not isinstance(numeros, list):
        raise ValueError("SE ESPERA UNA LISTA DE NÚMEROS.")
    if len(numeros) == 0:
        raise ValueError("LA LISTA NO PUEDE ESTAR VACÍA.")
    total = sum(numeros)
    return total / len(numeros)

# BLOQUE PRINCIPAL PARA PROBAR LAS FUNCIONES
if __name__ == "__main__":
    # PRUEBA DE SALUDAR
    saludar("Ana")

    # PRUEBA DE CALCULAR PROMEDIO CON DATOS CORRECTOS
    lista = [10, 20, 30, 40]
    print("PROMEDIO:", calcular_promedio(lista))

    # PRUEBA DE CALCULAR PROMEDIO CON DATOS INCORRECTOS PARA VER DOCUMENTACIÓN Y ERROR
    try:
        calcular_promedio("no es lista")
    except ValueError as e:
        print("ERROR DETECTADO:", e)

    # USO DE HELP PARA VER LA DOCUMENTACIÓN DE LA FUNCIÓN
    help(calcular_promedio)
    help(saludar)
