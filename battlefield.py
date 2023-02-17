from random import randrange

from robot import Robot
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.display_welcome()
        #initialize lists of combatant(s)
        self.robot_list = []
        self.dinosaur_list = []
        #check for single or fleet of robots
        #if single, append choice to list, otherwise load list from fleet.py and herd.py
        user_input = int(input("Would you like a single robot or a fleet of 3 robots to fight one at a time?"
        "\nChoose 1 for single, 2 for fleet\n"))
        if user_input < 1 or user_input > 2: 
            print("Invalid input, choice randomly made...")
            user_input = randrange(1,3)
        if user_input == 1:
            self.robot = Robot(input("Please enter a Robot name: \n"), input("Please choose a "
                "robot weapon,' your choices are\n1 for Robot Nunchucks\n2 for Yamato Gun"
                "\n3 for Laser Staff\nEnter input:   "))
            self.robot_list.append(self.robot)
        elif user_input == 2:
            fleet = Fleet()
            self.robot_list = fleet.list
        #choose single or herd of dinosaurs 
        user_input = int(input("Would you like a single dinosaur or a herd of 3 dinosaurs to fight one at a time?"
        "\nChoose 1 for single, 2 for herd:\n"))
        if user_input < 1 or user_input > 2: 
            print("Invalid input, choice randomly made...")
            user_input = randrange(1,3)
        if user_input == 1:
            self.dinosaur = Dinosaur(input("Please choose the dinosaur's name:\n"), int(input("Please "
            " choose the dinosaur's power level:\n")))
            self.dinosaur_list.append(self.dinosaur)
        elif user_input == 2:
            herd = Herd()
            self.dinosaur_list = herd.list
    
    def run_game(self):
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("\nWelcome to Robot vs Dinosaur!\n")


        #win condition is if list is empty
        #check through list if class.health below zero, if yes remove from list
    def battle_phase(self):
        #choose who attacks first
        random = randrange(1,2)
        if random == 1:
            print(f"Team robot strikes first!")
            while self.robot_list != [] and self.dinosaur_list != []:
                self.robot_list[0].attack(self.dinosaur_list[0])
                if self.dinosaur_list[0].health <= 0:
                    print(f"{self.dinosaur_list[0]} has been defeated!\n")
                    del self.dinosaur_list[0]
                elif self.dinosaur_list[0].health >= 0:
                    self.dinosaur_list[0].attack(self.robot_list[0])
        if random == 2:
            print(f"Team dinosaur strikes first!")
            while self.robot_list != [] and self.dinosaur_list != []:
                self.dinosaur_list[0].attack(self.robot_list[0])
                if self.robot_list[0].health <= 0:
                    print(f"{self.robot_list[0]} has been defeated!\n")
                    del self.robot_list[0]
                elif self.robot_list[0].health >= 0:
                    self.robot.attack(self.dinosaur_list[0])

    def display_winner(self):
        if self.robot_list != [] and self.dinosaur_list == []:
            print(f"Team robot has won the battle!\n")
        else:
            print("Team dinosaur has won the battle!\n")
    