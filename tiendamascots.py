#5. Tienda de mascotas: alimento por tipo de animal
#Pide el tipo de mascota:
#• perro
#• gato
#• conejo
#Luego muestra una recomendación de alimento según el animal.
#Practica: comparaciones con texto

animal = input("Tipo de mascota: ")

if animal == "perro":
    print("Recomendado: concentrado para perro")
elif animal == "gato":
    print("Recomendado: comida para gato")
elif animal == "conejo":
    print("Recomendado: zanahoria y heno")
else:
    print("Mascota no registrada")