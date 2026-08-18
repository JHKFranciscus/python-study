const scores = [68, 91, 73, 88, 59];
const scoreAnalysis = document.querySelector("#analysis");
const result = document.querySelectorAll(".result");


function count70(scores) {
    let count = 0;
    for (let i = 0; i < scores.length; i++) {
        if (scores[i] >= 70) {
            count += 1;
        }
    }

    return count;
}

function maximumScore(scores) {
    let maxScore = scores[0];
    for (let i = 0; i < scores.length; i++) {
        if (maxScore <= scores[i]) {
            maxScore = scores[i];
        }
    }
    return maxScore;
}

function printResult(result, scores) {
    result[0].textContent = `- ${count70(scores)}`;
    result[1].textContent = `- ${maximumScore(scores)}`;
}

scoreAnalysis.addEventListener("click", () => { printResult(result, scores) });