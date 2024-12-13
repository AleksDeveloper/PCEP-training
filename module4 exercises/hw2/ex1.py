meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

def print_as_number(num):
    return meses[num-1]

def main():
    print(print_as_number(int(input("Número de mes: "))))

main()
