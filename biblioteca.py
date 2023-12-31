import libros
import json
import os
import pathlib

class Biblioteca:
    def __init__(self) -> None:
        self._libros = []
        self.recuperar_libros("libros.json")

    def __del__(self):
        self.almacenar_libros('libros.json')

    @property
    def libros(self):
        return self._libros

    @libros.setter
    def libros(self, valor):
        self._libros = valor

    def recuperar_libros(self, ruta):
        if pathlib.Path(ruta).exists():
            with open(ruta, 'r') as archivo:
                dta = json.load(archivo)

            for lib in dta['libros']:
                self.libros.append(libros.libro_decoder(lib))

    def almacenar_libros(self, ruta):
        with open(ruta, 'w') as archivo:
            json.dump({'libros' : self._libros}, archivo, cls=libros.Libro_Enconder, indent=4)

    def agregar_libro(self):
        os.system("clear")
        isbn = input("Introduce el codigo isbn del libro: ")
        titulo = input("Introduce el titulo del libro: ")
        autor = input("Intriduce el nombre del autor: ")
        self.libros.append(libros.Libro(isbn, titulo, autor))
        input("Libro agregado! ")

    def consultar_libros(self):
        os.system('clear')
        if len(self.libros) == 0:
            print("No hay libro")
        else:
            for lib in self.libros:
                print(f'{lib}')
                print("-" * 20)

    def menu(self):
        while True:
            os.system('clear')
            print('''       Biblioteca
            
1. Agregar libro
2. Consultar libros
0. Salir''')
            opc = input()
            try:
                opc = int(opc)

            except:
                opc = -1

            if opc == 1:
                self.agregar_libro()

            elif opc == 2:
                self.consultar_libros()

            elif opc == 0:
                print('Nos vemos!')
                break

            else:
                print("Opcion incorrrecta")

            input("Presiona enter para continuar...")

