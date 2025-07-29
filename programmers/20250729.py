# n보다 커질 때까지 더하기
# next() 사용으로 변경해보기

def solution(numbers, n):
    answer = 0

    for i in range(len(numbers)):
        answer += numbers[i]
        if answer > n:
            return answer
        
    return answer