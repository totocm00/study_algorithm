# 정수가 담긴 리스트 num_list가 주어질 때,
# 모든 원소들의 곱이 
# 모든 원소들의 합의 제곱보다 작으면 1을
# 크면 0을 return하도록 solution 함수
#
# num_list	        result
# [3, 4, 5, 2, 1]	1        합: 15  합-제곱:225  곱:120  
# [5, 7, 8, 3]	    0        합: 23  합-제곱:529  곱:840

def solution(num_list):
    total_sum = sum(num_list)          # 원소들의 합
    total_product = 1                  # 곱 초기값
    for num in num_list:
        total_product *= num           # 곱 계산
    
    return 1 if total_product < total_sum ** 2 else 0