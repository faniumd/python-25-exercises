"""12. Gimnasio: promedio de rendimiento semanal
Registrar 5 personas en un gimnasio.
Por cada una pedir:
• nombre
• días asistidos en la semana
• minutos promedio entrenados por día
Clasificar:
• menos de 3 días → bajo compromiso
• 3 a 4 días → compromiso medio
• 5 o más → compromiso alto
Al final mostrar cuántas personas quedaron en cada categoría.
Practica: ciclos, contadores, condicionales."""


bajo = 0
medio = 0
alto = 0

for i in range(5):
    nombre = input("Nombre: ")
    dias = int(input("Dias asistidos: "))
    minutos = int(input("Minutos promedio: "))

    if dias < 3:
        print("Bajo compromiso")
        bajo += 1
    elif dias <= 4:
        print("Compromiso medio")
        medio += 1
    else:
        print("Compromiso alto")
        alto += 1

print("Bajo:", bajo)
print("Medio:", medio)
print("Alto:", alto)