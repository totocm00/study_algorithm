# n = int(input())

# def ja(n):
#     if n == 1:
#         return 1
#     return n * ja(n -1)

# print(ja(n))
# 런타임 에러..

n = int(input())
answer = 0
for i in range(1,n+1):
    answer += i
print(answer)