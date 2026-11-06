matVentas = []
lstPrecios = []

numprod=int(input("Ingrese el numero de productos: "))

for f in range(numprod):
    precio = int(input(f"Precio del producto {f+1}: "))
    lstPrecios.append(precio)
    
    fila=[]
    
    for c in range(7):
        cantidad = int(input(f"Producto {f+1}, día {c+1}: "))
        fila.append(cantidad)

    matVentas.append(fila)
    
# 1. producto que genera mas ingresos  en la semana

def lstTotalProductosxsem(Ventas,Precios):
    fils = len(Ventas)
    cols = len(Ventas[0])
    lstTotales=[]
    for f in range(fils):
        suma=0
        for c in range(cols):
            suma += Ventas[f][c]*Precios[f]
        lstTotales.append(suma)

    return lstTotales


lstTotales = lstTotalProductosxsem(matVentas,lstPrecios)

maxTotal= max(lstTotales)
prodVentMax= lstTotales.index(maxTotal)+1


print(f"El producto {prodVentMax} es el que mas vende a la semana con ventas de ${maxTotal:,}")

# 2. dia que mas se vende
 
def lstTotaldiasxsem(Ventas,Precios):
    fils = len(Ventas)
    cols = len(Ventas[0])
    lstTotalesdia=[]
    for c in range(cols):
        suma=0
        for f in range(fils):
            suma += Ventas[f][c]*Precios[f]
        lstTotalesdia.append(suma)

    return lstTotalesdia

lstTotalesdia = lstTotaldiasxsem(matVentas,lstPrecios)

maxTotaldia= max(lstTotalesdia)
diaventMax= lstTotalesdia.index(maxTotaldia)+1

print(f"El día {diaventMax} fue el de mayores ingresos con ${maxTotaldia:,}")