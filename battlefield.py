from random import randrange

from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot(input("Please enter a Robot name: "), input("Please choose a \
            robot weapon,' your choices are\n1 for Robot Nunchucks\n2 for Yamato Gun\
                \n3 for Laser Staff"))
        self.dinosaur = Dinosaur(input("Please choose the dinosaur's name"), int(input("Please \
            choose the dinosaur's power level")))
    
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("Welcome to Robot vs Dinosaur\n\n")
    def battle_phase(self):
        #choose who attacks first
        random = randrange(1,2)
        if random == 1:
            print(f"{self.robot.name} strikes first!")
            while self.robot.health > 0 and self.dinosaur.health > 0:
                self.robot.attack(self.dinosaur)
                if self.dinosaur.health <= 0:
                    break
                self.dinosaur.attack(self.robot)
        if random == 2:
            print(f"{self.dinosaur.name} strikes first!")
            while self.robot.health > 0 and self.dinosaur.health > 0:
                self.dinosaur.attack(self.robot)
                if self.robot.health <= 0:
                    break
                self.robot.attack(self.dinosaur)

    def display_winner(self):
        if self.robot.health > 0 and self.dinosaur.health <= 0:
            print(f"{self.robot.name} has won the battle!")
        elif self.robot.health <= 0 and self.dinosaur.health > 0:
            print(f"{self.dinosaur.name} has won the battle!")
        else:
            print("They have both perished! Oh the monstermainity!")
    