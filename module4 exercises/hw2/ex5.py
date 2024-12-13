fruits = {}
cart = {}
total = 0
def create_dir():
    opt = ""
    global fruits
    while opt != "bye":
        opt = input("teclea bye para salir, cualquiera para añadir furta )
        if opt == "bye":
            break
        fruit = {input("name of fruit: ") : float(input("price per kilo: "))}
        fruits.update(fruit)

def give_results(fruit, howmuch):
    if fruit in fruits:
        print(fruit + " - " + str(fruits[fruit] * howmuch))

def buy():
    fruit = input("Fruit: ")
    howmuch = input("Kilos: ")
    global fruits, cart
    if fruit in fruits:
        item = {fruit : howmuch}
        cart.update(item)
    else:
        print(f"Fruit {fruit} does not exist.")

def checkout():
    if bool(cart) == False:
        print("Cart is empty")
    else:
        print(cart)

def main():
    menu = """1: Agrega un menu que tenga las siguientes opciones:\n
    a) Agregar Fruta\n
    b) Carrito de Compras\n
    c) Pagar\n
    d) Salir"""
    opt = input(menu)
    while opt != "d":
        
    create_dir()
    give_results(input("Fruit: "), float(input("How much: ")))

main()
