# Generar comportamientos a los objetos

class Persona:

    def __init__(self) -> None:
        self._nombre = None
        self._edad = None

    def hablar(self, mensaje):
        print(mensaje)

    def comer(self, comida, lista_alimentos):
        for i in lista_alimentos:
            if i == comida:
                print("Entra en la dieta y fue comido")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if type(nombre) == str:
            self._nombre = nombre
        else:
            self._nombre = None

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        if type(edad) == int:
            if 0 <= edad <= 120:
                self._edad = edad
            else:
                self._edad = None
        else:
            self._edad = None


def main():
    roberto = Persona()
    roberto.nombre = "Roberto Culo abierto"
    roberto.edad = 20
    roberto.hablar("Ola que hace")
    print(roberto.nombre)
    mi_dieta = ["Vodka", "Mas Vodka"]
    roberto.comer("Vodka", mi_dieta)


main()
