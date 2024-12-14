fruits = {}
cart = {}
total = 0

def add_fruit():
    opt = ""
    global fruits
    # while opt != "bye":
    #     opt = input("teclea bye para salir, cualquiera para añadir furta")
    #     if opt == "bye":
    #         break
    #     fruit = {input("name of fruit: ") : float(input("price per kilo: "))}
    #     fruits.update(fruit)
    fruit = {input("Fruit to add: ") : int(input("Price per kilo: "))}
    fruits.update(fruit)
    return False

def give_results(fruit, howmuch):
    if fruit in fruits:
        print(fruit + " - " + str(fruits[fruit] * howmuch))

def buy():
    opt = ""
    while opt != "2":
        fruit = input(f"Fruit you want to buy: {fruits} - Insert XXX to exit:  ")
        if fruit == "XXX":
            break
        if fruits.get(fruit):
            howmuch = input(f"Price per kilo is {fruits.get(fruit)}, buy Kilos: ")
            global cart
            item = {}
            if cart.get(fruit):
                item = {fruit : (float(cart.get(fruit)) + float(howmuch))}
                cart.update(item)
            else:
                item = {fruit : howmuch}
                cart.update(item)
        else:
            print(f"The fruit \"{fruit}\" does not exist!!")

def checkout():
    if bool(cart) == False:
        print("Cart is empty")
    else:
        print_cart()
        #system.exit(0)

def print_cart():
    global fruits, cart
    outputL = []
    concat = ""
    print(f"Carrito de Compras\nFruta\tKilos\tTotal")
    for fruit, quantity in cart.items():
        if fruits.get(fruit):
            total = float(quantity) * float(fruits.get(fruit))
            print(f"{fruit}\t{quantity}\t{float(quantity) * float(fruits.get(fruit))}")

    

def main():
    opt = ""
    menu = """
    a) Add Fruit
    b) Shopping Cart
    c) Checkout
    d) Exit\n"""
    while opt != "d":
        opt = input(menu)
        if opt == "d":
            break
        elif opt == "a":
            add_fruit()
        elif opt == "b":
            buy()
        elif opt == "c":
            checkout()
            break

main()
