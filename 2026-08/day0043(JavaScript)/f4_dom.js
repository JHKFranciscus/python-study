const statusText = document.querySelector("#status");
const startButton = document.querySelector("#startButton");

console.log(statusText);

startButton.addEventListener("click", function () {
    console.log("버튼 클릭");
    statusText.textContent = "공부를 시작했습니다.";
})