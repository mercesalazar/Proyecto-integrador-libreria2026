from consultar_listar import encabezado3, detalle_articulos
#--------------------------- FUNCION ARTICULOS SIN STOCK --------------------- 
def productos_sin_stock(articulos):
    """Retorna una lista con los productos activos cuyo stock sea igual a cero."""
    sin_stock=False
    for articulo in articulos:
        if articulo["status"] == "A" and articulo["stock"] == 0:
           sin_stock=True
           break
    if sin_stock==False:
       print()
       print("No hay productos con stock igual a cero(0)...")
       print()
    else:
        print()
        print("Listado de artículos sin stock.")
        print("-" * 31)
        encabezado3()
        for articulo in articulos:
            if articulo["status"] == "A" and articulo["stock"] == 0:
               detalle_articulos(articulo)
        print()

#--------------------------- FUNCION VALOR TOTAL INVENTARIO -------------------- 
def valor_total_inventario(articulos):
    """Calcula el valor monetario total del inventario de artículos."""
    valor_total=0.0
    for articulo in articulos:
        valor_total += articulo["precio"] * articulo["stock"] 
    print()
    print("El valor total del inventario es:",valor_total)
    print()    

#--------------------------- FUNCION MENÚ REPORTES --------------------------             
def reportes(articulos):
    opcion_reporte = 0
    while opcion_reporte != 3:
          print()
          print(" REPORTES DE ARTÍCULOS")
          print("----------------------")
          print("1. Productos sin stock")
          print("2. Valor total del inventario")
          print("3. Volver al menú principal")
          while True:
                try:
                  print()
                  opcion_reporte = int(input("Seleccione una opción [1-3]:"))
                  break
                except ValueError:
                    print()
                    print("Error!!! Debe ingresar un número entero")
                  
          if opcion_reporte == 1:
              productos_sin_stock(articulos)
    
          elif opcion_reporte == 2:
               valor_total_inventario(articulos)
    
          elif opcion_reporte == 3:
               print()
               print("Volviendo al menú principal...")
               print()
          else:
               print()
               print("Opción de reporte inválida...")
               print()
    
