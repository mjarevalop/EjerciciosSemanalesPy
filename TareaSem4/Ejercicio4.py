from datetime import datetime

class Registro:

    def texto():
        nombre = input("nombre del archivo:")
        archivo = open(nombre,'w')
        archivo.write('')
        print("archivo creado")

        mensaje = input("introdusca su mensaje:")
        fecha = datetime.now()
        today = fecha.strftime("%d/%m/%Y %H:%M:%S")
        finmen=archivo.write(f"{today} - Archivo: {nombre} - Mensaje: {mensaje}")

        archivo = open(nombre,'r')
        value= archivo.read(finmen)
        print(value)
        archivo.close()
    texto()
    

    


    


    




  