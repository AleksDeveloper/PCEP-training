"""3. Escribe un programa que pida al usuario su nombre, estatura (en metros, ej. 1.71) y edad.

    3.1 - Convierte la estatura a centímetros.
    3.2 - Convierte la estatura a pies.
    3.3 - Convierte la estatura a pulgadas.
    3.4 - Convierte la estatura a pies y pulgadas.

Imprime la salida de la siguiente manera:

|      Nombre      |       Edad         |
    
    Rodrigo Lopez           25


|                            Estatura                             |
|    m     |    cm     |    ft    |    in     |       ft - in     |
|   1.71   |    171    |   5.61   |    67.32  |      5ft + 7in    |


Nota: Recuerda que un pie es igual a 30.48 cm y una pulgada es igual a 2.54 cm.
"""
nombre = input("nombre: ")
edad = input("edad: ")
estatura = float(input("Estatura en cm: "))

print("|\tNombre", "Edad", sep="\t|\t")
#print(f"\t{nombre}\t\t{edad}\n")
print(f"\t{nombre}", edad, sep="\t\t")
print("| \t\t\tEstatura \t\t\t |")
#print(f"|\tm\t|\tcm\t|\tft\t|\tin\t|\tft-in\t|")
print("|\tm","cm","ft","in","ft-in",sep="\t|\t")
print("|\t"+str(estatura/10), estatura, round(estatura/30.48,2), round(estatura/2.54,2), "5ft + 7in", sep="\t|\t")
