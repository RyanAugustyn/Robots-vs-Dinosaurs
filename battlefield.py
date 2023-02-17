from random import randrange

from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot("MegaWeapon", "Robot Nunchucks")
        self.dinosaur = Dinosaur("Ted", 5)
    
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
            print("Robot strikes first!")
            while self.robot.health > 0 and self.dinosaur.health > 0:
                self.robot.attack()
                self.dinosaur.attack()
        if random == 2:
            print("Dinosaur strikes first!")
            while self.robot.health > 0 and self.dinosaur.health > 0:
                self.dinosaur.attack()
                self.robot.attack()

    def display_winner(self):
        if self.robot.health > 0 and self.dinosaur.health <= 0:
            print(f"{self.robot.name} has won the battle!")
        elif self.robot.health <= 0 and self.dinosaur.health > 0:
            print(f"{self.dinosaur.name} has won the battle!")
        else:
            print("They have both perished! Oh the monstermainity!")
    