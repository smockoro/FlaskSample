from flask import Flask, render_template

app = Flask(__name__)

@app.route("/list")
def list():
    books = ["Rasyoumon", "KumonoIto", "Tosisyun"]
    return render_template("list.html", items=books)

app.run()
