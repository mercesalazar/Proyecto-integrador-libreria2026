from consultar_listar import listar_id

#--------------------------- FUNCIONES DE EDITAR --------------------------- 
def editar_descripcion(articulos,pos):
    print()
    print("Editando descripción...")
    print()
    articulos[pos]['desc'] = input("Ingrese la nueva descripción:").capitalize()
    print()
    print("Descripción actualizada con éxito.")

def editar_precio(articulos,pos):
    print()
    print("Editando precio...")
    print()
    articulos[pos]['precio'] = float(input("Ingrese el nuevo precio:"))
    print()
    print("Precio actualizado con éxito.")
    
def editar_stock(articulos,pos):
    print()
    print("Editando stock del stock...")
    print()
    articulos[pos]['stock'] = input("Ingrese la nueva cantidad:")
    print()
    print("Stock actualizado con éxito.")

                                                                  
def modificar_articulo(articulos):
    hay_articulos=False
    for articulo in articulos:
        if articulo['status']!="E":
           hay_articulos=True
           break
    if not hay_articulos:
       print("No hay artículos para edición....Agregue artículos al inventario.") 
       print()
    else:
        listar_id(articulos)
        id_buscar = int(input("Ingrese el Id del artículo a editar:"))
        encontrado = False
        opcion=0
        pos=0
        while pos<len(articulos) and not encontrado:
          if articulos[pos]['id'] == id_buscar:
             encontrado = True
             subopcion = 0
             while opcion!=5:
                print() 
                print("EDITAR UN ARTÍCULO")
                print("------------------")
                print("[1] Descripción")
                print("[2] Precio") 
                print("[3] Cantidad en Stock")
                print("[4] Volver al menú principal")
                print()
                while True:
                 try:
                   subopcion2 = int(input("Seleccione una opción [1-4]:"))
                   break
                 except ValueError:
                   print()
                   print("ERROR!!! Introduzca un número entero entre 1 y 4....")
                   print()
                if subopcion2 == 1:
                   editar_descripcion(articulos,pos)
                elif subopcion2 == 2:
                     editar_precio(articulos,pos)
                elif subopcion2 == 3:
                     editar_stock(articulos,pos)
                elif subopcion2 == 4:
                     print()
                     print(f"Fin del proceso de edición para el id {id_buscar}.") 
                     print()
                     break      
                else:
                    print()
                    print("ERROR!!! Opción de edición inválida. Intente de nuevo.")  
                    print()   
          pos+=1
        if not encontrado:
               print()
               print("ERROR!!! No existe ningún artículo con ese ID.") 
               print()
