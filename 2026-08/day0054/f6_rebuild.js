let task_id = null;

$(".edit-btn").on("click", function () {
    task_id = $(this).data("task-id");

    $.ajax({
        url: `/tasks/${task_id}/data`,
        type: "GET",
        success: function (response) {
            $("#edit-title").val(response["title"]);

            if (response["done"] === true) {
                $("#edit-status").text("완료");
            } else {
                $("#edit-status").text("미완료");
            }
        }
    });
});

$("#save-btn").on("click", function () {
    $.ajax({
        url: `/tasks/${task_id}/title`,
        type: "POST",
        data: {
            title: $("#edit-title").val(),
        },
        success: function (response) {
            $(`#task-title-${task_id}`).text(response.title)
        }
    });
});