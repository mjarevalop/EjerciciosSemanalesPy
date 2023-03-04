options="""
    1) Area del circulo
    2) Area del triangulo
    3) Area del cuadrado
"""
print(options)
opt=int(input("ingrese la opcion que desea desarrollar: "))

if type(opt) == int:
    if opt == 1:
        numero = int(input("Ingrese el radio: "))
        print(f"El área del cirulo es {numero*numero}π")
    elif opt == 2:
        base = int(input("Ingrese la base del triangulo: "))
        altura = int(input("Ingrese la altura del triangulo: "))
        print(f"El área del tringulo es {(base*altura)/2}")
    elif opt == 3:
        lado = int(input("Ingrese el lado del cuadrado: "))
        print(f"El área del cuadrado es {lado*lado}")
    else:
        print("Ingrese una opción correcta")    

else:
    print("ingrese un valor entero ,valor no permitido")