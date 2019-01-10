from flask import Flask, render_template
from jogo import Jogo

app = Flask(__name__)

lista_de_jogos = []
jogo1 = Jogo("Dota", "MOBA", "PC")
lista_de_jogos.append(jogo1)

@app.route("/")
def index():
    return render_template("index.html", 
                           titulo="Jogos",
                           jogos = lista_de_jogos)

app.run(debug=True)

