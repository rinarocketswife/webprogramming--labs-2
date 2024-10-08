from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

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

        <a href="/lab1">Первая лабораторная</a>

        <footer>
            &copy; Ирина Проскурякова, ФБИ-24, 3 курс, 2024
        </footer> 
</html>
"""
@app.route("/lab1")
def lab1():
     return """
<!doctype html>
<html>
    <head>
        <title>Проскурякова Ирина Дмитриевна, лабораторная 1</title>
    </head>
    <body>
        <header>

        <h1>web-сервер на flask</h1>

        </header>

        <p>
        Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </p>

        <p>
            <ul>
                <li><a href="/menu">Меню</a></li>
            </ul>
        </p>

        <h2>Реализованные роуты</h2>

        <p>
            <ul>
                <li><a href="/lab1/oak">Дуб</a></li>
                <li><a href="/lab1/student">Студент</a></li>
                <li><a href="/lab1/python">Python</a></li>
                <li><a href="/lab1/personal">Personal</a></li>
            </ul>
        </p>

        <footer>
            &copy; Ирина Проскурякова, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""
@app.route('/lab1/oak')
def oak():
     return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') +'''">
    </body>
</html>
'''
@app.route('/lab1/student')
def student():
     return '''
<!doctype html>
<html>
    <head>
        <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Студент</title>
    </head>
    <body>
        <h1>Проскурякова Ирина Дмитриевна</h1>
        <img src="''' + url_for('static', filename='logo.png') + '''" class="Student">
    </body>
</html>
'''
@app.route('/lab1/python')
def python():
     return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Python</title>
    </head>
    <body>
        <h1>Что такое Python?</h1>
        <p>
            Python – это высокоуровневый язык программирования, который был разработан в конце 1980-х годов. Его разработчик, Гвидо ван Россум, вложил в основу языка простоту и читабельность кода, что позволяет 
            использовать Python для быстрой и эффективной разработки. Много популярных веб-сайтов, компьютерных игр и программ, написанных на Python, вы используете ежедневно: Dropbox, Uber, Sims, Google, GIMP и другие.
        </p>
        <p>
            Язык отличается понятным синтаксисом, поэтому Python подходит для начинающих программистов. Он широко используется 
            во многих областях: веб-разработка, научные исследования, анализ данных, искусственный интеллект, машинное обучение, разработка игр. 
        </p>
        <img src="''' + url_for('static', filename='python.jpg') + '''"class="Python">
    </body>
</html>
'''

@app.route('/lab1/personal')
def personal():
     return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>NIKE</title>
    </head>
    <body>
                <h1>NIKE</h1>
        <p>
            Nike — американская транснациональная компания, специализирующаяся на спортивной одежде и обуви. 
            Штаб-квартира — в городе Бивертон (штат Орегон).
        </p>
        <p>
           Почти вся продукция Nike производится сторонними компаниями-подрядчиками вне территории США (в основном в Азии), сама компания является правообладателем торговых марок, разрабатывает дизайн продукции и владеет сетью магазинов 
           (около 1150 по всему миру), а также торговых центров NikeTown. С 20 сентября 2013 года входит в Промышленный индекс Доу Джонса. Nike является самым дорогим спортивным брендом в мире.
        </p>
        <p>
        Компания, основанная 25 января 1964 года под названием Blue Ribbon Sports, официально стала Nike, Inc. в 1978 году. Nike продаёт свою продукцию под собственным брендом, а также под марками Nike Golf, Nike Pro, Nike +, Air Jordan, Nike Blazers, Air Force 1, Nike Dunk, Air Max, Foamposite, Nike Skateboarding, Nike CR7, Hurley International, Converse. 
        Nike является спонсором многих спортсменов и спортивных команд по всему миру. Начиная с 1990-х годов компания регулярно подвергается критике за то, что её продукция производится на фабриках, где нарушается трудовое законодательство.
        </p>
        <img src="''' + url_for('static', filename='nike.png') + '''"class="Car">
    </body>
</html>
'''

# @app.route('/lab2/a')
# def a():
#      return 'без слэша'

# @app.route('/lab2/a/')
# def a():
#      return 'со слэшем'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']
     
@app.route('/lab2/add_flower/<name>')
def add_flower(name):
     flower_list.append(name)
     return f'''
<!docktype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name} </p>
    <p>Всего цветов: {len(flower_list)} </p>
    <p>Полный список: {flower_list} </p>
    </body>
</html>
'''

@app.route('/lab2/example')
def example():
     return render_template('example.html')
