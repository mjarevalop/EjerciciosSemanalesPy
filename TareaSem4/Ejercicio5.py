import re

def validadrcel():
    try:
        num = int(input("Ingrese el numero de celular a validar: "))
    
        if len(str(num)) == 9:
        
            abc= re.compile(r'\b9[0-9]*\d')
            xyz = abc.match(str(num))
            if int(bool(xyz)):
                    print(f"El numero {num} es valido")
            else:
                    print(f"El numero {num} es invalido")
        else:
            print("El numero es corto")
    except:
             print("Ingrese valores admitidos")

validadrcel()