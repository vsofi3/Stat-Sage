from flask import Flask, render_template, request, redirect, url_for, session
from newsapi import NewsApiClient
import os
from datetime import datetime, timedelta

# initialize once (you need to sign up at newsapi.org and get an API key)
# newsapi = NewsApiClient(api_key=os.getenv("NEWSAPI_KEY"))
# Your API key is: 448484be285c48c484fcb3b0f1d88252
newsapi = NewsApiClient(api_key="448484be285c48c484fcb3b0f1d88252")


def get_nfl_news(limit=10):
    response = newsapi.get_top_headlines(
        q="NFL",
        language="en",
        page_size=limit
    )
    return response.get("articles", [])



app = Flask(__name__)
app.secret_key = "password"

# Temporary login credentials
USER = {
    "username": "test@gmail.com",
    "password": "password"
}

# ================= ROUTES ================= #

@app.route("/")
def login():
    return render_template("index.html")


@app.route("/index", methods=["POST"])
def login_post():
    username = request.form["username"]
    password = request.form["password"]

    if username == USER["username"] and password == USER["password"]:
        session["user"] = username
        return redirect(url_for("home"))
    else:
        return "Invalid login. Try again."


@app.route("/homepage")
def home():
    if "user" not in session:
        return redirect(url_for("login"))

    news = get_nfl_news(limit=10)

    return render_template(
        "homepage.html",
        user=session["user"],
        news=news
    )


@app.route("/overall-rankings")
def overall():
    return render_template("overall_rankings.html")


@app.route("/upcoming-games")
def upcoming():
    return render_template("upcoming_games.html")


@app.route("/injury-reports")
def injuries():
    return render_template("injury_reports.html")


@app.route("/my-team")
def myteam():
    return render_template("my_team.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
