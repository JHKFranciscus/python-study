$("#findBook").on("click", function() {
    $.ajax({
        url: "./books.json",
        type: "GET",
        success: function(response){
            const number = Number($("#findBook-number").val());
            const findBook = response[number];

            $("#title").text(findBook.title);
            $("#price").text(findBook.price);

            if (findBook.stock >= 1) {
                $("#countStatus").text("구매 가능");
            } else {
                $("#countStatus").text("품절");
            }
        }
    });
});
$("#request-buy").on("click", function() {
    const buyBookNumber = Number($("#buyBook-number").val());
    const buyBookCount = Number($("buyBook-count").val());

    $.ajax({
        url: "./books.json",
        type: "POST",
        data: {
            bookNumber: buyBookNumber,
            quantitiy: buyBookCount
        },
        success: function(response) {
            $("#responseMessage").text(response.message);
        }
    });
    console.log("구매 요청 전송");
});