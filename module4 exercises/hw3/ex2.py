from random import randrange

numero_aleatorio = randrange(1,11)

while True:
    try:
        intento_adivinar_numero = int(input('Ingresa un numero aleatorio: '))
        if numero_aleatorio == intento_adivinar_numero:
            print('Le atinaste al numero')
            break
        else:
            print('Sigue intentando')
    except Exception as e:
        print(f"Error during exe - {e}")
