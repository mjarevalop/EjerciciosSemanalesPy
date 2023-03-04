ListPersona = [("Ana",12,85634595),("Marcos",25,96547521),("Miguel",23,72935475),("Sara",33,45967809)]
ListDnis = [85634595,65987845,72935475,96547521]

for i in ListPersona :
        if int(i[1]) >= 18 :
            if i[2] in ListDnis :
                print(i[0])
 

