from flask import Flask, redirect, url_for, render_template, session
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5  
from lab6 import lab6
from lab7 import lab7 

app = Flask(__name__)

app.secret_key = 'секретно-секретный секрет'

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)  
app.register_blueprint(lab6)
app.register_blueprint(lab7)    

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
     return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>

        <h1>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1>

        </header>
        <nav>
            <ul>
                <li><a href="/lab1">Первая лабораторная</a></li>
            </ul>
            <ul>
                <li><a href="/lab2">Вторая лабораторная</a></li>
            </ul>
            <ul>
                <li><a href="/lab3">Третья лабораторная</a></li>
            </ul>
            <ul>
                <li><a href="/lab4">Четвертая лабораторная</a></li>
            </ul>
            <ul>
                <li><a href="/lab5">Пятая лабораторная</a></li>
            </ul>
            <ul>
                <li><a href="/lab6">Шестая лабораторная</a></li>
            </ul>
            <ul>
                <li><a href="/lab7">Седьмая лабораторная</a></li>
            </ul>
        </nav>
        <footer>
            &copy; Проскурякова Ирина Дмитриевна, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""