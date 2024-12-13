numbers = [1, 2, 3]

def modify_global_list(addition):
    global numbers
    numbers.extend(addition)

def main():
    print(numbers)
    modify_global_list([10, 9, 8, 7])
    print(numbers)

main()
