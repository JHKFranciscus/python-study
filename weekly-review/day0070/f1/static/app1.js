const newTitle = document.querySelector("#new_title")
const newPriority = document.querySelector("#new_priority")

const addButton = document.querySelector("#add-button")
addButton.addEventListener("click", addTask)

function addTask() {
    const title = newTitle.value;
    const priority = newPriority.value;

    const new_task = {
        "title": title,
        "priority": priority
    }

    fetch("/task", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(
            { "new_task": new_task }
        )
    })
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(errorData => {
                        throw new Error(errorData.result);
                    })
            }

            return response.json();
        })
        .then(data => {
            newTitle.value = "";
            loadTasks();
        })
        .catch(err => {
            console.log(err.message);
        })
}

const statusSelector = document.querySelector("#status")
const prioritySelector = document.querySelector("#priority")
const sortSelector = document.querySelector("#sort")

statusSelector.addEventListener("change", loadTasks)
prioritySelector.addEventListener("change", loadTasks)
sortSelector.addEventListener("change", loadTasks)

function loadTasks() {
    const status = statusSelector.value;
    const priority = prioritySelector.value;
    const sort = sortSelector.value;

    const queryParams = new URLSearchParams();

    if (status !== "") {
        queryParams.append("status", status);
    }

    if (priority !== "") {
        queryParams.append("priority", priority);
    }

    queryParams.append("sort", sort);

    let queryString = queryParams.toString();

    let url = "/task"

    if (queryString) {
        url = url + "?" + queryString;
    }

    fetch(url)
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(errorData => {
                        throw new Error(errorData.result);
                    })
            }

            return response.json()
        })
        .then(data => {
            const tasks = data["tasks"];

            const tasksList = document.querySelector("#tasks-list")
            tasksList.innerHTML = "";

            for (const task of tasks) {
                const tr = document.createElement("tr");

                const tdTitle = document.createElement("td");
                const tdStatus = document.createElement("td");
                const tdPriority = document.createElement("td");
                const tdSort = document.createElement("td");
                const tdUpdate = document.createElement("td");
                const tdDelete = document.createElement("td");

                const updateButton = document.createElement("button");
                const deleteButton = document.createElement("button");

                tdTitle.textContent = task.title;
                tdStatus.textContent = task.status;
                tdPriority.textContent = task.priority;

                updateButton.textContent = "status변경";
                deleteButton.textContent = "삭제";

                updateButton.addEventListener("click", () => {
                    updateTask(task._id, task.status);
                })

                deleteButton.addEventListener("click", () => {
                    deleteTask(task._id);
                })

                tdUpdate.appendChild(updateButton);
                tdDelete.appendChild(deleteButton);

                tr.appendChild(tdTitle);
                tr.appendChild(tdStatus);
                tr.appendChild(tdPriority);
                tr.appendChild(tdSort);
                tr.appendChild(tdUpdate);
                tr.appendChild(tdDelete);

                tasksList.appendChild(tr);
            }
        })
        .catch(err => {
            console.log(err.message);
        })
}

loadTasks();

function updateTask(task_id, status) {
    let update_status

    if (status === "todo") {
        update_status = "doing"
    } else if(status === "doing") {
        update_status = "done";
    } else if(status === "done") {
        update_status = "todo";
    }

    fetch(`/task/${task_id}`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(
            { "update_status": update_status }
        )
    })
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(errorData => {
                        throw new Error(errorData.result)
                    })
            }

            return response.json()
        })
        .then(data => {
            loadTasks();
        })
        .catch(err => {
            console.log(err.message)
        })
}


function deleteTask(task_id) {
    fetch(`/task/${task_id}`, {
        method: "DELETE"
    })
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(errorData => {
                        throw new Error(errorData.result)
                    })
            }

            return response.json()
        })
        .then(data => {
            loadTasks();
        })
        .catch(err => {
            console.log(err.message)
        })
}