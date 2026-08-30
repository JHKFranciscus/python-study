function loadAll(response) {
    $("#allTaskList").empty()

    for (let i = 0; i < response.length; i++) {
        task = response[i]

        taskList = `
        <div>
            <h2>제목: ${ task.title }</h2>

            <p class="doneTask" data-task-id=${i} onclick="changeDone(this)">완료 여부: ${task.done}</p>
        </div>
        `

        $("#allTaskList").append(taskList)
    }
}


function loadTask() {
    $.ajax({
        url: "/loadTasks",
        type: "GET",
        success: function (response) {
            loadAll(response);
        }
    });
};


function addTask() {
    $.ajax({
        url: "/addTask",
        type: "POST",
        data: {
            "title": $("#addtask").val(),
        },
        success: function (response) {
            if (response["result"] == "success")
                loadTask();
        }
    });
};

function changeDone(el) {
    task_id = $(el).data("task-id")

    $.ajax({
        url: `/changeTaskDone/${task_id}`,
        type: "POST",
        success: function (response) {
            if (response["result"] == "success")
                loadTask();
        }
    });
};
