"""14. Cine: control de sala
Pedir la capacidad total de una sala de cine y luego registrar cuántas
personas ingresan.
Por cada persona pedir edad y clasificar:
• niño
• adulto
• adulto mayor
Al final mostrar:
• total de personas ingresadas
• cuántos niños
• cuántos adultos
• cuántos adultos mayores
• si la sala se llenó o no
Practica: ciclos con límite, contadores"""

capacidad = int(input("Capacidad sala: "))

niños = 0
adultos = 0
mayores = 0

for i in range(capacidad):
    edad = int(input("Edad persona: "))

    if edad < 12:
        niños += 1
    elif edad < 60:
        adultos += 1
    else:
        mayores += 1

print("Total:", capacidad)
print("Niños:", niños)
print("Adultos:", adultos)
print("Mayores:", mayores)
print("Sala llena")