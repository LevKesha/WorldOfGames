import random
from time import sleep
import os


def generate_sequence(difficulty):
    i = 0
    sequence = ""
    while i < int(difficulty):
        sequence = sequence + str(random.randint(0, 101))
        i = i+1

    return sequence


def is_list_equal(user_list, comp_list):
    if user_list == comp_list:
        return True
    else:
        return False


def play(difficulty):
    game_seq = generate_sequence(difficulty)
    print(game_seq)
    sleep(1)
    os.system("cls")
    user_seq = str(input("Please enter identical set of numbers "))
    return is_list_equal(user_seq, game_seq)

