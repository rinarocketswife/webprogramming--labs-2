from flask import Blueprint, render_template, request, jsonify

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')

films = [
    {
        "title": "Prometheus",
        "title_ru": "Прометей",
        "year": 2024,
        "description": "Бывший сотрудник спецслужб Шапошников занимается расследованием дела об исчезновении в 1998 году пассажирского самолета. Прошлое находит отголоски в настоящем, когда своей семье дозванивается один из пассажиров пропавшего рейса. К делу подключают журналистку Анну, привыкшую замечать детали, которые упускают другие."
    },
    {
        "title": "Hands up!",
        "title_ru": "Руки Вверх! ",
        "year": 2024,
        "description": "Из провинциального мальчишки, мечтающего впечатлить девушку робкими песнями о любви, Сергей Жуков становится одним из самых востребованных артистов страны и голосом целого поколения."
    },
    {
        "title": "The last hero. Heritage",
        "title_ru": "Последний богатырь. Наследие",
        "year": 2024,
        "description": "У Ивана, которому как раз исполнилось 50, две дочери: старшая, богатырка Марья, и младшая, начинающая колдунья Софья. Все в Белогорье идет своим чередом, но визит колдуна Северина, которому привиделось страшное бедствие, вносит смуту в размеренную жизнь волшебников. Чтобы спасти и Белогорье, и жизнь собственного отца, Софье придется отправиться в Москву прошлого, где все еще живет молодой и ни о чем не подозревающий Иван, а Марье — сразиться со злом в самом городе."
    },
    {
        "title": "Cat",
        "title_ru": "Кошка",
        "year": 2023,
        "description": "В городе один за другим пропадают дети. Родители в отчаянии, полиция уверена, что те вернутся сами, волонтеров на всех не хватает. Что если детей похищают с определенной целью? За дело берется Оксана Кошкина по прозвищу Кошка, совсем недавно вернувшаяся в полицию. Похоже, пропавшие дети — часть большой схемы, в которой задействовано множество сторон. Чем глубже Оксана погружается в дело, тем больше осознает масштаб катастрофы. И тем острее ее ранят собственные воспоминания из прошлого."
    },
    {
        "title": "Call",
        "title_ru": "Вызов",
        "year": 2023,
        "description": "Торакальный хирург Женя Беляева за месяц должна подготовиться к космическому полету, чтобы отправиться на МКС и спасти заболевшего космонавта. Ей придётся преодолеть неуверенность и страхи, а также провести сложнейшую операцию в условиях невесомости, от которой зависят шансы космонавта вернуться на Землю живым."
    },
]

@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return jsonify(films)

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if id < 0 or id >= len(films):
        return jsonify({"error": "Film not found"}), 404
    return jsonify(films[id])

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if id < 0 or id >= len(films):
        return jsonify({"error": "Film not found"}), 404
    del films[id]
    return '', 204

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    if id < 0 or id >= len(films):
        return jsonify({"error": "Film not found"}), 404
    film = request.get_json()

    # Если оригинальное название пустое, заполняем его русским названием
    if not film.get('title'):
        film['title'] = film['title_ru']

    # Проверка на пустое описание
    if not film.get('description'):
        return jsonify({"error": "Description cannot be empty"}), 400

    films[id] = film
    return jsonify(films[id])

@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    new_film = request.get_json()

    # Если оригинальное название пустое, заполняем его русским названием
    if not new_film.get('title'):
        new_film['title'] = new_film['title_ru']

    films.append(new_film)
    new_film_id = len(films) - 1
    return jsonify({"message": "Film added", "id": new_film_id}), 201