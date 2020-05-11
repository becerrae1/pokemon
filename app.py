import time
import numpy as np
import sys

def delay_print(s):
    #print one letter at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)



# Create the Class
class Pokemon:
    def __init__(self, name, types, moves, EVs, health='====='):
        # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.bars = 20 # of health bars

    def fight(self, Pokemon2):
        #Allow 2 pokemon to fight each other


if __name__ == '__main__':
    pass



