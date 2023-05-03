from time import sleep
from os import system
import random

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

    def attack(self, target):
        damage = self.ataque - target.defensa
        if damage < 0:
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

class fight_system:
    def __init__(self, jugador):
        self.jugador = Human, Demon, Angel
        
    def start(self):
        for i in range(5):
            print(f"--- Turno {i+1} ---")
            for jugador in self.jugador:
                if jugador.vida <= 0:
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
                        if target != jugador and target.vida > 0:
                            print(f"{j+1}. {target.nombre}")
                    target = int(input()) - 1
                    jugador.attack(self.jugador[target])

                elif opcion == 2:
                    cantidad = random.randint(10, 30)
                    jugador.curar(cantidad)

                elif opcion == 3:
                    jugador.defenderse()
                    
                else:
                    print("Opción inválida. Pierdes tu turno.")
                    
            for jugador in self.jugadores:
                jugador.reset_defensa()
                    
        print("Fin del juego.")
        vivos = [jugador for jugador in self.jugadores if jugador.vida > 0]
        if len(vivos) == 1:
            print(f"{vivos[0].nombre} ha ganado.")
        else:
            print("¡Ha sido un empate!")
                

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