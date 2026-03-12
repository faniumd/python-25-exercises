"""9. Spa: servicio disponible
En un spa hay estos servicios:
• masaje
• facial
• manicure
Pide al usuario qué servicio desea y muestra un mensaje confirmando
si existe o no.
Practica: condicionales con texto."""

servicio = input("Servicio: ")

if servicio == "masaje":
    print("Servicio disponible")
elif servicio == "facial":
    print("Servicio disponible")
elif servicio == "manicure":
    print("Servicio disponible")
else:
    print("Servicio no existe")