import random

class sorteo:
    lista = []

    def randomnum ():
        valmax = int(input("Ingrese el mayor valor de la lista: "))
        valcant = int(input("Ingrese la cantidad de valores que tendra la lista: "))
        lista:sorteo = [random.randint(0,valmax) for b in range(valcant)]
        print(lista)
        print("El numero aleatorio escogido es : ",random.choice(lista))
        
    randomnum()
        


