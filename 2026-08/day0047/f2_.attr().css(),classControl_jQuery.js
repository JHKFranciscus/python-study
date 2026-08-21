$("#profile-link").attr("href", "profile2.html");
$("#profile-card").css("background-color", "lightgray")
$("#profile-card").addClass("active")
$("#profile-card").removeClass("active")
$("#profile-card").toggleClass("active")

// 전자는 DOM 요소의 style attribute에 CSS property를 직접 지정하는 것이고,
// 후자는 DOM 요소의 class attribute에 class를 추가하는 것이다.