from flask import Blueprint, render_template, request, redirect, url_for

lab9 = Blueprint('lab9', __name__)


# Начальная страница: ввод имени
@lab9.route('/lab9/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        return redirect(url_for('lab9.age', name=name))
    return render_template('lab9/index.html')

# Вторая страница: ввод возраста
@lab9.route('/lab9/age', methods=['GET', 'POST'])
def age():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        return redirect(url_for('lab9.gender', name=name, age=age))
    name = request.args.get('name')
    return render_template('lab9/age.html', name=name)

# Третья страница: выбор пола
@lab9.route('/lab9/gender', methods=['GET', 'POST'])
def gender():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        return redirect(url_for('lab9.preference1', name=name, age=age, gender=gender))
    name = request.args.get('name')
    age = request.args.get('age')
    return render_template('lab9/gender.html', name=name, age=age)

# Четвертая страница: первый вопрос (вкусное/красивое)
@lab9.route('/lab9/preference1', methods=['GET', 'POST'])
def preference1():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        preference1 = request.form.get('preference1')
        return redirect(url_for('lab9.preference2', name=name, age=age, gender=gender, preference1=preference1))
    name = request.args.get('name')
    age = request.args.get('age')
    gender = request.args.get('gender')
    return render_template('lab9/preference1.html', name=name, age=age, gender=gender)

# Пятая страница: второй вопрос (сладкое/сытное)
@lab9.route('/lab9/preference2', methods=['GET', 'POST'])
def preference2():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        preference1 = request.form.get('preference1')
        preference2 = request.form.get('preference2')
        return redirect(url_for('lab9.result', name=name, age=age, gender=gender, preference1=preference1, preference2=preference2))
    name = request.args.get('name')
    age = request.args.get('age')
    gender = request.args.get('gender')
    preference1 = request.args.get('preference1')
    return render_template('lab9/preference2.html', name=name, age=age, gender=gender, preference1=preference1)

# Финальная страница: поздравление и картинка
@lab9.route('/lab9/result')
def result():
    name = request.args.get('name')
    age = request.args.get('age')
    gender = request.args.get('gender')
    preference1 = request.args.get('preference1')
    preference2 = request.args.get('preference2')

    # Логика для выбора подарка и картинки
    if preference1 == 'tasty':
        if preference2 == 'sweet':
            gift = "мешочек конфет"
            image = "candy.jpg"
        else:
            gift = "пицца"
            image = "pizza.jpg"
    else:
        if preference2 == 'sweet':
            gift = "букет цветов"
            image = "flowers.jpg"
        else:
            gift = "книга"
            image = "book.jpg"

    # Формирование поздравления с учетом пола
    if gender == 'male':
        greeting = (
            f"Поздравляю тебя, {name}, с Новым Годом! 🎄\n"
            "Желаю, чтобы ты быстро вырос, был умным, здоровым и счастливым!\n"
            "Пусть в новом году исполнятся все твои мечты! 🎅"
        )
    else:
        greeting = (
            f"Поздравляю тебя, {name}, с Новым Годом! 🎄\n"
            "Желаю, чтобы ты быстро выросла, была умной, здоровой и счастливой!\n"
            "Пусть в новом году исполнятся все твои мечты! 🎅"
        )

    return render_template('lab9/result.html', greeting=greeting, gift=gift, image=image)