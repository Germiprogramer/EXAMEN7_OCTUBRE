class Producto():
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo

        print("creado con exito")

    def __str__(self):
        return f"{self.codigo} {self.nombre} {self.precio} {self.tipo}"