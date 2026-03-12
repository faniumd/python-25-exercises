"""15. Parqueadero: control de vehículos
Registrar 8 vehículos en un parqueadero.
Por cada uno pedir:
• placa
• tipo: carro o moto
• horas parqueado
Tarifas:
• carro: 4000 por hora
• moto: 2000 por hora
Al final mostrar:
• total recaudado
• cuántos carros ingresaron
• cuántas motos ingresaron
• cuál vehículo pagó más
Practica: ciclos, máximos, acumuldores."""


total = 0
carros = 0
motos = 0

max_pago = 0
max_placa = ""

for i in range(8):
    placa = input("Placa: ")
    tipo = input("Tipo (carro/moto): ")
    horas = int(input("Horas: "))

    if tipo == "carro":
        pago = horas * 4000
        carros += 1
    else:
        pago = horas * 2000
        motos += 1

    total += pago

    if pago > max_pago:
        max_pago = pago
        max_placa = placa

print("Total recaudado:", total)
print("Carros:", carros)
print("Motos:", motos)
print("Pago más alto:", max_placa, max_pago)

