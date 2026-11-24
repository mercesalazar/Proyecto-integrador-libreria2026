#--------------------------- FUNCIONES DE VENTA  ---------------------------------- 
def registrar_venta(articulos,cantidad,indice,subtotal):
    if articulos[indice]["stock"] >= cantidad:
       articulos[indice]["stock"] -= cantidad
       print()
       subtotal=subtotal+(articulos[indice]["precio"]*cantidad)
       print(f"Venta exitosa: Se vendieron {cantidad} unidad(es) de '{articulos[indice]['desc']}' a un precio de '{articulos[indice]['precio']}'. Stock restante: {articulos[indice]['stock']}")
       print()
       print("Monto vendido del artículo:",subtotal)
       print()
       return(subtotal)
    else:
        print()
        print(f"Error: Stock insuficiente. Stock actual de '{articulos[indice]['desc']}': {articulos[indice]['stock']}")
        print()
        subtotal=0
        return(subtotal)
   
def venta(articulos):
    """Busca un artículo por código y disminuye su stock si hay suficiente."""
    seguir="S"
    total_venta=0.0
    print()
    print("PROCESAR VENTA")
    print("--------------")
    while seguir=="S":
        pos=0
        indice=0
        encontrado=False
        subtotal=0.0
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
           if cantidad<=0:
               print()
               print("ERROR: La cantidad a comprar debe ser mayor a 0...")
               print()
           else:
               monto_parcial=registrar_venta(articulos,cantidad,indice,subtotal)
               total_venta+=monto_parcial
        else:
           print()
           print("Error: Artículo no existe en el inventario.") 
           print()
        seguir=input("¿Desea comprar otro artículo? [S/N]:").upper()  
    print() 
    print("Monto total de la venta:",total_venta)
    print()
    print("Gracias por preferir nuestros productos...")
    print()
        