class Product:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        print('Se agrego el producto: ',self.nombre)

    def __str__(self):
        return '{} del Pais {} y codigo {} '.format(self.nombre, self.codigo.split("-")[0],self.codigo.split("-")[1])

class Show:
    mostrar = []

    def __init__(self, mostrar =[]):
        self.mostrar = mostrar

    def agregar(self, au):
        self.mostrar.append(au)

    def mostrar_all(self):
        for au in self.mostrar:
            print(au)


au = Product("Galleta","Argentina-0001-2022")
asd = Show([au])
asd.mostrar_all()