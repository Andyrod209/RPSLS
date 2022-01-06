from player import Player
import random

class Ai(Player):
    def __init__(self):
        self.name = "Sheldon"
        super().__init__() 
    
    def random_gesture_choice(self):
        self.ai_option = self.attack_list[random.randint(0, 4)]
        print(f'the ai has chose {self.ai_option} as its attack')
        