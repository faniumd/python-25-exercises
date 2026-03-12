"""16. Tienda de mascotas: ventas por categoría
Registrar ventas de una tienda de mascotas.
Categorías:
• alimento
• juguete
• accesorio
Pedir 10 ventas. En cada venta:
• categoría
• valor de la compra
Al final mostrar:
• cuánto se vendió por cada categoría
• cuál categoría generó más dinero
Practica: acumuladores separados."""


alimento = 0
juguete = 0
accesorio = 0

for i in range(10):
    cat = input("Categoria: ")
    valor = int(input("Valor: "))

    if cat == "alimento":
        alimento += valor
    elif cat == "juguete":
        juguete += valor
    elif cat == "accesorio":
        accesorio += valor

print("Alimento:", alimento)
print("Juguete:", juguete)
print("Accesorio:", accesorio)

if alimento > juguete and alimento > accesorio:
    print("Mas ventas: alimento")
elif juguete > accesorio:
    print("Mas ventas: juguete")
else:
    print("Mas ventas: accesorio")