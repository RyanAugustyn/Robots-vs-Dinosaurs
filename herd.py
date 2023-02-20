from random import randrange
from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.list =[Dinosaur("Dave", randrange(4,6)), Dinosaur("Daenerys", randrange(4,6)), Dinosaur("Dupree'", randrange(4,6))]