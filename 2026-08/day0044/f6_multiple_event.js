const buttons = document.querySelectorAll(".action")
const result = document.querySelector("#result")

function changeText () {
    result.textContent = "버튼이 클릭되었습니다."
}

function checkbutton (i) {
    console.log(`확인${i + 1} 버튼이 클릭되었습니다.`)
}

for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", changeText)
}

for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", () => {checkbutton (i)})
}