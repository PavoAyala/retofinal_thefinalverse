from msilib.schema import SelfReg
from time import sleep
from os import system
import stats
delay = 1
lang = input("----Wich class are you going to choose for your new game?----\n\t\t\t[Human]\n\t\t\t[Demon]\n\t\t\t[Angel]\n-------------------------------------------------------------\n")
match lang:
    case "Human":
        print("You just woke up from a hundred years sleep, is a dark place you are trapped somewhere so you push and get out from a coffin. ")
        sleep(delay)
        print("You are in the middle of a snowy forest it is to cold for you soyou start lookin around and you see a cabin and you peek in and see some Hunters, what are you going to do?")
        sleep(delay)
        lang2 = input("What are you going to do?\n\t\t\t[1.- You go fight the Hunters]\n\t\t\t[2.- You go searchin for another place to shellter]")
        #while lang2 == "1":
                