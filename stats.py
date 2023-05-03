from time import sleep
from os import system

#Aqui van a estar las bases de stats de las razas
class Individual:

    base_stats = {
        'human': {
            'hp': 150, 
            'Dexterity': 50,
            'mana': 50,
            'faith': 50,
            'dark': 50,
            'strenght': 150,
        },
        'demon': {
            'hp': 175, 
            'Dexterity': 75,
            'mana': 100,
            'faith': 0,
            'dark': 200,
            'strenght': 100,
        },
        'angel': {
            'hp': 200, 
            'Dexterity': 75,
            'mana': 125,
            'faith': 200,
            'dark': 0,
            'strenght': 100,
        }
    }


    def __init__(self, **options) -> None:
        self.hp: int = options.get("hp", None) or 150 
        self.Dexterity: int = options.get("Dexterity", None) or 50
        self.mana: int = options.get("mana", None) or 50
        self.faith: int = options.get("faith", None) or 50
        self.dark: int = options.get("darkness", None) or 50
        self.strenght: int = options.get("strenght", None) or 150

    def __repr__(self) -> str:
        return f"Hp: {self.hp}\n Stamina: {self.stamina}\n Mana: {self.mana}\n Faith: {self.faith}\n Darkness: { self.dark}\n Strenght: {self.strenght}\n"
    
    def attack (self, target):
        target.hp -= self.Dexterity

class Human(Individual):
    def __init__(self, **options) -> None:
        super().__init__(**super().base_stats['human'])

    def attack (self, target):
        target.hp -= self.strenght
        target.recibir_damage(self.attaque)
    
    def recib_attack(self, damage):
        self.hp -= damage
        print(f" you recib {damage} of damage")
        if self.hp  <= 0:
            print(f"haz muerto")

class Demon(Individual):
    def __init__(self, **options) -> None:
        super().__init__(**super().base_stats['demon'])

    def attack (self, target):
        target.hp -= self.dark
    
class Angel(Individual):
    def __init__(self, **options) -> None:
        super().__init__(**super().base_stats['angel'])
    
    def attack (self, target):
        target.hp -= self.faith

#Aqui va a estar el sistemas de combate

class combat:
    def __init__(self, jugador):
        self.jugador = Human, Demon, Angel

    def start(self):

        while not self.fin_del_comabte():
            for jugador in self.jugador:
                if self.fin_del_combate():
                    break
                print(f"Turn of {jugador}")
                delay = 2
                sleep(delay)
                print("Chosse the target: ")
                for i, objetivo in enumerate(self.jugador):
                    if jugador != objetivo and objetivo.vida > 0:
                        print(f"{i+1}. {objetivo}")
                



'''
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
'''