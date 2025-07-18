# 45분 일찍 일어나기

H, M = map(int, input().split())

M = M - 45

if M < 0:
    M = 60 + M
    H = H - 1
    if H < 0:
        H = 24 + H

print(f"{H} {M}")