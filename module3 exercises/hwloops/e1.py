dias_compra = int(input("Cuántos días han pasado desde la compra?"))
usado = input("Ha sido usado? (y/n)")
defectos = input("Tiene defectos? (y/n)")
print(dias_compra, usado, defectos)

#LOGIC
if (dias_compra < 10 and usado == "f") or defectos == "y":
    print("Puedes devolver")
else:
    print("No puedes devolver")
