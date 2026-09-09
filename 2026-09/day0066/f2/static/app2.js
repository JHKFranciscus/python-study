function loadRecord() {
    fetch("/record")
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(error => {
                        return error.message
                    })
            }

            return response.json()
        })
        .then(data => {
            const recordsList = data.records

            const statusList = document.querySelector("#status-list")
            const updateButton = document.createElement(button)
            const deleteButton = document.createElement(button)

            for (const record of recordsList) {
                statusList.innerHTML += `
                <li>${record.title}</li>
                <li>${record.department}</li>
                <li>${record.status}</li>`
            }

            updateButton.textContent("변경")
            updateButton.addEventListener("click", () => {
                updateRecord($record._id)
            })

            deleteButton.textContent("삭제")

            statusList.appendChild(updateButton)
            statusList.appendChild(deleteButton)
        })
}

function updateRecord() {}