def main():
    opt = ""
    mytuple = ()
    while opt != "bye":
        opt = input("Add to tuple: ")
        if opt == "bye":
            break
        temp = (int(opt),)
        mytuple += temp
    printby2(mytuple)
    
def printby(thetuple):
    counters = []
    for x in thetuple:
        if x in counters:
            value = {
                "number": x,
                "times": thetuple.count(x)
                }
            counters.append(value)

def printby2(thetuple):
    unique = []
    highest = 0
    for x in thetuple:
        if x not in unique:
            unique.append(x)
    print(unique)
    for x in unique:
        print(thetuple.count(x))
        if thetuple.count(x) > highest:
            highest = x
    print(highest)

main()
