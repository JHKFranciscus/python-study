const newCompany = document.querySelector("#new-company")
const newPosition = document.querySelector("#new-position")
const newDeadline = document.querySelector("#new-deadline")
const newStage = document.querySelector("#new-stage")
const newMemo = document.querySelector("#new-memo")

const addButton = document.querySelector("#add-button")
addButton.addEventListener("click", addItem)

function addItem() {
    const company = newCompany.value
    const position = newPosition.value
    const deadline = newDeadline.value
    const stage = newStage.value
    const memo = newMemo.value


    const newItem = {
        "company": company,
        "position": position,
        "deadline": deadline,
        "stage": stage,
        "memo": memo
    }
    fetch("/application", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(
            { "new_item": newItem }
        )
    })
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(errorData => {
                        throw new Error(errorData.error)
                    })
            }

            return response.json()
        })
        .then(data => {
            newCompany.value = ""
            newPosition.value = ""
            newDeadline.value = ""
            newStage.value = ""
            newMemo.value = ""
            loadItems()
        })
        .catch(error => {
            console.log(error.message)
        })
}

const stageSelector = document.querySelector("#stage")
const startDateSelector = document.querySelector("#start_date")
const endDateSelector = document.querySelector("#end_date")
const sortSelector = document.querySelector("#sort")

stageSelector.addEventListener("change", loadItems)
startDateSelector.addEventListener("change", loadItems)
endDateSelector.addEventListener("change", loadItems)
sortSelector.addEventListener("change", loadItems)

function loadItems() {
    const stage = stageSelector.value;
    const start_date = startDateSelector.value;
    const end_date = endDateSelector.value;
    const sort = sortSelector.value;

    const queryParams = new URLSearchParams();

    if (stage !== "") {
        queryParams.append("stage", stage)
    }

    if (start_date !== "") {
        queryParams.append("start_date", start_date)
    }

    if (end_date !== "") {
        queryParams.append("end_date", end_date)
    }

    if (sort !== "") {
        queryParams.append("sort", sort)
    }

    const queryString = queryParams.toString();

    let url = `/applications`

    if (queryString !== "") {
        url = url + "?" + queryString
    }

    fetch(url)
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(errorData => {
                        throw new Error(errorData.error)
                    })
            }

            return response.json()
        })
        .then(data => {
            itemsList = data.items_list;
            renderItems(data.items_list)
        })
        .catch(error => {
            console.log(error.message)
        })
}

loadItems();

function renderItems(items_list) {
    const itemsList = document.querySelector("#items-list")
    itemsList.innerHTML = ""

    for (const item of items_list) {
        const tr = document.createElement("tr")

        const td1 = document.createElement("td")
        const td11 = document.createElement("input")
        const td2 = document.createElement("td")
        const td22 = document.createElement("input")
        const td3 = document.createElement("td")
        const td33 = document.createElement("input")
        const td4 = document.createElement("td")
        const td44 = document.createElement("input")
        const td5 = document.createElement("td")
        const td55 = document.createElement("input")

        td11.value = item.company
        td22.value = item.position
        td33.value = item.deadline
        td44.value = item.stage
        td55.value = item.memo

        const tdUpButton = document.createElement("td")
        const updateButton = document.createElement("button")
        updateButton.textContent = "변경"
        updateButton.addEventListener("click", () => {
            updateItem(item._id, td11.value, td22.value, td33.value, td44.value, td55.value)
        })

        const tdDelButton = document.createElement("td")
        const deleteButton = document.createElement("button")
        deleteButton.textContent = "삭제"
        deleteButton.addEventListener("click", () => {
            deleteItem(item._id)
        })

        td1.appendChild(td11)
        td2.appendChild(td22)
        td3.appendChild(td33)
        td4.appendChild(td44)
        td5.appendChild(td55)

        tdUpButton.appendChild(updateButton)
        tdDelButton.appendChild(deleteButton)

        tr.appendChild(td1)
        tr.appendChild(td2)
        tr.appendChild(td3)
        tr.appendChild(td4)
        tr.appendChild(td5)

        tr.appendChild(tdUpButton)
        tr.appendChild(tdDelButton)

        itemsList.appendChild(tr)
    }
}

function updateItem(item_id, company, position, deadline, stage, memo) {
    const update_item = {}

    if (company) {
        update_item.company = company
    }

    if (position) {
        update_item.position = position
    }

    if (deadline) {
        update_item.deadline = deadline
    }

    if (stage) {
        update_item.stage = stage
    }

    update_item.memo = memo

    fetch(`/application/${item_id}`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ "update_item": update_item })
    })
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(errorData => {
                        throw new Error(errorData.error)
                    })
            }

            return response.json()
        })
        .then(data => {
            loadItems()
        })
        .catch(error => {
            console.log(error.message)
        })
}

function deleteItem(item_id) {
    fetch(`/application/${item_id}`, {
        method: "DELETE"
    })
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(errorData => {
                        throw new Error(errorData.error)
                    })
            }

            return response.json()
        })
        .then(data => {
            loadItems()
        })
        .catch(error => {
            console.log(error.message)
        })
}

const resetButton = document.querySelector("#reset")
resetButton.addEventListener("click", filterReset)

function filterReset() {
    startDateSelector.value = "";
    endDateSelector.value = "";
    sortSelector.value = "";
    loadItems();
}





