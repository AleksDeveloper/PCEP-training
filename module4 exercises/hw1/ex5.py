def is_valid_triangle(n1, n2, n3):
    if n1+n2 <= n3:
        return False
    else:
        return True

def main():
    print(is_valid_triangle(int(input("n1: ")),int(input("n2: ")),int(input("n3: "))))

main()
