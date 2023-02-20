from random import randrange

class Weapon:
    def __init__(self, user_input):
        user_input = int(user_input)
        #check for correct input
        if user_input < 1 or user_input > 3:
            print("Invalid input, weapon randomly chosen")
            user_input = randrange(1,4)

        if user_input == 1:
            print("\nThe nunchucks have low damage, but you're very likely to hit something!\n")
            self.name = 'Robot Nunchucks' 
            self.attack_power = 3
            self.hit_chance = 90
            self.attack_message = ["whip around with lightning speed!"] #not implemented, alternating messages for the weapons
        elif user_input == 2:
            print("\nThe powerful Yamato Gun is devastating, but is sometimes hard to hit with!\n")
            self.name = 'Yamato Gun'  
            self.attack_power = 9
            self.hit_chance = 35
        elif user_input == 3:
            print("\nThe LaZer Staff is dependable. The working robot's weapon of choice!\n")
            self.name = 'LaZer Staff'
            self.attack_power = 5
            self.hit_chance = 75
        else:
            print("incorrect")