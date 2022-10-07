#1
if __name__ == '__main__':
    funcion = int(input("elige un num del 1 al 4:   "))

    if funcion == 1:   
        try:
            numero = 7/0
        except ZeroDivisionError:
            print("no se puede dividir entre 0")

    elif funcion == 2:
        try:
            lista = [4, 7, 30, 23, 5]

            lista[10]
        except IndexError:
            print("la lista no es tan larga")

    elif funcion == 3:
        try:

            paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 

            paises["alemania"]

        except KeyError:
            print("alemania no esta en el diccionario")

    elif funcion == 4:
        try:
            resulltado = "2" + 10
        except:
            print("son valores de tipos distintos")
            pass

        
