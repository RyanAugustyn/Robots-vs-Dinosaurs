from random import randrange
from weapon import Weapon

class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon(weapon)

    def attack(self, dinosaur):
        attack_damage = randrange(0,3) * self.active_weapon.attack_power
        if attack_damage == 0:
            print("Robot misses!\n")
        else:
            print(f"Robot hits for {attack_damage} damge")
            dinosaur.health -= attack_damage
            print(f"{dinosaur.name} currently has {dinosaur.health} health remaining\n\n")
