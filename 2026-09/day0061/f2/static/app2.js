function loadTasks() {
    fetch("/tasks")
        .then(response => response.json())
        .then(data => {
            tasks = data['tasks'];

            const taskStatus = document.querySelector("#task-status");

            taskStatus.innerHTML = '';

            tasks.forEach(task => {
                let tStatus = '';

                if (task.status === true) {
                    tStatus = "완료"
                } else {
                    tStatus = "미완료"
                }

                taskStatus.innerHTML += `
                <tr>
                    <td>${task.task}</td>
                    <td>${tStatus}</td>
                    <td><button type="button" class="update-status" data-id="${task._id}">상태 변경</button></td>
                    <td><button type="button" class="delete-button" data-id="${task._id}">삭제</button></td>
                <tr>
                `
            });
            const updateButton = document.querySelectorAll(".update-status")
            updateButton.forEach(button => {
                button.addEventListener("click", () => { updateTask(button.dataset.id) })
            })

            const deleteButton = document.querySelectorAll(".delete-button")
            deleteButton.forEach(button => {
                button.addEventListener("click", () => { deleteTask(button.dataset.id) })
            })
        })
}

loadTasks();


function addTasks() {
    const new_task = document.querySelector("#task").value;
    fetch("/tasks", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(
            { 'task': new_task, }
        )
    })
        .then(response => response.json())
        .then(data => {
            loadTasks();
        })
}

const addButton = document.querySelector("#add-button")
addButton.addEventListener("click", addTasks)


function updateTask(task_id) {
    fetch(`/tasks/update/${task_id}`, {
        method: "PATCH"
    })
        .then(response => response.json())
        .then(data => {
            loadTasks();
        })
}


function deleteTask(task_id) {
    fetch(`/tasks/delete/${task_id}`, {
        method: "DELETE"
    })
        .then(response => response.json())
        .then(data => {
            loadTasks();
        })
}