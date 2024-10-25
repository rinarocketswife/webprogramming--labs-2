from flask import Blueprint, redirect, url_for
lab2 = Blueprint('lab2', __name__)


# @lab2.route('/lab2/a')
# def a():
#       return 'без слэша'


# @lab2.route('/lab2/a/')
# def a():
#       return 'со слэшем'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']
@lab2.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.lab2end(name)
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


@lab2.route('/lab2/flowers')
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


@lab2.route('/lab2/flowers/<int:flower_id>')
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


@lab2.route('/lab2/clear_flowers')
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


@lab2.route('/lab2/example')
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


@lab2.route('/lab2/')
def lab():
     return render_template('lab2.html')


@lab2.route('/lab2/filters')
def filters():
     phrase = "0 <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
     return render_template('filter.html', phrase = phrase)


@lab2.route('/lab2/calc/<int:a>')
def redirect_to_default_with_a(a):
    return redirect(url_for('calculate', num1=a, num2=1))


@lab2.route('/lab2/calc/')
def redirect_to_default():
    return redirect(url_for('calculate', num1=1, num2=1))


@lab2.route('/lab2/calc/<int:num1>/<int:num2>')
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


@lab2.route('/lab2/books')
def show_books():
    return render_template('books.html', books=books)
objects = [
    {"name": "Яблоко", "image": "lab2le.jpg", "description": "Сладкий и сочный фрукт."},
    {"name": "Машина", "image": "car.jpg", "description": "Средство передвижения на колесах."},
    {"name": "Кошка", "image": "cat.jpg", "description": "Домашнее животное с мягкой шерстью."},
    {"name": "Стул", "image": "chair.jpg", "description": "Мебель для сидения с опорой для спины."},
    {"name": "Книга", "image": "book.jpg", "description": "Источник знаний и развлечений."},
]


@lab2.route('/lab2/objects')
def show_objects():
    return render_template('objects.html', objects=objects)
