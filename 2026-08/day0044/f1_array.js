const prices = [1200, 2500, 1800, 3000];

console.log(prices);
console.log(prices[0]);
console.log(prices[2]);
console.log(prices.length);

console.log("===직접 작성===")

const numbers1 = [12, 7, 25, 18, 4, 31];

let count = 0

for (let i = 0; i < numbers1.length; i++) {
    if (numbers1[i] > 15) {
        count++;
    }
}

console.log(count)