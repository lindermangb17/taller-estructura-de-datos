def crearMatCuadrada(tam, valor=0):
    mat = []
    for f in range(tam):
        mat.append([valor] * tam)
    return mat

def printMatriz(mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            print(mat[f][c], end="\t")
        print("")

tamaño=int(input("Indique el atmaño de la matriz cuadrada: "))

while tamaño <= 0:
    tam = int(input("Ingrese un tamaño mayor que cero: "))
    
matriz = crearMatCuadrada(tamaño)

# PRIMERA MATRIZ
cont = 1
for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        matriz[f][c] = cont
        cont +=1
print("PRIMERA MATRIZ ")        
printMatriz(matriz)
print(" ")

# SEGUNDA MATRIZ
matriz = crearMatCuadrada(tamaño)
cont = 1
signo=1
for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        matriz[f][c] = cont
        cont =cont + signo * 1
    signo *= -1
    cont =cont + signo * 1

print("SEGUNDA MATRIZ ")  
asc = list(range(1,tamaño+1))
des = asc[::-1]
matriz = []
for i in range(tamaño):
    matriz.append(asc if i%2 == 0 else des)
printMatriz(matriz)

# TERCERA MATRIZ
matriz = crearMatCuadrada(tamaño)

for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        if [f]==[c]:
            matriz[f][c] = 1
            
print("TERCERA MATRIZ ")  
printMatriz(matriz)
            
# CUARTA MATRIZ
matriz = crearMatCuadrada(tamaño)

for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        if f + c == tamaño - 1:
            matriz[f][c] = 1

print("CUARTA MATRIZ ")  
printMatriz(matriz)

# QUINTA MATRIZ
matriz = crearMatCuadrada(tamaño)

for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        if f >= c:
            matriz[f][c] = 1

print("QUINTA MATRIZ ")  
printMatriz(matriz)

# SEXTA MATRIZ
matriz = crearMatCuadrada(tamaño)

for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        if f <= c:
            matriz[f][c] = 1

print("SEXTA MATRIZ ")  
printMatriz(matriz)

# SEPTIMA MATRIZ
matriz = crearMatCuadrada(tamaño)

cont = 1
for c in range(tamaño):
    for f in range(tamaño):
        matriz[f][c] = cont
        cont +=1
print("SEPTIMA MATRIZ ")        
printMatriz(matriz)
print(" ")

# OCTAVA MATRIZ
matriz = crearMatCuadrada(tamaño," ")

cont = " "
for f in range(tamaño):
    for c in range(tamaño):
        if f >= c:
            if c %2==0:
                matriz[f][c] = "A"
            else:
                matriz[f][c] = "B"
                
        
print("OCTAVA MATRIZ ")        
printMatriz(matriz)
print(" ")

