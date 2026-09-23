const newTitle = document.querySelector("#new-title")
const newLocation = document.querySelector("#new-location")
const newCategory = document.querySelector("#new-category")
const newPriority = document.querySelector("#new-priority")
const newReportDate = document.querySelector("#new-report_date")
const newMemo = document.querySelector("#new-memo")

const addButton = document.querySelector("#add-button")
addButton.addEventListener("click", addIssue)

function addIssue() {
    const title = newTitle.value;
    const location = newLocation.value;
    const category = newCategory.value;
    const priority = newPriority.value;
    const report_date = newReportDate.value;
    const memo = newMemo.value;

    const newIssue = {
        "title": title,
        "location": location,
        "category": category,
        "priority": priority,
        "report_date": report_date,
        "memo": memo
    }

    fetch("/issue", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(
            { new_issue: newIssue }
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
            newTitle.value = "";
            newLocation.value = "";
            newCategory.value = "";
            newPriority.value = "";
            newReportDate.value = "";
            newMemo.value = "";
            loadIssues()
        })
        .catch(err => {
            console.log(err.message)
        })
}

const categorySelector = document.querySelector("#category")
const prioritySelector = document.querySelector("#priority")
const statusSelector = document.querySelector("#status")
const startDateSelector = document.querySelector("#start_date")
const endDateSelector = document.querySelector("#end_date")
const sortSelector = document.querySelector("#sort")

categorySelector.addEventListener("change", loadIssues)
prioritySelector.addEventListener("change", loadIssues)
statusSelector.addEventListener("change", loadIssues)
startDateSelector.addEventListener("change", loadIssues)
endDateSelector.addEventListener("change", loadIssues)
sortSelector.addEventListener("change", loadIssues)

function loadIssues() {
    const category = categorySelector.value;
    const priority = prioritySelector.value;
    const status = statusSelector.value;
    const start_date = startDateSelector.value;
    const end_date = endDateSelector.value;
    const sort = sortSelector.value;

    const queryParams = new URLSearchParams();

    if (category) {
        queryParams.append("category", category)
    }

    if (priority) {
        queryParams.append("priority", priority)
    }

    if (status) {
        queryParams.append("status", status)
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

    let url = "/issues"

    if (queryString) {
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
            const issuesListElement = document.querySelector("#issues-list")
            issuesListElement.innerHTML = ""

            const issuesList = data["issues_list"]

            for (const issue of issuesList) {
                const tr1 = document.createElement("tr")

                const td1 = document.createElement("td")
                const td2 = document.createElement("td")
                const td3 = document.createElement("td")
                const td4 = document.createElement("td")
                const td5 = document.createElement("td")
                const td6 = document.createElement("td")
                const td7 = document.createElement("td")

                td1.textContent = issue.title
                td2.textContent = issue.location
                td3.textContent = issue.category
                td4.textContent = issue.priority
                td5.textContent = issue.report_date
                td6.textContent = issue.status
                td7.textContent = issue.memo

                const td8 = document.createElement("td")

                const updateButton = document.createElement("button")
                updateButton.textContent = "변경"
                updateButton.addEventListener("click", () => {
                    updateIssue(issue._id)
                })

                td8.appendChild(updateButton)

                const td9 = document.createElement("td")

                const deleteButton = document.createElement("button")
                deleteButton.textContent = "삭제"
                deleteButton.addEventListener("click", () => {
                    deleteIssue(issue._id)
                })

                td9.appendChild(deleteButton)

                tr1.appendChild(td1)
                tr1.appendChild(td2)
                tr1.appendChild(td3)
                tr1.appendChild(td4)
                tr1.appendChild(td5)
                tr1.appendChild(td6)
                tr1.appendChild(td7)
                tr1.appendChild(td8)
                tr1.appendChild(td9)

                issuesListElement.appendChild(tr1)
            }
        })
        .catch(err => {
            console.log(err.message)
        })
}

loadIssues();

function updateIssue(update_id) {
    let updateStatus = prompt("현재 진행 상황", "reported, processing, done")

    if (updateStatus === null) {
        return;
    }

    fetch(`/issue/${update_id}`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(
            { "update_status": updateStatus }
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
            loadIssues()
        })
        .catch(err => {
            console.log(err.message)
        })
}

function deleteIssue(update_id) {
    fetch(`/issue/${update_id}`, {
        method: "DELETE",
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
            loadIssues()
        })
        .catch(err => {
            console.log(err.message)
        })
}