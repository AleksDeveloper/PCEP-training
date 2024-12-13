lst = [1, 2, 3, 4, 5]
lst.insert(1,6)
print(lst)
del lst[len(lst)-1]
print(lst)
lst.append(1)
print(lst)
print("------------")
lst = [1, [2, 3, 100, 200, 300], 4]
print(lst[1])
print(len(lst))
print("------------")
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

print(list_1, list_2, list_3)

del list_1[0]
del list_2[0]

print(list_3)


