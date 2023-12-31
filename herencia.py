# Como implementar la herencia
import deportista
import estudiante
from persona import Persona


def main() -> None:
    bro = Persona("Bro", 20)
    the_rock = deportista.Deportista("The Rock", 45, "Gym dude")
    Peter = estudiante.Estudiante("Peter Parker", 17, 9, "0001202003334")
    print(the_rock)
    print(bro)
    print(Peter)


main()
