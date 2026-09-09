function loadStudies(studies) {
    const list = document.querySelector("#study-list");

    list.innerHTML = "";

    studies.forEach(study => {
        const item = document.createElement("div");
        const deleteButton = document.createElement("button");
        const updateButton = document.createElement("button");


        item.textContent = `${study.date} / ${study.subject}`;

        deleteButton.textContent = "삭제";
        deleteButton.addEventListener("click", () => {
            deleteStudy(study._id);
        });

        updateButton.textContent = "수정";
        updateButton.addEventListener("click", () => {
            updateStudy(study._id);
        });

        item.appendChild(deleteButton);
        item.appendChild(updateButton)

        list.appendChild(item);
    });
}

function deleteStudy(id) {
    fetch(`/api/studies/${id}`, {
        method: "DELETE"
    })
        .then(response => {
            if (!response.ok) {
                throw new Error("삭제 실패");
            }

            return response.json();
        })
        .then(data => {
            loadStudies();
        })
        .catch(error => {
            console.log(error.message);
        });
}

function updateStudy(id) {
    const minutesInput = document.querySelector("#minutes-input");
    const minutes = Number(minutesInput.value);

    const updateData = {
        minutes: minutes
    };

    fetch(`api/studies/${id}`, {
        method: "PATCH",
        headers: {
            "Content-Tye": "application/json"
        },
        body: JSON.stringify(updateData)
    })
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(errorData => {
                        throw new Error(errorData.error);
                    });
            }
        })
        .then(data => {
            loadStudies();
        })
        .catch(error => {
            console.log(error.message);
        })
}