const age = 21;
const hasCompletedLesson = true;
const isRestricted = false;

const studyProcess = document.querySelector("#study");
const startButton = document.querySelector("#check");


startButton.addEventListener("click", function () {
    if ((age >= 18 && hasCompletedLesson) && !isRestricted) {
        studyProcess.textContent ="다음 단계 진행 가능";
    } else {
        studyProcess.textContent = "다음 단계 진행 불가";
    }
});



