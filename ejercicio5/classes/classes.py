class Vehiculo():

    def __init__(self, color, ruedas):

        self.color = color

        self.ruedas = ruedas


    def __str__(self):

        return "color {}, {} ruedas".format( self.color, self.ruedas )

    def get_clase(self):
        return "Vehiculo"



class Coche(Vehiculo):

 

    def __init__(self, color, ruedas, velocidad, cilindrada):

        Vehiculo.__init__(self, color, ruedas)

        self.velocidad = velocidad

        self.cilindrada = cilindrada

 

    def __str__(self):

        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)
    
    def get_clase(self):
        return "Coche"

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):

        Coche.__init__(self, color, ruedas, velocidad, cilindrada)

        self.carga = carga

    def __str__(self):

        return Coche.__str__(self) + ", {} kg".format(self.carga)

    def get_clase(self):
        return "Camioneta"

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):

        Vehiculo.__init__(self, color, ruedas)

        self.tipo = tipo

    def __str__(self):

        return Vehiculo.__str__(self) + ", {}".format(self.tipo)
    
    def get_clase(self):
        return "Bicicleta"

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):

        Bicicleta.__init__(self, color, ruedas, tipo)

        self.velocidad = velocidad

        self.cilindrada = cilindrada

    def __str__(self):

        return Bicicleta.__str__(self) + ", {}km/h, {}cc".format(self.velocidad, self.cilindrada)
    
    def get_clase(self):
        return "Motocicleta"
    

    

