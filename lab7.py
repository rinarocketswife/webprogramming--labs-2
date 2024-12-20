from flask import Flask, Blueprint, render_template, request, jsonify
from datetime import datetime
import psycopg2

app = Flask(__name__)

DB_CONFIG = {
    'dbname': 'irina_proskuryakova_knowledge_base',  
    'user': 'irina_proskuryakova_knowledge_base', 
    'password': '123',  
    'host': '127.0.0.1',  
}

def get_db_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("Успешное подключение к базе данных")  
        return conn
    except Exception as e:
        print("Ошибка подключения к базе данных:", e)
        return None

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')

@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM films')
    films = cursor.fetchall()
    conn.close()
    return jsonify([{'id': film[0], 'title': film[1], 'title_ru': film[2], 'year': film[3], 'description': film[4]} for film in films])

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM films WHERE id = %s', (id,))
    film = cursor.fetchone()
    conn.close()
    if film is None:
        return jsonify({"error": "Film not found"}), 404
    return jsonify({'id': film[0], 'title': film[1], 'title_ru': film[2], 'year': film[3], 'description': film[4]})

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    cursor = conn.cursor()
    cursor.execute('DELETE FROM films WHERE id = %s', (id,))
    conn.commit()
    conn.close()
    return '', 204

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    cursor = conn.cursor()
    film = request.get_json()

 
    if not film.get('title_ru'):
        return jsonify({"error": "Русское название не может быть пустым"}), 400

    if not film.get('title') and not film.get('title_ru'):
        return jsonify({"error": "Оригинальное название не может быть пустым, если русское название пустое"}), 400

    if not film.get('year') or not (1895 <= int(film['year']) <= datetime.now().year):
        return jsonify({"error": "Год должен быть от 1895 до текущего года"}), 400

    if not film.get('description') or len(film['description']) > 2000:
        return jsonify({"error": "Описание должно быть непустым и не более 2000 символов"}), 400

  
    if not film.get('title'):
        film['title'] = film['title_ru']

    cursor.execute('''
        UPDATE films
        SET title = %s, title_ru = %s, year = %s, description = %s
        WHERE id = %s
    ''', (film['title'], film['title_ru'], film['year'], film['description'], id))
    conn.commit()
    conn.close()
    return jsonify(film)

@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    cursor = conn.cursor()
    new_film = request.get_json()


    if not new_film.get('title_ru'):
        return jsonify({"error": "Русское название не может быть пустым"}), 400

    if not new_film.get('title') and not new_film.get('title_ru'):
        return jsonify({"error": "Оригинальное название не может быть пустым, если русское название пустое"}), 400

    if not new_film.get('year') or not (1895 <= int(new_film['year']) <= datetime.now().year):
        return jsonify({"error": "Год должен быть от 1895 до текущего года"}), 400

    if not new_film.get('description') or len(new_film['description']) > 2000:
        return jsonify({"error": "Описание должно быть непустым и не более 2000 символов"}), 400

    if not new_film.get('title'):
        new_film['title'] = new_film['title_ru']

    cursor.execute('''
        INSERT INTO films (title, title_ru, year, description)
        VALUES (%s, %s, %s, %s)
        RETURNING id
    ''', (new_film['title'], new_film['title_ru'], new_film['year'], new_film['description']))
    new_film_id = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return jsonify({"message": "Film added", "id": new_film_id}), 201

app.register_blueprint(lab7)

if __name__ == '__main__':
    app.run(debug=True)