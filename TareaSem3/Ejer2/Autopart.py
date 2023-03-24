class producto:
    def __init__(self, nombre, precio, marca ):
        self.nombre = nombre
        self.precio = precio
        self.marca = marca
        print('Se agrego el producto: ',self.nombre)

    def __str__(self):
        return '{} ({}) al precio de {}'.format(self.nombre, self.marca, self.precio)

class Catalogo:
    autopartes = []
    def __init__(self, autopartes=[]):
        self.autopartes = autopartes

    def agregar(self, au):
        self.autopartes.append(au)

    def mostrar(self):
        for au in self.autopartes:
            print(au)

au = producto("Faro",50,"Panasonic")
cat = Catalogo([au])
cat.mostrar()

