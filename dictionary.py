dictionary = {}
for i in range(2):
    name = input("enter name: ")
    last = input("enter last: ")
    dictionary[i + 1] = {"name" : name , "last" : last}
print(dictionary)