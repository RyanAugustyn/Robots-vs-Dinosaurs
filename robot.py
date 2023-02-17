from random import randrange
from weapon import Weapon

class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon(weapon)

    def attack(self, dinosaur):
        chance = randrange(0, 100)
        #check for hit chance
        if self.active_weapon.hit_chance < chance:
            print(f"{self.name} the robot misses!\n")  
        elif chance > 95:
            print("CRITICAL HIT!!")
            attack_damage = 5 * self.active_weapon.attack_power 
            print(f"{self.name} the robot hits for {attack_damage} damge")
            dinosaur.health -= attack_damage
            print(f"{dinosaur.name} currently has {dinosaur.health} health remaining\n\n")
        else:
            attack_damage = randrange(1,3) * self.active_weapon.attack_power 
            print(f"{self.name} the robot hits for {attack_damage} damge")
            dinosaur.health -= attack_damage
            print(f"{dinosaur.name} currently has {dinosaur.health} health remaining\n\n")
