class Pelicula:
    def __init__(self, titulo, anio, duracion) -> None:
        self._titulo = titulo
        self._anio = anio
        self._duracion = duracion

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, nombre):
        if type(nombre) == str:
            self._titulo = nombre
        else:
            self._titulo = None

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, nombre):
        if type(nombre) == int:
            self._anio = nombre
        else:
            self._anio = None

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, nombre):
        if type(nombre) == int:
            self._duracion = nombre
        else:
            self._duracion = None

    def __str__(self) -> str:
        return f'''Titulo: {self._titulo}
Anio: {self._anio}
Duracion: {self._duracion} mins'''

    def __lt__(self, other):
        return self._titulo < other._titulo 
