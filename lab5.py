from flask import Blueprint, render_template, request, redirect, url_for, session
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash

lab5 = Blueprint('lab5', __name__)

@lab5.route('/lab5')
def index():
    username = session.get('username', 'anonymous')
    return render_template('lab5/menu.html', username=username)


def db_connect():
    conn = psycopg2.connect(
        host='127.0.0.1',
        database='vladislav_pechenkin_knowledge_base',
        user='vladislav_pechenkin_knowledge_base',
        password='123'
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

@lab5.route('/lab5/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab5/register.html')
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not (login or password):
        return render_template('lab5/register.html', error='Заполните все поля')
    
    conn, cur = db_connect()

    cur.execute("SELECT * FROM users WHERE login=%s;", (login, ))
    if cur.fetchone():
        db_close(conn, cur)
        return render_template('lab5/register.html', error="Такой пользователь уже существует")

    password_hash = generate_password_hash(password)    
    cur.execute("INSERT INTO users (login, password) VALUES (%s, %s);", (login, password_hash))

    db_close(conn, cur)
    return render_template('lab5/success.html', login=login)

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

    
    if not title or not article_text:
        return render_template('lab5/create_article.html', error="Тема и текст статьи не могут быть пустыми")

    conn, cur = db_connect()

    cur.execute("SELECT * FROM users WHERE login=%s;", (login, ))
    user = cur.fetchone()
    if not user:
        db_close(conn, cur)
        return "Пользователь не найден"  
    login_id = user["id"]

    cur.execute("INSERT INTO articles(login_id, title, article_text) VALUES (%s, %s, %s);", 
                (login_id, title, article_text))

    db_close(conn, cur)

    return redirect('/lab5')

@lab5.route('/lab5/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('lab5.index'))

@lab5.route('/lab5/edit_article/<int:article_id>', methods=['GET', 'POST'])
def edit_article(article_id):
    login = session.get('username')
    if not login:
        return redirect('/lab5/login')

    conn, cur = db_connect()

    cur.execute("SELECT * FROM articles WHERE id=%s;", (article_id,))
    article = cur.fetchone()

    if not article:
        db_close(conn, cur)
        return "Статья не найдена"

    cur.execute("SELECT id FROM users WHERE login=%s;", (login,))
    user_id = cur.fetchone()["id"]

    if article["login_id"] != user_id:
        db_close(conn, cur)
        return "У вас нет прав на редактирование этой статьи"

    if request.method == 'POST':
        title = request.form.get('title')
        article_text = request.form.get('article_text')

        if not title or not article_text:
            db_close(conn, cur)
            return render_template('lab5/edit_article.html', article=article, error="Тема и текст статьи не могут быть пустыми")

        cur.execute("UPDATE articles SET title=%s, article_text=%s WHERE id=%s;", (title, article_text, article_id))
        db_close(conn, cur)

        return redirect(url_for('lab5.list'))

    db_close(conn, cur)
    return render_template('lab5/edit_article.html', article=article)

@lab5.route('/lab5/delete_article/<int:article_id>', methods=['POST'])
def delete_article(article_id):
    login = session.get('username')
    if not login:
        return redirect('/lab5/login')

    conn, cur = db_connect()

    cur.execute("SELECT * FROM articles WHERE id=%s;", (article_id,))
    article = cur.fetchone()

    if not article:
        db_close(conn, cur)
        return "Статья не найдена"

    cur.execute("SELECT id FROM users WHERE login=%s;", (login,))
    user_id = cur.fetchone()["id"]

    if article["login_id"] != user_id:
        db_close(conn, cur)
        return "У вас нет прав на удаление этой статьи"

    cur.execute("DELETE FROM articles WHERE id=%s;", (article_id,))
    db_close(conn, cur)

    return redirect(url_for('lab5.list'))

@lab5.route('/lab5/users')
def users():
    conn, cur = db_connect()

    cur.execute("SELECT login FROM users;")
    users = cur.fetchall()

    db_close(conn, cur)

    return render_template('lab5/users.html', users=users)

@lab5.route('/lab5/toggle_favorite/<int:article_id>', methods=['POST'])
def toggle_favorite(article_id):
    login = session.get('username')
    if not login:
        return redirect('/lab5/login')

    conn, cur = db_connect()

    cur.execute("SELECT * FROM articles WHERE id=%s;", (article_id,))
    article = cur.fetchone()

    if not article:
        db_close(conn, cur)
        return "Статья не найдена"

    cur.execute("SELECT id FROM users WHERE login=%s;", (login,))
    user_id = cur.fetchone()["id"]

    if article["login_id"] != user_id:
        db_close(conn, cur)
        return "У вас нет прав на изменение этой статьи"

    
    new_is_favorite = not article["is_favorite"]
    cur.execute("UPDATE articles SET is_favorite=%s WHERE id=%s;", (new_is_favorite, article_id))

    db_close(conn, cur)

    return redirect(url_for('lab5.list'))

@lab5.route('/lab5/public_articles')
def public_articles():
    conn, cur = db_connect()

    cur.execute("""
        SELECT articles.*, users.login AS author_login 
        FROM articles 
        JOIN users ON articles.login_id = users.id 
        WHERE articles.is_public=True;
    """)
    public_articles = cur.fetchall()

    db_close(conn, cur)

    return render_template('lab5/public_articles.html', public_articles=public_articles)

@lab5.route('/lab5/toggle_public/<int:article_id>', methods=['POST'])
def toggle_public(article_id):
    login = session.get('username')
    if not login:
        return redirect('/lab5/login')

    conn, cur = db_connect()

    cur.execute("SELECT * FROM articles WHERE id=%s;", (article_id,))
    article = cur.fetchone()

    if not article:
        db_close(conn, cur)
        return "Статья не найдена"

   
    cur.execute("SELECT id FROM users WHERE login=%s;", (login,))
    user_id = cur.fetchone()["id"]

    if article["login_id"] != user_id:
        db_close(conn, cur)
        return "У вас нет прав на изменение этой статьи"

    new_is_public = not article["is_public"]
    cur.execute("UPDATE articles SET is_public=%s WHERE id=%s;", (new_is_public, article_id))

    db_close(conn, cur)

    return redirect(url_for('lab5.list'))