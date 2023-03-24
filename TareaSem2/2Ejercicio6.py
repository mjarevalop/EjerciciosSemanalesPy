
evento = {
    'nombre': "Concierto",
    'precio': "200",
    'stock': 500,
    'Lugar':"Auditorio"
}

def buscar_evento(nombre):
    if evento['nombre'] == nombre:
        return evento
    else:
        return False

def verificar_lugar(pri):
    if pri['Lugar']:
        return pri['Lugar']

def verificarStock(product:dict)->int:
    if product['stock']:
        return product['stock']
    
def main():
    eventoname = input('Introduzca nombre del evento: ')
    evento_1 = dict()
    if buscar_evento(eventoname):
        evento_1=buscar_evento(eventoname)
    else:
        print("No exste el evento")
    
    if verificarStock(evento_1):
        print(f"El stock es {verificarStock(evento_1)}")
    else:
        print("No hay")
    
    if verificar_lugar(evento_1):
        print(f"El evento es en el {verificar_lugar(evento_1)}")
main()