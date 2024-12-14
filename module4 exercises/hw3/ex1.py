from math import sqrt  
def raices_ecuacion_cuadratica(a,b,c):
    try:
        raiz_discriminante = sqrt(b**2 - 4*a*c)
        x1, x2 = ((-b + raiz_discriminante)/(2*a), (-b - raiz_discriminante)/(2*a))
        print(f"Las raices de la ecuacion son: {x1}, {x2}")
    except ZeroDivisionError as e:
        print(f'La ecuacion no es de primer grado - {e}')
    except ValueError as ex:
        print(f'Raices complejas - {ex}')

def main():
    raices_ecuacion_cuadratica(1, 2, -15)
    raices_ecuacion_cuadratica(1, 1, 1)
    raices_ecuacion_cuadratica(0, 1, 2)
    raices_ecuacion_cuadratica(1, 0, -3)

main()