from flask import Flask, render_template, request, redirect
from jogo import Jogo

app = Flask(__name__)

lista_de_jogos = []


@app.route("/")
def index():
    return render_template("index.html", 
                           titulo="Jogos",
                           jogos=lista_de_jogos)

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

app.run(debug=True)

