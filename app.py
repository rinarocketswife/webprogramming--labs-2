from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
    return """
<!docktype html> 
<html> 
    <head>
        <title>Проскурякова Ирина Дмитриевна, Лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>

        <footer>
            &copy; Ирина Проскурякова, ФБИ-24, 3 курс, 2024
        </footer> 
</html>
"""