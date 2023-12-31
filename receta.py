#Clase receta para componer con la clase ingrediente
import ingrediente
import os

class Receta:
    def __init__(self, nombre) -> None:
        self._nombre = nombre
        self._ingredientes = []
        self._pasos = []

    def __str__(self) -> str:
        if len(self._ingredientes) == 0:
            return "Nada agregado"
        else:
            return f'''         {self._nombre}'''

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if type(nombre) == str:
            nombre[0] = nombre[0].upper()
            self._nombre = nombre
        else:
            self._nombre = None

    @property
    def ingredientes(self):
        return self._ingredientes

    @ingredientes.setter
    def ingredientes(self, value):
        if type(value) == list:
            self._ingredientes = value
        else:
            self._ingredientes = []

    @property
    def pasos(self):
        return self._pasos

    @pasos.setter
    def pasos(self, value):
        if type(value) == list:
            self._pasos = value
        else:
            self._pasos = []

    def menu(self):
        continuar = True
        while continuar:
            print(f"""        {self._nombre}
1. Agregar ingrediente
2. Consultar ingredientes
3. Agregar pasos
4. Consultar pasos
0. Salir
""")
            valor = int(input("Selecciona una opcion"))
            if valor == 1:
                self.agregar_ingredientes()
            elif valor == 2:
                self.consultar_ingredientes()
            elif valor == 3:
                self.agregar_pasos()
            elif valor == 4:
                self.consultar_pasos(0)
            elif valor == 0:
                continuar = False
                print("Nos vemos...")
            else:
                print("Valor incorrecto")
            input("Presiona enter para continuar")

    def agregar_ingredientes(self):
        c = True
        while c:
            os.system("clear")
            print("     Agregar ingrediente")
            nombre = input("Nombre")
            cantidad = -1
            while cantidad <= 0:
                cantidad = input("cantidad: ")
                try:
                    cantidad = float(cantidad)
                except:
                    cantidad = -1
            unidad = input("Unidad de medida: ")
            ingredienteX = ingrediente.Ingrediente(nombre, cantidad, unidad)
            self.ingredientes.append(ingredienteX)
            valor  = int(input("Desea continuar, 1. Si, 2. No: "))
            c = False if valor == 2 else True


    def consultar_ingredientes(self):
        os.system("clear")
        print("     Ingredientes")
        if len(self.ingredientes) >=1:
            for i in self.ingredientes:
                print(i)
        else:
            print("No tienes Ingredientes registrados")

    def agregar_pasos(self):
        c = True
        while c:
            os.system("clear")
            paso = input("Agrega el paso: ")
            self._pasos.append(paso)
            valor = input("Desea continuar? (s/n): ")
            c = False if valor == "n" else True

    def consultar_pasos(self):
        os.system("Clear")
        if len(self._pasos) >= 1:
            for i in range(0, len(self._pasos) - 1):
                print (f"{i}. {self._pasos[i]}")
        else:
            print("No tienes pasos a seguir")

