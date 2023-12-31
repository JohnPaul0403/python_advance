#Implementacion del polimorfismo
import enemigo
import os
import random

def main() -> any:
    enemigos = []
    for i in range(5):
        n = random.randint(0, len(enemigo.tipos))-1
        if 0 == n:
            enemigos.append(enemigo.Momia())
        elif 1 == n:
            enemigos.append(enemigo.Zombi())
        else:
            enemigos.append(enemigo.Vampiro())

    personaje = {'energia' : 100, 'fuerza' : 6}
    gan_ener = 5
    gan_fuerza = 4

    while personaje['energia'] > 0 and len(enemigos) > 0:
        while personaje['energia'] > 0 and enemigos[0].energia > 0:
            pass



main()