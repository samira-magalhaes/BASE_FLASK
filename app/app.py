from flask import Flask, render_template



app = Flask(__name__)


@app.route("/")    #método rota que faz a página conectar nos links  -  essa barrinha / para indicar que é rota principal
def home():       # criado função rota da home (por exemplo, hello world)
    # return "Olá, mundo! Aplicação rodando no Docker."
    return render_template('index.html')


@app.route('/user/<username>')
def show_user(username):
    return f"Bem-vindo, {username}!"


@app.route("/sobre")
def sobre():
    return render_template('sobre.html')


# @app.route("/sobre")
# def sobre():
#     return render_template('sobre.html')


if __name__ == "__main__":
    app.run(debug=True)   # aqui para avisar sobre erros


