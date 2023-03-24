print( """

1) Hacer un cuadrado con "*".
2) Identificar si es multiplo de 2.
3) Imprimir los mayores de edad
    
""")

option = input()

if option == '1':
    square = int(input('Ingrese la medida del lado del cuadrado: '))
    for f in range(0, square):
        for c in range(0, square):
            print('*', end='')
        print()

elif option == '2':
    listanum = [5,8,51,23,3,73,24]
    for num in listanum:
        if (num % 2 == 0) :
            print(f"Numero par: {num}")

elif option == '3':
    content = [("Maria",20),("Juan",15),("Raul",32),("Carola",27),("Cristina",17), ("Ruben",18)]
    print("Los mayores de edad son:")
    for ed in content :
        if int (ed[1]) >= 18 :
            print(ed)
else:
    print("Adios")
