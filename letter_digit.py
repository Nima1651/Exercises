str = input(": ")
a = b = 0
for i in str:
    if i.isdigit():
        a += 1
    elif i.isalpha():
        b += 1

print(b,"Letters")
print(a,"Digits")