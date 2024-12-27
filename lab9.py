from flask import Blueprint, redirect, url_for, render_template, request, session

lab9 = Blueprint('lab9', __name__)

# Начальная страница: ввод имени
@lab9.route('/lab9/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['name'] = request.form.get('name')  # Сохраняем имя в сессии
        return redirect(url_for('age'))
    
    # Проверяем, есть ли данные в сессии
    if all(key in session for key in ['name', 'age', 'gender', 'preference1', 'preference2']):
        # Если данные есть, отображаем их
        name = session['name']
        age = session['age']
        gender = session['gender']
        preference1 = session['preference1']
        preference2 = session['preference2']
        return render_template('lab9/index.html', name=name, age=age, gender=gender, preference1=preference1, preference2=preference2)
    
    # Если данных нет, отображаем пустую форму
    return render_template('lab9/index.html')

# Вторая страница: ввод возраста
@lab9.route('/lab9/age', methods=['GET', 'POST'])
def age():
    if request.method == 'POST':
        session['age'] = request.form.get('age')  # Сохраняем возраст в сессии
        return redirect(url_for('gender'))
    return render_template('lab9/age.html')

# Третья страница: выбор пола
@lab9.route('/lab9/gender', methods=['GET', 'POST'])
def gender():
    if request.method == 'POST':
        session['gender'] = request.form.get('gender')  # Сохраняем пол в сессии
        return redirect(url_for('preference1'))
    return render_template('lab9/gender.html')

# Четвертая страница: первый вопрос (вкусное/красивое)
@lab9.route('/lab9/preference1', methods=['GET', 'POST'])
def preference1():
    if request.method == 'POST':
        session['preference1'] = request.form.get('preference1')  # Сохраняем первый выбор
        return redirect(url_for('preference2'))
    return render_template('lab9/preference1.html')

# Пятая страница: второй вопрос (сладкое/сытное)
@lab9.route('/lab9/preference2', methods=['GET', 'POST'])
def preference2():
    if request.method == 'POST':
        session['preference2'] = request.form.get('preference2')  # Сохраняем второй выбор
        return redirect(url_for('result'))
    return render_template('lab9/preference2.html')

# Финальная страница: поздравление и картинка
@lab9.route('/lab9/result')
def result():
    # Проверяем, есть ли данные в сессии
    if not all(key in session for key in ['name', 'age', 'gender', 'preference1', 'preference2']):
        return redirect(url_for('index'))  # Если данных нет, возвращаем на начальную страницу

    # Получаем данные из сессии
    name = session['name']
    age = session['age']
    gender = session['gender']
    preference1 = session['preference1']
    preference2 = session['preference2']

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

# Сброс данных и возврат на начальную страницу
@lab9.route('/lab9/reset')
def reset():
    session.clear()  # Очищаем сессию
    return redirect(url_for('index'))  # Возвращаем на начальную страницу

if __name__ == '__main__':
    lab9.run(debug=True)