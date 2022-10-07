import ejercicio12.main as ej12
import ejercicio3.main as ej3
import ejercicio4.main as ej4
import ejercicio5.main as ej5

def iniciar():
    opcion = input("> ")

    if opcion == '1':
           ej12.main()

    elif opcion == '2':
            ej3.main()

    elif opcion == '3':
            ej4.main()

    elif opcion == '4':
            ej5.main()
    else:
        pass
