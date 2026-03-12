"""10. Academia de baile: asistencia
Pide la cantidad de clases asistidas por un estudiante en un mes.
Reglas:
• menos de 5 → asistencia baja
• entre 5 y 8 → asistencia media
• 9 o más → asistencia alta
Practica: clasificación por rangos."""

clases = int(input("Clases asistidas: "))

if clases < 5:
    print("Asistencia baja")
elif clases <= 8:
    print("Asistencia media")
else:
    print("Asistencia alta")