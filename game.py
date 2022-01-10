
from human import Human
from ai import Ai



class Game:
    def __init__(self):
        self.player_one = None #player 1
        self.player_two = None #player2 = none
    

    def rules(self):
        print("The game you will play is called RPSLS(Rock, Paper, Scissors, Lizard, Spock)")
        print('')
        print('''this how you play the game...
- rock crushes scissors
- rock crushes lizard        
- scissors cuts paper        
- scissors cuts lizard        
- paper disproves spock        
- paper covers rock        
- lizard eats paper        
- lizard posions spock        
- spock smashes scissors        
- spock vaporizes rock''')               
        
        
        
    # selecting player vs player_two or PVP
    def game_type(self):
        print('')
        invalid = True
        while invalid is True:
            game_choice = input('What game would you like to play? Press 1 to play vs Sheldon or Press 2 to play multiplayer or press 3 to watch Sheldon vs Sheldon: ')
            print('')
            if game_choice == '1':
                self.player_one = Human()
                self.player_two = Ai()
                invalid = False
            elif game_choice == '2':
                self.player_one = Human()
                self.player_two = Human()
                invalid = False
            elif game_choice == '3':
                self.player_one = Ai()
                self.player_two = Ai()
                invalid = False 
            else:
                print("Invalid input")


    def battle(self):
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
    
        self.player_one.gesture_options()
        self.player_two.gesture_options()

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
            print('')
            print(f"{self.player_one.name} has won the round!")
            print('')
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
            print('')
            print(f"{self.player_two.name} has won the round!")
            print('')
            self.player_two.score += 1
            
        if self.player_one.user_attack == self.player_two.user_attack:
            print('')
            print("It's a tie!")
            print('')
        print(f"Scores are {self.player_one.name}:{self.player_one.score} {self.player_two.name}:{self.player_two.score}")
        print('')

   
