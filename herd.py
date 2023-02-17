from random import randrange
from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.list =[Dinosaur("Dinosaur-1", randrange(4,6)), Dinosaur("Dinosaur-2", randrange(4,6)), Dinosaur("Dinosaur-3", randrange(4,6))]