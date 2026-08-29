function readMemo() {
    $.ajax({
        url: "/memo",
        type: "GET",
        success: function(response) {
            $("#memo-list").empty();

            for (let i = 0; i < response.length; i++) {
                let memo = response[i];

                let memo_list = `
                <h1>${memo["id"]}</h1>
                <p>${memo["title"]}</p>
                <p>${memo["content"]}</p>
                `

                $("#memo-list").append(memo_list)
            }
        }
    })
}


$("#add-button").on("click", function (){
    $.ajax({
        url: "/memo",
        type: "POST",
        data: {
            title: $("#title").val(),
            content: $("#content").val(),
        },
        success: function(response) {
            if (response == "success") {
                readMemo()
            }
        }
    });
});

