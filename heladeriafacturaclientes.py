"""11. Heladería: factura de varios clientes
Una heladería quiere registrar varios clientes hasta que el usuario
decida salir.
Productos:
• cono = 3000
• vaso = 4000
• banana split = 9000
Por cada cliente:
• pedir producto
• pedir cantidad
• calcular total
Al final mostrar:
• total vendido
• cuántos clientes se atendieron
• cuál producto se pidió más veces
Practica: ciclos, acumuladores, contadores."""

total_dia = 0
clientes = 0

cono = 0
vaso = 0
banana = 0

while True:
    producto = input("Producto (cono/vaso/banana/salir): ")
    if producto == "salir":
        break

    cantidad = int(input("Cantidad: "))

    if producto == "cono":
        precio = 3000
        cono += cantidad
    elif producto == "vaso":
        precio = 4000
        vaso += cantidad
    elif producto == "banana":
        precio = 9000
        banana += cantidad
    else:
        print("Producto inválido")
        continue

    total = precio * cantidad
    print("Total cliente:", total)

    total_dia += total
    clientes += 1

print("Total vendido:", total_dia)
print("Clientes:", clientes)

if cono > vaso and cono > banana:
    print("Producto más vendido: cono")
elif vaso > banana:
    print("Producto más vendido: vaso")
else:
    print("Producto más vendido: banana split")