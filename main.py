import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def index():
    return render_template("index.html")

@app.route("/about_me")
def about_me():

    godina = datetime.datetime.now().year

    poruka = "Pozdrav iz Python programa!"

    return render_template("about_me.html", godina=godina, poruka=poruka)

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

if __name__ == '__main__' :
    app.run()


