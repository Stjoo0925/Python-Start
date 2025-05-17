from random import *

print("Hello, World!")

print(5)

# quiz 1

# 변수명 = station
# 변수명 = "사당"
# 변수명 = "신도림"
# 변수명 = "인천공항"

# print(변수명 + "행 열차가 들어오고 있습니다.")



def solution():
    station = ["사당", "신도림", "인천공항"]

    for i in station:
        print(i + "행 열차가 들어오고 있습니다.")


solution()


# 랜덤 함수

print(random())
print(int(random() * 10))

print(randrange(1, 46))

result = []
for _ in range(1, 6):
    result.append(randrange(1, 46))

print(result)

#  quiz 2

# 출력 예시
# 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.

# 조건1 : 랜덤으로 날짜 뽑기
# 조건2 : 월별 날짜는 1~30일 중 하루
# 조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

def random_date():
    date = randrange(4, 28)
    return date

print("오프라인 스터디 모임 날짜는 " + str(random_date()) + "일로 선정되었습니다.")








