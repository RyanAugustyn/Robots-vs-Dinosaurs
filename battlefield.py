from random import randrange

from robot import Robot
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.display_welcome()
        #check for single or fleet of robots
        user_input = int(input("Would you like a single robot or a fleet of 3 robots to fight one at a time?"
        "\nChoose 1 for single, 2 for fleet\n"))
        if user_input < 1 or user_input > 2: 
            print("Invalid input, choice randomly made...")
            user_input = randrange(1,3)
        if user_input == 1:
            self.robot = Robot(input("Please enter a Robot name: \n"), input("Please choose a "
                "robot weapon,' your choices are\n1 for Robot Nunchucks\n2 for Yamato Gun"
                "\n3 for Laser Staff\nEnter input:   "))
        elif user_input == 2:
            self.robot_list = Fleet()
        #choose single or herd of dinosaurs 
        user_input = int(input("Would you like a single dinosaur or a herd of 3 dinosaurs to fight one at a time?"
        "\nChoose 1 for single, 2 for herd\n"))
        if user_input < 1 or user_input > 2: 
            print("Invalid input, choice randomly made...")
            user_input = randrange(1,3)
        if user_input == 1:
            self.dinosaur = Dinosaur(input("Please choose the dinosaur's name:\n"), int(input("Please "
            " choose the dinosaur's power level:\n")))
        elif user_input == 2:
            self.dinosaur_list = Herd()
    
    def run_game(self):
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("\nWelcome to Robot vs Dinosaur!\n")
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
            print(f"{self.robot.name} the robot has won the battle!\n")
        elif self.robot.health <= 0 and self.dinosaur.health > 0:
            print(f"{self.dinosaur.name} the dinosaur has won the battle!\n")
    