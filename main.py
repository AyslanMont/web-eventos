from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os 

login_manager = LoginManager()
load_dotenv()

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_PORT'] = int(os.getenv('MYSQL_PORT'))
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
app.config['MYSQL_CURSORCLASS'] = os.getenv('MYSQL_CURSORCLASS')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

mysql = MySQL(app)
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
        self.id = None
    
    @classmethod
    def get(cls, id):
        cursor = mysql.connection.cursor()
        SELECT = "SELECT * FROM users WHERE id = %s"
        cursor.execute(SELECT, (id,))
        dados = cursor.fetchone()
        cursor.close()
        if dados:
            user = User(dados['email'], dados['senha'])
            user.id = dados['id']
            return user
        return None

    @classmethod
    def get_by_email(cls, email):
        cursor = mysql.connection.cursor()
        SELECT = "SELECT * FROM users WHERE email = %s"
        cursor.execute(SELECT, (email,))
        dados = cursor.fetchone()
        cursor.close()
        if dados:
            user = User(dados['email'], dados['senha'])
            user.id = dados['id']
            return user
        return None


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/", methods=["GET", "POST"])
def home():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    else:
        return redirect(url_for('login'))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        senha = request.form['password']
        user = User.get_by_email(email)
        
        
        if user and check_password_hash(user.senha, senha):
            login_user(user)
            return redirect(url_for("eventos"))
    
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form['email']
        senha = request.form['password']
        user = User.get_by_email(email)
        senha_hash = generate_password_hash(senha)

        if user:
            pass
        else:
            cursor = mysql.connection.cursor()
            INSERT = "INSERT INTO users (email, senha) VALUES (%s, %s)"
            cursor.execute(INSERT, (email, senha_hash))
            mysql.connection.commit()
            cursor.close()
            flash("Registrado com sucesso", "success")
            return redirect(url_for("login"))
    
    return render_template("register.html")

@app.route("/cadastrar-eventos", methods=["GET", "POST"])
@login_required
def cadastrar_eventos():
    return render_template("cadastrar_eventos.html")

@app.route("/eventos", methods=["GET", "POST"])
@login_required
def eventos():
    return render_template("eventos.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))
