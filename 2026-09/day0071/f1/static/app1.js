const newName = document.querySelector("#new_name");
const newRoom = document.querySelector("#new_room");
const newDate = document.querySelector("#new_date");
const newPurpose = document.querySelector("#new_purpose");

const addButton = document.querySelector("#add-button");
addButton.addEventListener("click", addReservation);

function addReservation() {
    const name = newName.value;
    const room = newRoom.value;
    const date = newDate.value;
    const purpose = newPurpose.value;

    const new_reservation = {
        "name": name,
        "room": room,
        "date": date,
        "purpose": purpose
    }

    fetch("/reservation", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(
            { "new_reservation": new_reservation }
        )
    })
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(errData => {
                        throw new Error(errData.err)
                    })
            }

            return response.json()
        })
        .then(data => {
            console.log(data.result)
            loadReservations()
        })
        .catch(err => {
            console.log(err.message)
        })
}

const roomSelector = document.querySelector("#room");
const startDateSelector = document.querySelector("#start_date");
const endDateSelector = document.querySelector("#end_date");
const sortSelector = document.querySelector("#sort");

const showButton = document.querySelector("#show-button");
showButton.addEventListener("click", loadReservations);

function loadReservations() {
    const room = roomSelector.value;
    const start_date = startDateSelector.value;
    const end_date = endDateSelector.value;
    const sort = sortSelector.value;

    const queryParams = new URLSearchParams();

    if (room) {
        queryParams.append("room", room)
    }

    if (start_date) {
        queryParams.append("start_date", start_date)
    }

    if (end_date) {
        queryParams.append("end_date", end_date)
    }

    if (sort) {
        queryParams.append("sort", sort)
    }

    const queryString = queryParams.toString();

    let url = "/reservations"

    if (queryString !== "") {
        url = url + "?" + queryString
    }

    fetch(url)
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(errData => {
                        throw new Error(errData.err)
                    })
            }

            return response.json()
        })
        .then(data => {

            const reservationsList = data["reservations"]

            const reservations = document.querySelector("#reservations-list")
            reservations.innerHTML = ""

            for (const reservation of reservationsList) {
                const tr = document.createElement("tr")

                const outName = document.createElement("td")
                const inName = document.createElement("input")
                inName.type = "text"
                inName.value = reservation.name

                const outRoom = document.createElement("td")
                const middleRoom = document.createElement("select")
                const inRoomA = document.createElement("option")
                inRoomA.value = "A"
                inRoomA.textContent = "A"
                const inRoomB = document.createElement("option")
                inRoomB.value = "B"
                inRoomB.textContent = "B"
                const inRoomC = document.createElement("option")
                inRoomC.value = "C"
                inRoomC.textContent = "C"

                const outDate = document.createElement("td")
                const inDate = document.createElement("input")
                inDate.type = "text"
                inDate.value = reservation.date


                const outPurpose = document.createElement("td")
                const inPurpose = document.createElement("input")
                inPurpose.type = "text"
                inPurpose.value = reservation.purpose


                const outUpdateButton = document.createElement("td")
                const inUpdateButton = document.createElement("button")
                inUpdateButton.addEventListener("click", () => {
                    updateReservation(reservation._id, inName.value, middleRoom.value, inDate.value, inPurpose.value)
                })
                inUpdateButton.textContent = "저장 버튼"

                const outDeleteButton = document.createElement("td")
                const inDeleteButton = document.createElement("button")
                inDeleteButton.addEventListener("click", () => {
                    deleteReservation(reservation._id)
                })
                inDeleteButton.textContent = "삭제"

                outName.appendChild(inName)

                middleRoom.appendChild(inRoomA)
                middleRoom.appendChild(inRoomB)
                middleRoom.appendChild(inRoomC)

                middleRoom.value = reservation.room

                outRoom.appendChild(middleRoom)

                outDate.appendChild(inDate)
                outPurpose.appendChild(inPurpose)

                outUpdateButton.appendChild(inUpdateButton)
                outDeleteButton.appendChild(inDeleteButton)

                tr.appendChild(outName)
                tr.appendChild(outRoom)
                tr.appendChild(outDate)
                tr.appendChild(outPurpose)
                tr.appendChild(outUpdateButton)
                tr.appendChild(outDeleteButton)

                reservations.appendChild(tr)
            }
        })
        .catch(err => {
            console.log(err.message)
        })
}

loadReservations();

function updateReservation(reserve_id, name, room, date, purpose) {
    const editReservation = {}

    if (name !== "") {
        editReservation.name = name
    }

    if (room !== "") {
        editReservation.room = room
    }

    if (date !== "") {
        editReservation.date = date
    }

    editReservation.purpose = purpose

    fetch(`/reservation/${reserve_id}`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(
            { "editReservation": editReservation }
        )
    })
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(errData => {
                        throw new Error(errData.err)
                    })
            }

            return response.json()
        })
        .then(data => {
            console.log(data.result)
            loadReservations()
        })
        .catch(err => {
            console.log(err.message)
        })
}

function deleteReservation(reserve_id) {
    fetch(`/reservation/${reserve_id}`, {
        method: "DELETE"
    })
        .then(response => {
            if (!response.ok) {
                return response.json()
                    .then(errData => {
                        throw new Error(errData.err)
                    })
            }

            return response.json()
        })
        .then(data => {
            console.log(data.result)
            loadReservations()
        })
        .catch(err => {
            console.log(err.message)
        })
}