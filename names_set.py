names = set()
for i in range(5):
    name = input("enter name: ")
    if name in names:
        print("exist")
    else:
        names.add(name)
print(names)
