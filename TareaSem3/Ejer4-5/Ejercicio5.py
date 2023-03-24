import os
from Producto import Product, Show

try:
    a = Product("Leche","Peru-0001-2023")
    b = Show([a])
    b.mostrar_all()
except:
    print("No hay productos")

else:
    ruta = os.getcwd()
    print(f"La ruta es:{ruta}")

finally:
    print("Proceso Terminado")