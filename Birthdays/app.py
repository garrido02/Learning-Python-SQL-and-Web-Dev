import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # Add the user's entry into the database
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")
        db.execute("INSERT INTO birthdays(name, month, day) VALUES (?, ?, ?)", name, month, day)
        return redirect("/")

    else:

        # Display the entries in the database on index.html
        entries = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", entries=entries)


@app.route("/delete", methods=["POST"])
def delete():

    # Get the id of each row, delete that row if called and redirect to root
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM birthdays WHERE id = ?", id)
    return redirect("/")


@app.route("/edit", methods=["POST"])
def edit():
    # create a new route that sends user to another html to edit
    # get the id that the user wants to edit
    id = request.form.get("id")
    return render_template("edit.html", id=id)

@app.route("/change", methods=["POST"])
def change():

    # get all variables that the user wants to edit, being the id the same
    id = request.form.get("id")
    name = request.form.get("name")
    month = request.form.get("month")
    day = request.form.get("day")

    # conditions to every change the user can possibly make
    if id and month and day:
        db.execute("UPDATE birthdays SET month = ?, day = ? WHERE id = ?", month, day, id)

    elif id and month:
        db.execute("UPDATE birthdays SET month = ? WHERE id = ?", month, id)

    else:
        db.execute("UPDATE birthdays SET day = ? WHERE id = ?", day, id)

    return redirect("/")

