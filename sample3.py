from flask import Flask, url_for, redirect, render_template

app = Flask(__name__)

@app.route("/to_list")
def to_list():
    return redirect("list")

@app.route("/")
def index():
    return redirect(url_for("show_list"))

@app.route("/list")
def show_list():
    return "list"

app.run()
