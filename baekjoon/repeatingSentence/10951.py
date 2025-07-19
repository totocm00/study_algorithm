import sys
input = sys.stdin.readline
write = sys.stdout.write

while 1:
    try:
        A, B = map(int, input().split())
        write(f"{A+B}\n")
    except ValueError:
        break