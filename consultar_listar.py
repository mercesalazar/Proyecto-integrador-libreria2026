#--------------------------- FUNCIONES LISTAR/CONSULTAR ARTICULOS  -------------------------   
def encabezado():
    print()
    print("Listado de todos los Artículos")
    print("-" * 30)
    print()
    print("-" * 75)
    print(f"{'CÓDIGO':<15}{'DESCRIPCIÓN':<25}{'PRECIO':<25}{'STOCK':<30}")
    print("-" * 75)

def detalle_articulos(articulo):
    print(f"{articulo['codigo']:<15}"
          f"{articulo['desc']:<25}"
          f"{articulo['precio']:<25}"
          f"{articulo['stock']:<30}")  

def encabezado2():
    print()
    print("Listado de todos los Artículos")
    print("-" * 30)
    print()
    print(f"{'ID':<5}{'CÓDIGO':<15}{'DESCRIPCIÓN':<25}{'PRECIO':<25}{'STOCK':<30}")
    print("-" * 85)

def encabezado3():
    print()
    print("-" * 75)
    print(f"{'CÓDIGO':<15}{'DESCRIPCIÓN':<25}{'PRECIO':<25}{'STOCK':<30}")
    print("-" * 75)
    
def detalle_articulos2(articulo):
    print(f"{articulo['id']:<5}"
          f"{articulo['codigo']:<15}"
          f"{articulo['desc']:<25}"
          f"{articulo['precio']:<25}"
          f"{articulo['stock']:<30}")
    
def listar_id(articulos):
    encabezado2()
    for articulo in articulos:
        if articulo["status"] != "E":
           detalle_articulos2(articulo)
    print() 
     
def listar_todos(articulos):
    encabezado()
    for articulo in articulos:
        if articulo["status"]!="E":
           detalle_articulos(articulo)
    print()

def consultar_articulos(articulos):
    hay_articulos=False
    for articulo in articulos:
        if articulo['status']!="E":
           hay_articulos=True
           break
    if not hay_articulos:
       print()
       print("No hay artículos que listar....Agregue artículos al inventario.") 
       print()
    else:
       listar_todos(articulos)
       print()

def listar_borrados_temporalmente(articulos):
    print()
    print("Listado de artículos eliminados temporalmente.")
    print("---------------------------------------------")
    print()
    print(f"{'ID':<5}{'CÓDIGO':<15}{'DESCRIPCIÓN':<25}{'PRECIO':<25}{'STOCK':<30}")
    print("-" * 85)
    for articulo in articulos:
        if articulo["status"] == "E":
           detalle_articulos2(articulo)
    print()

def listar_por_codigo(articulos,codigo_buscado):
    print()
    print("Búsqueda de artículo por código") 
    print("-" * 31)
    encabezado3()
    for articulo in articulos:
        if articulo["status"]!="E":
           if articulo["codigo"]==codigo_buscado:
              detalle_articulos(articulo)
    print() 
        