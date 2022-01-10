from player import Player
import random

class Ai(Player):
    def __init__(self):
        self.name = "Sheldon"
        super().__init__() 
    
    def gesture_options(self):
        self.user_attack = self.attack_list[random.randint(0, 4)]
        print(f'the ai has chosen {self.user_attack} as its attack')
        