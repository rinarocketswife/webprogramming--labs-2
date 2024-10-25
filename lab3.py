from flask import Blueprint, render_template, request, make_response, redirect
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    age = request.cookies.get('age')

    if name is None:
        name = 'аноним'
    if age is None:
        age = 'неизвестный'

    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name=name, age=age, name_color=name_color)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
   
    age = request.args.get('age')
    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    #Пусть кофе стоит 120 рублей, черный чай - 80 рублей, зеленый - 70 рублей
    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    #Добавка молока удорожает напиток на 30 рублей, а сахар - на 10
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('lab3/pay.html', price=price)


@lab3.route('/lab3/success')
def success():
    price = 1000  # Пример суммы к оплате
    return render_template('pay.html', price=price)


@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    if color:
        resp = make_response(redirect('/lab3/settings'))
        resp.set_cookie('color', color)
        return resp
    
    color = request.cookies.get('color')

    background_color = request.args.get('background_color')
    if background_color:
        resp = make_response(redirect('/lab3/settings'))
        resp.set_cookie('background_color', background_color)
        return resp
    
    background_color = request.cookies.get('background_color')

    font_size = request.args.get('font_size')
    if font_size:
        resp = make_response(redirect('/lab3/settings'))
        resp.set_cookie('font_size', font_size)
        return resp
    
    font_size = request.cookies.get('font_size')
    resp = make_response(render_template('/lab3/settings.html', color=color, background_color=background_color, font_size=font_size))
    return resp


@lab3.route('/lab3/clear_cookies')
def clear_cookies():
    resp = make_response(redirect('/lab3/settings'))
    resp.delete_cookie('color')
    resp.delete_cookie('background_color')
    resp.delete_cookie('font_size')
    return resp

@lab3.route('/lab3/ticket')
def ticket():
    if ticket:
        fio = request.form.get('fio')
        age = int(request.form.get('age'))
        bunk = request.form.get('bunk')
        bedding = 'bedding' in request.form
        baggage = 'baggage' in request.form
        departure = request.form.get('departure')
        destination = request.form.get('destination')
        date = request.form.get('date')
        insurance = 'insurance' in request.form
        errors = {}
        if not fio:
            errors['fio'] = 'Заполните поле!'
        if age < 1 or age > 120:
            errors['age'] = 'Возраст должен быть от 1 до 120 лет!'
        if not departure:
            errors['departure'] = 'Заполните поле!'
        if not destination:
            errors['destination'] = 'Заполните поле!'
        if not date:
            errors['date'] = 'Заполните поле!'
        if errors:
            return render_template('lab3/ticket_form.html', errors=errors)
        base_price = 700 if age < 18 else 1000
        if bunk in ['lower', 'lower_side']:
            base_price += 100
        if bedding:
            base_price += 75
        if baggage:
            base_price += 250
        if insurance:
            base_price += 150
        return render_template('lab3/ticket.html', fio=fio, age=age, bunk=bunk, bedding=bedding, baggage=baggage, departure=departure, destination=destination, date=date, insurance=insurance, price=base_price)
    return render_template('lab3/ticket_form.html', errors={})