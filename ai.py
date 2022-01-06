from player import Player
import random

class Ai(Player):
    def __init__(self):
        self.name = "Sheldon"
        super().__init__() 
    
    def random_gesture_choice(self):
        print(self.attack_list[random.randint(0, 4)])