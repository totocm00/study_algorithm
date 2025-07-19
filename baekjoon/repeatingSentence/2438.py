import sys
write = sys.stdout.write

N = int(input())

for i in range(1,N+1):
    write(str("*" * i + "\n"))