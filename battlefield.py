from random import randrange
from time import sleep

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
                 
    def run_game(self):
        self.choose_game_type()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("\nWelcome to Robot vs Dinosaur!\n")


   
    def choose_game_type(self):
         #check for single or fleet of robots and append choice to init lists
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
            fleet_choice = int(input("You can choose a default list or manually choose your robot names and weapons.\n"
            "Choose 1 to load the default list\nChoose 2 to input yourself\n"))
            if fleet_choice < 1 or fleet_choice > 2: 
                print("Invalid input, we'll just use the default list")
                user_input = 1
            if fleet_choice == 1:
                fleet = Fleet()
                self.robot_list.append(fleet)
            elif fleet_choice == 2:
               self.robot_list = self.manual_entry(Robot)

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
            herd_choice = int(input("You can choose a default list or manually choose your dinosaur names and weapons.\n"
            "Choose 1 to load the default list\nChoose 2 to input yourself\n"))
            if herd_choice < 1 or herd_choice > 2: 
                print("Invalid input, we'll just use the default list")
                user_input = 1
            if herd_choice == 1:
                herd = Herd()
                self.dinosaur_list.append(herd)
            elif herd_choice == 2:
               self.dinosaur_list = self.manual_entry(Dinosaur)



    def manual_entry(self, choose_class):
        #ask user for name/weapon or pwr lvl and return as list of 3
        list = []
        string_name = ''
        string_attack = ''
        if choose_class == Robot:
            string_name = "robot's"
            string_attack = """Please choose a robot weapon, your choices are\n1 for Robot Nunchucks\n2 for Yamato Gun
            3 for Laser Staff\nEnter input:    """
        elif choose_class == Dinosaur:
            string_name = "dinosaur's"
            string_attack = "Please choose the dinosaur's power level (5 is a good starting level):\n"

        input_name = input(f"Please enter the first {string_name} name: \n")
        input_attack = input(string_attack)
        fighter = choose_class(input_name, input_attack) 
        list.append(fighter)
        fighter = choose_class(input(f"Please enter the second {string_name} name: \n"), input(string_attack))
        list.append(fighter)
        fighter = choose_class(input(f"Please enter the third {string_name} name: \n"), input(string_attack))
        list.append(fighter)

        return list    

 
    def battle_phase(self):
        #choose who attacks first
        random = randrange(1,2)
        if random == 1:
            print(f"\n\nTeam robot strikes first!\n")
            #win condition is if list is empty
            #check through list if class.health below zero, if yes remove from list
            while self.robot_list != [] and self.dinosaur_list != []:
                #sleep(2) #delay to watch battle progress
                self.robot_list[0].attack(self.dinosaur_list[0])
                if self.dinosaur_list[0].health <= 0:
                    print(f"{self.dinosaur_list[0].name} has been defeated!\n")
                    del self.dinosaur_list[0]
                elif self.dinosaur_list[0].health >= 0:
                    self.dinosaur_list[0].attack(self.robot_list[0])
                    if self.robot_list[0].health <= 0:
                        print(f"{self.robot_list[0].name} has been defeated!\n")
                        del self.robot_list[0]
        if random == 2:
            print(f"\n\nTeam dinosaur strikes first!\n")
            while self.robot_list != [] and self.dinosaur_list != []:
                #sleep(2) #delay to watch battle progress
                self.dinosaur_list[0].attack(self.robot_list[0])
                if self.robot_list[0].health <= 0:
                    print(f"{self.robot_list[0].name} has been defeated!\n")
                    del self.robot_list[0]
                elif self.robot_list[0].health >= 0:
                    self.robot.attack(self.dinosaur_list[0])
                    if self.dinosaur_list[0].health <= 0:
                        print(f"{self.dinosaur_list[0].name} has been defeated!\n")
                        del self.dinosaur_list[0]

    def display_winner(self):
        if self.robot_list != [] and self.dinosaur_list == []:
            print(f"Team robot has won the battle!\n")
        else:
            print("Team dinosaur has won the battle!\n")
    