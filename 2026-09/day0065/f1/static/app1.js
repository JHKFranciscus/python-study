const date = document.querySelector("#borrow-date") //DOM element
const category = document.querySelector("#category") //DOM element
const bookStatus = document.querySelector("#books-status") //DOM element
const statusReset = document.querySelector("#reset")

date.addEventListener("change", loadBooks)
category.addEventListener("change", loadBooks)
statusReset.addEventListener("click", () => {
    date.value = "";
    category.value = "";
    loadBooks();
})


function loadBooks() {
    let borrowDate = date.value; //string
    let selectedCategory = category.value; //string

    let queryParams = new URLSearchParams(); //Params 객체

    if (borrowDate) {
        queryParams.append("borrow_date", borrowDate)
    }

    if (selectedCategory) {
        queryParams.append("category", selectedCategory)
    }

    let url = "/books"; //string

    const queryString = queryParams.toString(); //stirng

    url = url + `?${queryString}` //stirng

    fetch(url)
        .then(response => {
            console.log(response.ok);
            return response.json();
        })
        .then(data => {
            books_list = data.books //Array

            bookStatus.innerHTML = ""

            for (book of books_list) {
                bookStatus.innerHTML += `
                <tr>
                <td>${book.borrow_date}</td>
                <td>${book.category}</td>
                <td>${book.title}</td>
                <td>${book.borrower}</td>
                </tr>`
            }
        })
}

loadBooks();






