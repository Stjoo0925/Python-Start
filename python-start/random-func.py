from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값을 생성

print(random()*10) # 0.0 ~ 10.0 미만의 임의의 값을 생성

print(int(random()*10)) # 0 ~ 10 미만의 임의의 값을 생성

print(int(random()*10) + 1) # 1 ~ 10 이하의 임의의 값을 생성

# random 활용

print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값을 생성


# randrange

print(randrange(1, 46)) # 1 ~ 45 미만의 임의의 값을 생성

# randint 

print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값을 생성

