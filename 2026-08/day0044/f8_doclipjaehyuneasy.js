const scores = [68, 91, 73, 88, 59];
const scoreAnalysis = document.querySelector("#analysis");
const result = document.querySelectorAll(".result");

let count = 0;
let maxScore = scores[0];

for (let i = 0; i < scores.length; i++) {
    if (scores[i] >= 70) {
        count += 1;
    }
    if (maxScore <= scores[i]) {
        maxScore = scores[i];
    }
}

// for (let i = 1; i < scores.length; i++) {
//     if (maxScore <= scores[i]) {
//         maxScore = scores[i];
//     }
// }

function printResult() {
    result[0].textContent = count;
    result[1].textContent = maxScore;
}

scoreAnalysis.addEventListener("click", printResult);