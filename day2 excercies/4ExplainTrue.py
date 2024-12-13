"""4. ¿Podrías explicar porque la siguiente expresión imprime un "True" en la pantalla?
print(False < (True > (True < False)))"""
print(True < False)
print(True > False)
print(False < True)
print("""The explanation is: TRUE > FALSE and FALSE < TRUE\n
      if you eval something different than these, they will be false\n
      And you need to start eval from the inner parenthesis first """)
