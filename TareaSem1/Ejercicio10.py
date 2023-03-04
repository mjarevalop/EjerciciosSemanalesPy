info_curso = {"nombre de curso":"", "cantidad de alumnos":0, "activo":True, "nombre de profesor":"", "max nota":0, "alumnos":[]}

input1 = input("Ingrese nombre de alumno:")
info_curso["alumnos"].append(input1)
input2 = input("Ingrese nombre de alumno:")
info_curso["alumnos"].append(input2)
input3 = int(input("Ingrese la nota maxima:"))
info_curso["max nota"] = input3
print(info_curso)