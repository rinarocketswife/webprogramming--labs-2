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

            let tdTitle = document.createElement('td');
            let tdTitleRus = document.createElement('td');
            let tdYear = document.createElement('td');
            let tdActions = document.createElement('td');

         
            tdTitle.innerText = films[i].title == films[i].title_ru ? '' : films[i].title;
            tdTitleRus.innerText = films[i].title_ru;
            tdYear.innerText = films[i].year;

            let editButton = document.createElement('button');
            editButton.innerText = 'редактировать';
            editButton.addEventListener('click', function() {
                editFilm(i); 
            });

            let delButton = document.createElement('button');
            delButton.innerText = 'удалить';
            delButton.onclick = function() {
                deleteFilm(i, films[i].title_ru);
            };

            function deleteFilm(id, title) {
                if(! confirm('вы точно хотите удалить фильм "${title}"?'))
                    return;

                fetch('/lab7/rest-api/films/${id}', {method: 'DELETE'})
                    .then(function () {
                        fillFilmList();
                    })
            }

            tdActions.append(editButton);
            tdActions.append(delButton);

            tr.append(tdTitle);
            tr.append(tdTitleRus);
            tr.append(tdYear);
            tr.append(tdActions); 

            tbody.append(tr);
        }
    })
    .catch(function(error) {
        console.error('Ошибка при загрузке фильмов:', error);
    });
}

function editFilm(index) {
    console.log('Редактирование фильма с индексом:', index);
}

function deleteFilm(index) {
    console.log('Удаление фильма с индексом:', index);
}