
def howmany(value, mytuple):
    times = 0
    for x in mytuple:
        if x == value:
            times += 1
    print(times)

def howmany2(value, mytuple):
    print(mytuple.count(value))

def main():
    opt = ""
    mytuple = ()
    while opt != "bye":
        opt = input("Add to tuple: ")
        if opt == "bye":
            break
        temp = (int(opt),)
        mytuple += temp
    howmany(int(input("Which value: ")), mytuple)
    howmany(int(input("Which value: ")), mytuple)
    
main()
