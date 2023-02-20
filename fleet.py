from random import randrange
from robot import Robot

class Fleet:
    def __init__(self):
        self.list =[Robot("Rob", randrange(1,3)), Robot("Ryder", randrange(1,3)),Robot("Roman", randrange(1,3))]
