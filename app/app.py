from flask import Flask



app = Flask(__name__)


@app.route("/")    #método rota que faz a página conectar nos links  -  essa barrinha / para indicar que é rota principal
def home():       # criado função rota da home (por exemplo, hello world)
    return "Olá, mundo! Aplicação rodando no Docker."


if __name__ == "__main__":
    app.run(debug=True)   # aqui para avisar sobre erros


