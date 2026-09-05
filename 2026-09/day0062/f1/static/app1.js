function loadTasks() {
    fetch("/task")
        .then(response => response.json())
        .then(data => {
            const tasks = data.tasks;

            const taskStatus = document.querySelector("#task-status");

            taskStatus.innerHTML = '';

            tasks.forEach(task => {
                taskStatus.innerHTML += `
                <tr>
                <td>${task.content}</td>
                <td>${task.important}</td>
                <td>
                <button type="button" class="update-button" data-id="${task._id}" data-important="${task.important}">상태 변경</button>
                </td>
                <td>
                <button type="button" class="delete-button" data-id="${task._id}">삭제</button>
                </td>
                </tr>
                `
            });
            const updateButtons = document.querySelectorAll(".update-button");
            updateButtons.forEach(updateButton => {
                updateButton.addEventListener("click", () => {
                    updateTask(updateButton.dataset.id, updateButton.dataset.important === "true");
                })
            });
            const deleteButtons = document.querySelectorAll(".delete-button");
            deleteButtons.forEach(deleteButton => {
                deleteButton.addEventListener("click", () => {
                    deleteTask(deleteButton.dataset.id);
                })
            });
        })
}

loadTasks()

function addTasks() {
    const new_content = document.querySelector("#content").value

    fetch("/task", {
        method: "post",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "content": new_content
        })
    })
        .then(response => response.json())
        .then(data => {
            document.querySelector("#content").value = ""
            loadTasks()
        })
}

const addButton = document.querySelector("#add-button");
addButton.addEventListener("click", addTasks);

function updateTask(task_id, task_important) {
    let new_important

    if (task_important === true) {
        new_important = false
    } else {
        new_important = true
    }

    fetch(`/task/${task_id}`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "important": new_important
        })
    })
        .then(response => response.json())
        .then(data => {
            loadTasks();
        })
}

function deleteTask(task_id) {
    fetch(`/task/${task_id}`, {
        method: "DELETE"
    })
        .then(response => response.json())
        .then(data => {
            loadTasks();
        })
}