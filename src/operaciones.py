#imports de las funciones.
import random


# funcion para tirar un numero x cantidad de veces y devolver la cantidad total de las caras
def tirarDado(dado, cantidadTiros):
    total = 0
    for x in range(cantidadTiros):
        total += random(1, dado)
    return total
