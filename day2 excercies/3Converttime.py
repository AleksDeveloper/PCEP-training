"""3. Imprimir en pantalla la conversión de segundos a las diferentes unidades
de tiempo, tal y como se muestra en el siguiente ejemplo:
"100700 segundos es el equivalente a: 1 dia, 27 horas, 1678 minutos"
	
	a) 65000 segundos
	b) 180000 segundos"""

aminute = round(65000 / 60)
ahour = round(aminute / 60)
aday = round(ahour / 24)
bminute = round(180000 / 60)
bhour = round(bminute / 60)
bday = round(bhour / 24)

print(f"65000 segundos es el equivalente a {aday} día(s), {ahour} hora(s), {aminute} minuto(s)")
print(f"180000 segundos es el equivalente a {bday} día(s), {bhour} hora(s), {bminute} minuto(s)")
