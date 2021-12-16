# coding=utf-8

b = [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]
print(b[3])  # 4
print(b[-1])  # 4
print(b[1: 4])  # 슬라이싱 [2, 3, 4]

empty1 = []
empty2 = list()
print(empty1)  # []
print(empty2)  # []
print(empty2 == empty1)  # True

# init
n = 10
arr1 = [0] * n
print(arr1)  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 리스트 컴프리헨션(리스트를 초기화하는 방법 중 하나. 대괄호안에 조건문과 반복문을 넣는 방식으로 리스트를 초기화)
arr2 = [i for i in range(20) if i % 2 == 1]
print(arr2)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
arr3 = [i * i for i in range(1, 10)]
print(arr3)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]
n = 3
m = 4
arr4 = [[0] * m for _ in range(n)]
print(arr4)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# 언더바(_)는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 사용함.

# 잘못된 방법. 아래와 같이 하면 똑같은 일차원 리스트를 2차원으로 가지고있는 꼴이 됨. 그래서 [1][1]의 값을 변경했는데 모든 [n][1]의 값이 변경되는것으로 보임
err_arr = [[0] * m] * n
print(err_arr)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
err_arr[1][1] = 5
print(err_arr)  # [[0, 5, 0, 0], [0, 5, 0, 0], [0, 5, 0, 0]]

# list method
# append-O(1), sort-O(NlogN), insert-O(N), count-O(N), reverse-O(N)
a = [1, 4, 3]

a.append(2)
print(a)  # [1, 4, 3, 2]
a.reverse()  # 리스트 원소 뒤집기
print(a)  # [2, 3, 4, 1]
a.sort()  # 오름차순 정렬
print(a)  # [1, 2, 3, 4]
a.sort(reverse=True)  # 내림차순 정렬
print(a)  # [4, 3, 2, 1]
a.insert(2, 3)  # 특정 인덱스에 데이터 추가
print(a)  # [4, 3, 3, 2, 1]
print(a.count(3))  # 특정 값인 데이터 개수 세기(2)
a.remove(1)  # 특정 값 데이터 삭제
print(a)  # [4, 3, 3, 2, 1]

# 특정한 값의 원소를 모두 제거하는 방법
remove_set = {3, 4}
result = [i for i in a if i not in remove_set]
print(result)  # [2]
