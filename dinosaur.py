from random import randrange
from robot import Robot #circular import error ?

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
    
    def attack(self, robot):
        attack_damage = randrange(0,3) * self.attack_power
        if attack_damage == 0:
            print(f"{self.name} the dinosaur misses!\n")
        else:
            print(f"Dinosaur hits for {attack_damage} damge")
            robot.health -= attack_damage
            print(f"{robot.name} currently has {robot.health} health remaining\n\n")

