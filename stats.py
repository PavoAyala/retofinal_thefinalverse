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
        self.defense: int = options.get("defense", None) or 50
        self.mana: int = options.get("mana", None) or 50
        self.faith: int = options.get("faith", None) or 50
        self.dark: int = options.get("dark", None) or 50
        self.strength: int = options.get("strength", None) or 150

    def __repr__(self) -> str:
        return f"Hp: {self.hp}\nDefense: {self.defense}\nMana: {self.mana}\nFaith: {self.faith}\nDarkness: {self.dark}\nStrength: {self.strength}\n"
    
    def attack(self, target):
        damage = self.strength - target.defense
        if damage < 0:
            damage = 0
        target.receive_damage(damage)
        
    def receive_damage(self, damage):
        self.hp -= damage
        print(f"Received {damage} damage.")
        if self.hp <= 0:
            print("You are dead.")
            
    def heal(self, amount):
        self.hp += amount
        if self.hp > 100:
            self.hp = 100
        print(f"Healed {amount} life points.")
        
    def defend(self):
        self.defense += 5
        print("You are defending.")
        
    def reset_defense(self):
        self.defense = 0

class Human(Individual):
    def __init__(self, **options) -> None:
        super().__init__(**Individual.base_stats['human'])

class Demon(Individual):
    def __init__(self, **options) -> None:
        super().__init__(**Individual.base_stats['demon'])

class Angel(Individual):
    def __init__(self, **options) -> None:
        super().__init__(**Individual.base_stats['angel'])

class EnemyStats:
    enemy = {
        'hunter': {
            'hp': 110,
            'defense': 10,
            'mana': 30,
            'faith': 20,
            'dark': 20,
            'strength': 50,
        },
        'thief': {
            'hp': 120,
            'defense': 15,
            'mana': 90,
            'faith': 30,
            'dark': 30,
            'strength': 60,
        },
        'goblin': {
            'hp': 70,
            'defense': 5,
            'mana': 30,
            'faith': 0,
            'dark': 40,
            'strength': 30,
        },
        'knight': {
            'hp': 140,
            'defense': 50,
            'mana': 80,
            'faith': 80,
            'dark': 40,
            'strength': 100,
        },
        'dark knight': {
            'hp': 180,
            'defense': 100,
            'mana': 140,
            'faith': 120,
            'dark': 80,
            'strength': 160,
        },
        'boss holy knight': {
            'hp': 250,
            'defense': 180,
            'mana': 200,
            'faith': 180,
            'dark': 120,
            'strength': 200,
        },
        'skeletons': {
            'hp': 180,
            'defense': 120,
            'mana': 100,
            'faith': 0,
            'dark': 110,
            'strength': 80,
        },
        'malenia': {
            'hp': 300,
            'defense': 200,
            'mana': 190,
            'faith': 160,
            'dark': 60,
            'strength': 230,
        },
        'elden ghost': {
            'hp': 350,
            'defense': 240,
            'mana': 230,
            'faith': 300,
            'dark': 0,
            'strength': 200,
        }
    }

    def __init__(self, enemy_type, **options):
        stats = self.enemy.get(enemy_type)
        if stats is not None:
            self.hp = stats.get('hp', 150)
            self.defense = stats.get('defense', 50)
            self.mana = stats.get('mana', 50)
            self.faith = stats.get('faith', 50)
            self.dark = stats.get('dark', 50)
            self.strength = stats.get('strength', 150)
        else:
            raise ValueError(f"Invalid enemy type: {enemy_type}")

    def __repr__(self) -> str:
        return f"Hp: {self.hp}\nDefense: {self.defense}\nMana: {self.mana}\nFaith: {self.faith}\nDarkness: {self.dark}\nStrength: {self.strength}\n"

    def attack(self, target):
        damage = self.strength - target.defense
        if damage < 0:
            damage = 0
        target.receive_damage(damage)

    def receive_damage(self, damage):
        self.hp -= damage
        print(f"Received {damage} damage.")
        if self.hp <= 0:
            print("The enemy is defeated.")
            
    def heal(self, target):
        amount = random.randint(10, 30)
        target.heal(amount)
        print(f"{target} has been healed for {amount} HP.")
        
    def defend(self):
        self.defense += 5
        print("Defending!")

    def reset_defense(self):
        self.defense = 0


class Hunter(EnemyStats):
    def __init__(self, **options):
        super().__init__('hunter', **options)


class Thief(EnemyStats):
    def __init__(self, **options):
        super().__init__('thief', **options)


class Goblin(EnemyStats):
    def __init__(self, **options):
        super().__init__('goblin', **options)


class Knight(EnemyStats):
    def __init__(self, **options):
        super().__init__('knight', **options)


class DarkKnight(EnemyStats):
    def __init__(self, **options):
        super().__init__('dark knight', **options)


class BossHolyKnight(EnemyStats):
    def __init__(self, **options):
        super().__init__('boss holy knight', **options)


class Skeletons(EnemyStats):
    def __init__(self, **options):
        super().__init__('skeletons', **options)


class Malenia(EnemyStats):
    def __init__(self, **options):
        super().__init__('malenia', **options)


class EldenGhost(EnemyStats):
    def __init__(self, **options):
        super().__init__('elden ghost', **options)


class FightSystem:
    def __init__(self, player_type):
        if player_type == 'human':
            self.player = Human()
        elif player_type == 'demon':
            self.player = Demon()
        elif player_type == 'angel':
            self.player = Angel()
        else:
            raise ValueError("Invalid player type")

    def start(self):
        for i in range(1, 4):  # Número de turnos
            print(f"--- Turno {i} ---")
            if self.player.hp <= 0:
                print("You are defeated.")
                break

            print("It's your turn!")
            print("What action do you want to take?")
            print("1. Attack")
            print("2. Heal")
            print("3. Defend")
            option = int(input())

            if option == 1:
                print("Choose your target:")
                for j, target in enumerate(self.enemies):
                    if target.hp > 0:
                        print(f"{j + 1}. {target.__class__.__name__}")
                target_index = int(input()) - 1
                self.player.attack(self.enemies[target_index])

            elif option == 2:
                amount = random.choice([10, 30, 50, 70, 90, 110])
                self.player.heal(amount)

            elif option == 3:
                self.player.defend()

            else:
                print("Invalid option. You lose one turn.")

            for enemy in self.enemies:
                if enemy.hp > 0:
                    enemy.attack(self.player)
                else:
                    enemy.reset_defense()

        print("End of the fight.")
        alive_enemies = [enemy for enemy in self.enemies if enemy.hp > 0]
        if self.player.hp <= 0:
            print("You are defeated.")
        elif len(alive_enemies) == 0:
            print("You win!")
        else:
            print("It's a tie.")
                

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