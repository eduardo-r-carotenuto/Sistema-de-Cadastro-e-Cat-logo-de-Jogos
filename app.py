from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# caminho correto do banco
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(BASE_DIR, 'loja.db')


def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db()
    cur = conn.cursor()

    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        generos = request.form['generos']
        nota = request.form['nota']
        lancamento = request.form['lancamento']
        imagem = request.form['imagem']

        cur.execute("""
            INSERT INTO jogos (nome, preco, generos, nota, lancamento, imagem)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nome, preco, generos, nota, lancamento, imagem))

        conn.commit()
        conn.close()
        return redirect('/')

    cur.execute("SELECT * FROM jogos")
    jogos = cur.fetchall()
    conn.close()

    return render_template('index.html', jogos=jogos)


@app.route('/importar-api')
def importar_api():
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
