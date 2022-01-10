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
    # selecting player vs ai or PVP
    def game_type(self):
        pass


    def Battle(self):
        # self.human.gesture_options()
        # self.ai.random_gesture_choice()
        self.game_logic()
        while self.human.score <= 2 or self.ai.score <= 2:
            self.game_logic()
            if self.human.score == 2:
                print('')
                print(f'{self.human.name} has won the game!!!')
                break
            elif self.ai.score == 2:
                print('')
                print(f'{self.ai.name} has won the game!!!')
                break
           
                

        
        pass

    def game_logic(self):
        # doesn't make sense but refortor later...
        self.human.gesture_options()
        self.ai.random_gesture_choice()
        # self.opponent = opponent
        # self.player = player
        if (self.human.user_attack == 'Rock' and self.ai.ai_option == 'Scissors') or \
            (self.human.user_attack == "Lizard" and self.ai.ai_option == "Spock") or \
            (self.human.user_attack == "Paper" and self.ai.ai_option == "Rock") or \
            (self.human.user_attack == "Paper" and self.ai.ai_option == "Spock") or \
            (self.human.user_attack == "Rock" and self.ai.ai_option == "Lizard") or \
            (self.human.user_attack == "Spock" and self.ai.ai_option == "Scissors") or \
            (self.human.user_attack == "Spock" and self.ai.ai_option == "Rock") or \
            (self.human.user_attack == "Scissors" and self.ai.ai_option == "Paper") or \
            (self.human.user_attack == "Lizard" and self.ai.ai_option == "Paper") or \
            (self.human.user_attack == "Scissors" and self.ai.ai_option == "Lizard"):
            print("You win!")
            self.human.score += 1
            
        if (self.ai.ai_option == 'Rock' and self.human.user_attack == 'Scissors') or \
            (self.ai.ai_option == "Lizard" and self.human.user_attack == "Spock") or \
            (self.ai.ai_option == "Paper" and self.human.user_attack == "Rock") or \
            (self.ai.ai_option == "Paper" and self.human.user_attack == "Spock") or \
            (self.ai.ai_option == "Rock" and self.human.user_attack == "Lizard") or \
            (self.ai.ai_option == "Spock" and self.human.user_attack == "Scissors") or \
            (self.ai.ai_option == "Spock" and self.human.user_attack == "Rock") or \
            (self.ai.ai_option == "Scissors" and self.human.user_attack == "Paper") or \
            (self.ai.ai_option == "Lizard" and self.human.user_attack == "Paper") or \
            (self.ai.ai_option == "Scissors" and self.human.user_attack == "Lizard"):
            print('better luck next time')
            self.ai.score += 1
            
        if self.human.user_attack == self.ai.ai_option:
            print('Tie!')
        print(f"Scores are {self.human.name}:{self.human.score} {self.ai.name}:{self.ai.score}")

   

    
    def display_winner(self):
        pass


# ''' if self.human.user_attack == 'Rock':
#             if self.ai.ai_option == "Scissors":
#                 self.human.score += 1
#                 print(f'winner of this round {self.human.name}')
#             elif self.ai.ai_option == "Lizard":
#                 self.human.score += 1
#                 print(f'winner of this round {self.human.name}')
#             elif self.ai.ai_option == "Spock":
#                 self.ai.score += 1
#                 print(f'winner of this round {self.ai.name}')
#             elif self.ai.ai_option == "paper":
#                 self.ai.score += 1
#                 print(f'winner of this round {self.ai.name}')
#             elif self.ai.ai_option == "Rock":
#                 print("It's a tie!")
            

#         elif self.human.user_attack == "Scissors":
#             if self.ai.ai_option == "Paper":
#                 self.human.score += 1
#                 print(f'winner of this round {self.human.name}')
#             elif self.ai.ai_option == "Lizard":
#                 self.human.score += 1
#                 print(f'winner of this round {self.human.name}')
#             elif self.ai.ai_option == "Rock":
#                 self.ai.score += 1
#                 print(f'winner of this round {self.ai.name}')
#             elif self.ai.ai_option == "Spock":
#                 self.ai.score += 1
#                 print(f'winner of this round {self.ai.name}')
#             elif self.ai.ai_option == "Scissors":
#                 print("It's a tie!")
#             print(f'winner of this round {self.human.name}') 

#         elif self.human.user_attack == "paper":
#             if self.ai.ai_option == "Rock":
#                 self.human.score += 1
#                 print(f'winner of this round {self.human.name}')
#             elif self.ai.ai_option == "Spock":
#                 self.human.score += 1
#                 print(f'winner of this round {self.human.name}')
#             elif self.ai.ai_option == "Lizard":
#                 self.ai.score += 1
#                 print(f'winner of this round {self.ai.name}')
#             elif self.ai.ai_option == "Scissors":
#                 self.ai.score += 1
#                 print(f'winner of this round {self.ai.name}')
#             elif self.ai.ai_option == "paper":
#                 print("It's a tie!")    
         
#         elif self.human.user_attack == "Lizard":
#             if self.ai.ai_option == "Paper":
#                 self.human.score += 1
#                 print(f'winner of this round {self.human.name}')
#             elif self.ai.ai_option == "Spock":
#                 self.human.score += 1
#                 print(f'winner of this round {self.human.name}')
#             elif self.ai.ai_option == "Rock":
#                 self.ai.score += 1
#                 print(f'winner of this round {self.ai.name}')
#             elif self.ai.ai_option == "Scissors":
#                 self.ai.score += 1
#                 print(f'winner of this round {self.ai.name}')
#             elif self.ai.ai_option == "Lizard":
#                 print("It's a tie!")
        
#         elif self.human.user_attack == "Spock":
#             if self.ai.ai_option == "Scissors":
#                 self.human.score += 1
#                 print(f'winner of this round {self.human.name}')
#             elif self.ai.ai_option == "Rock":
#                 self.human.score += 1
#                 print(f'winner of this round {self.human.name}')
#             elif self.ai.ai_option == "Paper":
#                 self.ai.score += 1
#                 print(f'winner of this round {self.ai.name}')
#             elif self.ai.ai_option == "Spock":
#                 self.ai.score += 1
#                 print(f'winner of this round {self.ai.name}')
#             elif self.ai.ai_option == "Scissors":
#                 print("It's a tie!")
#                 '''