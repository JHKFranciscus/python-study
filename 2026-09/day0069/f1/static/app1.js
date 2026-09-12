const subjectSelector = document.querySelector("#subject")
const startDate = document.querySelector("#start_date")
const endDate = document.querySelector("#end_date")
const sortSelector = document.querySelector("#sort")

subjectSelector.addEventListener("change", loadRecords)
startDate.addEventListener("change", loadRecords)
endDate.addEventListener("change", loadRecords)
sortSelector.addEventListener("change", loadRecords)

function loadRecords() {
    const subject = subjectSelector.value;
    const start_date = startDate.value;
    const end_date = endDate.value;
    const sort = sortSelector.value;

    const queryParams = new URLSearchParams();

    if (subject) {
        queryParams.append("subject", subject);
    }

    if (start_date) {
        queryParams.append("start_date", start_date);
    }

    if (end_date) {
        queryParams.append("end_date", end_date);
    }

    if (sort) {
        queryParams.append("sort", sort);
    }

    const queryString = queryParams.toString();

    let url = `/records`

    if (queryString) {
        url = url + "?" + queryString;;
    }

    fetch(url)
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(errorData => {
                        throw new Error(errorData.error)
                    })
            }

            return response.json()
        })
        .then(data => {
            const recordsList = document.querySelector("#records-list");
            recordsList.innerHTML = "";

            const records_list = data["result"];

            for (const record of records_list) {
                const li1 = document.createElement("li");
                const li2 = document.createElement("li");
                const li3 = document.createElement("li");
                const li4 = document.createElement("li");

                const div1 = document.createElement("div");

                const updatechosenButton = document.createElement("button");
                const deleteButton = document.createElement("button");

                li1.textContent = `subject: ${record.subject}`;
                li2.textContent = `study_date: ${record.study_date}`;
                li3.textContent = `minutes: ${record.minutes}`;
                li4.textContent = `memo: ${record.memo}`;

                updatechosenButton.textContent = "수정";
                deleteButton.textContent = "삭제";

                updatechosenButton.setAttribute("data-id", `${record._id}`);
                updatechosenButton.addEventListener("click", () => {
                    preupdateRecord(updatechosenButton.dataset.id, `${record.subject}`, `${record.study_date}`, `${record.minutes}`, `${record.memo}`)
                });

                deleteButton.setAttribute("data-id", `${record._id}`);
                deleteButton.addEventListener("click", () => {
                    deleteRecord(deleteButton.dataset.id)
                });

                recordsList.appendChild(li1);
                recordsList.appendChild(li2);
                recordsList.appendChild(li3);
                recordsList.appendChild(li4);

                div1.appendChild(updatechosenButton);
                div1.appendChild(deleteButton);

                recordsList.appendChild(div1);
            }
        })
        .catch(err => {
            console.log(err.message)
        });
}

loadRecords();

const newSubjectSeletor = document.querySelector("#new_subject")
const newStudyDateSeletor = document.querySelector("#new_study_date")
const newMinutesSeletor = document.querySelector("#new_minutes")
const newMemoSeletor = document.querySelector("#new_memo")

function addRecord() {
    const newRecord = {}

    const new_subject = newSubjectSeletor.value;
    const new_study_date = newStudyDateSeletor.value;
    const new_minutes = newMinutesSeletor.value;
    const new_memo = newMemoSeletor.value;

    newRecord["subject"] = new_subject
    newRecord["study_date"] = new_study_date
    newRecord["minutes"] = new_minutes
    newRecord["memo"] = new_memo

    fetch("/record", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ "new_record": newRecord })
    })
        .then(response => {
            if (!response.ok) {
                response.json()
                    .then(errorData => {
                        throw new Error(errorData.error)
                    })
            }

            return response.json();
        })
        .then(data => {
            newStudyDateSeletor.value = null;
            newMinutesSeletor.value = "";
            newMemoSeletor.value = "";
            loadRecords();
        })
        .catch(err => {
            console.log(err.message)
        });
}

const addButton = document.querySelector("#add-button")
addButton.addEventListener("click", addRecord)


function deleteRecord(recordId) {
    fetch(`/record/${recordId}`, {
        method: "DELETE"
    })
        .then(response => {
            if (!response.ok) {
                response.json()
                    .then(errorData => {
                        throw new Error(errorData.error)
                    })
            }

            return response.json()
        })
        .then(data => {
            loadRecords();
        })
        .catch(err => {
            console.log(err.message)
        });
}

const updateSubjectSelector = document.querySelector("#update_subject");
const updateStudyDateSelector = document.querySelector("#update_study_date");
const updateMinutesSelector = document.querySelector("#update_minutes");
const updateMemoSelector = document.querySelector("#update_memo");

function preupdateRecord(recordId, subject, study_date, minutes, memo) {
    updateSubjectSelector.value = subject
    updateStudyDateSelector.value = study_date
    updateMinutesSelector.value = minutes
    updateMemoSelector.value = memo

    editingId = recordId
}

let editingId = null;

const updateButton = document.querySelector("#update-button")
updateButton.addEventListener("click", () => {
    updateRecord(editingId)
})

function updateRecord(editingId) {
    const update_subject = updateSubjectSelector.value;
    const update_study_date = updateStudyDateSelector.value;
    const update_minutes = updateMinutesSelector.value;
    const update_memo = updateMemoSelector.value;

    const updateRecord = {};

    if (update_subject !== "") {
        updateRecord["subject"] = update_subject;
    }

    if (update_study_date !== "") {
        updateRecord["study_date"] = update_study_date;
    }

    if (update_minutes !== "") {
        updateRecord["minutes"] = Number(update_minutes);
    }

    if (update_memo !== "") {
        updateRecord["memo"] = update_memo;
    }

    fetch(`record/${editingId}`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ "update_record": updateRecord })
    })
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(errData => {
                        throw new Error(errData.error)
                    })
            }

            return response.json()
        })
        .then(data => {
            updateSubjectSelector.value = "Python"
            updateStudyDateSelector.value = null
            updateMinutesSelector.value = ""
            updateMemoSelector.value = ""
            loadRecords();
        })
        .catch(err => {
            console.log(err.message)
        });
}

