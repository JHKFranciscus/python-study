const subjectElement = document.querySelector("#subject-select");
const chosenSubject = subjectElement.value;

let requestURL = `api/records`

requestURL.innerHTML += `?filter=${chosenSubject}`

fetch(requestURL)
    .then(response => response.json())
    .then(recordArray => {
        listElement.innerHTML = "";

        recordArray.forEach(record => {
            listElement.innerHTMl += `
            <li>
                ${record.subject} - ${record.minutes}분
            </li>
            `;
        });
    });