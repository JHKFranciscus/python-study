$(".complete-btn").on("click", function (){
    const taskId = $(this).data("task-id")

    $.ajax({
        url: `/tasks/${taskId}/complete`,
        type: "POST",
        success: function(response) {
            $(`#task-status-${taskId}`).text("완료")
        }
    })
})