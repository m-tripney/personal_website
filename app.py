from flask import Flask, render_template, url_for
from flask_talisman import Talisman

SELF = "'self'"
# fmt: off
csp = {
    'default-src': SELF,
    'script-src': [
        SELF,
        'unsafe-inline',
        'use.typekit.net',
        'cdn.jsdelivr.net/npm/clipboard@2/dist/clipboard.min.js',
    ],
    'style-src': [SELF, 'use.typekit.net'],
    'font-src': [SELF, 'use.typekit.net'],
    'img-src': [SELF, 'p.typekit.net'],
    'object-src': 'none',
}
# fmt: on

app = Flask(__name__)
talisman = Talisman(app, content_security_policy=csp)

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
