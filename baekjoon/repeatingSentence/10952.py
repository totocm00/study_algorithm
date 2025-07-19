import sys
input = sys.stdin.readline
write = sys.stdout.write

while 1:
    A, B = map(int, input().split())
    if A == B and A == 0:
        break
    write(f"{A+B}\n")

