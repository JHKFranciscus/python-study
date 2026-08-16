# 보완 확인 1
```html
<div class="toolbar">
    <button>이전</button>
    <span>1 / 10</span>
    <button>다음</button>
</div>
```
세 요소를 한 줄에 놓고 서로 배치하려면 display: flex는 어느 요소에 적용해야 하며 왜 그런가?

flexbox는 부모 요소 안의 자식 요소들을 한 방향으로 배치하고 정렬하기 때문에 세 요소를 배치하려면 <div class="toolbar">요소에 display: flex를 적용해야한다.

# 보완 확인 2
```html
<article class="card">
    <h3>HTML</h3>
    <p>기본 구조 복습</p>
    <button>완료</button>
</article>
```

요구사항:
마우스를 카드 위에 올렸을 때 카드 전체의 그림자가 진해진다.
:hover selector의 대상은 .card와 button 중 무엇인가? 이유도 적어라.

특정 상황일 떄 카드 전체의 형태가 변화하는 것이기 때문에 :hover selector의 대상은 .card이다.

# 보완 확인 3

다음 중 <label>이 가장 적절한 경우는 무엇인가?

A
```html
<label>오늘의 할 일</label>
```

B
```html
<label for="username">사용자 이름</label>
<input id="username" type="text">
```
C
```html
<label>Python 복습</label>
<button>확인</button>
```
하나를 고르고 <label>의 역할도 한 문장으로 설명해봐.
B로 label은 input의 요소에 이름을 붙여 연결하는 것이 좋기 때문이다.