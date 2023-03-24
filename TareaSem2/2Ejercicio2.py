Biblioteca = {
    "Categoria":["Literatura","Historia","Filosofia","Religion"],
    "Libros":[
        
            ### Titulo, Autor, Disponibilidad 
            ["Cien años de Soledad","Gabriel garcia Marquez", "disponible"],
            ["Origenes","Lewis Dartnell", "disponible"],
            ["Crítica a la razón pura", "Immanuel Kant", "prestado"],
            ["La divina Comedia","Dante Alighieri", "disponible"],
    ],
    "Usuarios":[]
}

def mostrar_categoria():
    print(Biblioteca["Categoria"])

def mostrar_libros ():
    print(Biblioteca["Libros"])

def agregar_usuario():
    print("Escriba exit cuando desee dejar de colocar usuarios")
    nomusuario = input("Agregue el nombre del usuario: ")
    while nomusuario != "exit":
        Biblioteca["Usuarios"].append(nomusuario)
        nomusuario = input("Agregue el nombre del usuario: ")
    print("Estos son los usuarios agregados", '\n',Biblioteca['Usuarios']) 

def cambiar_estado_libro():
    print(Biblioteca["Libros"])
    cambio = input("Ingresar el nombre del libro a cambiar ")
    print("Estados: disponible o prestado")
    estado = input("Ingresar el nuevo estado: ")
    for i in range(0,3):
        if Biblioteca["Libros"][i][0] == cambio:
            Biblioteca["Libros"][i][2] = estado
            print(Biblioteca["Libros"])
        else:
            print("No se encontro el libro")


##mostrar_categoria()
##mostrar_libros()
# agregar_usuario()
cambiar_estado_libro()