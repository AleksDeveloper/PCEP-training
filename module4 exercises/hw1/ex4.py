def merge_strings(listofstrings):
    reverselist = []
    reversestring = ""
    for x in listofstrings:
        reverselist.append(x[::-1])
        reversestring += x[::-1] + " "
    return reversestring

def main():
    print(merge_strings(["hello", "world"]))

main()
