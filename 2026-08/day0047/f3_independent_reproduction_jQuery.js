//1. #preview-button을 클릭했을 때만 아래 작업이 실행
const button = $("#preview-button")
button.on("click", function (event) {
    readTitle();
    calValue();
    changeAttribute();
    manageClass();
    changeButtonText(event);
})
//2. 제목 읽기 / #book-title의 현재 value를 읽는다 / 읽은 
function readTitle() {
    $("#title-result").text($("#book-title").val());
}
//3. 가격 읽기 /
function changeValueType() {
    const numPrice = Number($("#book-price").val());
    return numPrice;
}
//4. 가격 계산
function calValue() {
    const numPrice = changeValueType();

    const priceResult = numPrice + 2000;
    $("#price-result").text(priceResult);
}
//5. attribute 변경
function changeAttribute() {
    $("#detail-link").attr("href", "book-preview.html");
}
//6. 가격에 따른 class 처리
function manageClass() {
    const numPrice = changeValueType()

    if (numPrice <= 20000) {
        $("#book-card").addClass("cheap");
    } else {
        $("#book-card").removeClass("cheap");
    }
}
//7. 버튼 text 변경
function changeButtonText(event) {
    $(event.target).text("미리보기 완료");
}
