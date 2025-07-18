a = int(input())
b = int(input())

temp = []
for i in range(3):
    integ = (b // (10 ** i)) % 10 
    temp.append(a * integ)
    print(temp[i])

result = temp[0] + temp[1] * 10 + temp[2] * 100
print(result)
