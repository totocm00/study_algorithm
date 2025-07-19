import sys
input = sys.stdin.readline
write = sys.stdout.write

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    # print(A+B)
    write(str(A + B) + '\n')
