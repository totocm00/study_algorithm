# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	1305767	508911	345056	38.418%
# 문제) 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력) 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 출력) 첫째 줄에 A+B를 출력한다.

try:
    a, b = map(int, input().split())
    
    if a <= 0:
        raise print("a의 값을 1이상으로 입력하세요")
    elif b >= 10:
        raise print("b의 값을 10미만으로 입력하세요")
    print(a+b)
except ValueError as e:
    print("정수를 입력하세요")