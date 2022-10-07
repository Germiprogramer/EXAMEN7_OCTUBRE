#1
if __name__ == '__main__':
    funcion = int(input("elige un num del 1 al 4:   "))

    if funcion == 1:   
        try:
            numero = 7/0
        except ZeroDivisionError:
            print("ZeroDivisionError")

    elif funcion == 2:
        try:
            lista = [4, 7, 30, 23, 5]

            lista[10]
        except IndexError:
            print

    elif funcion == 3:
        try:

            paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 

            paises["alemania"]
        