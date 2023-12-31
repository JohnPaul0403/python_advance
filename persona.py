#Clase persona, las cosas que todas las personas tenemos en comun

class Persona:

    def __init__(self, nombre='', edad=None) -> None:
        self._nombre = nombre
        self._edad = edad

    def hablar(self, mensaje):
        print(mensaje)

    def comer(self, comida, lista_alimentos):
        for i in lista_alimentos:
            if i == comida:
                print("Entra en la dieta y fue comido")

    def __str__(self):
        return f"{self._nombre}, tiene una edad de {self._edad}"

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
