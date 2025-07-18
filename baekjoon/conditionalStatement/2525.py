# 오븐 시계

A, B = map(int, input().split())
C = int(input())

H = A
M = B + C

if M >= 60:
    if M > 119:
        H_plus = M // 60
        M = M % 60
        H = H + H_plus
        if H >= 24:
            H = abs(24 - H)
    else:
        H = H + 1
        M = abs(60 - M)
        if H >= 24:
            H = abs(24 - H)

print(f"{H} {M}")