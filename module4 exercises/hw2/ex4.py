fruits = {}
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

def main():
    create_dir()
    give_results(input("Fruit: "), float(input("How much: ")))

main()
