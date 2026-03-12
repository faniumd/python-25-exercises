"""8. Tienda deportiva: contar productos caros
Pide el precio de 6 productos deportivos.
Al final indica cuántos cuestan más de 100000.
Practica: ciclo, contador, condicional."""

contador = 0

for i in range(6):
    precio = int(input("Precio producto: "))
    if precio > 100000:
        contador += 1

print("Productos caros:", contador)