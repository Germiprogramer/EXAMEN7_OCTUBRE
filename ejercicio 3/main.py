from classes.producto import Producto

if __name__ == '__main__':
    leche = Producto("1324","leche", 2, "alimento")
    #modificamos el precio de la leche
    leche.precio = 3

    print(leche)
