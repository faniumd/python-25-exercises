#4. Cine: entrada según edad
#El precio de la entrada cambia así:
#• niños menores de 12 → 8000
#• adultos de 12 a 59 → 12000
#• mayores de 60 → 9000
#Pide la edad del cliente y muestra cuánto debe pagar.
#Practica: condicionales.

print("Bienvenido al  menu viratual de peliculass cinez")

try:
 edad = int(input("Edad: "))

 if edad < 12:
    precio = 8000
 elif edad <= 59:
    precio = 12000
 else:
    precio = 9000

 print("Debe pagar:", precio)

except ValueError:
  print("Ingrese un valor valido")