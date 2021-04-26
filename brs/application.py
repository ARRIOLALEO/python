import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        delete = request.form.get("delete")
        if delete:
            # first i need to know if the id exist
            exist = db.execute("SELECT COUNT(*) FROM birthdays WHERE id=(?)",delete)
            if exist:
                db.execute("DELETE FROM birthdays WHERE id=(?)",delete)
        else:
            name=request.form.get("name")
            month = request.form.get("month")
            day = request.form.get("day")
            db.execute("INSERT INTO birthdays(name, month, day) values(?,?,?)",name,month,day)

        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        birdday = db.execute('SELECT * FROM birthdays')
        return render_template("index.html", birdday = birdday)


