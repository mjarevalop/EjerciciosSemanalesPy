import pandas as pd

rut = 'D:\\Python\\worksapace0223\\EjerciciosSemanales\\TareaProyecto\\AQP.csv'
ab = pd.read_csv(rut, sep = ";")

col = ab[["Provincia","Ingreso"]]
print(ab)

Listprov = ab.values.tolist()
print(Listprov)

# msg="""
#     1)Mostrar provincias ordenado por ingresos
#     2)Mostrar provincia especifica
#     3)Salir
# """
# while True:
#     print(msg)
#     choose=int(input("Ingrese el numero de ejercicio a realizar: "))

#     if choose == 1:
#         print(ab.sort_values(by='Ingreso'))
    
#     if choose ==2:
#         prov = input("Ingrese nombre de provincia: ")
#         ab2 = ab[ab['Provincia'] == prov]
#         print(ab2)

#     if choose ==3:
#         print("Hasta Luego ")
#         break
