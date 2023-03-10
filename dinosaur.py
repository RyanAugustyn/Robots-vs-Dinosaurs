from random import randrange
from robot import Robot

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = int(attack_power)
        self.health = 30
    
    def attack(self, robot):
        attack_damage = randrange(0,3) * self.attack_power
        if attack_damage == 0:
            print(f"{self.name} the dinosaur misses!\n")
        else:
            print(f"{self.name} the dinosaur hits for {attack_damage} damge")
            robot.health -= attack_damage
            if robot.health < 0:
                robot.health = 0
            print(f"{robot.name} the robot currently has {robot.health} health remaining\n\n")

