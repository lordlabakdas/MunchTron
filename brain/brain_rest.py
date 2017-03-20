from flask import Flask
from brain import brain

app = Flask(__name__)

@app.route("/weather")
def weather():
    br = brain()
    w_stats = br.get_weather()
    return w_stats


if __name__ == "__main__":
    app.run()
