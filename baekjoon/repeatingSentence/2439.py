import sys
write = sys.stdout.write

N = int(input())
plus = 1
for i in range(N-1,-1,-1):
    print(str(" " * (i) + ("*" * plus )))
    plus += 1