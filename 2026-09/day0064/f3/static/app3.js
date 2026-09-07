function loadRecords() {
    const subjectElement =
        document.querySelector("#subject-filter");

    const sortElement =
        document.querySelector("#sort-select");

    const chosenSubject =
        subjectElement.value;

    const chosenSort =
        sortElement.value;

    const queryParams =
        new URLSearchParams();

    if (chosenSubject) {
        queryParams.append("filter", chosenSubject);
    }

    if (chosenSort) {
        queryParams.append("order", chosenSort);
    }

    const queryString =
        queryParams.toString();

    let requestUrl =
        `/api/records`;

    if (queryString) {
        requestUrl += `?${queryString}`;
    }

    fetch(requestUrl)
        .then(response => response.json())
        .then(recordArray => {
            const listElement =
                document.querySelector("#record-list");

            listElement.innerHTML = "";

            for (const record of recordArray) {
                listElement.innerHTML += `
                    <li>
                        ${record.subject} - ${record.minutes}분
                    </li>
                `;
            }
        });
}