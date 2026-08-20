const showButton = document.querySelector("#showButton");
const nameElements = document.querySelectorAll(".productName");

const productsJson =
    '[{"name":"마우스","price":18000},{"name":"키보드","price":35000}]';

function showProducts() {
    const products = JSON.parse(productsJson);

    for (let i = 0; i < products.length; i++) {
        nameElements[i].textContent = products[i].name;
    }
}

showButton.addEventListener("click", showProducts);
