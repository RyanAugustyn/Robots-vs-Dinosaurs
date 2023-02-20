from random import randrange
from robot import Robot

class Fleet:
    def __init__(self):
        self.list =[Robot("Robot-1", randrange(1,3)), Robot("Robot-2", randrange(1,3)),Robot("Robot-3", randrange(1,3))]
