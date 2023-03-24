print( """

1) Convertir a minusculas.
2) identificar la longitud del texto.
3) Separa cada palabra del texto
    
""")

op = input()

FuncionString = ("Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas 'Letraset', las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum.")

if op == '1':
    print(FuncionString.lower())
elif op == '2':
    print(f"La longitud es: {len(FuncionString)}")
elif op == '3':
    print(FuncionString.split(sep=" "))
