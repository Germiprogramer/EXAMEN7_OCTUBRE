from classes.alumno import Alumno

if __name__ == '__main__':
    #creacion alumnos
    carlos = Alumno("Carlos", 10)
    german = Alumno("Germi", 0)

    #nota
    print(carlos.calificacion)
    #ejecucion str
    print(carlos)