print('-' * 10)
print('CADASTRE UMA PESSOA')
print('-' * 10)
homens = 0
anos18 = 0
mulheres20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).upper().strip()[0]
    if sexo == 'M':
        homens += 1
    if idade > 18:
        anos18 += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    print('-' * 10)
    continua = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continua == 'S':
        continue
    if continua == 'N':
        break
print(f'Cadastro realizado!')
print(f'{anos18} Pessoas cadastradas possuem mais de 18 anos')
print(f'{homens} Foram cadastrados')
print(f'{mulheres20} Mulheres possuem menos de 20 anos')