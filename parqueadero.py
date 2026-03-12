#6. Parqueadero: cobro por horas
#Pide cuántas horas estuvo un carro en un parqueadero.
#Reglas:
#• primera hora = 5000
#• cada hora adicional = 3000
#Muestra el total a pagar.
#Practica: condicionales y operaciones.

horas = int(input("Horas parqueado: "))

if horas == 1:
    total = 5000
else:
    total = 5000 + (horas - 1) * 3000

print("Total a pagar:", total)