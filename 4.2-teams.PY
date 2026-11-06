pesos =[]


def repartir(pesos):
    equipo1=0
    equipo2=0

    for i in range(cant):
        if i%2==0:
            equipo1 += pesos[i]
        else:
            equipo2 += pesos[i]
    return[equipo1,equipo2]



cant=int(input("cantidad de personas:"))

while cant <=0:
    print("Ingrese cantidad mayor que 0 ")
    cant=int(input("cantidad de personas:"))

for i in range(1,cant+1):
        peso= int(input(f"peso persona {i}:"))
        pesos.append(peso) 

print(f"Peso total de cada equipo: {repartir(pesos)}")
