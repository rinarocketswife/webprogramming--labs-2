function fillFilmList() {
    fetch('/lab7/rest-api/films')
    .then(function (data) {
        return data.json();
    })
    .then(function(films) {
        let tbody = document.getElementById('film-list');
        tbody.innerHTML = ''; 

        for(let i = 0; i < films.length; i++) {
            let tr = document.createElement('tr'); 

            
            let tdTitleRus = document.createElement('td');
            let tdTitle = document.createElement('td');
            let tdYear = document.createElement('td');
            let tdActions = document.createElement('td');

            tdTitleRus.innerText = films[i].title_ru; 
            tdTitle.innerHTML = `<i>(${films[i].title})</i>`; 
            tdYear.innerText = films[i].year;

      
            let editButton = document.createElement('button');
            editButton.innerText = 'редактировать';
            editButton.addEventListener('click', function() {
                editFilm(films[i].id); 
            });

            let delButton = document.createElement('button');
            delButton.innerText = 'удалить';
            delButton.onclick = function() {
                deleteFilm(films[i].id, films[i].title_ru); 
            };

     
            tdActions.append(editButton);
            tdActions.append(delButton);

         
            tr.append(tdTitleRus);
            tr.append(tdTitle);
            tr.append(tdYear);
            tr.append(tdActions);

     
            tbody.append(tr);
        }
    })
    .catch(function(error) {
        console.error('Ошибка при загрузке фильмов:', error);
    });
}


function editFilm(id) {
  
    fetch(`/lab7/rest-api/films/${id}`)
        .then(function(response) {
            if (!response.ok) {
                throw new Error('Ошибка при получении данных о фильме');
            }
            return response.json();
        })
        .then(function(film) {
       
            document.getElementById('id').value = film.id;
            document.getElementById('title').value = film.title;
            document.getElementById('title-ru').value = film.title_ru;
            document.getElementById('year').value = film.year;
            document.getElementById('description').value = film.description;
            showModal(); 
        })
        .catch(function(error) {
            console.error('Ошибка при выполнении запроса:', error);
        });
}


function deleteFilm(id, title) {

    if (!confirm(`Вы точно хотите удалить фильм "${title}"?`)) {
        return;
    }

    fetch(`/lab7/rest-api/films/${id}`, { method: 'DELETE' })
        .then(function(response) {
            if (response.ok) {
                fillFilmList(); 
            } else {
                console.error('Ошибка при удалении фильма');
            }
        })
        .catch(function(error) {
            console.error('Ошибка при выполнении запроса:', error);
        });
}

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
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(film)
    })
    .then(function(response) {
        if (response.ok) {
            fillFilmList(); 
            hideModal(); 
        } else {
            console.error('Ошибка при сохранении фильма');
        }
    })
    .catch(function(error) {
        console.error('Ошибка при выполнении запроса:', error);
    });
}

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