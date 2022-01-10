from human import Human
from ai import Ai
from player import Player


class Game:
    def __init__(self):
        self.player_one = Human() #player 1
        self.player_two = None #player2 = none
    

    def rules(self):
        print("The game you will play is called RPSLS(Rock, Paper, Scissors, Lizard, Spock)")
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
    # selecting player vs player_two or PVP
    def game_type(self):
        game_choice = int(input('what game would you like to play? Press 1 to play vs Ai or Press 2 to play multiplayer: '))
        if game_choice == 1:
            self.player_two = Ai()
        elif game_choice == 2:
            self.player_two = Human()


    def battle(self):
        # self.player_one.gesture_options()
        # self.player_two.random_gesture_choice()
        self.game_logic()
        while self.player_one.score <= 2 or self.player_two.score <= 2:
            self.game_logic()
            if self.player_one.score == 2:
                print('')
                print(f'{self.player_one.name} has won the game!!!')
                break
            elif self.player_two.score == 2:
                print('')
                print(f'{self.player_two.name} has won the game!!!')
                break

    def game_logic(self):
        # doesn't make sense but refortor later...
        self.player_one.gesture_options()
        self.player_two.gesture_options()
        # self.opponent = opponent
        # self.player = player
        if (self.player_one.user_attack == 'Rock' and self.player_two.user_attack == 'Scissors') or \
            (self.player_one.user_attack == "Lizard" and self.player_two.user_attack == "Spock") or \
            (self.player_one.user_attack == "Paper" and self.player_two.user_attack == "Rock") or \
            (self.player_one.user_attack == "Paper" and self.player_two.user_attack == "Spock") or \
            (self.player_one.user_attack == "Rock" and self.player_two.user_attack == "Lizard") or \
            (self.player_one.user_attack == "Spock" and self.player_two.user_attack == "Scissors") or \
            (self.player_one.user_attack == "Spock" and self.player_two.user_attack == "Rock") or \
            (self.player_one.user_attack == "Scissors" and self.player_two.user_attack == "Paper") or \
            (self.player_one.user_attack == "Lizard" and self.player_two.user_attack == "Paper") or \
            (self.player_one.user_attack == "Scissors" and self.player_two.user_attack == "Lizard"):
            print("You win!")
            self.player_one.score += 1
            
        if (self.player_two.user_attack == 'Rock' and self.player_one.user_attack == 'Scissors') or \
            (self.player_two.user_attack == "Lizard" and self.player_one.user_attack == "Spock") or \
            (self.player_two.user_attack == "Paper" and self.player_one.user_attack == "Rock") or \
            (self.player_two.user_attack == "Paper" and self.player_one.user_attack == "Spock") or \
            (self.player_two.user_attack == "Rock" and self.player_one.user_attack == "Lizard") or \
            (self.player_two.user_attack == "Spock" and self.player_one.user_attack == "Scissors") or \
            (self.player_two.user_attack == "Spock" and self.player_one.user_attack == "Rock") or \
            (self.player_two.user_attack == "Scissors" and self.player_one.user_attack == "Paper") or \
            (self.player_two.user_attack == "Lizard" and self.player_one.user_attack == "Paper") or \
            (self.player_two.user_attack == "Scissors" and self.player_one.user_attack == "Lizard"):
            print('better luck next time')
            self.player_two.score += 1
            
        if self.player_one.user_attack == self.player_two.user_attack:
            print('Tie!')
        print(f"Scores are {self.player_one.name}:{self.player_one.score} {self.player_two.name}:{self.player_two.score}")

   

    
    def display_winner(self):
        pass


<<<<<<< HEAD
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
=======
''' if self.player_one.user_attack == 'Rock':
            if self.player_two.user_attack == "Scissors":
                self.player_one.score += 1
                print(f'winner of this round {self.player_one.name}')
            elif self.player_two.user_attack == "Lizard":
                self.player_one.score += 1
                print(f'winner of this round {self.player_one.name}')
            elif self.player_two.user_attack == "Spock":
                self.player_two.score += 1
                print(f'winner of this round {self.player_two.name}')
            elif self.player_two.user_attack == "paper":
                self.player_two.score += 1
                print(f'winner of this round {self.player_two.name}')
            elif self.player_two.user_attack == "Rock":
                print("It's a tie!")
            

        elif self.player_one.user_attack == "Scissors":
            if self.player_two.user_attack == "Paper":
                self.player_one.score += 1
                print(f'winner of this round {self.player_one.name}')
            elif self.player_two.user_attack == "Lizard":
                self.player_one.score += 1
                print(f'winner of this round {self.player_one.name}')
            elif self.player_two.user_attack == "Rock":
                self.player_two.score += 1
                print(f'winner of this round {self.player_two.name}')
            elif self.player_two.user_attack == "Spock":
                self.player_two.score += 1
                print(f'winner of this round {self.player_two.name}')
            elif self.player_two.user_attack == "Scissors":
                print("It's a tie!")
            print(f'winner of this round {self.player_one.name}') 

        elif self.player_one.user_attack == "paper":
            if self.player_two.user_attack == "Rock":
                self.player_one.score += 1
                print(f'winner of this round {self.player_one.name}')
            elif self.player_two.user_attack == "Spock":
                self.player_one.score += 1
                print(f'winner of this round {self.player_one.name}')
            elif self.player_two.user_attack == "Lizard":
                self.player_two.score += 1
                print(f'winner of this round {self.player_two.name}')
            elif self.player_two.user_attack == "Scissors":
                self.player_two.score += 1
                print(f'winner of this round {self.player_two.name}')
            elif self.player_two.user_attack == "paper":
                print("It's a tie!")    
         
        elif self.player_one.user_attack == "Lizard":
            if self.player_two.user_attack == "Paper":
                self.player_one.score += 1
                print(f'winner of this round {self.player_one.name}')
            elif self.player_two.user_attack == "Spock":
                self.player_one.score += 1
                print(f'winner of this round {self.player_one.name}')
            elif self.player_two.user_attack == "Rock":
                self.player_two.score += 1
                print(f'winner of this round {self.player_two.name}')
            elif self.player_two.user_attack == "Scissors":
                self.player_two.score += 1
                print(f'winner of this round {self.player_two.name}')
            elif self.player_two.user_attack == "Lizard":
                print("It's a tie!")
        
        elif self.player_one.user_attack == "Spock":
            if self.player_two.user_attack == "Scissors":
                self.player_one.score += 1
                print(f'winner of this round {self.player_one.name}')
            elif self.player_two.user_attack == "Rock":
                self.player_one.score += 1
                print(f'winner of this round {self.player_one.name}')
            elif self.player_two.user_attack == "Paper":
                self.player_two.score += 1
                print(f'winner of this round {self.player_two.name}')
            elif self.player_two.user_attack == "Spock":
                self.player_two.score += 1
                print(f'winner of this round {self.player_two.name}')
            elif self.player_two.user_attack == "Scissors":
                print("It's a tie!")
                '''
>>>>>>> 2035e10e9738342a4300d7b81911b7648c6a08a9
