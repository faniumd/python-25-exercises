#1. Heladería: sabor más pedido
#Una heladería quiere registrar 5 pedidos.
#Por cada cliente, el programa debe pedir el sabor elegido:
#• vainilla
#• chocolate
#• fresa
#Al final debe mostrar cuántas veces se pidió cada sabor.
#Practica: ciclos, condicionales, contadores.

print("HELADERIA, ICE CREAM YUMMY! \nBIENVENIDO AL MENU")


contavai=0
contachoco=0
contafresa=0

cantidad = int(input("CUANTOS HELADOS DESEA COMPRAR?: "))
for i in range(cantidad):

    print("\nPEDIDOS", i+cantidad)
    
    
    
    print("Usted compró", cantidad, "helados")
        
    print("SABORES DE HELADOS DISPONIBLES: " )
    print("VAINILLA (1)")
    print("CHOCOLATE (2)")
    print("FRESA (3)")

    saborh=int(input("QUE SABOR DE HELADOS ES DE SU PREFERENCIA:__"))
    if saborh == 1:
      contavai+=1
      

    elif saborh == 2:
      contachoco+=1
           
       
    elif saborh == 3:
      contafresa +=1
        
print("\nCOMPRA EXITOSA!!")
print("\nRESUMEN DE LA COMPRAR...")
print("cantidad de helados sabor vainilla comprados: ", contavai)  
print("cantidad de helados sabor fresa comprados: ", contafresa) 
print("cantidad de helados sabor chocolate comprados: ", contachoco)  


