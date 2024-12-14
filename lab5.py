from flask import Blueprint, render_template, request, redirect, url_for, session
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash

lab5 = Blueprint('lab5', __name__)

@lab5.route('/lab5')
def index():
    username = session.get('username', 'anonymous')
    return render_template('lab5/menu.html', username=username, login=session.get('username'))

def db_connect():
    conn = psycopg2.connect(
        host='127.0.0.1',
        database='irina_proskuryakova_knowledge_base',
        user='irina_proskuryakova_knowledge_base',
        password='123',
    )
    cur = conn.cursor(cursor_factory=RealDictCursor)
    return conn, cur 
    
def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

@lab5.route('/lab5/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab5/login.html')
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not (login or password):
        return render_template('lab5/login.html', error="Заполните поля")
    
    try:
        conn, cur = db_connect()

        cur.execute("SELECT * FROM users WHERE login=%s;", (login, ))
        user = cur.fetchone()

        if not user:
            db_close(conn, cur)
            return render_template('lab5/login.html', error='Логин и/или пароль неверны')
        
        if not check_password_hash(user['password'], password):
            db_close(conn, cur)
            return render_template('lab5/login.html', error='Логин и/или пароль неверны')
        
        db_close(conn, cur)
        session['username'] = login  
        return render_template('lab5/success_login.html', login=login)
    except Exception as e:
        return render_template('lab5/login.html', error=f"Ошибка при подключении к базе данных: {str(e)}")

@lab5.route('/lab5/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab5/register.html')
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not (login or password):
        return render_template('lab5/register.html', error='Заполните все поля')
    
    try:
        conn, cur = db_connect()

        cur.execute("SELECT * FROM users WHERE login=%s;", (login,))
        if cur.fetchone():
            db_close(conn, cur)
            return render_template('lab5/register.html', error="Такой пользователь уже существует")

        password_hash = generate_password_hash(password)    
        cur.execute("INSERT INTO users (login, password) VALUES (%s, %s);", (login, password_hash))

        db_close(conn, cur)
        return render_template('lab5/success.html', login=login)
    except Exception as e:
        return render_template('lab5/register.html', error=f"Ошибка при подключении к базе данных: {str(e)}")

@lab5.route('/lab5/list')
def list():
    login = session.get('username')
    if not login:
        return redirect('/lab5/login')
    
    conn, cur = db_connect()

    cur.execute("SELECT id FROM users WHERE login=%s;", (login,))
    login_id = cur.fetchone()["id"]

    cur.execute("""
        SELECT * FROM articles 
        WHERE login_id=%s 
        ORDER BY is_favorite DESC, id ASC;
    """, (login_id,))
    articles = cur.fetchall()

    db_close(conn, cur)

    no_articles = len(articles) == 0

    return render_template('/lab5/articles.html', articles=articles, no_articles=no_articles)

@lab5.route('/lab5/create', methods=['GET', 'POST'])
def create():
    login = session.get('username')

    if not login:
        return redirect('/lab5/login')
    
    if request.method == 'GET':
        return render_template('lab5/create_article.html')
    
    title = request.form.get('title')
    article_text = request.form.get('article_text')

    conn, cur = db_connect()

    cur.execute("SELECT * FROM users WHERE login=%s;", (login, ))
    user = cur.fetchone()
    
    login_id = user["id"]
    cur.execute(f"INSERT INTO articles(login_id, title, article_text) \
                VALUES ({login_id}, '{title}', '{article_text}')")
    
    db_close(conn, cur)
    return redirect('/lab5')