somaidade = 0
media = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print(f'-----{c}ª PESSOA -----')
    Nome = str(input('Nome: ')).strip()
    Idade = int(input('Idade: '))
    Sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += Idade
    if c == 1 and Sexo in 'Mm':
        maioridadehomem = Idade
        nomevelho = Nome
    if Sexo in 'Mm' and Idade > maioridadehomem:
        maioridadehomem = Idade
        nomevelho = Nome
    if Sexo in 'Ff' and Idade < 20:
        totmulher20 += 1
media = somaidade / 4
print(f'A media de idade do grupo é de {media} anos')
print(f'O homem mais velho do grupo tem {maioridadehomem} e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} com menos de 20 anos')
