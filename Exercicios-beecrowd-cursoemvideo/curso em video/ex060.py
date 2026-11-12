num = int(input('Digite o valor que deseja calcular a fatorial: '))
c = num
resultado = 1
while c >= 1:
    resultado *= c
    c -= 1
print(resultado)