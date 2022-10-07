from classes.classes import Vehiculo, Coche

if __name__ == '__main__':
    #creamos algunos vehiculos
    coche = Vehiculo("rojo", 4)
    rayoMcQueen = Coche("rojo", 4, 200, 3)

    lista = []
    lista.append(coche)
    lista.append(rayoMcQueen)

    def catalogar(l):
        for i in range(len(l)):
            print("{}".format(l[i]))

    catalogar(lista)

    print(coche.get_clase())

