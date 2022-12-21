from flask import Flask, render_template, request
from c2001 import calculate_points
from random import randint, randrange

POSSIBLE_DICES = tuple(f"D{_}" for _ in (3, 4, 6, 8, 10, 12, 20, 100))
app = Flask(__name__)


def random_dice():
    """Return random code of possible dices"""
    return POSSIBLE_DICES[randrange(0, len(POSSIBLE_DICES))]


def roll_the_dice(code):
    return randint(1, int(code[1:]))


def max_true_index(l):
    """Return max index of True item in list"""
    for i, x in reversed(list(enumerate(l))):
        if x:
            return i


def parse_turn(user_points=0, computer_points=0,
               user_dice_1="", user_dice_2=""):
    form_items_name = ("upts", "cpts", "ud1", "ud2", "cd1", "cd2",
                       "win", "ur1", "ur2", "cr1", "cr2", "rk")
    computer_dice_1 = random_dice()
    computer_dice_2 = random_dice()
    if not user_dice_1 and not user_dice_2:
        # start the game with default values
        user_roll_1 = user_roll_2 = 0
        computer_roll_1 = computer_roll_2 = 0
        user_points = computer_points = 0
    else:
        user_roll_1 = roll_the_dice(user_dice_1)
        user_roll_2 = roll_the_dice(user_dice_2)
        computer_roll_1 = roll_the_dice(computer_dice_1)
        computer_roll_2 = roll_the_dice(computer_dice_2)
        user_points = calculate_points(user_roll_1 + user_roll_2,
                                       user_points)
        computer_points = calculate_points(computer_roll_1 + computer_roll_2,
                                           computer_points)
    win = max_true_index((True,
                          2001 < user_points > computer_points,
                          2001 < computer_points > user_points,
                          2001 < user_points == computer_points))
    return dict(zip(form_items_name,
                    (user_points, computer_points,
                     user_dice_1, user_dice_2,
                     computer_dice_1, computer_dice_2,
                     win, user_roll_1, user_roll_2,
                     computer_roll_1, computer_roll_2,
                     POSSIBLE_DICES)))


@app.route("/2001", methods=["GET", "POST"])
def f2001():
    if request.method == "POST":
        return render_template("2001.html",
                               **parse_turn(int(request.form["upts"]),
                                            int(request.form["cpts"]),
                                            request.form["ud1"],
                                            request.form["ud2"]))
    else:
        return render_template("2001.html", **parse_turn())


if __name__ == "__main__":
    app.run(debug=True)
