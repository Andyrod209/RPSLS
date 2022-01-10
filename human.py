from player import Player


class Human(Player):
    def __init__(self):
        self.name = input("What's your name? ")
        print('')
        super().__init__()

    def gesture_options(self):
        invalid = True
        while invalid is True:
            user_choice = int(input('''Select which attack you want to use:
- 1. Rock
- 2. Paper
- 3. Scissors
- 4. Lizard
- 5. Spock
Entered number: '''))
            print('')

            if user_choice == 1:
                self.user_attack = self.attack_list[0]
                print(self.user_attack)
                invalid = False
            elif user_choice == 2:
                self.user_attack = self.attack_list[1]
                print(self.user_attack)
                invalid = False
            elif user_choice == 3:
                self.user_attack = self.attack_list[2]
                print(self.user_attack)
                invalid = False
            elif user_choice == 4:
                self.user_attack = self.attack_list[3]
                print(self.user_attack)
                invalid = False
            elif user_choice == 5:
                self.user_attack = self.attack_list[4]
                print(self.user_attack)
                invalid = False
            else:
                print('invalid input')
            