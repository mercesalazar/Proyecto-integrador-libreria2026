from consultar_listar import listar_id, listar_borrados_temporalmente
#--------------------------- FUNCIONES DE ELIMINAR -------------------------------- 
def restaurar_articulo(articulos,id_buscar):
    encontrado = False 
    seguro=""
    for i in range(len(articulos)): 
        if articulos[i]['status'] == "E":
           if articulos[i]['id']==id_buscar:
              seguro=input("¿Seguro/a que desea restaurar este artículo? [S/N]:").upper()
              if seguro=="S":
                 articulos[i]['status']="A"
                 encontrado=True
                 print()
                 print(f"El Artículo con id {id_buscar} fue restaurado con éxito.")
                 break
    if seguro!="N":
       if not encontrado:
          print("El artículo con id {id_buscar} no está eliminado. ¡Intente con otro Id!.")   
    else:
        print()
        print("Si no estás seguro(a) inténtalo nuevamente en otro momento.")  
              
def eliminacion_temporal(articulos,id_buscar):
    encontrado = False 
    seguro=""
    for i in range(len(articulos)): 
        if articulos[i]['status'] != "E":
            if articulos[i]['id']==id_buscar:
               seguro=input("¿Seguro/a que desea borrar este artículo? [S/N]:").upper()
               if seguro=="S":
                  articulos[i]['status']="E"
                  encontrado=True
                  print()
                  print(f"El artículo con id {id_buscar} fue eliminado con éxito.")
                  break
    if seguro!="N":
       if not encontrado:
          print("Id del artículo no se encontró. ¡Intente con otro Id!.")   
    else:
          print()
          print("Si no estás seguro(a) de tu eliminación, inténtalo nuevamente en otro momento.")   
             
def eliminar_articulo(articulos):
    subopcion = 0
    while subopcion != 2:
          print()
          print("ELIMINAR UN ARTÍCULO")
          print("--------------------")
          print("[1] Eliminar un Artículo")
          print("[#] Listar artículos eliminados")
          print("[#] Restaurar artículos eliminados")
          print("[2] Volver al Menú Principal")
          print()
          while True:
            try:
              subopcion= int(input("Seleccione una opción [1-2]:"))
              break
            except ValueError:
               print()
               print("ERROR!!! Introduzca un número entero entre 1 y 5....")
               print()
          if subopcion == 1:
             if len(articulos)==0:
                print()
                print("No hay artículos para eliminación...")
                print()
             else:
                listar_id(articulos)
                print()
                id_buscar = int(input("Ingrese el Id del artículo a eliminar:"))
                print()
                eliminacion_temporal(articulos,id_buscar)
          elif subopcion == 98:   
               eliminados=False
               for articulo in articulos:
                   if articulo['status']=="E":
                      eliminados=True
                      break
               if eliminados:
                   listar_borrados_temporalmente(articulos)
               else:
                   print()
                   print("No hay artículos eliminados...")
                   print()      
                                             
          elif subopcion == 99: 
               eliminados=False
               for articulo in articulos:
                   if articulo['status']=="E":
                      eliminados=True
                      break
               if eliminados:
                  listar_borrados_temporalmente(articulos)
                  print()
                  id_buscar = int(input("Ingrese el Id del artículo a restaurar:"))
                  print()
                  restaurar_articulo(articulos,id_buscar)
               else:
                  print()
                  print("No hay artículos para restaurar...")
                  print()  
          elif subopcion == 2: 
                print() 
                print("Fin del proceso de eliminación...¡Hasta pronto!")  
                print()
          else: 
               print()
               print("ERROR!!! Opción de eliminación inválida. Intente de nuevo.")  
               print()       
   