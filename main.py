from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/cadastrar-eventos")
def cadastrar_eventos():
    return render_template("cadastrar_eventos.html")

@app.route("/eventos")
def eventos():
    return render_template("eventos.html")