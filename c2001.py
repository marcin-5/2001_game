from random import randint, randrange


def roll_the_dices(number_of_dices, rnd=False):
    """
    Simulates roll the dices (random or from input)
    :param int number_of_dices:
    :param boolean rnd:
    :return: Two tuples: codes of used dices and results
    """
    possible_dices = tuple(f"D{_}" for _ in (3, 4, 6, 8, 10, 12, 20, 100))
    results = []
    for i in range(number_of_dices):
        if not i:
            print(f"Choose dice{'s' if number_of_dices > 1 else ''} from: {', '.join(possible_dices)}.")
        if rnd:
            code = possible_dices[randrange(len(possible_dices))]
        else:
            code = ""
            while not code or code not in possible_dices:
                code = input(f"Dice {i+1}: ")
                if code not in possible_dices:
                    print(f"Wrong input for dice {i+1}!")
        results.append((code, randint(1, int(code[1:]))))
    return tuple(_[0] for _ in results), tuple(_[1] for _ in results)


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
        user_rolls = roll_the_dices(2)[1]
        user_rolls_sum = sum(user_rolls)
        user_points = calculate_points(user_rolls_sum, user_points)
        computer_dices, computer_rolls = roll_the_dices(2, rnd=True)
        computer_rolls_sum = sum(computer_rolls)
        computer_points = calculate_points(computer_rolls_sum, computer_points)
        print(user_rolls)
        print("User roll:", ", ".join(map(str, user_rolls)))
        print(f"Computer roll:", ", ".join(map(str, computer_rolls)), "Used dices:", ", ".join(computer_dices))
        print(f"User points: {user_points}, computer points: {computer_points}")
    if user_points > computer_points:
        print("User win!!!")
    elif user_points < computer_points:
        print("Computer win!")
    else:
        print("DRAW")


if __name__ == "__main__":
    game_2001()
