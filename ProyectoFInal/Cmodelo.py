import pandas as pd
import sqlite3
connec =sqlite3.connect('provin.db')
cur=connec.cursor()

rut = 'D:\\Python\\worksapace0223\\EjerciciosSemanales\\TareaProyecto\\AQP.csv'
ab = pd.read_csv(rut, sep = ";")

col = ab[["Provincia","Ingreso"]]
# print(ab)

Listprov = ab.values.tolist()
# print(Listprov)

def crear_table():
    cur.execute("CREATE TABLE Prov_Ing (Provincia Varchar(25), Ingreso Varchar(25));")
    cur.executemany("INSERT INTO Prov_Ing values(?,?)",Listprov)
    connec.commit()
# crear_table()


def insertar_tbl():
    nomprov = input("Ingrese nombre de nueva provincia: ")
    ingprov = int(input("Ingrese el ingreso de esa provincia: "))
    cur.execute("INSERT INTO Prov_Ing values(?,?)",(nomprov,ingprov))
    connec.commit()
# insertar_tbl()


def mostrar_tabla():
    dat=cur.execute("SELECT * FROM Prov_Ing").fetchall()
    for i in dat:
        print(i) 
# mostrar_tabla()

