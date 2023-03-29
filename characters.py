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
delay = 1
sleep(delay)
system("cls")

lang = input("Wich class are you going to choose for your new game?\nHumano\nDemonio\nAngel\n")

    #Crear las clases de cada personaje y los objetos como los son armas y enemigos
    
match lang:
    case "Humano":
        print("You just woke up from a hundred years sleep, is a dark place you are trapped somewhere so you push and get out from a coffin. ")
        print("You are in the middle of a snowy forest it is to cold for you soyou start lookin around and you see a cabin and you peek in and see some demons, what are you going to do?")


    case "Demonio":
        print("-Wake up you stupid demon-")
        print("You are in a very hot place, you are in the ground cover with flames and you only have one job, TO ^SUFFER^, You have orders to discover new lands to get to the holy castle and you can take two ways the suffering river or the forest of pain, Wich way would you go?")


    case "Angel":
        print("-!!HEY!!")
        print("-What are you doing?")
        print("-You should be guarding the forest not sleeping here")
        print("-Get up, NOW")
        print("You are in an very windy place outside the holy region you are up in the sky in a forest wich is floating in the sky by clouds like all the holy kingdom.")
        print("Wait you heard something is humans trying to pass into the holy forest you need to defend it.")