from flask import Flask, request
from brain import brain

app = Flask(__name__)
br = brain()


@app.route("/weather", methods=["GET", "POST"])
def weather():
    if request.method == "GET":
        w_stats = br.get_weather()
        return w_stats
    elif request.method == "POST":
        data = request.get_json()
        data = data["sentence"].split()[-2:]
        print(data)
        data = ",".join(data)
        w_stats = br.get_weather(data)
        return w_stats


@app.route("/twitter", methods=["GET", "POST"])
def twitter():
    if request.method == "POST":
        data = request.get_json()
        print(data["sentence"])
        return br.twitter(data["sentence"])[0]


@app.route("/yelp", methods=["GET", "POST"])
def yelp():
    if request.method == "POST":
        data = request.get_json()
        print(data["sentence"])
        return br.yelp(data["sentence"])


@app.route("/spotify", methods=["GET", "POST"])
def spotify():
    if request.method == "POST":
        data = request.get_json()
        print(data["sentence"])
        return br.spotify(data["sentence"])


if __name__ == "__main__":
    app.run()
