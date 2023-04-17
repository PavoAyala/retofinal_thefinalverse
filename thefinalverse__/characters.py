from msilib.schema import SelfReg
from time import sleep
from os import system

#Aqui van a estar las bases de stats de las razas

class Human:
    def __init__(self, **options) -> None:
        self.hp: int = options.get("hp", None) or 150 
        self.Dexterity: int = options.get("Dexterity", None) or 50
        self.mana: int = options.get("mana", None) or 50
        self.faith: int = options.get("faith", None) or 50
        self.dark: int = options.get("darkness", None) or 50
        self.strenght: int = options.get("strenght", None) or 150

    def __repr__(self) -> str:
        return f"Hp: {self.hp}\n Stamina: {self.stamina}\n Mana: {self.mana}\n Faith: {self.faith}\n Darkness: { self.dark}\n Strenght: {self.strenght}\n"

class Demon:
    def __init__(self, **options) -> None:
         self.hp: int = options.get("hp", None) or 175 
         self.Dexterity: int = options.get("Dexterity", None) or 75
         self.mana: int = options.get("mana", None) or 100
         self.faith: int = options.get("faith", None) or 0
         self.dark: int = options.get("darkness", None) or 200
         self.strenght: int = options.get("strenght", None) or 100

    def __repr__(self) -> str:
        return f"Hp: {self.hp}\n Stamina: {self.stamina}\n Mana: {self.mana}\n Faith: {self.faith}\n Darkness: { self.dark}\n Strenght: {self.strenght}\n"


class Angel:
    def __init__(self, **options) -> None:
         self.hp: int = options.get("hp", None) or 200 
         self.Dexterity: int = options.get("Dexterity", None) or 75
         self.mana: int = options.get("mana", None) or 125
         self.faith: int = options.get("faith", None) or 200
         self.dark: int = options.get("darkness", None) or 0
         self.strenght: int = options.get("strenght", None) or 100

    def __repr__(self) -> str:
        return f"Hp: {self.hp}\n Stamina: {self.stamina}\n Mana: {self.mana}\n Faith: {self.faith}\n Darkness: { self.dark}\n Strenght: {self.strenght}\n"


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