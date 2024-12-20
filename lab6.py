from flask import Blueprint, render_template, request, session, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash

lab6 = Blueprint('lab6', __name__)

def db_connect():
    conn = psycopg2.connect(
        host='127.0.0.1',
        database='irina_proskuryakova_knowledge_base',
        user='irina_proskuryakova_knowledge_base',
        password='123'
    )
    cur = conn.cursor(cursor_factory=RealDictCursor)
    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

offices = []
for i in range(1, 11):
    offices.append({"number": i, "tenant": "", "price": 1000})

@lab6.route('/lab6/')
def main():
    return render_template('lab6/lab6.html')

@lab6.route('/lab6/json-rpc-api/', methods=['POST'])
def api():
    try:
        data = request.json
    except Exception as e:
        return jsonify({
            'jsonrpc': '2.0',
            'error': {
                'code': -32700,
                'message': 'Parse error'
            },
            'id': None
        }), 400

    if not all(key in data for key in ['jsonrpc', 'method', 'id']):
        return jsonify({
            'jsonrpc': '2.0',
            'error': {
                'code': -32600,
                'message': 'Invalid Request'
            },
            'id': data.get('id')
        }), 400

    id = data['id']
    method = data['method']

    if method == 'info':
        return jsonify({
            'jsonrpc': '2.0',
            'result': offices,
            'id': id
        })

    login = session.get('login')
    if not login:
        return jsonify({
            'jsonrpc': '2.0',
            'error': {
                'code': 1,
                'message': 'Unauthorized'
            },
            'id': id
        }), 401

    if method == 'booking':
        params = data.get('params')
        if not isinstance(params, int):
            return jsonify({
                'jsonrpc': '2.0',
                'error': {
                    'code': -32602,
                    'message': 'Invalid params'
                },
                'id': id
            }), 400

        for office in offices:
            if office['number'] == params:
                if office['tenant']:
                    return jsonify({
                        'jsonrpc': '2.0',
                        'error': {
                            'code': 2,
                            'message': 'Already booked'
                        },
                        'id': id
                    }), 400

                office['tenant'] = login
                return jsonify({
                    'jsonrpc': '2.0',
                    'result': 'success',
                    'id': id
                })

        return jsonify({
            'jsonrpc': '2.0',
            'error': {
                'code': 3,
                'message': 'Office not found'
            },
            'id': id
        }), 404

    return jsonify({
        'jsonrpc': '2.0',
        'error': {
            'code': -32601,
            'message': 'Method not found'
        },
        'id': id
    }), 404


@lab6.route('/lab6/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab6/login.html')
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not (login or password):
        return render_template('lab6/login.html', error="Заполните поля")
    
    conn, cur = db_connect()

    cur.execute("SELECT * FROM users WHERE login=%s;", (login, ))
    user = cur.fetchone()

    if not user:
        db_close(conn, cur)
        return render_template('lab6/login.html', error='Логин и/или пароль неверны')
    
    if not check_password_hash(user['password'], password):
        db_close(conn, cur)
        return render_template('lab6/login.html', error='Логин и/или пароль неверны')
    
    db_close(conn, cur)
    session['username'] = login
    return redirect(url_for('lab6.main'))

@lab6.route('/lab6/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab6/register.html')
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not (login or password):
        return render_template('lab6/register.html', error='Заполните все поля')
    
    conn, cur = db_connect()

    cur.execute("SELECT * FROM users WHERE login=%s;", (login, ))
    if cur.fetchone():
        db_close(conn, cur)
        return render_template('lab6/register.html', error="Такой пользователь уже существует")

    password_hash = generate_password_hash(password)    
    cur.execute("INSERT INTO users (login, password) VALUES (%s, %s);", (login, password_hash))

    db_close(conn, cur)
    return redirect(url_for('lab6.login'))

@lab6.route('/lab6/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('lab6.main'))

