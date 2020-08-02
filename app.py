from flask import Flask, render_template, url_for


app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", title="home")


@app.route("/work")
def work():
    return render_template("work.html", title="work")


@app.route("/writing")
def writing():
    return render_template("writing.html", title="writing")


@app.route("/contact")
def contact():
    return render_template("contact.html", title="contact")


if __name__ == "__main__":
    app.run()
