#------------------------------- AGREGAR ARTICULOS ---------------------------------
def agregar_articulo(articulos):
    print()
    print("Agregar Artículos")
    print("-----------------")
    print()
    seguir="S"
    while seguir=="S":
       codigo=input("Código del Producto:")
       descripcion=input("Descripción:").capitalize()
       precio=float(input("Precio:"))
       stock=int(input("Cantidad en Stock:"))
       ultimo_id=len(articulos)+1
       articulo={'id':ultimo_id, 'codigo':codigo, 'desc':descripcion, 'precio':precio, 'stock':stock, 'status':"A" }
       articulos.append(articulo)
       print()
       print("Artículo agregado con éxito...")
       print()
       seguir=input("Desea seguir agregando artículos [S/N]:").upper()
       print()