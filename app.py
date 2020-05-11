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

        #Print fight information
        print("----------POKEMON BATTLE----------")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3*(1+np.mean([self.attack,self.defense])))
        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3*(1+np.mean([Pokemon2.attack,Pokemon2.defense])))

        time.sleep(2)

        #Consider type advantages
        version = ['Fire', 'Water', 'Grass']
        for i, k in enumerate(version):
            if self.types == k:
                #both are same type
                if Pokemon2.types == k:
                    string_1_attack = 'Its not very effective....'
                    string_2_attack = 'Its not very effective....'
                
                #Pokemon 2 is Strong
                if Pokemon2.types == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    string_1_attack = "Its not very effective"
                    string_2_attack = "Its super effective!"

                #Pokemon 2 is Weak
                if Pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = "Its super effective!"
                    string_2_attack = "Its not very effective"

        # Actual fighting now
        while(self.bars > 0) and (Pokemon2.bar > 0):
            #print health of each pokemon
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{x+1},", x)
            index = int(input('Pick a move: '))
            delay_print(f"{self.name} used {moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            #Determine Damage
            Pokemon2.bars -= self.attack
            Pokemon.health = ""

            



if __name__ == '__main__':
    pass



