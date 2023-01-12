from random import randint, randrange
from re import sub


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
            print(f"Choose dice{'s' if number_of_dices > 1 else ''}",
                  f"from: {', '.join(possible_dices)}.")
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


def gprint(output):
    """Print in green."""
    print("\033[92m{}\033[00m".format(output))


def rprint(output):
    """Colorize digits in red and print."""
    print(sub(r"(\d+)",
              lambda m: "\033[91m{}\033[00m".format(m.group()),
              output))


def yprint(output):
    """Colorize dice codes and digits in yellow and print"""
    print(sub(r"([\d,D\s]{3,})",
              lambda m: "\033[93m{}\033[00m".format(m.group()),
              output))


def game_2001(number_of_dices=2):
    """2001 game (console version)"""
    user_points = computer_points = 0
    user_dices = []
    while user_points < 2001 and computer_points < 2001:
        user_dices, user_rolls = roll_the_dices(number_of_dices,
                                                last_choice=list(user_dices))
        user_rolls_sum = sum(user_rolls)
        user_points = calculate_points(user_rolls_sum, user_points)
        computer_dices, computer_rolls = roll_the_dices(number_of_dices, rnd=True)
        computer_rolls_sum = sum(computer_rolls)
        computer_points = calculate_points(computer_rolls_sum, computer_points)
        yprint("User roll: " + ", ".join(map(str, user_rolls)))
        yprint(f"Computer roll: "
               + ", ".join(map(str, computer_rolls))
               + " Used dices: " + ", ".join(computer_dices))
        rprint(f"User points: {user_points}, computer points: {computer_points}")
    gprint("User win!!!" if user_points > computer_points else
           "Computer win!" if user_points < computer_points else
           "DRAW")


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter number of dices greater than 0 or exit otherwise: "))
            if not n:
                break
            game_2001(n)
        except ValueError:
            break
