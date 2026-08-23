$("#findBook").on("click", function () {
    const bookNumber = Number($("#bookNumber").val());

    $.ajax({
        url: "books.json",
        type: "GET",
        success: function (response) {
            const book = response[bookNumber]

            $("#title").text(book.title);
            $("#price").text(book.price);
            $("#stock").text(book.stock);

            if (response[bookNumber].stock > 0) {
                $("#order").text("구매 가능");
            } else {
                $("#order").text("품절");
            }
        }
    });
});

