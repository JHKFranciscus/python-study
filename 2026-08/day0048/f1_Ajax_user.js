$("#loadUserButton").on("click", function () {
    $.ajax({
        url: "./user.json",
        type: "GET",
        success: function (response) {
            const nickname = response.nickname;
            const point = response.point;

            $("#nickname").text(nickname);
            $("#point").text(point);

            if (point >= 80) {
                $("#grade").text("통과");
            } else {
                $("#grade").text("미통과");
            }
        }
    });
    console.log("회원 조회 요청")
});

