let score = 70;
const maxScore = 100;

console.log(score);
console.log(maxScore);

score = 85;

console.log(score);


console.log("----------");
const userName = "Jungle";
let level = 1;
const isReady = false;

console.log(typeof userName);
console.log(typeof level);
console.log(typeof isReady);

level = 2;

console.log(level);
console.log(typeof level);


console.log("----------");
const testScore = 80;

if (testScore >= 60) {
    console.log("합격");
}


const age = 20;
let point = 55;

console.log(age >= 18);

if (point >= 60) {
    console.log("통과");
} else {
    console.log("재도전");
}

point = 70;

console.log(point >= 60);


console.log("----------");
const numberValue = 10;
const stringValue = 10;

console.log(numberValue === stringValue); 
console.log(numberValue == stringValue); 


console.log("----------");
const temperature = 23;

if (temperature >= 30) {
    console.log("더움");
} else if (temperature >= 20) {
    console.log("적당함");
} else {
    console.log("추움");
}


console.log("----------");
const age2 = 17;
const hasPermission = true;
const isBlocked = false;

console.log(age2 >= 18 && hasPermission);
console.log(age2 >= 18 || hasPermission);
console.log(!isBlocked);

if ((age2 >= 18 || hasPermission) && !isBlocked) {
    console.log("입장 가능");
} else {
    console.log("입장 불가");
}

