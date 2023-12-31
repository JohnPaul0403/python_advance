tipos = ["momia", "vampiro", "zombi"]

class Enemigo():
    def __init__(self, height, tipo, ataque, energia, fuerza) -> None:
        self._height = height
        self._tipo = tipo
        self._ataque = ataque
        self._energia = energia
        self._fuerza = fuerza

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, nombre):
        if type(nombre) == str:
            self._height = nombre
        else:
            self._height = None
    
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, nombre):
        if type(nombre) == str:
            self._tipo = nombre
        else:
            self._tipo = None

    @property
    def ataque(self):
        return self._ataque

    @ataque.setter
    def ataque(self, nombre):
        if type(nombre) == str:
            self._ataque = nombre
        else:
            self._ataque = None

    @property
    def energia(self):
        return self._energia

    @energia.setter
    def energia(self, nombre):
        if type(nombre) == str:
            self._energia = nombre
        else:
            self._energia = None

    @property
    def fuerza(self):
        return self._fuerza

    @fuerza.setter
    def fuerza(self, nombre):
        if type(nombre) == str:
            self._fuerza = nombre
        else:
            self._fuerza = None

    def atacar(self):
        print(f"{self._tipo} esta atacando con {self._ataque}")

    def __str__(self) -> str:
        return f"El enemigo de tipo {self._tipo}, tiene una fueza de {self._fuerza}/ 1000."

class Momia(Enemigo):
    def __init__(self) -> None:
        super().__init__("5' 11", "Momia", "enrrapar con papel", "100", "340")

class Zombi(Enemigo):
    def __init__(self) -> None:
        super().__init__("5' 2", "Zombi", "mordedura", "145", "520")

class Vampiro(Enemigo):
    def __init__(self) -> None:
        super().__init__("7' 2", "Vampiro", "chupar sanngre", "200", "830")
        self._recuperacion = 100

    def atacar(self):
        super().atacar()
        print(f'{self._tipo}, recupero {self._recuperacion} de energia')
