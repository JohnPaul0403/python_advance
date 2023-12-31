#Clase prenda para el script

class Prenda:

    def __init__(self) -> None:
        self._talla = ''
        self._color = ''
        self._capucha = False

    @property
    def talla(self):
        return self._talla

    @talla.setter
    def talla(self, talla):
        tallas = ['xs', 's', 'm', 'l', 'xl']
        for size in tallas:
            if talla.lower() == size:
                self._talla = talla.upper()

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def capucha(self):
        return self._capucha

    @capucha.setter
    def capucha(self, val):
        if type(val) == bool:
            self._capucha = val

    def __str__(self) -> str:
        return f'''Talla: {self.talla}
Color: {self.color}
{print("Si lleva capucha") if self._capucha else print("No lleva capucha")}
'''
