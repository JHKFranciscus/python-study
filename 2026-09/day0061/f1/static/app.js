function loadMovies() {
    fetch("/api/movies")
        .then(response => response.json())
        .then(data => {
            const movie_list = document.querySelector("#movie-list");

            movie_list.innerHTML = '';

            data.movies.forEach(movie => {
                movie_list.innerHTML += `<li>
                ${movie.title}
                <button type="button" class="delete-movie" data-movie-id=${movie._id}>삭제</button>
                <button type="button" class="update-movie" data-movie-id="${movie._id}" data-movie-title="${movie.title}">수정</button>
                </li>`;
            });
            const updateButton = document.querySelectorAll(".update-movie");

            updateButton.forEach(button => {
                button.addEventListener("click", () => {
                    const newTitle = prompt(
                        "새 제목을 입력하세요",
                        button.dataset.movieTitle
                    );
                    if (newTitle !== null) {
                        updateMovie(button.dataset.movieId, newTitle)
                    }
                })
            })


            const deleteButton = document.querySelectorAll(".delete-movie");

            deleteButton.forEach(button => {
                button.addEventListener("click", () => {
                    deleteMovie(button.dataset.movieId)
                });
            });
        });
}

loadMovies();

function addMovie() {
    const movieTitle = document.querySelector("#movie-title").value;

    fetch("/api/movies", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "title": movieTitle
        })
    }).then(response => response.json())
        .then(data => { loadMovies(); })
}

const addButton = document.querySelector("#add-movie")

addButton.addEventListener("click", addMovie)

function deleteMovie(movie_id) {
    fetch(`/api/movies/${movie_id}`, {
        method: 'DELETE'
    })
        .then(response => response.json())
        .then(data => {
            loadMovies();
        })
}

function updateMovie(movie_id, newTitle) {
    fetch(`/api/movies/${movie_id}`, {
        method: "PATCH",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            title: newTitle
        })
    })
        .then(response => response.json())
        .then(data => {
            loadMovies();
        })
}