const title = $("#book-title").val();
const price = Number($("#book-price").val());

$("#title-result").text(title);
$("#price-result").text(price + 2000);
$("#message").html("<strong>등록 완료</strong>")