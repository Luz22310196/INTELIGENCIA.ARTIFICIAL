# EJERCICIO 1: ¿POR QUÉ NECESITAMOS LISTAS?
def uso_listas():
    lista = ["manzana", "banana", "cereza", "durazno", "uva"]
    print("Lista de frutas:", lista)  # SE MUESTRA LA LISTA DE FRUTAS
    print("Tercer elemento:", lista[2])  # SE MUESTRA EL TERCER ELEMENTO DE LA LISTA

# EJERCICIO 2: INDEXACIÓN DE LISTAS
def indexacion_listas():
    numeros = [10, 20, 30, 40, 50]
    print("Primer elemento:", numeros[0])  # SE MUESTRA EL PRIMER ELEMENTO DE LA LISTA
    print("Último elemento:", numeros[-1])  # SE MUESTRA EL ÚLTIMO ELEMENTO DE LA LISTA
    print("Penúltimo elemento:", numeros[-2])  # SE MUESTRA EL PENÚLTIMO ELEMENTO DE LA LISTA

# EJERCICIO 3: ACCESO Y MODIFICACIÓN DE LISTAS
def modificar_listas():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    dias[2] = "Día especial"  # MODIFICAMOS EL TERCER ELEMENTO DE LA LISTA
    dias.remove("Sábado")  # REMOVEMOS "SÁBADO" DE LA LISTA
    print("Lista de días modificada:", dias)  # SE MUESTRA LA LISTA MODIFICADA

# EJERCICIO 4: AGREGANDO ELEMENTOS A UNA LISTA
def agregar_elementos():
    colores = []  # CREAMOS UNA LISTA VACÍA
    colores.append("Rojo")  # AGREGAMOS "Rojo" AL FINAL DE LA LISTA
    colores.append("Azul")  # AGREGAMOS "Azul" AL FINAL DE LA LISTA
    colores.append("Verde")  # AGREGAMOS "Verde" AL FINAL DE LA LISTA
    colores.insert(0, "Negro")  # AGREGAMOS "Negro" AL PRINCIPIO DE LA LISTA
    print("Lista de colores:", colores)  # SE MUESTRA LA LISTA DE COLORES

# EJERCICIO 5: FUNCIONES VS MÉTODOS
def funciones_vs_metodos():
    numeros = [4, 8, 1, 6, 9]
    print("Longitud de la lista:", len(numeros))  # SE MUESTRA LA LONGITUD DE LA LISTA
    print("Suma de elementos:", sum(numeros))  # SE MUESTRA LA SUMA DE LOS ELEMENTOS
    print("Valor máximo:", max(numeros))  # SE MUESTRA EL VALOR MÁXIMO EN LA LISTA
    print("Valor mínimo:", min(numeros))  # SE MUESTRA EL VALOR MÍNIMO EN LA LISTA
    numeros.sort()  # ORDENAMOS LA LISTA DE MENOR A MAYOR
    print("Lista ordenada:", numeros)  # SE MUESTRA LA LISTA ORDENADA
    numeros.reverse()  # INVERTIMOS EL ORDEN DE LA LISTA
    print("Lista invertida:", numeros)  # SE MUESTRA LA LISTA INVERTIDA

# EJERCICIO 6: APLICACIÓN PRÁCTICA
def lista_usuarios():
    nombres = [input("Ingresa un nombre: ") for _ in range(5)]  # SOLICITAMOS 5 NOMBRES DEL USUARIO
    print("Lista original:", nombres)  # SE MUESTRA LA LISTA ORIGINAL DE NOMBRES
    nombres.sort()  # ORDENAMOS LA LISTA ALFABÉTICAMENTE
    print("Lista ordenada:", nombres)  # SE MUESTRA LA LISTA ORDENADA
    nuevo_nombre = input("Ingresa un nuevo nombre: ")  # SOLICITAMOS UN NUEVO NOMBRE
    nombres.append(nuevo_nombre)  # AGREGAMOS EL NUEVO NOMBRE A LA LISTA
    print("Lista con nuevo nombre:", nombres)  # SE MUESTRA LA LISTA CON EL NUEVO NOMBRE
    del nombres[1]  # ELIMINAMOS EL SEGUNDO NOMBRE DE LA LISTA
    print("Lista después de eliminar el segundo nombre:", nombres)  # SE MUESTRA LA LISTA DESPUÉS DE LA ELIMINACIÓN

# EJECUTAR LOS EJERCICIOS
if __name__ == "__main__":  # COMPROBAMOS SI ESTE ES EL PROGRAMA PRINCIPAL
    print("--- Uso de Listas ---")
    uso_listas()  # EJECUTAMOS EL EJERCICIO DE USO DE LISTAS
    
    print("\n--- Indexación de Listas ---")
    indexacion_listas()  # EJECUTAMOS EL EJERCICIO DE INDEXACIÓN DE LISTAS
    
    print("\n--- Modificación de Listas ---")
    modificar_listas()  # EJECUTAMOS EL EJERCICIO DE MODIFICACIÓN DE LISTAS
    
    print("\n--- Agregar Elementos ---")
    agregar_elementos()  # EJECUTAMOS EL EJERCICIO DE AGREGAR ELEMENTOS A UNA LISTA
    
    print("\n--- Funciones vs Métodos ---")
    funciones_vs_metodos()  # EJECUTAMOS EL EJERCICIO DE FUNCIONES VS MÉTODOS
    
    print("\n--- Lista de Usuarios ---")
    lista_usuarios()  # EJECUTAMOS EL EJERCICIO DE LISTA DE USUARIOS
