#Clases como modulo y la funcion __str__
import prenda

prenda1 = prenda.Prenda()

prenda1.color = "Verde"
prenda1.talla = "Xl"

prenda2 = prenda.Prenda()

prenda2.color = "Negro"
prenda2.talla = "m"
prenda2.capucha = True

print(prenda1)
print(prenda2)
