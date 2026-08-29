function loadAll(response) {
    $("#work-list").empty();

    for (let i = 0; i < response.length; i++) {
        let do_work = response[i];

        let do_work_id = `
        <h2>${do_work["id"]}</h2>
        <p>${do_work["text"]}</p>
        <p>${do_work["done"]}</p>

        <button type="button" class="change" data-work-id=${do_work["id"]} onclick="changeStatus(this)">상태 변경 버튼</button>
        `

        $("#work-list").append(do_work_id);
    }
}

function loadall() {
    $.ajax({
        url: "/do_works",
        type: "GET",
        success: function (response) {
            loadAll(response);
        }
    });
}


function changeStatus(button) {
    const namba = Number($(button).data("work-id"));

    $.ajax({
        url: `/change-status/${namba}`,
        type: "POST",
        success: function (response) {
            if (response === "success") {
                loadall();
            }
        }
    });
};