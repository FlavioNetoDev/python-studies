frase = str(input('Digite uma frase: ')).lower()

if frase == frase[::-1]:
    print(f'A frase {frase}, é um PALÍNDROMO!')
else:
    print(f'A frase {frase}, não é um PALÍNDROMO')