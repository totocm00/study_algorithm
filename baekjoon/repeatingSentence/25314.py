N = int(input())
temp = 0
list_a = []
for i in range(1,N+1):
    if i % 4 == 0:
        temp+=1
        list_a.append("long")

print(" ".join(list_a)+" int")