# AQUÍ VAMOS A HACER ALGUNAS OPERACIONES BÁSICAS

# SUMA
suma = 8 + 5  # SUMAMOS 8 Y 5
print("Suma de 8 + 5:", suma)

# RESTA
resta = 10 - 4  # RESTAMOS 10 MENOS 4
print("Resta de 10 - 4:", resta)

# MULTIPLICACIÓN
multiplicacion = 7 * 6  # MULTIPLICAMOS 7 POR 6
print("Multiplicación de 7 * 6:", multiplicacion)

# DIVISIÓN
division = 20 / 4  # DIVIDIMOS 20 ENTRE 4
print("División de 20 / 4:", division)

# DIVISIÓN ENTERA (CUANDO SOLO QUIERO EL NÚMERO ENTERO SIN DECIMALES)
division_entera = 20 // 3  # DIVISIÓN ENTERA DE 20 ENTRE 3
print("División entera de 20 // 3:", division_entera)

# MÓDULO (RESTO DE LA DIVISIÓN)
modulo = 20 % 3  # OBTENEMOS EL RESTO DE LA DIVISIÓN DE 20 ENTRE 3
print("Módulo de 20 % 3:", modulo)

# POTENCIA (ES COMO HACER EXPONENTE)
potencia = 2 ** 3  # ELEVAMOS 2 A LA POTENCIA DE 3
print("Potencia de 2 ** 3:", potencia)

# PARTE 2: OPERADORES BÁSICOS
# USAMOS DOS NÚMEROS, A Y B, PARA PRACTICAR CON OPERACIONES
a = 15
b = 4

# SUMA
resultado_suma = a + b  # SUMAMOS A Y B

# RESTA
resultado_resta = a - b  # RESTAMOS B DE A

# MULTIPLICACIÓN
resultado_multiplicacion = a * b  # MULTIPLICAMOS A POR B

# DIVISIÓN
resultado_division = a / b  # DIVIDIMOS A ENTRE B

# POTENCIA
resultado_potencia = a ** b  # ELEVAMOS A A LA POTENCIA DE B

# MÓDULO
resultado_modulo = a % b  # OBTENEMOS EL RESTO DE LA DIVISIÓN DE A ENTRE B

# IMPRIMIR LOS RESULTADOS
print("\nResultados prácticos:")
print(f"{a} + {b} = {resultado_suma}")  # IMPRIME EL RESULTADO DE LA SUMA
print(f"{a} - {b} = {resultado_resta}")  # IMPRIME EL RESULTADO DE LA RESTA
print(f"{a} * {b} = {resultado_multiplicacion}")  # IMPRIME EL RESULTADO DE LA MULTIPLICACIÓN
print(f"{a} / {b} = {resultado_division}")  # IMPRIME EL RESULTADO DE LA DIVISIÓN
print(f"{a} ** {b} = {resultado_potencia}")  # IMPRIME EL RESULTADO DE LA POTENCIA
print(f"{a} % {b} = {resultado_modulo}")  # IMPRIME EL RESULTADO DEL MÓDULO

# PARTE 3: OPERADORES Y SUS PRIORIDADES
# EN PYTHON, LAS MULTIPLICACIONES Y DIVISIONES TIENEN MÁS PRIORIDAD QUE LAS SUMAS Y RESTAS

# AQUÍ, PYTHON VA A HACER PRIMERO LA MULTIPLICACIÓN
resultado_prioridad = 2 + 3 * 4  # PRIMERO HACE 3 * 4 Y DESPUÉS SUMA 2
print("\nResultado con prioridades de operadores (2 + 3 * 4):", resultado_prioridad)

# SI QUIERO CAMBIAR EL ORDEN DE LAS OPERACIONES, USO PARÉNTESIS
resultado_con_parentesis = (2 + 3) * 4  # PRIMERO HACE 2 + 3 Y DESPUÉS MULTIPLICA POR 4
print("Resultado con paréntesis (2 + 3) * 4:", resultado_con_parentesis)

# OTRA OPERACIÓN CON DIFERENTES OPERADORES
resultado_complejo = (5 + 3) * 2 ** 3 / 4  # PYTHON HACE LA POTENCIA ANTES QUE LA MULTIPLICACIÓN Y DIVISIÓN
print("Resultado de (5 + 3) * 2 ** 3 / 4:", resultado_complejo)

# OPERADORES LÓGICOS: ESTOS ME SIRVEN PARA HACER COMPARACIONES (TRUE/FALSE)
# POR EJEMPLO, AND, OR, NOT
condicion1 = True
condicion2 = False
and_result = condicion1 and condicion2  # AND, SÓLO ES TRUE SI AMBOS SON TRUE
or_result = condicion1 or condicion2  # OR, ES TRUE SI AL MENOS UNO ES TRUE
not_result = not condicion1  # NOT, INVIERTE EL VALOR DE TRUE A FALSE

print("\nOperadores lógicos:")
print(f"condicion1 and condicion2: {and_result}")  # IMPRIME EL RESULTADO DEL AND
print(f"condicion1 or condicion2: {or_result}")  # IMPRIME EL RESULTADO DEL OR
print(f"not condicion1: {not_result}")  # IMPRIME EL RESULTADO DEL NOT
