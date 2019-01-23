from flask import Flask, render_template, request, redirect, session, flash
from jogo import Jogo

app = Flask(__name__)
app.secret_key = "Zanguerson!"

lista_de_jogos = []

@app.route("/")
def index():

    return render_template("index.html", 
                            titulo="Jogos",
                            jogos=lista_de_jogos
    )

@app.route("/novo")
def novo_jogo():

    return render_template("novo-jogo.html",
                            titulo="Novo Jogo")

@app.route("/criar", methods=["POST",])
def criar_novojogo():
    nome = request.form["nome"]
    categoria = request.form["categoria"]
    console = request.form["console"]
    jogo = Jogo(nome, categoria, console)
    lista_de_jogos.append(jogo)

    return redirect("/")

@app.route("/login")
def login():
    
    return render_template("login.html",
                            titulo="Faça seu login")

@app.route("/autenticar", methods=["POST",])
def autenticar():
    usuario = request.form["usuario"]
    senha = request.form["senha"]
    if senha == "mestra":
        session["usuario_logado"] = usuario
        flash("{} logado com sucesso!".format(usuario))
        return redirect("/")
    flash("Usuário ou senha incorretos, tente novamente!")
    return redirect("/login")
        
app.run(debug=True)
