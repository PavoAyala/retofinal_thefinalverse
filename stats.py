from time import sleep
from os import system
import random

#Aqui van a estar las bases de stats de las razas
class Individual:

    base_stats = {
        'human': {
            'hp': 150, 
            'defense': 50,
            'mana': 50,
            'faith': 50,
            'dark': 50,
            'strenght': 150,
        },
        'demon': {
            'hp': 175, 
            'defense': 75,
            'mana': 100,
            'faith': 0,
            'dark': 200,
            'strenght': 100,
        },
        'angel': {
            'hp': 200, 
            'defense': 75,
            'mana': 125,
            'faith': 200,
            'dark': 0,
            'strenght': 100,
        }
    }


    def __init__(self, **options) -> None:
        self.hp: int = options.get("hp", None) or 150 
        self.Defense: int = options.get("defense", None) or 50
        self.mana: int = options.get("mana", None) or 50
        self.faith: int = options.get("faith", None) or 50
        self.dark: int = options.get("darkness", None) or 50
        self.strenght: int = options.get("strenght", None) or 150

    def __repr__(self) -> str:
        return f"Hp: {self.hp}\n Defense: {self.Defense}\n Mana: {self.mana}\n Faith: {self.faith}\n Darkness: { self.dark}\n Strenght: {self.strenght}\n"
    
    def attack (self, target):
        target.hp -= self.Defense

    def attack(self, target):
        damage = self.attack - target.Defense
        if damage < 0 - target.Defense:
            damage = 0
        target.recib_damage(damage)
        
    def recib_damage(self, damage):
        self.hp -= damage
        print(f"recib {damage} of damage.")
        if self.hp <= 0:
            print(f"You are Dead")
            
    def curar(self, amount):
        self.hp += amount
        if self.hp > 100:
            self.hp = 100
        print(f"has been cured {amount} life points.")
        
    def defenderse(self):
        self.defensa = 5
        print(f"¡it's defending!.")
        
    def reset_defensa(self):
        self.defensa = 0

class Human(Individual):
    def __init__(self, **options) -> None:
        super().__init__(**super().base_stats['human'])
    
    def attack(self, target):
        target.hp -= self.strenght

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

#Stats de los enemigos y boses

class enemy_stats:

    enemy = {

        'hunter': {
            'hp': 110, 
            'defense': 10,
            'mana': 30,
            'faith': 20,
            'dark': 20,
            'strenght': 50,
        },
        'thieve': {
            'hp': 120, 
            'defense': 15,
            'mana': 90,
            'faith': 30,
            'dark': 30,
            'strenght': 60,
        },
        'goblin': {
            'hp': 70, 
            'defense': 5,
            'mana': 30,
            'faith': 0,
            'dark': 40,
            'strenght': 30,
        },
        'knight':{
            'hp': 140, 
            'defense': 50,
            'mana': 80,
            'faith': 80,
            'dark': 40,
            'strenght': 100,
        },
        'dark knigh':{
            'hp': 180, 
            'defense': 100,
            'mana': 140,
            'faith': 120,
            'dark': 80,
            'strenght': 160,
        },
        ' boss holy knight':{
            'hp': 250, 
            'defense': 180,
            'mana': 200,
            'faith': 180,
            'dark': 120,
            'strenght': 200,
        }, 
        'esqueletons':{
            'hp': 180, 
            'defense': 120,
            'mana': 100,
            'faith': 0,
            'dark': 110,
            'strenght': 80,
        },
        'malenia':{
            'hp': 300, 
            'defense': 200,
            'mana': 190,
            'faith': 160,
            'dark': 60,
            'strenght': 230,
        },
        'God':{
            'hp': 350, 
            'defense': 240,
            'mana': 230,
            'faith': 300,
            'dark': 0,
            'strenght': 200,
        },
        'Demon King':{
            'hp': 350, 
            'defense': 240,
            'mana': 230,
            'faith': 0,
            'dark': 300,
            'strenght': 200,
        }
    }

    def __init__(self, **options) -> None:
        self.hp: int = options.get("hp", None) or 150 
        self.Defense: int = options.get("defense", None) or 50
        self.mana: int = options.get("mana", None) or 50
        self.faith: int = options.get("faith", None) or 50
        self.dark: int = options.get("darkness", None) or 50
        self.strenght: int = options.get("strenght", None) or 150

    def __repr__(self) -> str:
        return f"Hp: {self.hp}\n Defense: {self.Defense}\n Mana: {self.mana}\n Faith: {self.faith}\n Darkness: { self.dark}\n Strenght: {self.strenght}\n"
    
    def attack (self, target):
        target.hp -= self.Defense

    def attack(self, target):
        damage = self.attack - target.Defense
        if damage < 0 - target.Defense:
            damage = 0
        target.recib_damage(damage)
        
    def recib_damage(self, damage):
        self.hp -= damage
        print(f"recib {damage} of damage.")
        if self.hp <= 0:
            print(f"You are Dead")
            
    def curar(self, amount):
        self.hp += amount
        if self.hp > 100:
            self.hp = 100
        print(f"has been cured {amount} life points.")
        
    def defenderse(self):
        self.defensa = 5
        print(f"¡it's defending!.")
        
    def reset_defensa(self):
        self.defensa = 0

