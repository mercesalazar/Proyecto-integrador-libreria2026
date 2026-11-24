from consultar_listar import encabezado3, detalle_articulos, listar_por_codigo

#--------------------------- FUNCION BUSCAR ARTÍCULOS ---------------------------
def buscar_codigo(articulos):
    print()
    print("-" * 26)
    print("Buscar artículo por código")
    print("--------------------------")
    print()
    codigo_buscado = input("Ingrese el código a buscar:")
    print()
    encontrado=False
    for articulo in articulos:
        if articulo['status']!="E":
           if articulo['codigo'] == codigo_buscado:
              encontrado=True
              break
    if not encontrado:
           print("El código buscado no existe....") 
           print()
    else:
        listar_por_codigo(articulos,codigo_buscado)
        
def verificar_parcial(articulos,busqueda):
    for articulo in articulos:
        if articulo["status"]!="E":
           if busqueda.lower() in articulo["desc"].lower():
              return(True)
    return(False)       
               
          
def busqueda_parcial(articulos):
    print()
    print("Búsqueda por coincidencia parcial en la descripción.")
    print("-" * 52)
    print()
    busqueda = input("Ingrese la descripción parcial:")
    resultado=verificar_parcial(articulos,busqueda)
    if resultado==False:
       print()
       print("ERROR!! No se encontró coincidencia...") 
    else:
       encabezado3()
       for articulo in articulos:
           if articulo["status"]!="E":
              if busqueda.lower() in articulo["desc"].lower():
                 detalle_articulos(articulo) 
       print()

def buscar_por_rango(articulos):
    print()
    print("Listado de artículos por rango de precio")
    print("-" * 40)
    print()
    rango_min=float(input("Ingrese el rango inferior:"))
    rango_max=float(input("Ingrese el rango superior:"))
    if rango_min <= rango_max:
       encabezado3()
       for articulo in articulos:
           if articulo["status"]!="E":
              if (articulo['precio']>=rango_min) and (articulo['precio']<=rango_max):
                 detalle_articulos(articulo)
    else:
        print()
        print("ERROR!! El orden de ingreso de los rangos es incorrecto...")
    print()   
    
def stock_disponible(articulos):
    """Retorna una lista con los productos activos cuyo stock sea > 0"""
    con_stock=False
    for articulo in articulos:
        if articulo["status"] == "A" and articulo["stock"] > 0:
           con_stock=True
           break
    if con_stock==False:
       print()
       print("No hay productos con stock disponible...")
       print()
    else:
        print()
        print("Listado de artículos disponibles para la venta")
        print("-" * 46)
        encabezado3()
        for articulo in articulos:
            if articulo["status"] == "A" and articulo["stock"] > 0:
               detalle_articulos(articulo)
        print()

def buscar_articulos(articulos):
    print()
    opcion_busqueda = 0
    while opcion_busqueda != 5:
          print()
          print(" BÚSQUEDAS DE ARTÍCULOS")
          print("-----------------------")
          print("1. Por código de artículo")
          print("2. Por coincidencia parcial en la descripción")
          print("3. Por rango de precio")
          print("4. Artículos con stock disponible")
          print("5. Volver al menú principal")
          while True:
                try:
                  print()
                  opcion_busqueda = int(input("Seleccione una opción [1-5]:"))
                  break
                except ValueError:
                    print()
                    print("Error!!! Debe ingresar un número entero")
                  
          if opcion_busqueda == 1:
              buscar_codigo(articulos)
    
          elif opcion_busqueda == 2:
               busqueda_parcial(articulos)
               
          elif opcion_busqueda == 3:
               buscar_por_rango(articulos)
    
          elif opcion_busqueda == 4:
               stock_disponible(articulos)
               
          elif opcion_busqueda == 5:
               print()
               print("Volviendo al menú principal...")
               print()
          else:
               print()
               print("Opción de búsqueda inválida...")
               print()
               