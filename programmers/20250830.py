# 정수가 담긴 리스트 num_list가 주어집니다. 
# num_list의 홀수만 순서대로 이어 붙인 수와 
# 짝수만 순서대로 이어 붙인 수의 
# 합을 return하도록 solution 함수
#
# num_list	        result
# [3, 4, 5, 2, 1]	393
# [5, 7, 8, 3]	    581
def solution(num_list):
    odd = ''
    even = ''
    for n in num_list:
        if n % 2:   # 홀수
            odd += str(n)
        else:       # 짝수
            even += str(n)
    return int(odd) + int(even)