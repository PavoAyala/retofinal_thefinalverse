from time import sleep
from os import system
#from playsound import playsound

delay = 1
print("---------Bienvenido a nuestro mundo--------")
sleep(delay)
input("Presione una tecla para continuar...")

#profe ya me case me dare de baja de la carrera atte: Pablo
system('cls')

lang = input("Cual es la cuenta que quieres usar? \ncuenta1\ncuenta2\ncuenta3\n ")


match lang:
    case "cuenta1":
        print("Bienvenido a tu nueva cuenta.")


    case "cuenta2":
        print("Bienvenido a tu nueva cuenta.")

    case "cuenta3":
        print("Bienvenido a tu nueva cuenta.")
    