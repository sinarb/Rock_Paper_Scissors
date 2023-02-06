import datetime

from config import ALL_CHOICES, scoreboard
import random


def get_user_choice():
    user_choice = input('please enter your choice ("r","p","s"): ')
    if user_choice in ALL_CHOICES:
        return user_choice
    else:
        print('Please choose between 3 items')
        return get_user_choice()


def get_system_choice():
    system_choice = random.choice(ALL_CHOICES)
    return system_choice


def get_winner(user_choice, system_choice):
    if user_choice == system_choice:
        return 'equal'
    if (user_choice == 'r' and system_choice == 's') or (user_choice == 's' and system_choice == 'p') or (
            user_choice == 'p' and system_choice == 'r'):
        scoreboard['user'] += 1
        return 'you win'
    else:
        scoreboard['system'] += 1
        return 'you lose'


def log_time(func):
    def inner(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        end = datetime.datetime.now()
        duration = end - start
        print(f'total time: {duration.seconds // 3600}:{duration.seconds // 60}:{duration.seconds % 60}')
        return result

    return inner



def play_one_hand():
    while scoreboard["user"] < 3 and scoreboard["system"] < 3:
        user_choice = get_user_choice()
        system_choice = get_system_choice()
        winner = get_winner(user_choice, system_choice)

        print(f'user: {user_choice} and system {system_choice} result: {winner}')
        print('#' * 20)
        print(f'you win count: {scoreboard["user"]}')
        print(f'system win count: {scoreboard["system"]}')
        print('#' * 20)

    print('\n\n', '-' * 20)
    if scoreboard["user"] > scoreboard["system"]:
        result = 'win'
    else:
        result = 'lose'
    play_again = input(f'you {result} do you want play again? (y/any key): ')
    print('-' * 20, '\n\n')
    if play_again == 'y':
        scoreboard["user"] = 0
        scoreboard["system"] = 0
        play_one_hand()


@log_time
def play():
    play_one_hand()


if __name__ == '__main__':
    play()
