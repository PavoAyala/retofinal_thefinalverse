from time import sleep
from os import system

class razas:
    print("------------Choose a class------------")
    delay = 1
    sleep(delay)
    system("cls")

    lang = input("Wich class are you going to choose for your new game?\nHumano\nDemonio\nAngel\n")

    #Crear las clases de cada personaje y los objetos como los son armas y enemigos
    
    match lang:
        case "Humano":
            print("You just woke up from a hundred years seep, is a dark place you are trapped somewhere so you push and get out from a coffin, ")


        case "Demonio":
            print("Bienvenido a este Mundo Demonio")


        case "Angel":
            print("Bienvenido a este Mundo Angel")