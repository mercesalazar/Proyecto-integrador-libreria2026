#Programa que permitirá la gestión una librería
#Declaración de módulos de llamadas a funciones 
from agregar_articulos import *
from reportes import *
from consultar_listar import *
from registrar_venta import *
from reponer_stock import *
from buscar_articulo import *
from editar import *
from eliminar import *

# Lista principal donde se almacenarán los artículos
articulos = []
# Variable para generar IDs únicos
ultimo_id = 0
id_buscar=0
 
# -----------------------------------------------------------------------------------------
#                                           MENÚ PRINCIPAL
# -----------------------------------------------------------------------------------------

opcion = 0
while opcion != 9:

    print("--------------------------------")
    print(" LIBRERÍA - GESTIÓN DE ARTÍCULOS")
    print("--------------------------------")
    print("1. Agregar artículo")
    print("2. Consultar artículos")
    print("3. Buscar artículo")
    print("4. Modificar artículo")
    print("5. Eliminar artículo")
    print("6. Venta de artículo")
    print("7. Reposición de stock")
    print("8. Reportes")
    print("9. Salir")
    print("---------------------------------")
    print()
    while True:
        try:    
           opcion = int(input("Seleccione una opción [1-9]:"))
           break
           print()
        except ValueError:
               print("Error!!! Debe ingresar un número entero")
               print()
    
    if opcion == 1:
        agregar_articulo(articulos)

    elif opcion == 2:
        consultar_articulos(articulos)

    elif opcion == 3:
        buscar_articulos(articulos)

    elif opcion == 4:
        modificar_articulo(articulos)

    elif opcion == 5:
        eliminar_articulo(articulos)

    elif opcion == 6:
         venta(articulos)

    elif opcion == 7:
        reponer_stock(articulos)

    elif opcion == 8:
         reportes(articulos)
         
    elif opcion == 9:
        print()
        print("Hasta pronto!!! Gracias por comprar nuestros artículos.")
        print()
    else:
        print()
        print("Error!!!Opción de menú inválida...")
        print()