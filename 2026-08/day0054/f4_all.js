$(".change-title-btn").on("click", function () {
    const taskId = $(this).data("task-id");

    $.ajax({
        url: `/tasks/${taskId}/title`,
        type: "POST",
        data: {
            title: $("#title-input").val()
        },
        success: function(response){
            $("#task-title").text(response.title);
        }
    })
})

