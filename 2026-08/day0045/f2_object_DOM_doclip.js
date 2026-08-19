const products = [
    { name: "키보드", price: 32000 },
    { name: "마우스", price: 18000 },
    { name: "헤드셋", price: 45000 },
    { name: "웹캠", price: 27000 }
]

const prodsInfo = document.querySelectorAll(".prodInfo");
const count = document.querySelector(".count");
const button = document.querySelector(".button");

function priceCheck() {
    for (let i = 0; i < products.length; i++) {
        prodsInfo[i].textContent = `${products[i].name} : ${products[i].price}`;
    }
}

function check30000() {
    let count30000 = 0
    for (let i = 0; i < products.length; i++) {
        if (products[i].price >= 30000) {
            count30000 += 1;
        }
    }
    return count30000
}

function change30000() {
    const count30000 = check30000();
    count.textContent = `30000원 이상 상품 수 : ${count30000}`;
}


button.addEventListener("click", priceCheck)
button.addEventListener("click", change30000)


질문 1
객체
질문 2
{ name: "마우스", price: 18000 }
질문 3
{ name: "마우스", price: 18000 }이 객체의 price라는 이름의 가진 property의 값으로 18000이다.
질문 4
18000
질문 5
18000, let은 새로운 변수를 선언하기 위해서 필요하다. 근데 여기는 재할당할 일이 없는 변수이므로 const가 맞지 않나?
질문 6
두번째 .price에 해당하는 DOM 요소
질문 7
getPrice(products[1])이 실행되면 products 배열의 두번째 객체가 argument로 getPrice(product)의 product parameter에 저장된다. getPrice(product)함수가 실행되면 product.price라는 price property의 값을 반환한다. 그 후 변수 selectedPrice에 그 값이 대입된다. priceElements는 .price에 해당하는 DOM요소들을 모아둔 NodeList로 priceElements[1]는 두번째 .price DOM 요소이다. 그 요소의 textContent에 selectedPrice의 값이 대입된다. 그 후 브라우저의 화면의 내용이 바뀌게 된다.
