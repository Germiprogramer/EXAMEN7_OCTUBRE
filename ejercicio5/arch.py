from classes.classes import Vehiculo, Coche, Bicicleta, Camioneta, Motocicleta


#creamos algunos vehiculos
helicoptero = Vehiculo("rojo", 0)
rayoMcQueen = Coche("rojo", 4, 200, 3)
mate = Camioneta("marron", 4, 3, 10000000, 10000000)
bilbo_bici = Bicicleta("rojo", 2, "urbana")
motillo = Motocicleta("negro", 2, "deportiva", "mucha", 5)


lista = []
lista.append(helicoptero)
lista.append(rayoMcQueen)
lista.append(mate)
lista.append(bilbo_bici)
lista.append(motillo)

#funcion catalogar inicial
def catalogar(l, ruedas):
    contador = 0
    for i in range(len(l)):
        if ruedas == l[i].ruedas:
            contador = contador + 1
            print("{}, {}".format(l[i].get_clase(),l[i]))
    print("Se han encontrado {} vehiculos con {} ruedas".format(contador, ruedas))







