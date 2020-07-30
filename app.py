from datetime import date
from flask import Flask, render_template, url_for

app = Flask(__name__)
year = date.today().year


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", title="marktripney | home")


if __name__ == "__main__":
    app.run()
