"""19. Tienda de ropa deportiva: inventario crítico
Registrar 10 productos.
Por cada producto pedir:
• nombre
• cantidad disponible
Clasificar:
• 0 → agotado
• 1 a 5 → stock bajo
• 6 o más → stock normal
Al final mostrar:
• cuántos están agotados
• cuántos tienen stock bajo
• cuántos están normales
Practica: clasificación por rangos, ciclos."""


agotado = 0
bajo = 0
normal = 0

for i in range(10):
    nombre = input("Producto: ")
    cant = int(input("Cantidad: "))

    if cant == 0:
        agotado += 1
    elif cant <= 5:
        bajo += 1
    else:
        normal += 1

print("Agotados:", agotado)
print("Stock bajo:", bajo)
print("Stock normal:", normal)