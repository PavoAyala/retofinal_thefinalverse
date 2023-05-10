from random import randint, choice

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
    
    
        
    def receive_damage(self, damage):
        self.hp -= damage
        print(f"Received {damage} damage.")
        if self.hp <= 0:
            print("You are dead.")
            
    def heal(self, target):
        amount = randint(10, 30, 50, 70, 90, 110)
        target.heal(amount)
        print(f"{target} has been healed for {amount} HP.")
        
    def defend(self):
        self.defense += 5
        print("You are defending.")
        
    def reset_defense(self):
        self.defense = 0
 
class Human(Individual):
    def __init__(self, **options) -> None:
        super().__init__(**Individual.base_stats['human'])

    def attack(self, target):
        damage = self.strength - target.defense
        if damage < 0:
            damage = 0
        target.receive_damage(damage)

class Demon(Individual):
    def __init__(self, **options) -> None:
        super().__init__(**Individual.base_stats['demon'])
    
    def attack(self, target):
        damage = self.dark - target.defense
        if damage < 0:
            damage = 0
        target.receive_damage(damage)

class Angel(Individual):
    def __init__(self, **options) -> None:
        super().__init__(**Individual.base_stats['angel'])
    
    def attack(self, target):
        damage = self.faith - target.defense
        if damage < 0:
            damage = 0
        target.receive_damage(damage)

class Enemy:
    enemy_stats = {
        'hunter': {
            'hp': 110,
            'defense': 10,
            'mana': 30,
            'faith': 20,
            'dark': 20,
            'strength': 50,
        },
        'goblin': {
            'hp': 70,
            'defense': 5,
            'mana': 30,
            'faith': 0,
            'dark': 40,
            'strength': 30,
        },
        'fallenangel': {
            'hp': 180,
            'defense': 120,
            'mana': 100,
            'faith': 0,
            'dark': 110,
            'strength': 80,
        },
        'skeletons': {
            'hp': 180,
            'defense': 120,
            'mana': 100,
            'faith': 0,
            'dark': 110,
            'strength': 80,
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

    def __init__(self, enemy_type):
        stats = self.enemy_stats.get(enemy_type)
        if stats is not None:
            self.enemy_type = enemy_type.title()
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
        amount = randint(10, 30)
        target.heal(amount)
        print(f"{target} has been healed for {amount} HP.")
        
    def defend(self):
        self.defense += 5
        print("Defending!")

    def reset_defense(self):
        self.defense = 0


class Hunter(Enemy):
    def __init__(self, **options):
        super().__init__('hunter', **options)


class Goblin(Enemy):
    def __init__(self, **options):
        super().__init__('goblin', **options)

class FallenAngel(Enemy):
    def __init__(self, **options):
        super().__init__('fallenangel', **options)

class Skeletons(Enemy):
    def __init__(self, **options):
        super().__init__('skeletons', **options)


class EldenGhost(Enemy):
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
        for i in range(1, 3):  # Número de turnos
            print(f"--- Turno {i} ---")
            if self.player.hp <= 0:
                print("You are defeated.")
                break

            print("It's your turn!")
            print("What action do you want to take?")
            print("1. Attack")
            print("2. Heal")
            print("3. Defend")
            print("-----------------------------------------")
            option = int(input())

            self.enemies = (Enemy('hunter'), Enemy('goblin'), Enemy('skeletons'))

            if option == 1:
                for index, target in enumerate(self.enemies):
                    if target.hp > 0:
                        print(f"{index + 1}. {target.enemy_type}")
                target_index = int(input()) - 1
                self.player.attack(self.enemies[target_index])

            elif option == 2:
                amount = choice([10, 30, 50, 70, 90, 110])
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