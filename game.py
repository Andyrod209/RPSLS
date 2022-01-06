from human import Human
from ai import Ai
from player import Player


class Game:
    def __init__(self):
        self.human = Human()
        self.ai = Ai()
    

    def rules(self):
        print("The game you will play is called RPSLS(Rock, Paper, scissors, Lizard, Spock)")
        print('')
        print('''this how you play the game...
        rock crushes scissors
        scissors cuts paper
        paper covers rock
        rock crushes lizard
        lizard posions spock
        spock smashes scissors
        scissors cuts lizard
        lizard eats paper
        paper disproves spock
        spock vaporizes rock''')
    
    def game_type(self):
        pass

    def battle(self):
        pass

    def round(self):
        pass

    def game_logic(self):
        self.human.gesture_options()
        self.ai.random_gesture_choice() 
        if self.human.user_attack == 'Rock':
            if self.ai.ai_option == "Scissors":
                self.human.score += 1
                print(f'winner of this round {self.human.name}')
            elif self.ai.ai_option == "Lizard":
                self.human.score += 1
                print(f'winner of this round {self.human.name}')
            elif self.ai.ai_option == "Spock":
                self.ai.score += 1
                print(f'winner of this round {self.ai.name}')
            elif self.ai.ai_option == "paper":
                self.ai.score += 1
                print(f'winner of this round {self.ai.name}')
            elif self.ai.ai_option == "Rock":
                print("It's a tie!")
            

        elif self.human.user_attack == "Scissors":
            if self.ai.ai_option == "Paper":
                self.human.score += 1
                print(f'winner of this round {self.human.name}')
            elif self.ai.ai_option == "Lizard":
                self.human.score += 1
                print(f'winner of this round {self.human.name}')
            elif self.ai.ai_option == "Rock":
                self.ai.score += 1
                print(f'winner of this round {self.ai.name}')
            elif self.ai.ai_option == "Spock":
                self.ai.score += 1
                print(f'winner of this round {self.ai.name}')
            elif self.ai.ai_option == "Scissors":
                print("It's a tie!")
            print(f'winner of this round {self.human.name}') 

        elif self.human.user_attack == "paper":
            if self.ai.ai_option == "Rock":
                self.human.score += 1
                print(f'winner of this round {self.human.name}')
            elif self.ai.ai_option == "Spock":
                self.human.score += 1
                print(f'winner of this round {self.human.name}')
            elif self.ai.ai_option == "Lizard":
                self.ai.score += 1
                print(f'winner of this round {self.ai.name}')
            elif self.ai.ai_option == "Scissors":
                self.ai.score += 1
                print(f'winner of this round {self.ai.name}')
            elif self.ai.ai_option == "paper":
                print("It's a tie!")    
         
        elif self.human.user_attack == "Lizard":
            if self.ai.ai_option == "Paper":
                self.human.score += 1
                print(f'winner of this round {self.human.name}')
            elif self.ai.ai_option == "Spock":
                self.human.score += 1
                print(f'winner of this round {self.human.name}')
            elif self.ai.ai_option == "Rock":
                self.ai.score += 1
                print(f'winner of this round {self.ai.name}')
            elif self.ai.ai_option == "Scissors":
                self.ai.score += 1
                print(f'winner of this round {self.ai.name}')
            elif self.ai.ai_option == "Lizard":
                print("It's a tie!")
        
        elif self.human.user_attack == "Spock":
            if self.ai.ai_option == "Scissors":
                self.human.score += 1
                print(f'winner of this round {self.human.name}')
            elif self.ai.ai_option == "Rock":
                self.human.score += 1
                print(f'winner of this round {self.human.name}')
            elif self.ai.ai_option == "Paper":
                self.ai.score += 1
                print(f'winner of this round {self.ai.name}')
            elif self.ai.ai_option == "Spock":
                self.ai.score += 1
                print(f'winner of this round {self.ai.name}')
            elif self.ai.ai_option == "Scissors":
                print("It's a tie!")
            

    
    def display_winner(self):
        pass