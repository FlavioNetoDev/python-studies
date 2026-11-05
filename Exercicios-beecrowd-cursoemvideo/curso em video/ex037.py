num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] convertar para HEXADECIMAL''')
opçao = int(input('Sua opção: '))

if opçao == 1:
    print('{} convertido para BINARIO eh igual a {}'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('{} convertido para OCTAL eh igual a {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('{} convertido para HEXADECIMAL eh igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente.')