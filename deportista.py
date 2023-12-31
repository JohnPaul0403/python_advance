# Hereda de persona

import persona


class Deportista(persona.Persona):
    def __init__(self, nombre='', edad=None, deporte='') -> None:
        super().__init__(nombre, edad)
        self._deporte = deporte

    @property
    def deporte(self) -> any:
        return self._deporte

    @deporte.setter
    def deporte(self, deporte_x):
        self._deporte = deporte_x

    def entrenar(self):
        print(f'{self.nombre} Esta entrenando {self._deporte}')

    def __str__(self):
        return f'{super().__str__()} y tambien practica {self._deporte}'
