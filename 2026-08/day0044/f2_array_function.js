console.log("===함수에 배열 전달하기===")
function printNumbers(numbers2){
    for (let i = 0; i < numbers2.length; i++) {
        console.log(numbers2[i]);
    }
}

const values1 = [10, 20, 30];

printNumbers(values1);



console.log("===함수가 결과를 계산해서 반환하기===")
function countLargeNumbers(numbers3) {
    let count = 0;

    for (let i = 0; i < numbers3.length; i++) {
        if (numbers3[i] > 10) {
            count++;
        }
    }
    return count;
}

const values2 = [5, 12, 7, 20, 15];

const result = countLargeNumbers(values2);

console.log(result);
















