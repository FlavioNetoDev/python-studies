termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
cont = 1
while cont <= 10:
    print(termo, end=' > ')
    cont += 1
    termo += razao 
quantidade = int(input('\nQuantos termos a mais quer ver?: '))
while quantidade != 0:
    cont = 0
    while cont < quantidade:
        print(termo, end=' > ')
        termo += razao
        cont += 1
    
    quantidade = int(input('\nQuantos termos a mais quer ver?: '))
