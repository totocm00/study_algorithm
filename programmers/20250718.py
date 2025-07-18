input_str = input()
result = ""
for c in input_str:
    if c.isupper():
        result += c.lower()
    else:
        result += c.upper()
print(result)
