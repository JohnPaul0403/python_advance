#Como crear e implementar objetos

class Figura:
    def __init__(self) -> None:
        self._lados = None

    @property
    def lados(self) -> any:
        return self._lados

    @lados.setter
    def lados(self, num) -> None:
        if num <= 2:
            self._lados = None
        else:
            self._lados = num

    @lados.deleter
    def lados(self) -> None:
        del self._lados

def main():
    cuadrado = Figura()
    triangulo = Figura()
    cuadrado.lados = 4
    triangulo.lados = 3
    del cuadrado.lados #Borra el atributo

    print(f'El Cuadrado tiene {cuadrado.lados} lados')
    print(f'El triangulo tiene {triangulo.lados} lados')

main()
