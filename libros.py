import json
from typing import Any


class Libro:
    def __init__(self, isbn, titulo, autor) -> None:
        self._isbn = isbn
        self._titulo = titulo
        self._autor = autor

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, isbn):
        self._isbn = isbn

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, isbn):
        self._titulo = isbn

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, isbn):
        self._autor = isbn

    def __str__(self) -> str:
        return f'''Titulo: {self._titulo}
Autor: {self._autor}
isbn: {self._isbn}'''

class Libro_Enconder(json.JSONEncoder):
    def default(self, obj) -> Any:
        if isinstance(obj, Libro):
            return {"isbn" : obj.isbn, "Titulo" : obj.titulo, "Autor" : obj.autor}

        return json.JSONEncoder.default(self, obj)

def libro_decoder(dicc):
    return Libro(dicc["isbn"], dicc["Titulo"], dicc['Autor'])
