counter = 0

def update_counter():
    global counter
    counter += 1
    
def print_value():
    print(counter)

def main():
    print_value()
    update_counter()
    print_value()
    update_counter()
    print_value()
    update_counter()
    print_value()

main()
