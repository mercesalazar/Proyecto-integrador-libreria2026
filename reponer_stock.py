#--------------------------- FUNCION DE REPONER STOCK -------------------------------- 
def reponer_stock(articulos):
    """Aumenta el stock de un producto existente."""
    print()
    print("REPONER STOCK DE ARTÍCULOS")
    print("--------------------------") 
    seguir="S"
    while seguir=="S":
          pos=0
          indice=0
          encontrado=False
          print()
          cod_buscar=input("Ingrese el código del artículo:")
          while pos < len(articulos) and not encontrado:
                if articulos[pos]["status"] == "A" and articulos[pos]["codigo"] == cod_buscar:
                   indice=pos
                   encontrado=True 
                pos+=1   
          if encontrado:
               print()
               cantidad=int(input("Ingrese cantidad:"))
               if cantidad <= 0:
                  print()
                  print("Error: La cantidad a reponer debe ser mayor a cero.")
               else:
                  articulos[indice]["stock"] += cantidad
                  print()
                  print(f"Reposición exitosa: Se agregaron {cantidad} unidad(es) a '{articulos[indice]['desc']}'. Nuevo stock: {articulos[indice]['stock']}")
                  print()
          else:
               print()
               print("Error: Artículo no existe en el inventario.") 
               print()
          seguir=input("¿Desea reponer stock de otro artículo? [S/N]:").upper()  
          print()
                