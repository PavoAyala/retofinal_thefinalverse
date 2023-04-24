from msilib.schema import SelfReg
from time import sleep
from os import system


print("------------Choose a class------------")
delay = 2
sleep(delay)
#system("cls")
print(".")
print(".")
print(".")


lang = input("Wich class are you going to choose for your new game?\nHuman\nDemon\nAngel\n.\n.\n")



    #Crear las clases de cada personaje y los objetos como los son armas y enemigos



match lang:
    case "Human":
        print("You just woke up from a hundred years sleep, is a dark place you are trapped somewhere so you push and get out from a coffin. ")
        sleep(delay)
        print("You are in the middle of a snowy forest it is to cold for you soyou start lookin around and you see a cabin and you peek in and see some demons, what are you going to do?")
        sleep(delay)
        lang2 = input("Que quieres hacer?")
        


    case "Demon":
        print("-Wake up you stupid demon-")
        sleep(delay)
        print("You are in a very hot place, you are in the ground cover with flames and you only have one job, TO ^SUFFER^, You have orders to discover new lands to get to the holy castle and you can take two ways the suffering river or the forest of pain, Wich way would you go?")


    case "Angel":
        print("-!!HEY!!")
        sleep(delay)
        print("-What are you doing?")
        sleep(delay)
        print("-You should be guarding the forest not sleeping here")
        sleep(delay)
        print("-Get up, NOW")
        sleep(delay)
        print("You are in an very windy place outside the holy region you are up in the sky in a forest wich is floating in the sky by clouds like all the holy kingdom.")
        sleep(delay)
        print("Wait you heard something is humans trying to pass into the holy forest you need to defend it.")
    

class Conect_History:

    #Aqui se creara la historia que conecta a las 3 razas
    print("")