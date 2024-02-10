class Alumno:
    def __init__(self, nombre, apellido, dni, domicilio, notas=None, faltas=0, amonestaciones=0):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.domicilio = domicilio
        self.notas = {} if notas is None else notas
        self.faltas = faltas
        self.amonestaciones = amonestaciones

    def agregar_nota(self, materia, nota):
        if materia in self.notas:
            self.notas[materia].append(nota)
        else:
            self.notas[materia] = [nota]

    def asignar_falta(self):
        self.faltas += 1

    def asignar_amonestacion(self):
        self.amonestaciones += 1

    def cambiar_domicilio(self, nuevo_domicilio):
        self.domicilio = nuevo_domicilio

alumnos = [
    Alumno("Juan", "Perez", "12345678", "Calle 123", notas={"Matemáticas": [8, 7, 6]}),
    Alumno("Maria", "Gomez", "23456789", "Avenida 456", notas={"Lengua": [9, 8, 7]}),
    Alumno("Pedro", "Rodriguez", "34567890", "Calle 789", notas={"Historia": [7, 6, 8]}),
    Alumno("Laura", "Diaz", "45678901", "Avenida 012", notas={"Ciencias": [6, 7, 8]}),
]

alumnos[0].agregar_nota("Matemáticas", 9)
alumnos[0].asignar_falta()
alumnos[2].agregar_nota("Historia", 8)
alumnos[2].asignar_amonestacion()

for alumno in alumnos:
    print("Nombre:", alumno.nombre)
    print("Domicilio:", alumno.domicilio)
    print("Notas:", alumno.notas)
    print("Faltas:", alumno.faltas)
    print("Amonestaciones:", alumno.amonestaciones)
    print()
