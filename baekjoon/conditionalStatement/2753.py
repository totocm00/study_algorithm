# 윤년 4로 나누어 떨어지는 해

input_year = int(input())
y = input_year

if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print("1")
else:
    print("0")