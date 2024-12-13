def calculate_area(shape, width, height):
    if shape == "rectangle":
        return(width * height)
    if shape == "triangle":
        return((width * height) / 2)
    if shape == "circle":
        return(3.1416 * (width * width))

def main():
    print(calculate_area("rectangle", 10, 20))
    print(calculate_area("triangle", 20, 25))
    print(calculate_area("circle", 10, 10))

main()
