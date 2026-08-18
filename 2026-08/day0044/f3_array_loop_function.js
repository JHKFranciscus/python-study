const temperatures = [24, 28, 31, 36, 29];

function weatherWaring (numbers3) {
    for (let i = 0; i < numbers3.length; i++) {
        if (numbers3[i] >= 35) {
            return "폭염 경고"
        }
    }
    return "정상"
}

const weatherResult = weatherWaring(temperatures)

console.log(weatherResult)
