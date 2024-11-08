from flask import Blueprint, render_template, request, redirect, session

lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')

@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')

@lab4.route('/lab4/div', methods=['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены!')
    
    x1 = int(x1)
    x2 = int(x2)
    
    if x2 == 0:
        return render_template('lab4/div.html', error='На ноль делить нельзя!')
    
    result = x1 / x2
    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/sum-form')
def sum_form():
    return render_template('lab4/sum-form.html')

@lab4.route('/lab4/sum', methods=['POST'])
def sum():
    x1 = request.form.get('x1', '')
    x2 = request.form.get('x2', '')
    
    if x1 == '':
        x1 = 0
    else:
        x1 = int(x1)
    
    if x2 == '':
        x2 = 0
    else:
        x2 = int(x2)
    
    result = x1 + x2
    return render_template('lab4/sum.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/um-form')
def um_form():
    return render_template('lab4/um-form.html')

@lab4.route('/lab4/um', methods=['POST'])
def um():
    x1 = request.form.get('x1', '')
    x2 = request.form.get('x2', '')
    
    if x1 == '':
        x1 = 1
    else:
        x1 = int(x1)
    
    if x2 == '':
        x2 = 1
    else:
        x2 = int(x2)
    
    result = x1 * x2
    return render_template('lab4/um.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/sub-form')
def sub_form():
    return render_template('lab4/sub-form.html')

@lab4.route('/lab4/sub', methods=['POST'])
def sub():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    
    if x1 == '' or x2 == '':
        return render_template('lab4/sub.html', error='Оба поля должны быть заполнены!')
    
    x1 = int(x1)
    x2 = int(x2)
    result = x1 - x2
    return render_template('lab4/sub.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/st-form')
def st_form():
    return render_template('lab4/st-form.html')

@lab4.route('/lab4/st', methods=['POST'])
def st():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    
    if x1 == '' or x2 == '':
        return render_template('lab4/st.html', error='Оба поля должны быть заполнены!')
    
    x1 = int(x1)
    x2 = int(x2)
    
    if x1 == 0 or x2 == 0:
        return render_template('lab4/st.html', error='Ноль указывать нельзя!')
    
    result = x1 ** x2
    return render_template('lab4/st.html', x1=x1, x2=x2, result=result)

tree_count=0

@lab4.route('/lab4/tree', methods = ['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)
    
    operation = request.form.get('operation')

    if operation == 'cut':
        if tree_count > 0:
            tree_count -= 1
    elif operation == 'plant':
        tree_count += 1

    return redirect('/lab4/tree')

users = [
    {'login': 'alex', 'password': '123', 'name': 'Alex', 'sex': 'male'},
    {'login': 'bob', 'password': '555', 'name': 'Bob', 'sex': 'male'},
    {'login': 'fred', 'password': '111', 'name': 'Fred', 'sex': 'male'},
    {'login': 'rick', 'password': '222', 'name': 'Rick', 'sex': 'male'},
]

@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            authorized = True
            login = session['login']
            name = session['name']
        else:
            authorized = False
            login = ''
            name = ''
        return render_template('lab4/login.html', authorized=authorized, login=login, name=name)
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not login:
        error = 'Не введён логин'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)
    
    if not password:
        error = 'Не введён пароль'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)

    for user in users:
        if login == user['login'] and password == user['password']:
            session['login'] = login
            session['name'] = user['name']
            return redirect('lab4/login')
    
    error = 'Неверный логин и/или пароль'
    return render_template('lab4/login.html', error=error, authorized=False, login=login)

@lab4.route('/lab4/logout', methods=['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')

@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    if request.method == 'POST':
        temperature = request.form.get('temperature')

        if not temperature:
            error = 'Ошибка: не задана температура'
            return render_template('lab4/fridge.html', error=error)

        temperature = float(temperature)

        if temperature < -12:
            error = 'Не удалось установить температуру — слишком низкое значение'
            return render_template('lab4/fridge.html', error=error)

        if temperature > -1:
            error = 'Не удалось установить температуру — слишком высокое значение'
            return render_template('lab4/fridge.html', error=error)

        if -12 <= temperature <= -9:
            message = f'Установлена температура: {temperature}°С'
            snowflakes = '❄️❄️❄️'
        elif -8 <= temperature <= -5:
            message = f'Установлена температура: {temperature}°С'
            snowflakes = '❄️❄️'
        elif -4 <= temperature <= -1:
            message = f'Установлена температура: {temperature}°С'
            snowflakes = '❄️'

        return render_template('lab4/fridge.html', message=message, snowflakes=snowflakes)

    return render_template('lab4/fridge.html')

@lab4.route('/lab4/grain', methods=['GET', 'POST'])
def grain():
    if request.method == 'POST':
        grain_type = request.form.get('grain_type')
        weight = request.form.get('weight')

        if not weight:
            error = 'Ошибка: не указан вес'
            return render_template('lab4/grain.html', error=error)

        weight = float(weight)

        if weight <= 0:
            error = 'Ошибка: вес должен быть больше 0'
            return render_template('lab4/grain.html', error=error)

        if weight > 500:
            error = 'Ошибка: такого объёма сейчас нет в наличии'
            return render_template('lab4/grain.html', error=error)

        prices = {
            'ячмень': 12345,
            'овёс': 8522,
            'пшеница': 8722,
            'рожь': 14111
        }

        if grain_type not in prices:
            error = 'Ошибка: неверный тип зерна'
            return render_template('lab4/grain.html', error=error)

        price_per_ton = prices[grain_type]
        total_cost = price_per_ton * weight

        if weight > 50:
            discount = total_cost * 0.1
            total_cost -= discount
            discount_message = f'Применена скидка за большой объём: {discount} руб'
        else:
            discount_message = ''

        message = f'Заказ успешно сформирован. Вы заказали {grain_type}. Вес: {weight} т. Сумма к оплате: {total_cost} руб'
        return render_template('lab4/grain.html', message=message, discount_message=discount_message)

    return render_template('lab4/grain.html')

@lab4.route('/lab4/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        name = request.form.get('name')
        gender = request.form.get('gender')

        if not login or not password or not name or not gender:
            error = 'Ошибка: все поля должны быть заполнены'
            return render_template('lab4/register.html', error=error)

        for user in users:
            if login == user['login']:
                error = 'Ошибка: логин уже занят'
                return render_template('lab4/register.html', error=error)

        users.append({'login': login, 'password': password, 'name': name, 'gender': gender})
        return redirect('/lab4/login')

    return render_template('lab4/register.html')

@lab4.route('/lab4/users')
def users_list():
    if 'login' not in session:
        return redirect('/lab4/login')

    return render_template('lab4/users.html', users=users)

@lab4.route('/lab4/delete_user', methods=['POST'])
def delete_user():
    if 'login' not in session:
        return redirect('/lab4/login')

    login = session['login']
    users[:] = [user for user in users if user['login'] != login]
    session.pop('login', None)
    session.pop('name', None)
    return redirect('/lab4/login')

@lab4.route('/lab4/edit_user', methods=['GET', 'POST'])
def edit_user():
    if 'login' not in session:
        return redirect('/lab4/login')

    login = session['login']
    user = next((user for user in users if user['login'] == login), None)

    if request.method == 'POST':
        new_password = request.form.get('new_password')
        new_name = request.form.get('new_name')
        new_gender = request.form.get('new_gender')

        if new_password:
            user['password'] = new_password
        if new_name:
            user['name'] = new_name
        if new_gender:
            user['gender'] = new_gender

        return redirect('/lab4/users')

    return render_template('lab4/edit_user.html', user=user)
