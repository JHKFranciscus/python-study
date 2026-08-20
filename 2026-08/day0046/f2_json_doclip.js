const booksJson =
    '[{"title":"파이썬 입문","price":18000},{"title":"자바스크립트 기초","price":25000},{"title":"컴퓨터 구조","price":20000}]';

const button = document.querySelector("#button");

const booktitle = document.querySelectorAll(".title");
const bookprice = document.querySelectorAll(".price");

const under20000 = document.querySelector("#under20000")


function changeTitlePrice() {
    const books = JSON.parse(booksJson);

    for (let i = 0; i < books.length; i++) {
        booktitle[i].textContent = `제목: ${books[i].title}`;
        bookprice[i].textContent = `가격: ${books[i].price}`;
    }
}

function undercount() {
    const books = JSON.parse(booksJson);
    let count = 0;

    for (let i = 0; i < books.length; i++) {
        if (books[i].price <= 20000) {
            count += 1;
        }
    }
    return count;
}

function changeUnder20000() {
    const count20000 = undercount();

    under20000.textContent = `20,000원 이하 도서: ${count20000}`;
}

button.addEventListener("click", changeTitlePrice);
button.addEventListener("click", changeUnder20000);