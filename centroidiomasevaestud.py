"""18. Centro de idiomas: evaluación de estudiantes
Registrar varios estudiantes de un curso de inglés.
Por cada uno pedir:
• nombre
• nota speaking
• nota listening
• nota reading
Calcular promedio simple y clasificar:
• menor de 60 → bajo
• 60 a 79 → medio
• 80 o más → alto
Al final mostrar:
• promedio general del grupo
• mejor estudiante
• cuántos quedaron en cada nivel
Practica: promedios, maximos, contadores"""


total_prom = 0
mejor = 0
mejor_nombre = ""

bajo = 0
medio = 0
alto = 0

for i in range(5):
    nombre = input("Nombre: ")

    s = int(input("Speaking: "))
    l = int(input("Listening: "))
    r = int(input("Reading: "))

    prom = (s + l + r) / 3
    total_prom += prom

    if prom > mejor:
        mejor = prom
        mejor_nombre = nombre

    if prom < 60:
        bajo += 1
    elif prom < 80:
        medio += 1
    else:
        alto += 1

print("Promedio grupo:", total_prom / 5)
print("Mejor estudiante:", mejor_nombre)
print("Bajo:", bajo)
print("Medio:", medio)
print("Alto:", alto)