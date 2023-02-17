from random import range 
from weapon import Weapon

class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 100
        self.active_weapon = weapon.attack_power

    def attack(self, dinosaur):
        attack_damage = range(0,3) * self.attack_power
        if attack_damage == 0:
            print("Robot misses!")
        else:
            print(f"Robot hits for {attack_damage} damge")
            dinosaur.health -= attack_damage
