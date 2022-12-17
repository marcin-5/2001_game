from dice import roll_the_dice_re as roll_the_dice
from dice import POSSIBLE_DICES
from random import randrange


def calculate_points(roll, points):
    """Calculate points.
    :param int roll:
    :param int points:

    :rtype: int
    :return: new_points
    """
    if roll == 7:
        points //= roll
    elif roll == 11:
        points *= roll
    else:
        points += roll
    return points


def game_2001():
    """2001 game (console version)"""
    user_points = computer_points = 0
    while user_points < 2001 and computer_points < 2001:
        print(f"Choose dices from: {', '.join(POSSIBLE_DICES)}.")
        dice1 = dice2 = None
        while not dice1 or not dice1 in POSSIBLE_DICES:
            dice1 = input("Dice 1: ")
            if  not dice1 in POSSIBLE_DICES:
                print("Wrong input for dice 1:", dice1)
        while not dice2 or not dice2 in POSSIBLE_DICES:
            dice2 = input("Dice 2: ")
            if not dice2 in POSSIBLE_DICES:
                print("Wrong input for dice 2:", dice2)
        user_roll_1 = roll_the_dice(dice1)
        user_roll_2 = roll_the_dice(dice2)
        user_roll_sum = user_roll_1 + user_roll_2
        user_points = calculate_points(user_roll_sum, user_points)
        dice1 = POSSIBLE_DICES[randrange(0, len(POSSIBLE_DICES))]
        dice2 = POSSIBLE_DICES[randrange(0, len(POSSIBLE_DICES))]
        computer_roll_1 = roll_the_dice(dice1)
        computer_roll_2 = roll_the_dice(dice2)
        computer_roll_sum = computer_roll_1 + computer_roll_2
        computer_points = calculate_points(computer_roll_sum, computer_points)
        print(f"User roll: {user_roll_1} and {user_roll_2}")
        print(f"Computer roll: {computer_roll_1} and {computer_roll_2}. Used dices {dice1} and {dice2}")
        print(f"User points: {user_points}, computer points: {computer_points}")
    if user_points > computer_points:
        print("User win!!!")
    elif user_points < computer_points:
        print("Computer win!")
    else:
        print("DRAW")


if __name__ == "__main__":
    game_2001()
