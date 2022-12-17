from flask import Flask, render_template, request
from dice import roll_the_dice_re as roll_the_dice
from dice import POSSIBLE_DICES
from c2001 import calculate_points
from random import randrange

app = Flask(__name__)


@app.route("/2001", methods=["GET", "POST"])
def f2001():
    if request.method == "POST":
        user_points = int(request.form["upts"])
        computer_points = int(request.form["cpts"])
        user_dice_1 = request.form["ud1"]
        user_dice_2 = request.form["ud2"]
        computer_dice_1 = POSSIBLE_DICES[randrange(0, len(POSSIBLE_DICES))]
        computer_dice_2 = POSSIBLE_DICES[randrange(0, len(POSSIBLE_DICES))]
        user_roll_1 = roll_the_dice(user_dice_1)
        user_roll_2 = roll_the_dice(user_dice_2)
        user_roll_sum = user_roll_1 + user_roll_2
        computer_roll_1 = roll_the_dice(computer_dice_1)
        computer_roll_2 = roll_the_dice(computer_dice_2)
        computer_roll_sum = computer_roll_1 + computer_roll_2
        user_points = calculate_points(user_roll_sum, user_points)
        computer_points = calculate_points(computer_roll_sum, computer_points)
        if user_points > 2001 or computer_points > 2001:
            if user_points > computer_points: win = 1
            elif user_points < computer_points: win = 2
            else: win = 3
        else: win = 0
        return render_template("2001.html",
                               rk=POSSIBLE_DICES, win=win,
                               upts=user_points, cpts=computer_points,
                               ud1=user_dice_1, ud2=user_dice_2,
                               cd1=computer_dice_1, cd2=computer_dice_2,
                               ur1=user_roll_1, ur2=user_roll_2,
                               cr1=computer_roll_1, cr2=computer_roll_2)
    else:
        return render_template("2001.html",
                               rk=POSSIBLE_DICES, win=0,
                               upts=0, cpts=0,
                               cd1="D3", cd2="D3")


if __name__ == "__main__":
    app.run(debug=True)
