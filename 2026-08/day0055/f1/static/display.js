function loadMemos() {
    $.ajax({
        url: "/memo",
        type: "GET",
        success: function (response) {
            $("#memo-list").empty()

            const memos = response["memos"]

            for (let i = 0; i < memos.length; i++) {
                let memo = memos[i];

                let memoID = memo["id"];
                let memoTitle = memo["title"];
                let memoContent = memo["content"];

                let htmltest1 = `
                    <section>
                        <span>${memoID}</span>
                        <h2>${memoTitle}</h2>
                        <p>${memoContent}</p>
                    </section>
                `

                $("#memo-list").append(htmltest1)

            }
        }
    });
}


$("#addBtn").on("click", function () {
    $.ajax({
        url: "/memo",
        type: "POST",
        data: {
            title: $("#memo-title").val(),
            content: $("#memo-content").val(),
        },
        success: function(response) {
            if (response["result"] == "success") {
                loadMemos()
            }
        }
    })
})



