import random
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "hellokeyword"

# random.randint(1, 100)


# ================================
# Root Route - Renders Form
# ================================

@app.route("/")
def index():
    # try:
    #     print('session')
    #     session["comp_guss"] = random.randint(1, 100)
    #     print("success print")
    #     print(session["comp_guss"])
    # except:
    #     print("try failed")

    if "comp_guess" in session:
        print("computer_guess = " + str(session["comp_guess"]))
    else:
        session["comp_guess"] = random.randint(1, 100)
    if"comparison" not in session:
        session["comparison"] = "none"
        session["counter"]=0

    return render_template("index.html",
    comparison = session["comparison"], 
    counter=session["counter"])

# ================================
# Process Form
# ================================


@app.route("/process_guess", methods=["post"])
def process():
    print(request.form)

    session["counter"] = session["counter"]+1

    if request.form["guess"] != "":
        user_guess = int(request.form["guess"])
    else:
        return redirect("/")

    comp_guess = session["comp_guess"]

    # if session["comp_guess"]==user_guess:
    #     print("you got it right!")

    # else:
    #     print("You got it wrong!")

    # the below line is to check greater or less than
    if comp_guess > user_guess:
        session["comparison"] = "low"
    elif comp_guess < user_guess:
        session["comparison"] = "high"
    else:
        session["comparison"] = "perfect"

    print(session["comparison"])
    return redirect("/")  # <--our based route or can be a different route

# ================================
# Reset the Game
# ================================

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/ ")


if __name__ == "__main__":
    app.run(debug=True)
