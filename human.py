from player import Player


class Human(Player):
    def __init__(self):
        self.name = input("What's your name? ")
        super().__init__()

    def gesture_options(self):
        print(self.attack_list)
        user_choice = int(input('select which attack you want to use: '))
        if user_choice == 1:
            self.user_attack = self.attack_list[0]
        elif user_choice == 2:
            self.user_attack = self.attack_list[1]
        elif user_choice == 3:
            self.user_attack = self.attack_list[2]
        elif user_choice == 4:
            self.user_attack = self.attack_list[3]
        elif user_choice == 5:
            self.user_attack = self.attack_list[4]
        else:
            print('invalid input')
        print(self.user_attack)


