"""
Quiz) 변수를 이용하여 다음 문장을 출력하시오

변수명
: station

변수값
: "사당", "신도림", "인천공항" 순서대로 입력

출력 문장
: xx 행 열차가 들어오고 있습니다.

"""

station = ["사당", "신도림", "인천공항"]

for var in range(3) :
    print(station[var], "행 열차가 들어오고 있습니다.")

for var in station:
    print(var, "행 열차가 들어오고 있습니다.")