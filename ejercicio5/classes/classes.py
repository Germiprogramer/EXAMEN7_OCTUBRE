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