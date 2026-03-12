#3. Cafetería: total de una compra sencilla
#En una cafetería venden:
#• café = 4000
#• té = 3500
#• jugo = 5000
#Pide al usuario qué bebida quiere y cuántas unidades desea comprar.
#Luego muestra el total a pagar.
#Practica: condicionales, variables, multiplicación.

print("\nBIENVENIDO AL MENU DE CAFETERIA VIRTUAL MR. COFFE ☕")

try:
 
 print("\n   MENU DE CAFES")
 print("CAFE-$4000 ☕ OPC(1)")
 print("Té-$3500 🍵 OPC(2)")
 print("JUGO-$5000 🧃 OPC(3)")
 opc=int(input("\n  INGRESE LA OPCION DE BEBIDA:_ " ))
 if opc == 1:
    PNAME="CAFES"
    print("\n  AH SE SELECCIONADO OPCION 1 CAFE.")
    RESUMECOMPTOTALP=unicafe=int(input("\n CUANTAS UNIDADES DE CAFE DESEA COMPRAR?:_ " ))
    RESUMECOMPTOTAL=totalpagacafe=unicafe*4000
    print("\n  PERFECTO, COMPRA EXITOSA!!")
    print("\n  TOTAL A PAGAR 💲",totalpagacafe )
 elif opc == 2:
    print("AH SE SELECCIONADO OPCION 2 Té.")
    unite=int(input("CUANTAS UNIDADES DE Té DESEA COMPRAR?:_ "))
    totalpagate=unite*3500
    print("PERFECTO, COMPRA EXITOSA!!")
    print("TOTAL A PAGAR 💲",totalpagate )
 elif opc == 3:
    print("AH SE SELECCIONADO OPCION 3 JUGO.")
    unijugo=int(input("CUANTAS UNIDADES DE JUGO DESEA COMPRAR?:_ "))
    totalpagajugo=unijugo*5000
    print("PERFECTO, COMPRA EXITOSA!!")
    print("TOTAL A PAGAR 💲",totalpagajugo )


 print("\nRESUMEN DE LA COMPRA:") 
 print("OBJETOS COMPRADOS:", RESUMECOMPTOTALP, PNAME)
 print("TOTAL A PAGAR: ", RESUMECOMPTOTAL)

except ValueError:    
    print("ERROR 🚫: INGRESE UN VALOR VALIDO, PORFAVOR")

    
   