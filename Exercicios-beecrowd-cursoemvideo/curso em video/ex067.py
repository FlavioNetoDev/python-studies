while True:
    num = int(input('Qual numero voce quer ver a tabuada?: '))
    if num <= 0:
            print('Escreva um numero positivo. ')
            break
    c = 0
    while c < 10:
        c += 1
        tabuada = num * c
        print(f'{num} x {c} = {tabuada}')
print('FIM')