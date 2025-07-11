a = [1,2,3,100,99,98]

# 리스트 컴프리헨션
# 한 줄로 리스트를 만드는 문법


##### 기본 형태
# [표현식 for 변수 in 반복가능한 것]
# ex)----------------------------------------v
# nums = [1, 2, 3, 4, 5]
# squares = [x * x for x in nums]
# print(squares)   -> [1, 4, 9, 16, 25]
### nums 의 각 요소 x 를 제곱해서 새로운 리스트를 만드는 코드

#--------------------------------------------------------#

##### 조건문 추가 형태
# [표현식 for 변수 in 반복가능한것 if 조건]
# ex)----------------------------------------v
# nums = [1, 2, 3, 4, 5]
# even = [x for x in nums if x % 2 == 0]
# print(even)   -> [2, 4]
### if 조건이 있는 경우, 조건에 맞는 값만 리스트에 들어가는 코드

#--------------------------------------------------------#

##### if-else 삼항 조건문 형태
# [값1 if 조건 else 값2 for 변수 in 반복가능한것]
# ex)------------------------------------------v
# nums = [1, 2, 3, 4, 5]
# result = [x * 2 if x % 2 == 0 else x * 3 for x in nums]
# print(result)   -> [3, 4, 9, 8, 15]
### 짝수면 *2, 아니면 *3을 해서 새 리스트를 만드는 코드




def solution(arr):
    return [
        x // 2 if x >= 50 and x % 2 == 0 else
        x * 2 if x < 50 and x % 2 != 0 else
        x
        for x in arr
    ]
solution(a)

# x >= 50 and 짝수    이면    x // 2
# x < 50 and 홀수     이면    x * 2
# 아니면 그대로 x
# 이 형태를 리스트로 만드는 코드

# 너무 복잡한 내용은 가독성이 떨어짐 -> for문 추천

# 리스트 [1, 2, 3, 4, 5, 6] 에서
# 짝수는 2배, 홀수는 그대로 유지

# for x in [1, 2, 3, 4, 5, 6]:
#   if x % 2 == 0:
#       result.append(x * 2)
#   else:
#       result.append(x)

# result = [x * 2 if x % 2 == 0 else x for x in [1, 2, 3, 4, 5, 6]]
#print(result)    -> [1, 4, 3, 8, 5, 12]