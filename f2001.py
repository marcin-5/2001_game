from flask import Flask, render_template, request
from dice import roll_the_dice_re as roll_the_dice
from dice import POSSIBLE_DICES
from c2001 import calculate_points
from random import randrange

app = Flask(__name__)
form_names = ("upts", "cpts", "ud1", "ud2", "cd1", "cd2",
              "win", "ur1", "ur2", "cr1", "cr2", "rk")


def parse_turn(user_points=0, computer_points=0,
               user_dice_1="", user_dice_2=""):
    computer_dice_1 = POSSIBLE_DICES[randrange(0, len(POSSIBLE_DICES))]
    computer_dice_2 = POSSIBLE_DICES[randrange(0, len(POSSIBLE_DICES))]
    if not user_dice_1 and not user_dice_2:
        # start the game with default values
        user_roll_1 = user_roll_2 = 0
        computer_roll_1 = computer_roll_2 = 0
        user_points = computer_points = 0
    else:
        user_roll_1 = roll_the_dice(user_dice_1)
        user_roll_2 = roll_the_dice(user_dice_2)
        user_roll_sum = user_roll_1 + user_roll_2
        computer_roll_1 = roll_the_dice(computer_dice_1)
        computer_roll_2 = roll_the_dice(computer_dice_2)
        computer_roll_sum = computer_roll_1 + computer_roll_2
        user_points = calculate_points(user_roll_sum, user_points)
        computer_points = calculate_points(computer_roll_sum, computer_points)
    if user_points > 2001 or computer_points > 2001:
        if user_points > computer_points:
            win = 1
        elif user_points < computer_points:
            win = 2
        else:
            win = 3
    else:
        win = 0
    return dict(zip(form_names,
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