class hunter(enemy_stats):
    def __init__(self, **options) -> None:
        super().__init__(**super().enemy['hunter'])

class thieve(enemy_stats):
    def __init__(self, **options) -> None:
        super().__init__(**super().enemy['thieve'])

class goblin(enemy_stats):
    def __init__(self, **options) -> None:
        super().__init__(**super().enemy['goblin'])

class knight(enemy_stats):
    def __init__(self, **options) -> None:
        super().__init__(**super().enemy['knight'])

class dark_knight(enemy_stats):
    def __init__(self, **options) -> None:
        super().__init__(**super().enemy['datk knight'])

class boss_holy_knight(enemy_stats):
    def __init__(self, **options) -> None:
        super().__init__(**super().enemy['boss holy knight'])

class esqueletons(enemy_stats):
    def __init__(self, **options) -> None:
        super().__init__(**super().enemy['esqueletons'])

class malenia(enemy_stats):
    def __init__(self, **options) -> None:
        super().__init__(**super().enemy['malenia'])

class god(enemy_stats):
    def __init__(self, **options) -> None:
        super().__init__(**super().enemy['god'])

class demon_king(enemy_stats):
    def __init__(self, **options) -> None:
        super().__init__(**super().enemy['demon king'])
    
#Aqui va a estar el sistemas de combate

class fight_system:
    def __init__(self, jugador):
        self.jugador = Human, Demon, Angel
        
    def start(self):
        for i in range():
            print(f"--- Turno {i+1} ---")
            for jugador in self.jugador:
                if jugador.hp <= 0:
                    continue
                print(f"!Es tu turno¡")
                print("¿Qué acción deseas realizar?")
                print("1. Atacar")
                print("2. Curar")
                print("3. Defenderse")
                opcion = int(input())
                if opcion == 1:
                    print("Elige a quién atacar:")
                    for j, target in enumerate(self.jugador):
                        if target != jugador and target.hp > 0:
                            print(f"{j+1}. {target.nombre}")
                    target = int(input()) - 1
                    jugador.attack(self.jugador[target])

                elif opcion == 2:
                    cantidad = random.randint(10, 30, 50, 70, 90, 110, 300)
                    jugador.curar(cantidad)

                elif opcion == 3:
                    jugador.defenderse()
                    
                else:
                    print("invalid opcion. you lose one turn")
                    
            for jugador in self.jugador:
                jugador.reset_defensa()
                    
        print("En of the fight")
        vivos = [jugador for jugador in self.jugador if jugador.hp > 0]
        if len(vivos) == 1:
            print(f"{vivos[0]} you win.")
        else:
            print("¡it's a tie!")
                

'''
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
                        print(f"{i+1}. {objetivo}")'''
                



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