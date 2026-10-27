frase = str(input('Digite uma frase: ')).lower().strip()
print('A frase possui {} letras A'.format(frase.count('a')))
print('A primeira posição que A aparece é {}'.format(frase.find('a')+1))
print('A ultima posição que A aparece é {}'.format(frase.rfind('a')+1))