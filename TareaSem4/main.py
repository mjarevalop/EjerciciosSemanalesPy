import random
import requests

options="""
    "Tarea semana 4"
    1) Ejercicio 2
    2) Ejercicio 3
    3) Ejercicio 4 
    4) Ejercicio 5
    5) Salir 
    """

while True:
    print(options)
    choose=int(input("Ingrese el numero de ejercicio a realizar: "))

    if choose == 1:
        from Ejercicio2 import sorteo

    elif choose == 2:
        from Ejercicio3 import pokemon
        msg="""
            "Pokemons región Kanto"
            1) Listar pokemons
            2) Buscar pokemon
            3) Salir    
            """
        pokemon()
        pass
    elif choose == 3:
        from Ejercicio4 import Registro
    elif choose == 4:
        from Ejercicio5 import validadrcel
    elif choose == 5:
        print("Adios")
        break