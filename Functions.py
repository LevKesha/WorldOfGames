from guessGame import play as play_guess
from memoryGame import play as play_memory
from CurrencyRouletteGame import play as play_cur
import Score


def welcome(name):
    return f"""Hello {name} and welcome to the World of Games (WoG). 
Here you can find many cool games to play"""


def load_game():
    result = False
    game = input("""Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to
guess it back
2. Guess Game - guess a number and see if you chose like the computer
3. Currency Roulette - try and guess the value of a random amount of USD in ILS""")
    while not game.isnumeric():
        game = input("""Please choose a game to play - input a digit:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to
guess it back
2. Guess Game - guess a number and see if you chose like the computer
3. Currency Roulette - try and guess the value of a random amount of USD in ILS""")
    while int(game) < 1 or int(game) > 3:
        game = input("""Wrong input. Please choose a game to play:
            1. Memory Game - a sequence of numbers will appear for 1 second and you have to
            guess it back
            2. Guess Game - guess a number and see if you chose like the computer
            3. Currency Roulette - try and guess the value of a random amount of USD in ILS""")
    level = input("Please choose game difficulty from 1 to 5:")
    while not level.isnumeric():
        level = input("Please choose game difficulty from 1 to 5: - input a digit")
    while int(level) < 1 or int(level) > 5:
        level = input("Wrong input. Please choose game difficulty from 1 to 5:")

    game_id = int(game)
    if game_id == 1:
        result = play_memory(level)
    elif game_id == 2:
        result = play_guess(level)
    elif game_id == 3:
        result = play_cur(level)

    if result:
        Score.add_score(level)
    return result








