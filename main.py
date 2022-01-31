import Functions

name = input("Please enter your name: ")
bol_game = input("Would you like to play a game? Yes / No ")

while bol_game.lower() == 'yes':
    print(Functions.welcome(name))
    res_game = Functions.load_game()
    if res_game:
        print("You Won!")
    else:
        print("You lose!")
    bol_game = input("Would you like to play a game? Yes / No ")


