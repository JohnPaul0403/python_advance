class Ingrediente:
    def __init__(self, nombre='', cantidad='', unidad_de_medida='') -> None:
        self.nombre = nombre#Al no poner '_' se fuerza a utilizar el setter
        self.cantidad = cantidad
        self.unidad_de_medida = unidad_de_medida

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if type(nombre) == str:
            self._nombre = nombre
        else:
            self._nombre = None

    def __str__(self) -> str:
        return f'''El ingredinte es: {self.nombre}
Se requiere {self.cantidad}{self.unidad_de_medida}'''