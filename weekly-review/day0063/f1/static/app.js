"use strict";

function addItem() {
    const newItemName = document.querySelector("#item-name");
    const newStockQuantity = document.querySelector("#stock-quantity");

    fetch("/item", {
        method: "POST",
        headers: {
            "Content-Type": 'application/json'
        },
        body: JSON.stringify({
            "name": newItemName.value,
            "quantity": newStockQuantity.value
        })
    })
        .then(response => response.json())
        .then(data => {
            loadItems();
        })
};

function loadItems() {
    fetch("/item")
        .then(response => response.json())
        .then(data => {
            const itemsStatus = document.querySelector("#items-status")

            const items = data.items;

            itemsStatus.innerHTML = ""

            items.forEach(item => {
                itemsStatus.innerHTML += `
                <tr>
                <td>${item.name}
                <td>${item.quantity}
                <td>
                <button type="button" class="update-button" data-id="${item._id}" data-quantity="${item.quantity}">재고 변경</button>
                </td>
                <td>
                <button type="button" class="delete-button" data-id="${item._id}">상품 삭제</button>
                </td>
                </tr>`
            });

            const updateButtons = document.querySelectorAll(".update-button")
            updateButtons.forEach(button => {
                button.addEventListener("click", () => {
                    updateItems(button.dataset.id, button.dataset.quantity)
                });
            });

            const deleteButtons = document.querySelectorAll(".delete-button")
            deleteButtons.forEach(button => {
                button.addEventListener("click", () => {
                    deleteItems(button.dataset.id)
                });
            });
        });
}

loadItems();

function updateItems(item_id, stock_quantity) {
    const new_stock_quantity = prompt("변경 값", Number(stock_quantity));

    fetch(`/item/${item_id}`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "quantity": new_stock_quantity
        })
    })
        .then(response => response.json())
        .then(data => {
            loadItems();
        })
}


function deleteItems(item_id) {
    fetch(`/item/${item_id}`, {
        method: "DELETE"
    })
        .then(response => response.json())
        .then(data => {
            loadItems();
        })
}