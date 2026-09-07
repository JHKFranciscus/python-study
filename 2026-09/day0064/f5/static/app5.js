const levelFilter = document.querySelector("#level-filter");
const sortBy = document.querySelector("#sort-by");

levelFilter.addEventListener("change", loadStudy);
sortBy.addEventListener("change", loadStudy);

function loadStudy() {
    let chosenlevel = levelFilter.value;
    let chosenSort = sortBy.value;

    let queryPrams = new URLSearchParams();

    if (chosenlevel) {
        queryPrams.append("level_filter", chosenlevel);
    }

    if (chosenSort) {
        queryPrams.append("sort_by", chosenSort);
    }

    let requestUrl = "/api/lectures";

    const queryString = queryPrams.toString();

    if (queryString) {
        requestUrl += `?${queryString}`
    }

    fetch(requestUrl)
        .then(response => response.json())
        .then(lectureArray => {
            const list = document.querySelector("#lecture-list");

            list.innerHTML = ""

            lectureArray.forEach(study => {
                list.innerHTML += `
                <li>강의 제목:${study.title}, 강의 시간:${study.duration}</li>`
            })
        });
}

loadStudy();

