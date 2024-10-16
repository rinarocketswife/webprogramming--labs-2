from flask import Flask, redirect, url_for, render_template, abort
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
<!DOCTYPE html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name} </p>
    <p>Всего цветов: {len(flower_list)} </p>
    <p>Полный список: {flower_list} </p>
    </body>
</html>
'''

@app.route('/lab2/flowers')
def list_flowers():
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Список всех цветов</h1>
    <p>Всего цветов: {len(flower_list)} </p>
    <p>Полный список: {flower_list} </p>
    </body>
</html>
'''

@app.route('/lab2/flowers/<int:flower_id>')
def show_flower(flower_id):
    if flower_id < 0 or flower_id >= len(flower_list):
        abort(404, 'цветок не найден')
    
    flower = flower_list[flower_id]
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Цветок</h1>
    <p>Название цветка: {flower} </p>
    <a href="/lab2/flowers">Вернуться к списку всех цветов</a>
    </body>
</html>
'''
@app.route('/lab2/clear_flowers')
def clear_flowers():
    global flower_list
    flower_list = []
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Список цветов очищен</h1>
    <a href="/lab2/flowers">Перейти к списку всех цветов</a>
    </body>
</html>
'''

@app.route('/lab2/example')
def example():
     name, lab_num, group, course = 'Ирина Проскурякова', 2, 'ФБИ-24', 3
     fruits = [
          {'name': 'яблоки', 'price': 100 }, 
          {'name': 'груши', 'price': 120},  
          {'name': 'апельсины', 'price': 80}, 
          {'name': 'мандарины', 'price': 95}, 
          {'name': 'манго', 'price': 321}, 
    ]
     return render_template('example.html',
                            name=name, lab_num=lab_num, group=group,
                            course=course, fruits=fruits)

@app.route('/lab2/')
def lab2():
     return render_template('lab2.html')

@app.route('/lab2/filters')
def filters():
     phrase = "0 <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
     return render_template('filter.html', phrase = phrase)

@app.route('/lab2/calc/<int:a>')
def redirect_to_default_with_a(a):
    return redirect(url_for('calculate', num1=a, num2=1))

@app.route('/lab2/calc/')
def redirect_to_default():
    return redirect(url_for('calculate', num1=1, num2=1))

@app.route('/lab2/calc/<int:num1>/<int:num2>')
def calculate(num1, num2):
    result1 = num1 + num2
    result2 = num1 - num2
    result3 = num1 * num2
    result4 = num1 / num2 if num2 != 0 else "Деление на ноль!"
    result5 = num1 ** num2

    response = f"""
    Сумма: {num1} + {num2} = {result1}<br>
    Разность: {num1} - {num2} = {result2}<br>
    Произведение: {num1} * {num2} = {result3}<br>
    Деление: {num1} / {num2} = {result4}<br>
    Возведение в степень: {num1}<sup>{num2}</sup> = {result5}
    """

    return response

books = [
    {"author": "Джордж Оруэлл", "title": "1984", "genre": "Научная фантастика", "pages": 328},
    {"author": "Рэй Брэдбери", "title": "451 градус по Фаренгейту", "genre": "Научная фантастика", "pages": 158},
    {"author": "Федор Достоевский", "title": "Преступление и наказание", "genre": "Роман", "pages": 671},
    {"author": "Стивен Кинг", "title": "11/22/63", "genre": "Роман", "pages": 700},
    {"author": "Михаил Булгаков", "title": "Мастер и Маргарита", "genre": "Фантастика", "pages": 480},
    {"author": "Энтони Берджесс", "title": "Заводной апельсин", "genre": "Роман", "pages": 480},
    {"author": "Габриэль Гарсиа Маркес", "title": "Сто лет одиночества", "genre": "Магический реализм", "pages": 448},
    {"author": "Лев Толстой", "title": "Война и мир", "genre": "Исторический роман", "pages": 1440},
    {"author": "Виктор Гюго", "title": "Отверженные", "genre": "Роман", "pages": 1900},
    {"author": "Джером Д. Сэлинджер", "title": "Над пропастью во ржи", "genre": "Роман", "pages": 277},
]

@app.route('/lab2/books')
def show_books():
    return render_template('books.html', books=books)

