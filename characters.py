from msilib.schema import SelfReg
from time import sleep
from os import system
from stats import fight_system
import sys

delay = 1
print("---------Bienvenido a nuestro mundo--------")
sleep(delay)
input("Presione una tecla para continuar...")

system('cls')

delay = 4
lang = input("----Wich class are you going to choose for your new game?----\n\t\t\t[Human]\n\t\t\t[Demon]\n\t\t\t[Angel]\n-------------------------------------------------------------\n")
print("You just woke up from a hundred years sleep, is a dark place you are trapped somewhere so you push and get out from a coffin. ")
sleep(delay)
print("You are in the middle of a snowy forest it is to cold for you soyou start lookin around and you see a cabin and you peek in and see some Hunters.")
sleep(delay)
lang2 = input("What are you going to do?\n\t\t\t[1.- You go fight the Hunters]\n\t\t\t[2.- You go searchin for another place to shellter]")
if lang2 == "1":
        fight_system
        system("cls")
        print("You have defeated the hunters, you stay inside the shellter a few hours to sleep")
        sleep(delay)
                        
elif lang2 == "2":
    print("You found another cabain so you stay a few hours to sleep")

print("YOU WOKE UP, something loud woke you, you start lookin around in the middle of the night to see what was it")
sleep(delay)
print("You find some big guy comming for you, he is covered in flames, you need to fight him.")
sleep(delay)
#pelea
print("You destroyed that guy so you run to see his things and you find the godslayer sword")
sleep(delay)
print("With this sword you can defeat the elden ghost that is in the deep of the forest")
sleep(delay)
print("YoU start your way into the forest and manage to find a angel")
print("These angels aren't what they seem to be")
sleep(delay)
print("He starts attackin you but you manage to dodge his attacks")
sleep(delay)
#pelea
system("cls")
print("The way this angel acts is like if he wasn't in control")
sleep(delay)
print("You start lookin at him and you saw that he has no pupils, he was super pale, it's like if he was dead for a very long time.")
sleep(delay)
print("You decide to continiue your quest to look for the elden ghost")
sleep(delay)
print("You started walking and walking so you see an old house so you decide to explore it")
sleep(delay)
print("In this house you found a book")
print("in this book you found everything from the elden ghost and everything that he has done to other humans")
sleep(delay)
print("You need to fight him and defeat him, he does not deserve to live")
sleep(delay)
print("You got out of the house and some squeletons are waiting for you, Defeat them")
#pelea
system("cls")
print("You are super tired of fighting all day, you need to start lookin for a place to sleep")
print("You start lookin for a cabin, you walk for some time so yo decide to start a fire and sleep outside")
sleep(delay)
print("You wake up and decide to look for the elden ghost")
sleep(delay)
print("The book says that the elden ghost makes a silbing noise when he is near")
sleep(delay)
print("You start walkin and you found a cave with some signs and some ilustrations from the book")
sleep(delay)
print("You get into the cave and found a bunch of dead bodies on the floor")
sleep(delay)
print("You walk deeper into the cave, and you find some goblins takin the armour from the bodies")
print("They saw you so you fight them")
sleep(delay)
#Fight         
system("cls")
print("You saw that a lot of enemies are running to you so you prepared to fight all of them")
print("But they run pass you, if like they were running from someone")
print("You hear the silbing noise, its a scary whithe silbing that horrifies you.")
print("You need to fight that thing")
#fight
system("cls")
print("You have defeated the elden ghost you are now free")
print("End of the Game")

sys.exit()