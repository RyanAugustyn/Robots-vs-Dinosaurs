from random import range
from robot import Robot

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
    
    def attack(self, robot):
        attack_damage = range(0,3) * self.attack_power
        if attack_damage == 0:
            print("Dinosaur misses!")
        else:
            print(f"Dinosaur hits for {attack_damage} damge")
            robot.health -= attack_damage

