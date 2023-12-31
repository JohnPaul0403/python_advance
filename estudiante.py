#Clase con atributos de una persona mas los de un estudiante
import persona

class Estudiante(persona.Persona):
    def __init__(self, nombre='', edad=None, promedio = None, cod_estudiante = None) -> None:
        super().__init__(nombre=nombre, edad=edad)
        self._promedio = promedio
        self._cod_estudiante = cod_estudiante


    @property
    def promedio(self) -> any:
        return self._promedio

    @promedio.setter
    def deporte(self, x):
        self._promedio = x

    @property
    def cod_estudiante(self) -> any:
        return self._cod_estudiante

    @cod_estudiante.setter
    def deporte(self, x):
        self._cod_estudiante = x

    def estudiar():
        print("Estudiando")

    def __str__(self) -> str:
        return f"El estudiante {self.nombre}, con el codigo {self.cod_estudiante}, tiene un promedio de {self._promedio}."