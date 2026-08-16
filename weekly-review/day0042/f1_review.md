# 문제 1

## 질문 1
HTML에서 <header>, <main>, <section> 같은 semantic HTML을 사용하는 이유는 무엇인가?
<!-- 수정 전 오답: 구역을 나누어 구조화를 사여 부모와 자식 관계를 부여하기 위하여 -->
페이지의 각 영역에 의미와 역할을 나타내는 HTML요소를 사용하는 것

## 질문 2
External CSS를 HTML에 연결할 때 사용하는 HTML 요소와 주요 attribute는 무엇인가?
<link href="...'></link>

## 질문 3
다음 세 selector 중 일반적으로 specificity가 높은 순서대로 나열해라.

tag selector
class selector
id selector

id selector → class selector → tag selector

## 질문 4
CSS의 상속이란 무엇인가?
<!-- 보완 전 정답: 자식 요소에 별도의 CSS property를 생성하지 않으면 부모 요소의 property가 그 직계 자식 요소에도 적용되는 경우를 말한다. property마다 되는 것이 있고 안 되는 것이 있다. -->
상속되는 CSS property의 값이 자식 요소에 별도로 지정되지 않았을 떄 부모의 값을 물려받는 것

## 질문 5
Box Model을 구성하는 네 영역을 안쪽에서 바깥쪽 순서로 적어라.

content → padding → border → margin

## 질문 6
다음 CSS를 적용했을 때 width: 300px가 의미하는 범위가 기본 content-box와 어떻게 달라지는가?

```css
box-sizing: border-box;
width: 300px;
```

box-sizing: border-box로 설정하면 box의 크기에 border, padding, content를 다 포함하게 된다.

## 질문 7

다음 HTML에서 카드 3개를 가로 방향으로 배치하려고 한다.
```html
<section class="cards">
    <div class="card">Python</div>
    <div class="card">HTML</div>
    <div class="card">CSS</div>
</section>
```
display: flex는 .cards와 .card 중 어디에 적용해야 하는가?
그리고 왜 그 요소에 적용해야 하는가?

카드 3개를 가로 방향으로 배치하려고 하는 것은 카드의 위치를 지정하기 위해서인데 세 card를 flex item으로 만들어서 flex container 안에서 control하기 위해서는 .cards에 적용해야한다.

## 질문 8

Flexbox에서
```css
flex-direction: row;
```
인 상태라면,

justify-content는 어느 방향의 정렬을 담당하는가?
align-items는 어느 방향의 정렬을 담당하는가?

justify-content는 가로 방향을 main-axis로 하여 정렬을 담당한다.
align-items는 세로 방향을 cross-axis로 하여 정렬을 담당한다.

## 질문 9

Bootstrap을 사용하고 있어도 직접 CSS를 작성하는 이유는 무엇인가?

<!-- 보완 전 답: Bootstrap에서 제공되는 proprety 정해져 있기에 개인의 또 다른 요구사항이 존재하면 그에 맞추기 위하여 직접 CSS를 작성해야한다. -->
Bootstrap의 미리 정의된 class와 component로 공통적인 스타일과 레이아웃을 빠르게 만들고, 그것만으로 충족되니 않는 개별 디자인 요구사항은 직접 CSS로 작성한다.

## 질문 10

다음 두 상황에는 각각 transition과 animation 중 무엇이 더 적절한가?

A. 마우스를 버튼 위에 올렸을 때 버튼이 1.05배 커진다.
B. 페이지가 열리면 카드가 아래에서 위로 이동하면서 나타난다.

각각 무엇을 사용할지와 이유를 적어봐.

A. CSS property의 변화 과정에 시간을 부여하기 위하여 transition이 더 적합합니다.
<!-- 보완 전 답: B. 여러 변화 과정을 순서대로 실행하기 위해서 animation이 더 적합하다. -->
B. @keyframes로 시간에 따른 변화 과정을 정의하여 자체적으로 실행할 수 있다.

# 문제 2

```html
<main class="content">
    <section class="profile">
        <img src="profile.png" alt="프로필">
        <div class="info">
            <h2>홍길동</h2>
            <p>웹 개발 학습 중</p>
        </div>
    </section>


    <section class="skills">
        <div>Python</div>
        <div>HTML</div>
        <div>CSS</div>
    </section>
</main>
```
다음 요구사항마다 어느 요소에 CSS를 적용해야 하는지 + 이유를 답해봐.

## A. 프로필 이미지와 이름·설명 묶음을 가로로 나란히 배치한다.
<!-- 수정 전 오답: <div class="info">에 d-flex를 적용해야한다. flexbox는 한 부모 요소 안의 자식 요소를 한 방향으로 배치하고 정렬하기 때문이다. -->
<section class="profile">에 d-flex를 적용해야한다. flexbox는 한 부모 요소 안의 자식 요소를 한 방향으로 배치하고 정렬하기 때문이다.

## B. Python / HTML / CSS 세 항목을 가로로 나란히 배치한다.
<section class="skills">에 d-flex를 적용해야한다. flexbox는 한 부모 요소 안의 자식 요소를 한 방향으로 배치하고 정렬하기 때문이다.

## C. 프로필 영역 전체에 border, padding, border-radius를 적용한다.
<section class="profile">에 border, padding, border-radius를 적용해야한다. 그러면 프로필 영역 전체에 적용되기 때문이다.

# 문제 3
```html
<section class="dashboard">
    <h2>이번 주 학습</h2>


    <div class="cards">
        <article class="card">
            <h3>Python</h3>
            <button>보기</button>
        </article>


        <article class="card">
            <h3>HTML</h3>
            <button>보기</button>
        </article>


        <article class="card">
            <h3>CSS</h3>
            <button>보기</button>
        </article>
    </div>
</section>
```
다음 각각에 CSS를 적용할 대상을 답해봐.

## A. 세 개의 article.card를 가로로 배치한다.
<div class="cards">에 display: flex를 적용한다.

## B. 각 카드 안에서 h3와 버튼을 양쪽 끝에 배치한다.
<article class="card">에 display: flex와 justify-content: space-between을 적용한다.

## C. 세 카드 사이의 간격을 24px로 만든다.
<div class="cards">에 display: flex와 gap: 24px를 적용한다.

## D. 버튼에 마우스를 올렸을 때 1.05배 커지도록 만들고, 크기 변화가 부드럽게 보이게 한다.
<!-- 수정 전 오답:<article class="card">에 .card selector를 이용하여 transition: transform 0.5s을 정의하고, .card:hover selector를 이용하여 transform: scale(1.05)를 적용한다. -->
<button>...</button>에 .button selector를 이용하여 transition: transform 0.5s을 정의하고, .button:hover selector를 이용하여 transform: scale(1.05)를 적용한다.
