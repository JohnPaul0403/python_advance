import peliculas as pel
import os

def main():
    os.system("clear")
    peliculas = []
    peliculas.append(pel.Pelicula("Spiderman: No Way Home", 2021, 201))
    peliculas.append(pel.Pelicula("Spiderman: Far From Home", 2019, 201))
    peliculas.append(pel.Pelicula("Spiderman: Homecoming", 2017, 201))
    peliculas.append(pel.Pelicula("Spiderman 1", 2002, 201))

    peliculas.sort()

    for peli in peliculas:
        print(peli)
        print("-"*50)

main()