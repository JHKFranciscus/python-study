const addButton = document.querySelector("#add-button");
addButton.addEventListener("click", addRecord);

const newSubject = document.querySelector("#new_subject");
const newStudy_date = document.querySelector("#new_study_date");
const newMinutes = document.querySelector("#new_minutes");
const newMemo = document.querySelector("#new_memo");

function addRecord() {
    const new_subject = newSubject.value;
    const new_study_date = newStudy_date.value;
    const new_minutes = newMinutes.value;
    const new_memo = newMemo.value;

    const new_recordStatus = {}

    if (new_subject !== "") {
        new_recordStatus["new_subject"] = new_subject
    }

    if (new_study_date !== "") {
        new_recordStatus["new_study_date"] = new_study_date
    }

    if (new_minutes !== "") {
        new_recordStatus["new_minutes"] = Number(new_minutes)
    }

    if (new_memo !== "") {
        new_recordStatus["new_memo"] = new_memo
    }
    fetch("/record", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ "new_record": new_recordStatus })
    })
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(error => {
                        throw new Error(error.err)
                    })
            }

            return response.json()
        })
        .then(data => {
            loadRecords();
        })
        .catch(errorData => {
            console.log(errorData.message)
        })
}

const subjectSelector = document.querySelector("#subject");
subjectSelector.addEventListener("change", loadRecords)
const startDate = document.querySelector("#start-date");
startDate.addEventListener("change", loadRecords)
const endDate = document.querySelector("#end-date");
endDate.addEventListener("change", loadRecords)
const sortSelector = document.querySelector("#sort");
sortSelector.addEventListener("change", loadRecords)

function loadRecords() {
    const subject = subjectSelector.value;
    const start_date = startDate.value;
    const end_date = endDate.value;
    const sort = sortSelector.value;

    const queryparams = new URLSearchParams();

    if (subject !== "") {
        queryparams.append("subject", subject)
    }

    if (start_date !== "") {
        queryparams.append("start_date", start_date)
    }

    if (end_date !== "") {
        queryparams.append("end_date", end_date)
    }

    if (sort !== "") {
        queryparams.append("sort", sort)
    }

    const queryString = queryparams.toString();

    let url = "/record"

    if (queryString) {
        url = url + "?" + `${queryString}`
    }

    fetch(url)
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(error => {
                        throw new Error(error.err)
                    })
            }

            return response.json()
        })
        .then(data => {
            const recordList = document.querySelector("#records-list")
            const records_list = data.records;

            recordList.innerHTML = "";

            for (const record of records_list) {
                const div1 = document.createElement("div");
                const h3 = document.createElement("h3");
                const p1 = document.createElement("p");
                const p2 = document.createElement("p");
                const p3 = document.createElement("p");

                const br1 = document.createElement("br");

                const div2 = document.createElement("div");
                const subjectInput = document.createElement("input");
                const dateInput = document.createElement("input");
                const minutesInput = document.createElement("input");
                const memoInput = document.createElement("input");

                const br2 = document.createElement("br");

                const updateButton = document.createElement("button");
                const deleteButton = document.createElement("button");

                h3.textContent = `${record.subject}`;
                p1.textContent = `${record.study_date}`;
                p2.textContent = `${record.minutes}`;
                p3.textContent = `${record.memo}`;

                subjectInput.value = `${record.subject}`;
                dateInput.value = `${record.study_date}`;
                dateInput.type = "date";
                minutesInput.value = `${record.minutes}`;
                minutesInput.type = "number";
                memoInput.value = `${record.memo}`;

                updateButton.textContent = "수정";
                deleteButton.textContent = "삭제";

                updateButton.setAttribute("data-id", `${record._id}`);
                deleteButton.setAttribute("data-id", `${record._id}`);

                updateButton.addEventListener("click", () => { updateRecord(updateButton.dataset.id, `${subjectInput.value}`, `${dateInput.value}`, `${minutesInput.value}`, `${memoInput.value}`) });
                deleteButton.addEventListener("click", () => { deleteRecord(deleteButton.dataset.id) });

                div1.appendChild(h3)
                div1.appendChild(p1)
                div1.appendChild(p2)
                div1.appendChild(p3)
                div1.appendChild(br1)

                div2.appendChild(subjectInput)
                div2.appendChild(dateInput)
                div2.appendChild(minutesInput)
                div2.appendChild(memoInput)
                div2.appendChild(br2)

                recordList.appendChild(div1)
                recordList.appendChild(div2)
                recordList.appendChild(updateButton)
                recordList.appendChild(deleteButton)
            }
        })
        .catch(errorData => {
            const recordList = document.querySelector("#records-list")
            recordList.textContent = `${errorData.message}`
        })
}

loadRecords();

function updateRecord(record_id, uSubject, uDate, uMinutes, uMemo) {
    const update_recordStatus = {}

    if (uSubject !== "") {
        update_recordStatus["subject"] = uSubject
    }

    if (uDate !== "") {
        update_recordStatus["study_date"] = uDate
    }

    if (uMinutes !== "") {
        update_recordStatus["minutes"] = Number(uMinutes)
    }

    if (uMemo !== "") {
        update_recordStatus["memo"] = uMemo
    }
    fetch(`/record/${record_id}`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ "update_record": update_recordStatus })
    })
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(error => {
                        throw new Error(error.err)
                    })
            }

            return response.json()
        })
        .then(data => {
            loadRecords();
        })
        .catch(errorData => {
            console.log(errorData.message)
        })
}

function deleteRecord(record_id) {
    fetch(`/record/${record_id}`, {
        method: "DELETE"
    })
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(error => {
                        throw new Error(error.err)
                    })
            }

            return response.json()
        })
        .then(data => {
            loadRecords();
        })
        .catch(errorData => {
            const recordList = document.querySelector("#records-list")
            recordList.textContent = `${errorData.message}`
        })
}