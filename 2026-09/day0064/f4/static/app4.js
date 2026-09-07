const filterElement =
    document.querySelector("#subject-filter");

const pickedValue =
    filterElement.value;

const params =
    new URLSearchParams();

params.append("filter", pickedValue);

const queryText =
    params.toString();

const targetUrl =
    `/api/records?${queryText}`;

fetch(targetUrl)
    .then(httpResponse => httpResponse.json())
    .then(resultArray => {
        for (const item of resultArray) {
            console.log(item.subject);
        }
    });