'''
(5 points): As a developer, I want to create 2 additional Fleet and Herd classes,
 allowing for a list of 3 Robots to battle against a list of 3 Dinosaurs.'''

from random import randrange
from robot import Robot

class Fleet:
    def __init__(self):
        self.list =[Robot("Robot-1", randrange(1,3)), Robot("Robot-2", randrange(1,3)),Robot("Robot-3", randrange(1,3))]
