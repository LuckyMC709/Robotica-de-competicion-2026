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


# Crear objetos (estudiantes)
est1 = Estudiante("Ana", 6, 80)
est2 = Estudiante("Luis", 3, 60)

# Mostrar estado inicial
est1.mostrar_estado()
est2.mostrar_estado()

# Acciones
est1.estudiar()
est2.rendir()

# Mostrar estado final
est1.mostrar_estado()
est2.mostrar_estado()