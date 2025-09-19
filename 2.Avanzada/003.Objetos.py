# SE DECLARA LA CLASE VEHICULO
class Vehiculo():
    # ATRIBUTOS DE LA CLASE
    color = None              # COLOR DEL VEHÍCULO (SIN VALOR INICIAL)
    longitud_metros = None    # LONGITUD DEL VEHÍCULO EN METROS (SIN VALOR INICIAL)
    ruedas = 4                # NÚMERO DE RUEDAS (VALOR POR DEFECTO: 4)
    velocidad_maxima = None 

    # MÉTODO PARA ARRANCAR EL VEHÍCULO
    def arrancar(self):
        print("El motor ha arrancado.")  # IMPRIME MENSAJE DE ARRANQUE

    # MÉTODO PARA DETENER EL VEHÍCULO
    def detener(self):
        print("El motor está detenido.")  # IMPRIME MENSAJE DE DETENCIÓN

# SE CREAN DOS OBJETOS DE LA CLASE VEHICULO
objeto_vehiculo_1 = Vehiculo()  # OBJETO 1
objeto_vehiculo_2 = Vehiculo()  # OBJETO 2

# SE IMPRIMEN LAS REFERENCIAS DE LOS OBJETOS
#print(objeto_vehiculo_1)  # MUESTRA LA DIRECCIÓN DE MEMORIA DEL OBJETO 1
#print(objeto_vehiculo_2)  # MUESTRA LA DIRECCIÓN
print(objeto_vehiculo_1.ruedas) #IMPRIME EL VALOR DEL ATRIBUTO DENTRO DE LA CLASE

ruedas_vehiculo = objeto_vehiculo_1.ruedas #PARA ALMACENARLO FUERA DE EL ATRIBUTO

#SE ASIGNA UN VALOR (COLOR) A CADA ATRIBUTO
objeto_vehiculo_1.color = "Negro"
objeto_vehiculo_2.color = "Azul"

# COMPROBAMOS CAMBIOS REALIZADOS
print(objeto_vehiculo_1.color)
print(objeto_vehiculo_2.color)

#SE PUEDEN CREAR OBJETOS QUE NO SEAN PARTE DE LA CLASE
objeto_vehiculo_1 = Vehiculo()

#REASIGNAMOS EL VALOR DE EL ATRIBUTO
objeto_vehiculo_1.velocidad_maxima = 161

print(objeto_vehiculo_1.velocidad_maxima)

#SE LLAMA AL METODO DENTRO DE LA CLASE
objeto_vehiculo_1.arrancar()