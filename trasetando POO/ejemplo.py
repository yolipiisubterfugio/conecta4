class Persona:
    def __init__(self, nombre, profesion):
        self.nombre = nombre
        self.profesion = profesion

    def presentar(self):
        if self.profesion.upper() == "PROGRAMATA":
            return "UUUH"

        return f"Soy {self.nombre} y mi profesión es {self.profesion}"