from msilib.schema import SelfReg
from time import sleep
from os import system


delay = 1

lang = input("----Wich class are you going to choose for your new game?----\n\t\t\t[Human]\n\t\t\t[Demon]\n\t\t\t[Angel]\n-------------------------------------------------------------\n")

match lang:
    case "Human":
        print("You just woke up from a hundred years sleep, is a dark place you are trapped somewhere so you push and get out from a coffin. ")
        sleep(delay)
        print("You are in the middle of a snowy forest it is to cold for you soyou start lookin around and you see a cabin and you peek in and see some demons, what are you going to do?")
        sleep(delay)
        lang2 = input("What are you going to do?\n\t\t\t[1. You go fight the demons]\n\t\t\t[2. You go find another place to find shellter] \n-----------------------------------------------------------------------------------------------------\n")
        if (lang2 == 1):
            print("You go to see the demons to fight them")
        else:
            print("You go to explore another shelter to hide")


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