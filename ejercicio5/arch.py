from classes.classes import Vehiculo, Coche


#creamos algunos vehiculos
helicoptero = Vehiculo("rojo", 0)
rayoMcQueen = Coche("rojo", 4, 200, 3)

lista = []
lista.append(helicoptero)
lista.append(rayoMcQueen)

#funcion catalogar inicial
def catalogar(l, ruedas):
    contador = 0
    for i in range(len(l)):
        if ruedas == l[i].ruedas:
            contador = contador + 1
            print("{}, {}".format(l[i].get_clase(),l[i]))
    print("Se han encontrado {} vehiculos con {} ruedas".format(contador, ruedas))



catalogar(lista, 4)






