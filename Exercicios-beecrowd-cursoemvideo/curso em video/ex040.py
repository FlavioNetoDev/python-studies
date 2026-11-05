nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Entre {nota1} e {nota2}, a média do aluno é {media}')
if media < 5:
    print('O aluno foi REPROVADO')
elif media >= 5 and media <= 6.9:
    print('o aluno está em RECUPERAÇÃO')
elif media >= 7:
    print('O aluno foi APROVADO!')