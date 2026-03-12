"""20. Club recreativo: control de membresías
Registrar varias personas en un club.
Por cada una pedir:
• nombre
• edad
• tipo de plan: básico, premium, familiar
Reglas:
• básico = 50000
• premium = 90000
• familiar = 130000
Además:
• si la persona es menor de 18, mostrar “registro juvenil”
• si tiene 60 o más, mostrar “beneficio senior”
Al final mostrar:
• total recaudado
• cantidad de personas por plan
• plan más vendido
Practica: condicionales, contadores, acumuladores"""

total = 0

basico = 0
premium = 0
familiar = 0

while True:
    nombre = input("Nombre (salir para terminar): ")
    if nombre == "salir":
        break

    edad = int(input("Edad: "))
    plan = input("Plan: ")

    if plan == "basico":
        precio = 50000
        basico += 1
    elif plan == "premium":
        precio = 90000
        premium += 1
    elif plan == "familiar":
        precio = 130000
        familiar += 1

    total += precio

    if edad < 18:
        print("Registro juvenil")
    if edad >= 60:
        print("Beneficio senior")

print("Total recaudado:", total)

if basico > premium and basico > familiar:
    print("Plan más vendido: basico")
elif premium > familiar:
    print("Plan más vendido: premium")
else:
    print("Plan más vendido: familiar")