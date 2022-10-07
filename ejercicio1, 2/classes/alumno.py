from mailbox import NoSuchMailboxError


class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("Alumno construido")

    def calificacion(self):
        if self.nota < 5:
            print("{} ha suspendido".format(self.alumno))
            return "suspenso"
        else:
            print("{} ha aprobado".format(self.alumno))
            return "aprobado"
    
    def __str__(self):

        return f"{self.nombre} {self.nota}"




    