from Cmodelo import *

def consul(option:int):
    match option:
        case 1:
            crear_table()
            print("se ejecuto caso 1")
            return
        case 2:
            insertar_tbl()
            print("se ejecuto caso 2")
            return
        case 3:
            mostrar_tabla()
            return
        case 4:
            quit()

        

            
