import sys

# EOF = End Of File, 입력이 끝났다는 신호
# 더이상 입력이 없으면 자동으로 EOF 발생

for line in sys.stdin:
    A, B = map(int, line.split())
    print(A + B)