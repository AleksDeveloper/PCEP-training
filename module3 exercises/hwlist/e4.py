lista = ['a', 'b', 'c', 'e', 'i', 'o', 'u', 'x', 'z']
counter = 0
for x in lista:
    if x in ["a", "e", "i", "o", "u"]:
        print(str(x) + " It's a vocal")
        counter += 1
    else:
        print(str(x) + " It's not a vocal")

print("There are " + str(counter) + " vocals")
