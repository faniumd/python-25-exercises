#2. Gimnasio: acceso por edad
#Un gimnasio ofrece clases según la edad:
#• menor de 13 → no puede ingresar
#• de 13 a 17 → clase juvenil
#• de 18 a 59 → clase general
#• 60 o más → clase senior
#Pide la edad de una persona y muestra a qué grupo pertenece.
#Practica: if, elif, else.

print("BIENVENIDO AL SCHEDULE DE CLASES DEL GYM WARRIOR X")
print("APARTA TU CLASE SEGUN TU EDAD FACILMENTE, CON NUESTRA APP!")

try :
  
  edadUsu=int(input("INGRESE SU EDAD PARA COMPROBAR_:"))

  if edadUsu <13 :
     print(" 🚫 EDAD NO VALIDAD PARA INSCRIPCION. LO SENTIMOS 🥺 ")

  elif edadUsu >=13 and edadUsu <=17:
     print("PERFECTO!! SU EDAD ENTRA EN EL RANGO OPORTUNO ✅, PARA EL GRUPO DE LA CLASE JUVENIL")

  elif edadUsu >=18 and edadUsu <=59:
     print("PERFECTO!! SU EDAD ENTRA EN EL RANGO OPORTUNO ✅, PARA EL GRUPO DE LA CLASE GENERAL")   
  
  elif edadUsu >=60:
     print("PERFECTO!! SU EDAD ENTRA EN EL RANGO OPORTUNO ✅, PARA EL GRUPO DE LA CLASE SENIOR")


except ValueError:
    print("Ingrese un valor valido porfavor")