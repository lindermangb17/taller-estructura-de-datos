def agregarprod(productos):
    producto= input("nombre del producto nuevo:")
    productos.append(producto)
    print("Producto agregado correctamente")
    input("Presione enter para continuar")
    
def agregarlote(productos):
    cant=int(input("cantidad de productos del lote:"))
    
    while cant <=0:
        print("Ingrese cantidad mayor que 0")
    for i in range(1,cant+1):
        producto= input(f"nombre del producto {i}:")
        productos.append(producto)
        
    print("Lote agregado correctamente")
    input("Presione enter para continuar")

def eliminarprod(productos):
    producto= input("nombre del producto a eliminar:")
    if producto in productos:
        productos.remove(producto)
        print("Producto eliminado correctamente")
    else:
        print("Producto no existe")
    input("Presione enter para continuar")    
        
def eliminarReciente(productos):
    if len(productos)>0:
        producto=productos.pop()
        print(f"se elimino el producto {producto}:")
    else:
        print("inventario vacio")
    input("Presione enter para continuar")    
   
   
def ordenarprod(productos):
    productos.sort()
    
    print("Productos ordenados alfabeticamente!!")
    
    print(productos)
    input("Presione enter para continuar")
             
def totalprod(productos):
    total=len(productos)
    print(f"Hay {total} productos")
    input("Presione enter para continuar")

def salir():
    print(f"Gracias por usar el inventario")
    


productos = []
opcion=0
    
while opcion !=7:
    print("""
              MENÚ
    1. Agregar producto
    2. Agregar lote de productos
    3. Eliminar producto del inventario
    4. Eliminar el producto más reciente
    5. Ordenar productos alfabéticamente
    6. Mostrar número total de productos
    7. Salir """)
    opcion=int(input("Seleccicone una opcion: "))
    
    match opcion:
        case 1:
            agregarprod(productos)
        case 2:
            agregarlote(productos)
        case 3:
            eliminarprod(productos)
        case 4:
            eliminarReciente(productos)
        case 5:
            ordenarprod(productos)
        case 6:
            totalprod(productos)
        case 7: 
            salir()
        case _:
            print(f"opcion invalida")
    
    
    