const selecteddepartment = document.querySelector("#department");
const selectedstatus = document.querySelector("#status");

selecteddepartment.addEventListener("change", () => {
    loadRecord();
})
selectedstatus.addEventListener("change", () => {
    loadRecord();
})

function loadRecord() {
    chosenDepartment = selecteddepartment.value;
    chosenStatus = selectedstatus.value;

    let queryParams = new URLSearchParams();

    if (chosenDepartment) {
        queryParams.append("department", chosenDepartment);
    }

    if (chosenStatus) {
        queryParams.append("status", chosenStatus);
    }

    queryString = queryParams.toString();

    let url = `/record`
    if (queryString) {
        url += "?" + queryString;
    }

    fetch(url)
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(errorData => {
                        throw new Error(errorData.result);
                    })
            };

            return response.json()
        })
        .then(data => {
            const recordsList = data.records

            const statusList = document.querySelector("#status-list")
            statusList.innerHTML = ""


            for (const record of recordsList) {
                const items = document.createElement("li")

                const updateButton = document.createElement("button")
                const deleteButton = document.createElement("button")

                items.textContent = `${record.title}-${record.department}, ${record.status}`

                updateButton.textContent = "변경"
                updateButton.addEventListener("click", () => {
                    updateRecord(`${record._id}`)
                });

                deleteButton.textContent = "삭제"
                deleteButton.addEventListener("click", () => {
                    deleteRecord(`${record._id}`)
                });

                items.appendChild(updateButton)
                items.appendChild(deleteButton)

                statusList.appendChild(items)
            }
        })
        .catch(error => {
            console.log(error.message);
        });
}

loadRecord();

function deleteRecord(record_id) {
    fetch(`/record/${record_id}`, {
        method: "DELETE"
    })
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(errordata => {
                        throw new Error(errordata.result);
                    })
            }

            return response.json();
        })
        .then(data => {
            loadRecord();
        })
        .catch(error => {
            console.log(error)
        })
}

function updateRecord(record_id) {
    let newStatus = prompt("변경할 상태");

    fetch(`/record/${record_id}`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(
            { "status": newStatus }
        )
    })
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(errordata => {
                        throw new Error(errordata.result);
                    })
            }

            return response.json();
        })
        .then(data => {
            loadRecord();
        })
        .catch(error => {
            console.log(error)
        })
}


function resetStatus() {
    selecteddepartment.value = "";
    selectedstatus.value = "";

    loadRecord();
}

const resetButton = document.querySelector("#reset")
resetButton.addEventListener("click", () => {
    resetStatus();
})