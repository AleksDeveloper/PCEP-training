correct = 1988
respuesta = ""
while respuesta != str(correct):
    respuesta = input("Cuándo se estrenó Chucky?")
    if int(respuesta) > correct:
        print("un poco antes")
    elif int(respuesta) < correct:
        print("un poco después")
print("Correcto")
