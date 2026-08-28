$(".detail-btn").on("click", function () {
    const taskID = $(this).data("task-id");

    $.ajax({
        url: `/tasks/${taskId}/data`,
        type: "GET",
        success: function (response) {
            $("#task-title").text(response.title);

            const taskStatus = $("#task-status");

            if (response.done === true) {
                taskStatus.text("완료");
            } else {
                taskStatus.text("미완료")
            }
        }
    })
})


$(".detail-btn").on("click", function () {
    const taskId = $(this).data("task-id");

    $.ajax({
        url: `/tasks/${taskId}/data`,
        type: "GET",
        success: function (response) {
            console.log(response.title);
        }
    })
})


$(".detail-btn").on("click", function () {
    const taskId = $(this).data("task-id");

    $.ajax({
        url: `/tasks/${taskId}/data`,
        type: "GET",
        success: function (response) { 
            $("#task-title").text(response.title);
            if (response.done === true) {
                $("#task-status").text("완료");
            } else {
                $("#task-status").text("미완료");
            }
        }
    })
})