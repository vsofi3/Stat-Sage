from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

# Temporary login credentials
USER = {
    "username": "test",
    "password": "password"
}


# ================= ROUTES ================= #

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    username = request.form["username"]
    password = request.form["password"]

    if username == USER["username"] and password == USER["password"]:
        session["user"] = username
        return redirect(url_for("home"))
    else:
        return "Invalid login. Try again."


@app.route("/home")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("home.html", user=session["user"])


@app.route("/overall rankings")
def overall():
    return render_template("overall rankings.html")


@app.route("/upcoming games")
def upcoming():
    return render_template("upcoming games.html")


@app.route("/injury reports")
def injuries():
    return render_template("injury reports.html")


@app.route("/my team")
def myteam():
    return render_template("my team.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
