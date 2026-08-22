$("#saveUserButton").on("click", function() {
    const nickname = $("#newNickname").val();
    const point = Number($("#newPoint").val());

    $.ajax({
        url: "/users",
        type: "POST",
        data: {
            nickname: nickname,
            point: point
        },
        success: function(response) {
            $("#saveResult").text(response.message)
        }
    });
    console.log("회원 등록 요청");
});