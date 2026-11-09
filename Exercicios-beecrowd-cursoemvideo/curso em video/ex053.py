'''frase = str(input('Digite uma frase: ')).upper()
print(f'O inverso de {frase} é {frase[::-1]}')
if frase == frase[::-1]:
    print(f'A frase {frase}, é um PALÍNDROMO!')
else:
    print(f'A frase {frase}, não é um PALÍNDROMO')'''

frase = str(input('Digite uma frase ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1 , -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'O inverso de {junto} eh {inverso} Temos um PALÍNDROMO')
else:
    print(f'O inverso de {junto} eh {inverso} A frase digitada não é um PALÍNDROMO')