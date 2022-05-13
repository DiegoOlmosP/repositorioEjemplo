from pip import main


class Alumno(object):


    def __init__(self, nombre,nota ) -> None:
        self.nombre = nombre
        self.nota = nota
    
    def __str__(self) -> str:
        if self.nota >= 5:
            text = "aprobado"
        else:
            text = "suspenso"
        return f"El alumno {self.nombre} tiene de nota un {self.nota} por lo tanto está {text}."


if __name__ == "__main__":
    alumnos=[]
    while 1:
       try:
           nombre = input("Introduce un nombre: ")
           nota = int(input(f"Introduce la nota de {nombre}: "))
           alumnos.append(Alumno(nombre, nota))
           print("Intro para añadir un alumno \n pulsa F para ver todo")
           if (input()=="F"):
               break

       except:
           print("Nombre o nota no válido")

    for alumno in alumnos:
        print(alumno.__str__())