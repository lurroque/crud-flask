from flask import Flask, render_template, request, redirect, session, flash
from jogo import Jogo

app = Flask(__name__)
app.secret_key = "ASUDhwiqoudhsaqioweu!@3oasd23897a&%65"

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
                            titulo="Novo Jogo"
    )

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
                            titulo="Faça seu login"
    )

@app.route("/autenticar", methods=["POST",])
def autenticar():
    usuario = request.form["usuario"]
    senha = request.form["senha"]
    if senha == "mestra":
        session["usuario_logado"] = usuario
        flash("Login efetuado com sucesso!")
        flash("Bem-vindo, {}!".format(usuario.title()))
        return redirect("/")
    flash("Usuário ou senha incorretos, tente novamente!")
    return redirect("/login")

@app.route("/logout")
def logout():
    session["usuario_logado"] = None
    flash("Nenhum usuário logado")
    
    return redirect("/")
        
app.run(debug=True)
