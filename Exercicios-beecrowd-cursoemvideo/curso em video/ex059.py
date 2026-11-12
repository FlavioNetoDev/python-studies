from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
opcao = 0
while opcao != 5:
    print('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos numeros \n[ 5 ] sair')
    opcao = int(input('Qual sua opção?: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} eh {soma}')
        sleep(2)
    elif opcao == 2:
        multi = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} eh {multi}')
        sleep(2)
    elif opcao == 3:
        if n1 > n2:
            print(f'{n1} eh maior que {n2}')
        else:
            print(f'{n2} eh maior que {n1}')
            sleep(2)
    elif opcao == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    elif opcao > 5:
        print('Digite uma opcao correspondente: ')
        sleep(2)
print('Fechando...')