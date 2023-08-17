from flask import Flask, jsonify, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Rota para listar todos os filmes
@app.route('/api/filmes', methods=['GET'])
def obter_todos_os_filmes():
    conn = sqlite3.connect('netflix_db.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT Title FROM netflix_data")
    filmes = cursor.fetchall()
    conn.close()
    return jsonify(filmes)

# Rota para listar filmes similares
@app.route('/api/similares', methods=['GET'])
def obter_filmes_similares():
    titulo_do_filme = request.args.get('titulo_do_filme')
    
    if not titulo_do_filme:
        return jsonify({'erro': 'Parâmetro titulo_do_filme não fornecido'}), 400
    
    conn = sqlite3.connect('netflix_db.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT Title FROM netflix_data WHERE Genre LIKE '%' || (SELECT Genre FROM netflix_data WHERE Title = ?) || '%' OR Tags LIKE '%' || (SELECT Tags FROM netflix_data WHERE Title = ?) || '%'", (titulo_do_filme, titulo_do_filme))
    filmes_similares = cursor.fetchall()
    conn.close()
    return jsonify(filmes_similares)

if __name__ == '__main__':
    app.run(debug=True)
