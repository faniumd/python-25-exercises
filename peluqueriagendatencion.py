"""17. Peluquería: agenda de atención
Una peluquería atiende 7 clientes al día.
Por cada cliente pedir:
• nombre
• servicio solicitado: corte, cepillado, tintura
• valor pagado
Al final mostrar:
• total del día
• cantidad de clientes por servicio
• servicio más solicitado
Practica: contadores, acomusladores, comparaciones"""

total = 0
corte = 0
cepillado = 0
tintura = 0

for i in range(7):
    nombre = input("Nombre: ")
    servicio = input("Servicio: ")
    valor = int(input("Valor: "))

    total += valor

    if servicio == "corte":
        corte += 1
    elif servicio == "cepillado":
        cepillado += 1
    elif servicio == "tintura":
        tintura += 1

print("Total del dia:", total)

if corte > cepillado and corte > tintura:
    print("Servicio más pedido: corte")
elif cepillado > tintura:
    print("Servicio más pedido: cepillado")
else:
    print("Servicio más pedido: tintura")