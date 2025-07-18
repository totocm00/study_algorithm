# 사분면

x = int(input())
y = int(input())

if 0 < x and 0 < y:
    print("1")

if 0 < x and 0 > y:
    print("4")

if 0 > x and 0 < y:
    print("2")

if 0 > x and 0 > y:
    print("3")