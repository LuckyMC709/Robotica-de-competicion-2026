class Estudiante:
    def __init__(self, nombre, nota, asistencia):
        self.nombre = nombre
        self.nota = nota
        self.asistencia = asistencia

    def estudiar(self):
        self.nota += 1

    def rendir(self):
        self.nota -= 1

    def mostrar_estado(self):
        if self.nota >= 4:
            print(self.nombre, "aprueba")
        else:
            print(self.nombre, "desaprueba")


est1 = Estudiante("ana", 6, 80)
est2 = Estudiante("luiss", 3, 60)

est1.mostrar_estado()
est2.mostrar_estado()

est1.estudiar()
est2.rendir()

est1.mostrar_estado()
est2.mostrar_estado()