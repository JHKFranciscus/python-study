$(".book-btn").on("click", function(){
    let bookId = $(this).data("book-id");

    $.ajax({
        url: "/books/favorite",
        type: "POST",
        data: {
            book_id: bookId
        },
        success: function(response) {
            console.log(response);

            if (response["favorite"] === true) {
                $(`.book-status-${bookId}`).text("즐겨찾기");
            } else {
                $(`.book-status-${bookId}`).text("즐겨찾기 아님");
            }
        }
    });
});