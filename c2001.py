from random import randint, randrange


def roll_the_dices(number_of_dices, rnd=False, last_choice=[]):
    """
    Simulates roll the dices (random or from input)
    :param int number_of_dices:
    :param boolean rnd:
    :param list last_choice:
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
                try:
                    lc = f" ({last_choice[i]})"
                except IndexError:
                    lc = ""
                code = input(f"Dice {i+1}{lc}: ")
                if lc and not code:
                    code = last_choice[i]
                elif code not in possible_dices:
                    print(f"Wrong input for dice {i+1}!")
            if lc:
                last_choice[i] = code
            else:
                last_choice.append(code)
        results.append((code, randint(1, int(code[1:]))))
    return zip(*results)


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


def game_2001(number_of_dices=2):
    """2001 game (console version)"""
    user_points = computer_points = 0
    user_dices = []
    while user_points < 2001 and computer_points < 2001:
        user_dices, user_rolls = roll_the_dices(number_of_dices, last_choice=list(user_dices))
        user_rolls_sum = sum(user_rolls)
        user_points = calculate_points(user_rolls_sum, user_points)
        computer_dices, computer_rolls = roll_the_dices(number_of_dices, rnd=True)
        computer_rolls_sum = sum(computer_rolls)
        computer_points = calculate_points(computer_rolls_sum, computer_points)
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
