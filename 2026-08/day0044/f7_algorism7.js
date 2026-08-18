const temperatures = [22, 31, 27, 35, 29, 33];

let maxTemperatures = temperatures[0]

for (let i = 1; i < temperatures.length; i++) {
    if (maxTemperatures <temperatures[i]) {
        maxTemperatures = temperatures[i]
    }
}

console.log(maxTemperatures)