function fillFilmList() {
    fetch('/lab7/rest-api/films')
    .then(function (data) {
        return data.json();
    })
    .then(function(films) {
        let tbody = document.getElementById('film-list');
        tbody.innerHTML = ''; // Очищаем таблицу перед заполнением

        for(let i = 0; i < films.length; i++) {
            let tr = document.createElement('tr'); // Создаем строку

            // Создаем ячейки
            let tdTitle = document.createElement('td');
            let tdTitleRus = document.createElement('td');
            let tdYear = document.createElement('td');
            let tdActions = document.createElement('td');

            // Заполняем ячейки данными
            tdTitle.innerText = films[i].title == films[i].title_ru ? '' : films[i].title;
            tdTitleRus.innerText = films[i].title_ru;
            tdYear.innerText = films[i].year;

            // Создаем кнопки
            let editButton = document.createElement('button');
            editButton.innerText = 'редактировать';
            editButton.addEventListener('click', function() {
                editFilm(films[i].id); // Передаем ID фильма
            });

            let delButton = document.createElement('button');
            delButton.innerText = 'удалить';
            delButton.onclick = function() {
                deleteFilm(films[i].id, films[i].title_ru); // Передаем ID и название фильма
            };

            // Добавляем кнопки в ячейку действий
            tdActions.append(editButton);
            tdActions.append(delButton);

            // Добавляем ячейки в строку
            tr.append(tdTitle);
            tr.append(tdTitleRus);
            tr.append(tdYear);
            tr.append(tdActions);

            // Добавляем строку в таблицу
            tbody.append(tr);
        }
    })
    .catch(function(error) {
        console.error('Ошибка при загрузке фильмов:', error);
    });
}

// Функция для редактирования фильма
function editFilm(id) {
    // Получаем данные о фильме по его ID
    fetch(`/lab7/rest-api/films/${id}`)
        .then(function(response) {
            if (!response.ok) {
                throw new Error('Ошибка при получении данных о фильме');
            }
            return response.json();
        })
        .then(function(film) {
            // Заполняем форму данными фильма
            document.getElementById('id').value = id;
            document.getElementById('title').value = film.title;
            document.getElementById('title-ru').value = film.title_ru;
            document.getElementById('year').value = film.year;
            document.getElementById('description').value = film.description;
            showModal(); // Открываем модальное окно
        })
        .catch(function(error) {
            console.error('Ошибка при выполнении запроса:', error);
        });
}

// Функция для удаления фильма
function deleteFilm(id, title) {
    // Подтверждение удаления
    if (!confirm(`Вы точно хотите удалить фильм "${title}"?`)) {
        return;
    }

    // Отправляем DELETE-запрос на сервер
    fetch(`/lab7/rest-api/films/${id}`, { method: 'DELETE' })
        .then(function(response) {
            if (response.ok) {
                fillFilmList(); // Обновляем список фильмов после удаления
            } else {
                console.error('Ошибка при удалении фильма');
            }
        })
        .catch(function(error) {
            console.error('Ошибка при выполнении запроса:', error);
        });
}

// Функция для добавления/редактирования фильма
function sendFilm() {
    const id = document.getElementById('id').value;
    const film = {
        title: document.getElementById('title').value,
        title_ru: document.getElementById('title-ru').value,
        year: document.getElementById('year').value,
        description: document.getElementById('description').value,
    };

    const url = id ? `/lab7/rest-api/films/${id}` : '/lab7/rest-api/films/';
    const method = id ? 'PUT' : 'POST';

    fetch(url, {
        method: method,
        headers: { "Content-Type": "application/json" }, // Исправлена опечатка
        body: JSON.stringify(film)
    })
    .then(function(response) {
        if (response.ok) {
            fillFilmList(); // Обновляем список фильмов
            hideModal(); // Закрываем модальное окно
        } else {
            console.error('Ошибка при сохранении фильма');
        }
    })
    .catch(function(error) {
        console.error('Ошибка при выполнении запроса:', error);
    });
}

// Функции для работы с модальным окном
function showModal() {
    document.querySelector('div.modal').style.display = 'block';
}

function hideModal() {
    document.querySelector('div.modal').style.display = 'none';
}

function cancel() {
    hideModal();
}

function addFilm() {
    document.getElementById('id').value = '';
    document.getElementById('title').value = '';
    document.getElementById('title-ru').value = '';
    document.getElementById('year').value = '';
    document.getElementById('description').value = '';
    showModal();
}