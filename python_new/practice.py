## 1. 화면에 출력하기
`print()`는 화면에 글자나 숫자를 보여주는 기능이에요.

```python
print("안녕하세요!")  # 글자 출력
print(10)            # 숫자 출력
print("숫자:", 10)   # 여러 개 같이 출력
```

- **글자 붙이기**: `+`로 글자를 연결하거나, `{}`를 사용해 편리하게!
```python
station = "사당"
print(station + "행 열차가 들어옵니다!")  # 사당행 열차가 들어옵니다!
print(f"{station}행 열차가 들어옵니다!")  # 똑같은 결과
```

---

## 2. 변수: 데이터를 저장하는 상자
변수는 데이터를 담는 이름을 말해요. 상자에 물건을 넣듯 값을 저장합니다.

```python
name = "홍길동"  # 글자 저장
age = 20        # 숫자 저장
```

- **사용 팁**:
  - 이름은 영어, 숫자, `_`로 만들어요 (예: `my_name`, `age2`).
  - 숫자로 시작하면 안 돼요 (예: `2age` → 에러).
  - `if`, `for` 같은 특별한 단어는 못 써요.

---

## 3. 리스트: 여러 데이터를 한 줄로
리스트는 여러 데이터를 순서대로 모아놓은 상자예요. `[]`로 만듭니다.

```python
fruits = ["사과", "바나나", "오렌지"]
```

- **리스트 사용법**:
  - 추가: `append()`로 새 항목 추가
  - 꺼내기: `fruits[0]` → "사과"
  - 개수 세기: `len(fruits)` → 3

```python
my_list = []
my_list.append("공기놀이")  # ["공기놀이"]
print(my_list[0])          # 공기놀이
```

---

## 4. 반복: 똑같은 일을 여러 번
### for: 리스트나 숫자를 하나씩 꺼내기
리스트에 있는 항목을 하나씩 보면서 작업해요.

```python
stations = ["사당", "신도림", "인천공항"]
for station in stations:
    print(station + "행 열차가 들어옵니다!")
```

- 숫자 반복: `range(시작, 끝)`로 숫자 목록 만들기
```python
for num in range(1, 4):  # 1, 2, 3
    print(num, "번째!")
```

### while: 조건이 맞을 때까지 반복
조건이 참일 때 계속 반복해요.

```python
count = 1
while count <= 3:
    print(count, "번!")
    count = count + 1
```

---

## 5. 랜덤: 무작위로 뽑기
`random`으로 무작위 숫자를 뽑을 수 있어요.

```python
from random import *  # 랜덤 기능 가져오기
```

- 주요 기능:
  - `random()`: 0.0 ~ 1.0 사이 소수
  - `randrange(시작, 끝)`: 시작 ~ (끝-1) 사이 정수
  - `randint(시작, 끝)`: 시작 ~ 끝 사이 정수

```python
print(random())          # 예: 0.732...
print(randrange(1, 46))  # 1~45 중 하나 (로또 번호처럼!)
```

- **예시: 랜덤 날짜 뽑기**
```python
def random_date():
    return randrange(4, 29)  # 4~28 중 하루
print(f"스터디 날짜는 {random_date()}일입니다!")
```

---

## 6. 함수: 자주 쓰는 코드를 묶기
함수는 코드를 이름 붙여 저장해놓고 필요할 때 부르는 방법이에요.

```python
def say_hello():
    print("안녕!")
say_hello()  # 안녕!
```

- **입력과 출력**:
```python
def add(num1, num2):
    return num1 + num2
print(add(2, 3))  # 5
```

---

## 7. 조건문: 상황에 따라 다르게
`if`로 조건에 따라 다른 일을 해요.

```python
age = 15
if age >= 19:
    print("성인입니다.")
else:
    print("청소년입니다.")
```

- **조건 더 쓰기**:
```python
if age >= 19:
    print("성인")
elif age >= 13:
    print("청소년")
else:
    print("어린이")
```

---

## 8. 데이터 종류
- **숫자**: `5` (정수), `3.14` (소수)
- **글자**: `"안녕"` (문자열)
- **리스트**: `[1, 2, 3]`
- **참/거짓**: `True`, `False`

- **바꾸기**:
```python
num = 5
print(str(num) + "살")  # 5살
```

---

## 9. 입력받기
`input()`으로 사용자가 입력한 값을 받아요.

```python
name = input("이름이 뭐예요? ")
print(f"안녕, {name}!")
```

---

## 10. 꿀팁
- **들여쓰기**: 코드는 4칸 띄어서 구분해요.
- **주석**: `#`으로 설명 쓰기
```python
# 이건 주석이에요
"""
여러 줄
주석이에요
"""
```

- **에러 처리**:
```python
try:
    num = int(input("숫자를 입력하세요: "))
    print(num)
except:
    print("숫자가 아니에요!")
```

---

## 예시로 연습하기
### 퀴즈 1: 열차 도착 메시지
리스트를 사용해 역 이름을 하나씩 출력해요.

```python
def solution():
    stations = ["사당", "신도림", "인천공항"]
    for station in stations:
        print(station + "행 열차가 들어옵니다!")
solution()
```

### 퀴즈 2: 랜덤 날짜 뽑기
1~3일을 제외한 날짜를 무작위로 뽑아요.

```python
from random import *
def random_date():
    return randrange(4, 29)
print(f"스터디 날짜는 {random_date()}일입니다!")
```

---

이 문서를 따라 연습하면 파이썬 기초를 뿌셔뿌셔! 😄