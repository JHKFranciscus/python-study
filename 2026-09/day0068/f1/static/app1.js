const newTitleInput = document.querySelector("#new_title");
const newCategoryInput = document.querySelector("#new_category");
const newReadDateInput = document.querySelector("#new_read_date");
const newPagesInput = document.querySelector("#new_pages");

function addBook() {
    const new_title = newTitleInput.value;
    const new_category = newCategoryInput.value;
    const new_read_date = newReadDateInput.value;
    const new_pages = newPagesInput.value;

    fetch("/books", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(
            {
                "new_title": new_title,
                "new_category": new_category,
                "new_read_date": new_read_date,
                "new_pages": new_pages
            })
    })
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(error => {
                        throw new Error(error.result);
                    });
            }

            return response.json();
        })
        .then(data => {
            loadBooks();
        })
        .catch(error => {
            console.log(error.message);
        });
}

const addButton = document.querySelector("#add-button")
addButton.addEventListener("click", addBook)


const categorySelect = document.querySelector("#category")
const startDateSelect = document.querySelector("#start_date")
const endDateSelect = document.querySelector("#end_date")
const sortSelect = document.querySelector("#sort")

categorySelect.addEventListener("change", loadBooks)
startDateSelect.addEventListener("change", loadBooks)
endDateSelect.addEventListener("change", loadBooks)
sortSelect.addEventListener("change", loadBooks)

function loadBooks() {
    const category = categorySelect.value;
    const start_date = startDateSelect.value;
    const end_date = endDateSelect.value;
    const sort = sortSelect.value;

    let queryParams = new URLSearchParams();

    if (category) {
        queryParams.append("category", category);
    }

    if (start_date) {
        queryParams.append("start_date", start_date)
    }

    if (end_date) {
        queryParams.append("end_date", end_date)
    }

    if (sort) {
        queryParams.append("sort", sort)
    }

    const queryString = queryParams.toString();

    let url = "/books"

    if (queryString) {
        url = url + "?" + queryString
    }

    fetch(url)
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(error => {
                        throw new Error(error.result)
                    })
            }

            return response.json()
        })
        .then(data => {
            const books = data.books_list;
            const booksList = document.querySelector("#books-list")

            booksList.innerHTML = ""

            books.forEach(book => {
                const div = document.createElement("div")

                const h2 = document.createElement("h2")
                const li1 = document.createElement("li")
                const li2 = document.createElement("li")

                const updateButton = document.createElement("button")
                const deleteButton = document.createElement("button")


                h2.textContent = `${book.title}`
                li1.textContent = `${book.category}`
                li2.textContent = `읽은 날짜${book.read_date}, 읽은 페이지 수${book.pages}`


                updateButton.textContent = "변경"
                deleteButton.textContent = "삭제"


                updateButton.addEventListener("click", () => {
                    updateBook(`${book._id}`)
                })
                deleteButton.addEventListener("click", () => {
                    deleteBook(`${book._id}`)
                })

                div.appendChild(h2)
                div.appendChild(li1)
                div.appendChild(li2)
                div.appendChild(updateButton)
                div.appendChild(deleteButton)

                booksList.appendChild(div)
            })
        })
        .catch(error => {
            console.log(error.message);
        });
}

loadBooks();

function updateBook(book_id) {
    const update_title = document.querySelector("#update_title").value;
    const update_category = document.querySelector("#update_category").value;
    const update_read_date = document.querySelector("#update_read_date").value;
    const update_pages = document.querySelector("#update_pages").value;

    const updateData = {};

    if (update_title !== "") {
        updateData["update_title"] = update_title;
    }

    if (update_category !== "") {
        updateData["update_category"] = update_category;
    }

    if (update_read_date !== "") {
        updateData["update_read_date"] = update_read_date;
    }

    if (update_pages !== "") {
        updateData["update_pages"] = Number(update_pages);
    }

    fetch(`/books/${book_id}`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "update_data": updateData
        })
    })
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(error => {
                        throw new Error(error.error);
                    });
            }

            return response.json();
        })
        .then(data => {
            loadBooks();
        })
        .catch(error => {
            console.log(error.message);
        });
}

function deleteBook(book_id) {
    fetch(`/books/${book_id}`, {
        method: "DELETE",
    })
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(error => {
                        throw new Error(error.result);
                    });
            }

            return response.json();
        })
        .then(data => {
            loadBooks();
        })
        .catch(error => {
            console.log(error.message);
        });
}
