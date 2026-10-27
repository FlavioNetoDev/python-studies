nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 7:
    print('Sua média escolar entre {} e {} foi {}, parabéns você foi aprovado!'.format(nota1, nota2,media))
elif media >= 5:
    print('Sua média escolar entre {} e {} foi {}. você ficou em recuperação.'.format(nota1, nota2, media))
else:
    print('Sua média escolar entre {} e {} foi {}, infelizmente você foi reprovado.'.format(nota1, nota2, media))

