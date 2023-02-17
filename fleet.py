'''
(5 points): As a developer, I want to create 2 additional Fleet and Herd classes,
 allowing for a list of 3 Robots to battle against a list of 3 Dinosaurs.'''

from random import randrange
from robot import Robot

class Fleet:
    def __init__(self):
        self.list =[Robot("Robot-1", 4), Robot("Robot-2", 4),Robot("Robot-3", 4)]
