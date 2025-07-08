# 정수가 담긴 리스트 num_list가 주어질 때,
# 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을
# 크면 0을 return하도록 solution 함수를 완성해주세요.

def solution(num_list):
    answer = 1
    for i in range(len(num_list)):
        answer *= num_list[i]
    
    return 1 if answer < sum(num_list)**2 else 0