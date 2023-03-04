numero1 = int(input("Ingrese el 1° número: "))
numero2 = int(input("Ingrese el 2° número: "))
numero3 = int(input("Ingrese el 3° número: "))

print(f"La suma es {numero1+numero2+numero3}")
print(f"La resta es {numero1-numero2-numero3}")
print(f"La multiplicación es {numero1*numero2*numero3}")

if numero2 != 0:
    if numero3 !=0:
        print(f"La division es {(numero1/numero2)/numero3}")
    else:    
        print("No se puede dividir entre 0")
else:
    print("No se puede dividir entre 0")

if numero2 != 0:
    if numero3 !=0:
        print(f"La division entera es {(numero1//numero2)//numero3}")
    else:    
        print("No se puede dividir entre 0")
else:
    print("No se puede dividir entre 0")
