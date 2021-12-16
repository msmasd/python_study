# coding=utf-8
a = 0.3 + 0.6
print(a)  # 0.89999999
print(a == 0.9)  # False

# 소수점 값을 비교하는 작업이 필요한 문제에서는 round() 함수를 이용할 수 있다.
print(round(a, 4) == 0.9)  # True

print(round(123.456, 2))  # 123.46
