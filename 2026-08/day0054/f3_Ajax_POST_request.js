const taskId = "3";
const newTitle = "Flask 복습 완료";

$.ajax({
    url: `/tasks/${taskId}/title`,
    type: "POST",
    data: {
        title: newTitle
    },
    success: function(response) {
        console.log(response.title)
    }
})